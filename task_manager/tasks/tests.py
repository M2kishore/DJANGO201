from django.test import TestCase

# Create your tests here.
class QuestionModelTests(TestCase):
    def test_authenticated(self):
        """
        Try to GET the tasks listing page, expect the response to redirect to the login page
        """
        response = self.client.get("/tasks")
        self.assertEqual(response.status_code, 301)
        self.assertNotEqual(response.url, "/user/login?next=/tasks")