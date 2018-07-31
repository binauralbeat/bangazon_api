from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Customers
from .serializers import CustomersSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_user(first_name="", last_name=""):
        if first_name != "" and last_name != "":
            Customers.objects.create(first_name=first_name, last_name=last_name)

    def setUp(self):
        # add test data
        self.create_user("dingo", "dan")
        self.create_user("noodle", "claws")
        self.create_user("richard", "smith")


class GetAllCustomers(BaseViewTest):

    def test_get_all_customers(self):
        """
        This test ensures that all customers added in the setUp method
        exist when we make a GET request to the customers/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("customers-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Customers.objects.all()
        serialized = CustomersSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
