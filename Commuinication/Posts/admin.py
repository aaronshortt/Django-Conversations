# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Conversation, Person

# Register your models here.
admin.site.register(Conversation)
admin.site.register(Person)