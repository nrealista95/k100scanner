from django.db import models
from django.contrib.postgres.fields import JSONField
from django.conf import settings

# Create your models here.
class Scan(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    app_name = models.CharField(default='app_name', null=False, max_length=50, unique=False)
    app_icon = models.ImageField(null=True, max_length=80)
    risk_score = models.IntegerField(default=0)
    md5 = models.CharField(max_length=100)
    time = models.TimeField(auto_now=False, auto_now_add=False)   # Time during scan
    created_at = models.DateTimeField(auto_now_add=True)
    results = JSONField(default='{}')
