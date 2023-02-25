from django.contrib.auth.models import User, Group
from rest_framework import serializers

# from api_app.models import Board, Quest

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
'''

class BoardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Board
        fields = ['title', 'author']


class QuestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quest
        fields = ['title', 'description', 'state', 'board', 'author']


        '''