from django.test import TestCase
from datetime import date

from apps.hello.models import Person


def create_two_persons():
    person1 = Person()
    person1.first_name = 'testperson1_name'
    person1.last_name = 'testperson1_last_name'
    person1.date_of_birth = date(2000, 1, 1)
    person1.bio = 'testperson1 long long bio'
    person1.email = 'test1@example.com'
    person1.jid = 'jid_test1@example.com'
    person1.skype = 'test1_skype_id'
    person1.other = 'testperson1 other contacts'
    person1.save()

    person2 = Person()
    person2.first_name = 'testperson2_name'
    person2.last_name = 'testperson2_last_name'
    person2.date_of_birth = date(1998, 11, 1)
    person2.bio = 'testperson2 long long bio'
    person2.email = 'test2@example.com'
    person2.jid = 'jid_test2@example.com'
    person2.skype = 'test2_skype_id'
    person2.other = 'testperson2 other contacts'
    person2.username = 'test2@example.com'
    person2.save()


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

    def test_home_view_passes_hardcoded_data(self):
        """
        view.home should contain correct context with all variables.
        """
        response = self.client.get('/')
        self.assertEqual(response.context['first_name'], 'testperson1_name')
        self.assertEqual(
            response.context['last_name'], 'testperson1_last_name'
        )
        self.assertEqual(response.context['date_of_birth'], date(2000, 1, 1))
        self.assertEqual(response.context['bio'], 'testperson1 long long bio')
        self.assertEqual(response.context['email'], 'test1@example.com')
        self.assertEqual(response.context['jid'], 'jid_test1@example.com')
        self.assertEqual(response.context['skype'], 'test1_skype_id')
        self.assertEqual(
            response.context['other'], 'testperson1 other contacts'
        )


class ModelTests(TestCase):
    def test_saving_and_retrieving_items(self):
        """
        tests that DB can save and retrieve information about person
        """
        create_two_persons()

        persons = Person.objects.all()

        self.assertEqual(persons.count(), 2)
        self.assertEqual(persons[0].first_name, 'testperson1_name')
        self.assertEqual(persons[0].last_name, 'testperson1_last_name')
        self.assertEqual(persons[0].date_of_birth, date(2000, 1, 1))
        self.assertEqual(persons[0].bio, 'testperson1 long long bio')
        self.assertEqual(persons[0].email, 'test1@example.com')
        self.assertEqual(persons[0].jid, 'jid_test1@example.com')
        self.assertEqual(persons[0].skype, 'test1_skype_id')
        self.assertEqual(persons[0].other, 'testperson1 other contacts')

        self.assertEqual(persons[1].first_name, 'testperson2_name')
        self.assertEqual(persons[1].last_name, 'testperson2_last_name')
        self.assertEqual(persons[1].date_of_birth, date(1998, 11, 1))
        self.assertEqual(persons[1].bio, 'testperson2 long long bio')
        self.assertEqual(persons[1].email, 'test2@example.com')
        self.assertEqual(persons[1].jid, 'jid_test2@example.com')
        self.assertEqual(persons[1].skype, 'test2_skype_id')
        self.assertEqual(persons[1].other, 'testperson2 other contacts')
