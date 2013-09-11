from django.test import TestCase
from notifications.models import NotificationUser
from notifications.forms import NotificationUserForm


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class NotificationUserTest(TestCase):

    def test_notification_user_str(self):
        """
        Tests that the phone number is stored properly
        in the user object
        """
        user = NotificationUser(phone_number='6507761881')

        self.assertEquals(str(user), '6507761881')
        self.assertEquals(user.phone_number, '6507761881')

class NotificationUserFormTest(TestCase):

    def test_valid_data(self):
        """
        Test if valid data is cleaned through the form.
        """
        data = {
                'phone_number': '6507761881'
                }
        form = NotificationUserForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_contains_letters_data(self):
        """
        Test if the form is not valid if letters are given
        """
        data = {
                'phone_number': 'aaabbbcccc',
                }

        form = NotificationUserForm(data=data)
        self.assertFalse(form.is_valid())

    def test_phone_number_short_invalid_data(self):
        """
        Test if the form returns invalid when too short of a phone
        number is given
        """
        data = {
                'phone_number': '12345',
                }

        form = NotificationUserForm(data=data)
        self.assertFalse(form.is_valid())

    def test_no_phone_number(self):
        """
        Tests if the form can handle no phone number submission
        """
        data = {}

        form = NotificationUserForm(data=data)
        self.assertFalse(form.is_valid())
