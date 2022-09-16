from django.conf import settings
from django.db import models


class Word(models.Model):
    #The word is title, so we can add more features later on  without name conflicts
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    audio_url = models.URLField(max_length=400, null=True)
    dict_url = models.URLField(max_length=400, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
