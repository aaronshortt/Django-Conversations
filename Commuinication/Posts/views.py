# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .models import Conversation

def index(request):

    conversations = Conversation.objects.all()[:10]
    context = {
        'title':'Latest Conversations',
        'conversations': conversations 
    }

    return render(request, 'posts/index.html', context)

def details(request, id):

    conversation = Conversation.objects.get(id = id)
    context = {
        'conversation': conversation
    }

    return render(request, 'posts/details.html', context)
