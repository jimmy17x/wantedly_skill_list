from django.test import TestCase
from .models import SkillList
# test case to check if model can create a skill list with a name

class ModelTestCase(TestCase):
	"""This class defines the test suite for the skillist model."""


	def setUp(self):
		"""Define the test client and other test variables."""
		self.skill_name = "Python"
		self.skillList = SkillList(name=self.skill_name)

	def test_model_can_create_a_skilllist(self):
		"""Test the skill list model can create a list."""
		old_count = SkillList.objects.count()
		self.skillList.save()
		new_count = SkillList.objects.count()
		self.assertNotEqual(old_count,new_count)


