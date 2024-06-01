from django.db import models

class Profile(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, null=False, blank=False)
    second_name = models.CharField(max_length=30, null=False, blank=False)
    experience = models.IntegerField(null=False, blank=False)
    salary = models.IntegerField(null=False, blank=False)
    fit_criteries = models.IntegerField(null=False, blank=False)
    java = models.BooleanField()
    cpp = models.BooleanField()
    go = models.BooleanField()
    python = models.BooleanField()
    javascript = models.BooleanField()
    css = models.BooleanField()
    sql = models.BooleanField()

class MainInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, null=False, blank=False)
    second_name = models.CharField(max_length=30, null=False, blank=False)
    experience = models.IntegerField(null=False, blank=False)
    salary = models.IntegerField(null=False, blank=False)
    fit_criteries = models.IntegerField(null=False, blank=False)
# Create your models here.
