from django.db import models

class User(models.Model):

    id = models.AutoField(primary_key = True)
    user = models.CharField(max_length = 20)
    password = models.CharField(max_length = 140)

    class Meta:
        app_label = 'user_ms'
