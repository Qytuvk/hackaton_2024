from django.db import models

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Rezume(models.Model):
    name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phoneno = models.CharField(max_length=14)
    skills = models.TextField()

class OtherModel(models.Model):
    skill = models.TextField()

@receiver(post_save, sender=Rezume)
def copy_skills_to_other_model(sender, instance, created, **kwargs):
    if created:
        OtherModel.objects.create(skill=instance.skills)
    else:
        other_instance = OtherModel.objects.get()
        other_instance.skill = instance.skills
        other_instance.save()