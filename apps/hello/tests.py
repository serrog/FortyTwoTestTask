from django.test import TestCase
from datetime import date

class SomeTests(TestCase):
    def test_math(self):
        "put docstrings in your tests"
        assert(2 + 2 == 4)

class ViewTests(TestCase):
    def test_home_view_uses_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'hello/home.html')

    def test_home_view_passes_hardcoded_data(self):

        response = self.client.get('/')
        self.assertEqual(response.context['first_name'], 'Name_from_View')
        self.assertEqual(response.context['last_name'], 'Last_name_from_View')
        self.assertEqual(response.context['date_of_birth'], date.today())
        self.assertEqual(response.context['bio'], 'Bio test from view')
        self.assertEqual(response.context['email'], 'test_view@exampl.com')
        self.assertEqual(response.context['jid'], 'jid_test_view@exampl.com')
        self.assertEqual(response.context['skype'], 'skype_id')
        self.assertEqual(response.context['other'], 'Other contacts from view')
