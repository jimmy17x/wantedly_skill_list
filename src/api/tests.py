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

    def test_api_can_get_a_skilllist(self):
        """Test the api can get a given skill list."""
        skillList = SkillList.objects.get()
        response = self.client.get(
            reverse('details',
            kwargs={'pk': skillList.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, skillList)

    def test_api_can_update_skilllist(self):
        """Test the api can update a given skillList."""
        change_bucketlist = {'name': 'Something new'}
        skillList = SkillList.objects.get()
        res = self.client.put(
            reverse('details', kwargs={'pk': skillList.id}),
            change_bucketlist, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_skilllist(self):
        """Test the api can delete a skillList."""
        skillList = SkillList.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': skillList.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)        


