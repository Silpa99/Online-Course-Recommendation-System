from django.db.models.signals import post_save , pre_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.dispatch import receiver
from .utils.pdfconvertor import parsepdf
from web_app.models import Profile , Job_applications

def candidate_profile(sender, instance, created, **kwargs):
	if created:
		#group = Group.objects.get(name='candidate')
		#instance.groups.add(group)
		Profile.objects.create(
			username=instance,
			)
		print('Profile created!')



