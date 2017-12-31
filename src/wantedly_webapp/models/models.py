#import from django models module
from django.db import models

# This class will more or less map to a table in the database and defines skills at the application level
class GlobalSkillItem (models.Model):
    # this defines a required name that cannot be more than 100 characters.
    skill_name = models.CharField(max_length=100,unique=True)
    # this defines an arbitrary length text field which is optional.
    description = models.TextField(blank=True, default='')



# This class will more or less map to a table in the database and defines the many to many relationship between user-skill, this is our intermediate model
class UserSkill(models.Model):
    """ A Model for representing skill in user profile """
    unique_together = (('user', 'skill_item'),)

    user = models.ForeignKey('auth.User',on_delete=models.CASCADE)

	# Define a foreign key relating this model to the GlobalSkillItem model.
    # The parent user will be able to access it's skills with the related_name
    # 'all_user_skills'. When a parent is deleted, this will be deleted as well. 
    skill_item = models.ForeignKey(
        'GlobalSkillItem',
        related_name='all_user_skills', on_delete=models.CASCADE
    )

# this class adds a Many to Many field in existing django-rest auth UserProfile class for  user and his/her skills 
class UserProfile(models.Model):
	user = models.OneToOneField(User,unqiue=True)
	user_skills = models.ManyToManyField(
			'GlobalSkillItem',
			through='UserSkill',
			through_fields=('user','skill_item')
		)

