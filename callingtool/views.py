import re
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseNotAllowed, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings
from django.core.cache import cache
from django.db.models import Count
from django.utils.encoding import iri_to_uri
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

from simplesurvey.models import AnswerSet, Answer, Question, QuestionSet
from callingtool.models import LegislatorDetail
from uspolitics.politicians.models import Politician

from sunlightapi import sunlight
sunlight.apikey = settings.SUNLIGHT_API_KEY

CALLTOOL_QSET = QuestionSet.objects.get(slug='peo-eta')

BAD_WORDS = ('.ru', 'Porn', 'porn')

STATES = (
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
#    ('DC', 'District of Columbia'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming'),
)

STATE_DICT = dict(STATES)

def delete_url_cache(url):
    """ simple method to delete the cache for a particular URL """
    key_prefix = settings.CACHE_MIDDLEWARE_KEY_PREFIX
    cache_key = 'views.decorators.cache.cache_header.%s.%s' % (key_prefix,
                                                               iri_to_uri(url))
    cache.delete(cache_key)

def legislator_list(request):
    has_called = request.session.get('has_called', False)
    if has_called:
        del request.session['has_called']
    return render_to_response('callingtool/legislator_list.html',
                              {'legislator_list': LegislatorDetail.objects.all(),
                               'states': STATES,
                               'has_called': has_called},
                               context_instance=RequestContext(request))

def call_legislator(request, id):
    legislator = get_object_or_404(LegislatorDetail, id=id)
    calls = []
    for call in legislator.calls.filter(question_set=CALLTOOL_QSET):
        cdict = {'date':call.date}
        for q,a in call.q_and_a():
            if a:
                cdict[q.text] = a.text
        calls.append(cdict)

    return render_to_response('callingtool/legislator_call.html', {
        'legislator': legislator,
        'calls': calls,
        'bill': 'S.3335' if legislator.legislator.title == 'Sen' else 'H.R.5258'
    }, context_instance=RequestContext(request))

def state_senators(request, state):
    senators = LegislatorDetail.objects.filter(legislator__state=state, legislator__title='Sen')
    return render_to_response('callingtool/state_senators.html',
                              {'state_name': STATE_DICT[state],
                               'senators': senators},
                                  context_instance=RequestContext(request))

def state_reps(request, zipcode):
    ids = [l.bioguide_id for l in sunlight.legislators.allForZip(zipcode)]
    reps = LegislatorDetail.objects.filter(legislator__bioguide_id__in=ids)
    for rep in reps:
        rep.num_calls = rep.calls.filter(question_set=CALLTOOL_QSET).count()
    return render_to_response('callingtool/state_reps.html',
                              {'reps': reps},
                              context_instance=RequestContext(request))


def submit_call(request, id):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])

    # blank or zipcode
    zipcode = request.POST['zip']
    if not re.match('^(\d{5}(\-\d{4})?)?$', zipcode):
        return HttpResponseRedirect(reverse('legislator_list'))

    # quick hack, added in response to one specific spammer
    for word in BAD_WORDS:
        if word in request.POST['comments']:
            return HttpResponseRedirect(reverse('legislator_list'))

    call = AnswerSet.objects.create(question_set=CALLTOOL_QSET,
                                related_object=LegislatorDetail.objects.get(id=id))

    for q in request.POST.iterkeys():
        Answer.objects.create(answer_set=call,
                              question=Question.objects.get(text=q),
                              text=request.POST.get(q))

    request.session['has_called'] = id

    # clear related cache keys
    delete_url_cache('/')
    delete_url_cache('/state_senators/%s/' % LegislatorDetail.objects.get(pk=id).legislator.state)
    delete_url_cache('/call/%s/' % id)
    delete_url_cache('/all_calls/')

    return HttpResponseRedirect(reverse('legislator_list'))

def all_calls(request):
    calls = []
    for call in AnswerSet.objects.all().order_by('-date'):
        cdict = {'date':call.date, 'senator':call.related_object, 'id': call.id}
        for q,a in call.q_and_a():
            if a:
                cdict[q.text] = a.text
        calls.append(cdict)
    num_calls = len(calls)
    num_unique = Answer.objects.filter(question__text='email').values_list('text').distinct().count()
    num_sens = AnswerSet.objects.values_list('object_id').distinct().count()

    return render_to_response('callingtool/all_calls.html', {'calls': calls,
        'num_calls': num_calls, 'num_unique': num_unique, 'num_sens': num_sens},
           context_instance=RequestContext(request))


def call_totals(request):
    from collections import defaultdict

    answers = AnswerSet.objects.all()
    counter = defaultdict(int)
    for a in answers:
        counter[a.object_id] += 1

    legislators = LegislatorDetail.objects.in_bulk(counter.keys())
    call_totals = [(legislators[i], n) for i,n in counter.iteritems()]
    call_totals = sorted(call_totals, key=lambda x: x[0].legislator.lastname)

    return render_to_response('callingtool/call_totals.html',
                              {'call_totals': call_totals},
                              context_instance=RequestContext(request))

@login_required
def delete_call(request, id):
    ans = AnswerSet.objects.filter(id=id)[0]
    pol_id = ans.object_id
    ans.delete()
    delete_url_cache('/call/%s/' % pol_id)
    delete_url_cache('/all_calls/')
    return HttpResponseRedirect(reverse('all_calls'))
