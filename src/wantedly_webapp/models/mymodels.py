#import from django models module
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# This class will more or less map to a table in the database and defines skills at the application level
class Skill (models.Model):
    # this defines a required name that cannot be more than 100 characters.
    skill_name = models.CharField(max_length=100,unique=True)
    class Meta:
        app_label = "wantedly_webapp"

# This class will more or less map to a table in the database and defines the many to many relationship between user-skill, this is our intermediate model
class UserSkill(models.Model):
    """ A Model for representing skill in user profile """
    unique_together = (('user', 'skill_item'),)

    user = models.ForeignKey('UserProfile',on_delete=models.CASCADE,related_name='current_user_skills')

    skill_item = models.ForeignKey(Skill,on_delete=models.CASCADE,null=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.skill_item.skill_name)

# this class adds a Many to Many field in existing django-rest auth UserProfile class for  user and his/her skills 
class UserProfile(models.Model):
	user = models.OneToOneField('auth.User',unique=True,on_delete=models.CASCADE,related_name='user_profile')
	user_skills = models.ManyToManyField(
			Skill,
			through='UserSkill',
			through_fields=('user','skill_item'),null=True
		)
#create user profile signal handler
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)

class UserSkillUpvotes(models.Model):
    unique_together = (('user_skill', 'upvote_by'),)
    user_skill = models.ForeignKey('UserSkill',on_delete=models.CASCADE)
    upvote_by =  models.ForeignKey('auth.User',on_delete=models.CASCADE , related_name='all_upvote_by_user') 
    upvote_for = models.ForeignKey('auth.User',on_delete=models.CASCADE , related_name='all_upvote_for_user')

   

