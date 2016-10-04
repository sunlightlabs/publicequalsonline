#Django settings for equalsonline project.
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    (),
)

MANAGERS = ADMINS

TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'

SITE_ID = 1
USE_I18N = True

MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = ''

SECRET_KEY = ''

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    # 'django.template.loaders.eggs.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'facebook.djangofb.FacebookMiddleware',
    'socialregistration.middleware.FacebookMiddleware',
)

ROOT_URLCONF = 'publicequalsonline.urls'


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.comments',
    'django.contrib.contenttypes',
    'django.contrib.gis',
    'django.contrib.markup',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.messages',
    'django.contrib.admin',
    'debug_toolbar',
    'mediasync',
    'tagging',
    'blogdor',
    'feedinator',
    'meetup',
    'shortcuts',
    #registration bits and bobs
    'registration',
    'socialregistration',
    # brainstorm and anthill
    'anthill.people',
    'anthill.projects',
    'anthill.events',
    'brainstorm',
    # callingtool
    'uspolitics',
    'uspolitics.politicians',
    'simplesurvey',
    'callingtool',
    # peo
    'publicequalsonline.equals',
)

# SOCIAL REGISTRATION STUFF like keys and things


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'socialregistration.auth.FacebookAuth',
    'socialregistration.auth.TwitterAuth',
    'socialregistration.auth.OpenIDAuth',
)

ABSOLUTE_URL_OVERRIDES = {
    'auth.user': lambda o: "/people/%s/" % o.username,
    'brainstorm.idea': lambda o: "/ideas/%s/" % o.id,
    'brainstorm.subsite': lambda o: '/ideas/',
}

FACEBOOK_API_KEY = ''
FACEBOOK_SECRET_KEY = ''

TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET_KEY = ''
TWITTER_REQUEST_TOKEN_URL = ''
TWITTER_ACCESS_TOKEN_URL = ''
TWITTER_AUTHORIZATION_URL = ''

#SOCIALREGISTRATION_GENERATE_USERNAME = 'False'

ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window; you may, of course, use a different value.

EMAIL_HOST = ""
EMAIL_PORT = ""
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = ''

LOGIN_REDIRECT_URL = '/'

ANTHILL_DEFAULT_MARKUP = 'markdown'
ANTHILL_GMAPS_KEY = ''
ANTHILL_LINK_TYPES = [(0, 'Website')]
ANTHILL_ROLES = (
    ('memb', 'Member'),
    ('lead', 'Leader'),
    ('volu', 'Volunteer'),
)

AWS_KEY = ''
AWS_SECRET = ''
AWS_BUCKET = ''

MEDIASYNC_AWS_KEY = AWS_KEY
MEDIASYNC_AWS_SECRET = AWS_SECRET
MEDIASYNC_AWS_BUCKET = ''
MEDIASYNC_AWS_PREFIX = ''

MEDIASYNC = {
    'BACKEND': '',
    'AWS_KEY': AWS_KEY,
    'AWS_SECRET': AWS_SECRET,
    'AWS_BUCKET': '',
    'AWS_PREFIX': '',
}

GRAVATAR_DEFAULT = "/logos/public_equals_online_mark_64x64.png"
GRAVATAR_SIZE = 60
FORCE_LOWERCASE_TAGS = True

INTERNAL_IPS = ('127.0.0.1',)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'HIDE_DJANGO_SQL': False,
}

SUNLIGHT_API_KEY = ""

SHORTCUT_PREFIX = 'r'

try:
    from local_settings import *
except ImportError:
    pass
