from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from api_app.serializers import UserSerializer, GroupSerializer, BoardSerializer, QuestSerializer, ChildQuestSerializer

from . models import Board, Quest, ChildQuest

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]






<<<<<<< HEAD
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
=======
class BoardViewSet(viewsets.ModelViewSet):
>>>>>>> b8fbabf (add models to api and admin)
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Quest.objects.all()
    serializer_class = QuestSerializer
    permission_classes = [permissions.IsAuthenticated]


class ChildQuestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ChildQuest.objects.all()
    serializer_class = ChildQuestSerializer
    permission_classes = [permissions.IsAuthenticated]





