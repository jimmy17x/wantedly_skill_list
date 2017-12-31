from django.db import models

class SkillList (models.Model):
	"""This class represents the skill list model."""
	name = models.CharField(max_length=255,blank=False,unique=True)
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		"""Return a human readable representation of the model instance."""
		return "{}".format(self.name)
		



