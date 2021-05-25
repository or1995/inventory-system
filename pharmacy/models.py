from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    code = models.CharField(max_length=200)
    amount = models.IntegerField()

class CheckedItem(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    code = models.CharField(max_length=200)
    amount = models.IntegerField()

class Check(models.Model):
    item = models.ForeignKey(CheckedItem, null=True, on_delete=models.CASCADE)
    price = models.FloatField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)

