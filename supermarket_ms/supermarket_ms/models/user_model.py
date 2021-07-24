from django.db import models

class User(models.Model):

    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 20)
    email = models.CharField(max_length = 140)

    class Meta:
        app_label = 'supermarket_ms'
