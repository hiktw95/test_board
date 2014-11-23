from django.db import models
class User(models.Model):
    user_id = models.CharField(max_length=10)
    user_pw = models.CharField(max_length=20)
    user_name = models.CharField(max_length=20)
class Board(models.Model):
    user_id = models.CharField(max_length=10)
    board_content = models.CharField(max_length=20)
    board_title = models.CharField(max_length=20)
    count = models.IntegerField(null=True, blank=True)
# Create your models here.
