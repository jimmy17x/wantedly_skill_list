from django.test import TestCase
from .models import SkillList

from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

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

class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.skilllist_data = {'name': 'Python'}
        self.response = self.client.post(
            reverse('create'),
            self.skilllist_data,
            format="json")

    def test_api_can_create_a_skilllist(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


