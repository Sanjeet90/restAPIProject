from django.test import TestCase
from unittest import mock

# Create your tests here.


class EmployeeDetailTestcase(TestCase):

    @mock.patch("restAPIApp.views.EmployeeDetail.post")
    def api_test(self, mock_post_data):
        mock_post_data = data = {
            "ID" : '2289357',
            "Name" : "sanjeet kumar",
            "Age" : "32"}