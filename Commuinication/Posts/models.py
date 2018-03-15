from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Conversation(models.Model):
    title = models.CharField(max_length=128, null=True)
    body = models.TextField(max_length=1024)
    sender = models.ForeignKey(Person, null = True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Message(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(Person, null = True)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE ,null = True)
