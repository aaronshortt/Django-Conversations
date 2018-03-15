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
    messages = None
    try:
        messages = Message.objects.filter(conversation_id = id)
    except:
        print "Couldnt find any responses for " + id

    context = {
        'conversation': conversation,
        'messages': messages
    }

    return render(request, 'posts/details.html', context)

def addConversation(request):

    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        
        conversation = Conversation(title = title, body = body)
        name = request.POST['person']

        #Change to exists someday...
        if Person.objects.filter(name = name).count() == 0:
            person = Person(name= name, email= name+"@email.com")
        else:
            person = Person.objects.get(name = name)

        person.save()
        conversation.sender = person
        
        conversation.save()  

        return redirect('/posts')
    else:
        return render(request, 'posts/add-conversation.html')

def addMessage(request, id):
    
    conversation = Conversation.objects.get(id = id)

    if request.method == 'POST':
        body = request.POST['body']
        name = request.POST['person']

        if Person.objects.filter(name = name).count() == 0:
            person = Person(name= name, email= name+"@email.com")
        else:
            person = Person.objects.get(name = name)

        message = Message(body= body, sender = person, conversation = conversation)
        message.save()

        return redirect('/posts/details/' + id)
    else:
        context = {
            'conversation': conversation
        }
        return render(request, 'posts/add-message.html', context)

