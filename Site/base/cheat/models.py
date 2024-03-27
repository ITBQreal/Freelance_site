from django.db import models


class Channel(models.Model):
    channel_name = models.TextField(unique=True, null=False)
    def __str__(self):
        return f"{self.channel_name}"

class Streams(models.Model):
    stream_url = models.TextField(null=False)
    def __str__(self):
        return f"{self.stream_url}"

class BotAccounts(models.Model):
    owner = models.ForeignKey(Channel, to_field='channel_name', on_delete=models.CASCADE)
    login = models.TextField(null=False)
    password = models.TextField(null=False)

class Binds(models.Model):
    name = models.CharField(null=False, max_length=60)
    text = models.TextField(null=False)
