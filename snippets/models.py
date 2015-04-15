from django.db import models
from django.template.defaultfilters import slugify
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
'''
'''
# from pygments.lexers import get_lexer_by_name
# from pygments.formatters.html import HtmlFormatter
# from pygments import highlight
# from celery.worker.strategy import default

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    id = models.AutoField(primary_key=True)

    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)
#
class User(models.Model):
    id = models.AutoField(primary_key=True)
    Device_type = models.CharField(max_length=100, blank=True, default='')
    RegistrationId = models.CharField(max_length=100, blank=True, default='')
#     Token = models.CharField(max_length=100, blank=True, default='')

    def __unicode__(self):
        return '{}: {}'.format(self.Device_type, self.RegistrationId)
#
#    . return models.Model.__str__(self.UserName, self.Password,self.FirstName,self.RegestrationId)

class Serial(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100, blank=True, default='')
    Image_url = models.CharField(max_length=200, blank=True, default='')
    LongDescription = models.TextField()
    ShortDesctiption = models.CharField(max_length=100, blank=True, default='')
    SerialId = models.BigIntegerField()
  
    def get_absolute_url(self):
        return 'http://example.com?slug=%s' % (slugify(self.Name),)
      
    def user_is_subscribed(self, registration_id, serial_id):
        subscription = Subscription.objects.filter(
            UserId__RegistrationId=registration_id, SerialId_id=serial_id)
        return bool(subscription)
  
#     def user_is_subscribed(self, registration_id):
#         subscription = Subscription.objects.filter(
#             UserId__RegistrationId=registration_id)
#         return bool(subscription)
  
  
class Season(models.Model):
    id = models.AutoField(primary_key=True)
    NumberOfSeason = models.IntegerField()
    serial = models.ForeignKey(Serial, related_name='seasons')
    SeasonId = models.IntegerField()
  
    def __unicode__(self):
        return '%d: %d' % (self.id, self.NumberOfSeason)
  
  
class Episode(models.Model):
    id = models.AutoField(primary_key=True)
    Number = models.IntegerField()
    Name = models.CharField(max_length=100, blank=True, default='')
    DayRealease = models.DateField(auto_now_add=True)
    season = models.ForeignKey(Season, related_name='episode')
    EpisodeId = models.IntegerField()
  
    def __unicode__(self):
        return '%d: %d' % (self.id, self.DayRealease)
  
    def __str__(self):
        return models.Model.__str__(self.Number, self.Name, self.DayRealease, self.season, self.EpisodeId)
  
class Subscription(models.Model):
    id = models.AutoField(primary_key=True)
    UserId = models.ForeignKey(User, default='',related_name='user')
    SerialId = models.ForeignKey(Serial, default='',related_name='serial')
  
    def __unicode__(self):
        return '{}: {}'.format(self.UserId, self.SerialId)

# class Test(models.Model):
#     name = models.TextField()




