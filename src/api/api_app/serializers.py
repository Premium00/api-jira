from django.contrib.auth.models import User, Group
from rest_framework import serializers

from api_app.models import Board, Quest, ChildQuest

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class BoardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'


class QuestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quest
        fields = '__all__'


class ChildQuestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChildQuest
        fields = '__all__'
