from django.test import TestCase
from datetime import date

from apps.hello.models import Person


class SomeTests(TestCase):
    def test_math(self):
        "put docstrings in your tests"
        assert(2 + 2 == 4)


class ViewTests(TestCase):
    fixtures = ['_initial_data.json']

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
        self.assertEqual(response.context['first_name'], 'Sergii')
        self.assertEqual(
            response.context['last_name'], 'Roganin'
        )
        self.assertEqual(response.context['date_of_birth'], date(1973, 11, 25))
        self.assertEqual(response.context['bio'], 'was born many years ago')
        self.assertEqual(response.context['email'], 'roganin@me.com')
        self.assertEqual(response.context['jid'], 'serrog@42cc.co')
        self.assertEqual(response.context['skype'], 'sergio_rini')
        self.assertEqual(
            response.context['other'], 'nothing else'
        )


class ModelTests(TestCase):
    fixtures = ['_initial_data.json']

    def test_saving_and_retrieving_items(self):
        """
        tests that DB can save and retrieve information about person
        """

        persons = Person.objects.all()

        self.assertEqual(persons.count(), 1)
        self.assertEqual(persons[0].first_name, 'Sergii')
        self.assertEqual(persons[0].last_name, 'Roganin')
        self.assertEqual(persons[0].date_of_birth, date(1973, 11, 25))
        self.assertEqual(persons[0].bio, 'was born many years ago')
        self.assertEqual(persons[0].email, 'roganin@me.com')
        self.assertEqual(persons[0].jid, 'serrog@42cc.co')
        self.assertEqual(persons[0].skype, 'sergio_rini')
        self.assertEqual(persons[0].other, 'nothing else')
