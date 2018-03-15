# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Conversation, Message, Person

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

def addConversation(request):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        
        conversation = Conversation(title = title)
        message = Message(body = body)

        name = name = request.POST['person']
        person = Person.objects.get(name = name)
        message.sender = person
        
        message.save()
        conversation.message = message
        conversation.save()  

        return redirect('/posts')
    else:
        return render(request, 'posts/add-conversation.html')

