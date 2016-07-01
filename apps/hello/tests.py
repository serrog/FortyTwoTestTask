from django.test import TestCase
from datetime import date

from apps.hello.models import Person


class SomeTests(TestCase):
    def test_math(self):
        "put docstrings in your tests"
        assert(2 + 2 == 4)


class ViewTests(TestCase):
    def test_home_view_uses_correct_template(self):
        """
        views.home should return correct template 'hello/home.html'
        """
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'hello/home.html')

    def test_home_view_passes_data_from_fixtures(self):
        """
        view.home should contain correct context with all variables.
        """

        response = self.client.get('/')
        self.assertEqual(response.context['first_name'], 'fixtperson1_name')
        self.assertEqual(
            response.context['last_name'], 'fixtperson1_last_name'
        )
        self.assertEqual(response.context['date_of_birth'], date(1990, 1, 1))
        self.assertEqual(response.context['bio'], 'fixtperson1 long long bio')
        self.assertEqual(response.context['email'], 'fixt1@example.com')
        self.assertEqual(response.context['jid'], 'jid_fixt1@example.com')
        self.assertEqual(response.context['skype'], 'fixt1_skype_id')
        self.assertEqual(
            response.context['other'], 'fixtperson1 other contacts'
        )


class ModelTests(TestCase):
    def test_saving_and_retrieving_items(self):
        """
        tests that DB can save and retrieve information about person
        """

        persons = Person.objects.all()

        self.assertEqual(persons.count(), 1)
        self.assertEqual(persons[0].first_name, 'fixtperson1_name')
        self.assertEqual(persons[0].last_name, 'fixtperson1_last_name')
        self.assertEqual(persons[0].date_of_birth, date(1990, 1, 1))
        self.assertEqual(persons[0].bio, 'fixtperson1 long long bio')
        self.assertEqual(persons[0].email, 'fixt1@example.com')
        self.assertEqual(persons[0].jid, 'jid_fixt1@example.com')
        self.assertEqual(persons[0].skype, 'fixt1_skype_id')
        self.assertEqual(persons[0].other, 'fixtperson1 other contacts')
