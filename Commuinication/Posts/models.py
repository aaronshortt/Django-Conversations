from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(Person, null = True)

class Conversation(models.Model):
    title = models.CharField(max_length=128, null=True)
    message = models.ForeignKey(Message, null = True)
    def __str__(self):
        return self.title
