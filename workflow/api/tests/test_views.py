from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from .factories import WorkflowFactory


class WorkflowViewSetTestCase(TestCase):
    def setUp(self):
        self.list_url = reverse('api:WorkflowListPost')

    def test_get_list(self):
        """GET the list page of workflows."""
        workflows = [WorkflowFactory() for i in range(0, 3)]

        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            set(workflow['name'] for workflow in response.data['results']),
            set(workflow.name for workflow in workflows)
        )

    # def test_get_detail(self):
    #     """GET a detail page for a Company."""
    #     company = CompanyFactory()
    #     response = self.client.get(self.get_detail_url(company.id))
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data['name'], company.name)
    #
    # def test_post(self):
    #     """POST to create a Company."""
    #     data = {
    #         'name': 'New name',
    #         'description': 'New description',
    #         'street_line_1': 'New street_line_1',
    #         'city': 'New City',
    #         'state': 'NY',
    #         'zipcode': '12345',
    #     }
    #     self.assertEqual(Company.objects.count(), 0)
    #     response = self.client.post(self.list_url, data=data)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Company.objects.count(), 1)
    #     company = Company.objects.all().first()
    #     for field_name in data.keys():
    #           self.assertEqual(getattr(company, field_name), data[field_name])
    #
    # def test_put(self):
    #     """PUT to update a Company."""
    #     company = CompanyFactory()
    #     data = {
    #         'name': 'New name',
    #         'description': 'New description',
    #         'street_line_1': 'New street_line_1',
    #         'city': 'New City',
    #         'state': 'NY',
    #         'zipcode': '12345',
    #     }
    #     response = self.client.put(
    #         self.get_detail_url(company.id),
    #         data=data
    #     )
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    #     # The object has really been updated
    #     company.refresh_from_db()
    #     for field_name in data.keys():
    #         self.assertEqual(getattr(company, field_name), data[field_name])
    #
    # def test_patch(self):
    #     """PATCH to update a Company."""
    #     company = CompanyFactory()
    #     data = {'name': 'New name'}
    #     response = self.client.patch(
    #         self.get_detail_url(company.id),
    #         data=data
    #     )
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    #     # The object has really been updated
    #     company.refresh_from_db()
    #     self.assertEqual(company.name, data['name'])
    #
    # def test_delete(self):
    #     """DELETEing is not implemented."""
    #     company = CompanyFactory()
    #     response = self.client.delete(self.get_detail_url(company.id))
    #     self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
