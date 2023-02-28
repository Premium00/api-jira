from django.contrib import admin
from . models import Quest, Board, ChildQuest

admin.site.register(Board)
admin.site.register(Quest)
admin.site.register(ChildQuest)

