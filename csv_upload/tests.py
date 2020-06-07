from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages


# Create your tests here.
class TestUploadView(TestCase):
    def test_upload_no_file(self):
        response = self.client.get(reverse('csv_upload:upload_csv'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['message'], 'No file supplied')
        self.assertTemplateUsed(response, 'csv_upload/upload_error.html')

    def test_wrong_file_name(self):
        # read data as binary (mimics standard Django file import mechanism)
        with open('csv_upload/test_data/data_example.pdf', 'rb') as fp:
            response = self.client.post('/upload/', {'name': 'data_example.pdf', 'file': fp})
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'csv_upload/index.html')
            messages = [msg.message for msg in get_messages(response.wsgi_request)]
            self.assertTrue('Please use a CSV file.' in messages)

    def test_invalid_file(self):
        # read data as binary (mimics standard Django file import mechanism)
        with open('csv_upload/test_data/invalid.csv', 'rb') as fp:
            response = self.client.post('/upload/', {'name': 'invalid.csv', 'file': fp})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.context['message'], 'Invalid CSV file')
            self.assertTemplateUsed(response, 'csv_upload/upload_error.html')

    def test_successful_upload(self):
        with open('csv_upload/test_data/data_example.csv', 'rb') as fp:
            response = self.client.post('/upload/', {'name': 'invalid.csv', 'file': fp})
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'csv_upload/upload_success.html')
