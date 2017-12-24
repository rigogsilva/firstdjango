from django.db import models

class Item(models.Model):
	tittle = models.CharField(max_length=200)
	description = models.TextField()
	amount = models.IntegerField()