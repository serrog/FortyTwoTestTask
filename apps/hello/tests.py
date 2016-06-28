from django.test import TestCase

# Create your tests here.


class SomeTests(TestCase):
    def test_math(self):
        "put docstrings in your tests"
        assert(2 + 2 == 4)


class ViewTests(TestCase):
    def test_home_view_uses_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'hello/home.html')
