from django.db import models
from django.conf import settings

# Create your models here.
class Tool(models.Model):
    name = models.CharField(max_length=50, unique=True)
    github_link = models.URLField(max_length=200, unique=True, null=True)
    rate = models.IntegerField(default=0)
    number_of_votes = models.IntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
