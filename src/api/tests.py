from django.test import TestCase
from .models import SkillList

from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User


# test case to check if model can create a skill list with a name

class ModelTestCase(TestCase):
	"""This class defines the test suite for the skillist model."""


	def setUp(self):
		"""Define the test client and other test variables."""
		self.user = User.objects.create(username="test_user")  # create a test user
		self.skill_name = "Python"
		self.skillList = SkillList(name=self.skill_name, owner = self.user)

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
        user = User.objects.create(username="nerd")

        # Initialize client and force it to use authentication
        self.client = APIClient()
        self.client.force_authenticate(user=user)

        self.skilllist_data = {'name': 'Python'}
        self.response = self.client.post(
            reverse('create'),
            self.skilllist_data,
            format="json")

   	
    def test_api_can_create_a_skilllist(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        """Test that the api has user authorization."""
        new_client = APIClient()
        res = new_client.get('/bucketlists/', kwargs={'pk': 3}, format="json")
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)    

    def test_api_can_get_a_skilllist(self):
        """Test the api can get a given skill list."""
        skillList = SkillList.objects.get()
        response = self.client.get(
           	'skilllists',
           	kwargs={'pk': skillList.id}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, skillList)

    def test_api_can_update_skilllist(self):
        """Test the api can update a given skillList."""
        change_skillList = {'name': 'NewSkill'}
        skillList = SkillList.objects.get()
        res = self.client.put(
            reverse('details', kwargs={'pk': skillList.id}),
            change_skillList, format='json'
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


