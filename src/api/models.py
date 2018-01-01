from django.db import models

#signal dispatcher imports
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver

class SkillList (models.Model):
	"""This class represents the skill list model."""
	name = models.CharField(max_length=255,blank=False,unique=True)
	owner = models.ForeignKey('auth.User',
    related_name='skill_lists', 
    on_delete=models.CASCADE) 

	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		"""Return a human readable representation of the model instance."""
		return "{}".format(self.name)
		

# This receiver handles token creation immediately a new user is created.
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)	

