from django.db import models

class Kazananlar(models.Model):
    tc_num = models.CharField(max_length=11, primary_key=True)
    kazandi = models.BooleanField(default=False)
