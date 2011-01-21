from django.db import models
import datetime

class Letter(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    
    def __unicode__(self):
        if len(self.title) < 30:
            return self.title
        return self.title[:30] + '...'

class Signer(models.Model):
    letter = models.ForeignKey(Letter, related_name="signers")
    name = models.CharField(max_length=128)
    organization = models.CharField(max_length=128, blank=True)
    email = models.EmailField()
    url = models.URLField(verify_exists=False, blank=True)
    is_important = models.BooleanField(default=False)
    date_signed = models.DateTimeField(default=datetime.datetime.utcnow)
    
    class Meta:
        ordering = ('-date_signed',)
    
    def __unicode__(self):
        return self.name