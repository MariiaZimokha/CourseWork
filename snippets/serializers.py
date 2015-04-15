from django.forms import widgets
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES, Serial, Season, Subscription, Episode, User
from pyexpat import model
from urllib3 import fields
from rest_framework.views import APIView
from rest_framework import generics
from tutorial import settings


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')
        
class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ('UserId', 'SerialId')
'''
List serials
'''
class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields =  ('NumberOfSeason',)

class SerialSerializer(serializers.ModelSerializer):
    seasons = SeasonSerializer(many=True, read_only=True)
    class Meta:
        model = Serial
        fields = ('Name', 'Image_url', 'seasons')

'''Detail '''

class EpisodeDetailSerialize(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ('DayRealease','Number')


class SeasonDetailSerializer(serializers.ModelSerializer):
    episode = EpisodeDetailSerialize(many=True, read_only=True)
    class Meta:
        model = Season
        fields =  ('NumberOfSeason','episode')

# class SeasonNumberSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Season
#         fields = ('NumberOfSeason',)

class GiveAbsolute(serializers.Field):
    def to_native(self,value):
        return reverse('link_to_othermodel',
                     args=[value],
                     request=self.parent.request)


class SerialDetailSerializer(serializers.ModelSerializer):
#     seasons = serializers.SlugRelatedField(
#         many=True,
#         read_only=True,
#         slug_field='NumberOfSeason'
#     )
    seasons = SeasonDetailSerializer(many=True, read_only=True)
    is_subscribed = serializers.SerializerMethodField()
    absolute_url = serializers.SerializerMethodField()

    def get_absolute_url(self, obj):
        return obj.get_absolute_url()

    def get_is_subscribed(self, obj):
        return obj.user_is_subscribed(self.context.get('registration_id'),self.context.get('serial_id'))

    class Meta:
        model = Serial
        fields = ('Name', 'Image_url', 'LongDescription', 'is_subscribed',
                  'seasons', 'absolute_url')


'''for post user '''
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  ('Device_type', 'RegistrationId')


'''cron '''
class SeasonSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields =  ('NumberOfSeason','serial','SeasonId')
