# This file is the property of Feather
# Created by Abhinav Khanna
from django import forms
from django.core.exceptions import ValidationError
from notifications.models import NotificationUser
import re

class NotificationUserForm(forms.ModelForm):

    class Meta:
        model = NotificationUser

    def clean(self):
        # check that the value given in cleaned_data['phone_number'] is
        # a valid phone number
        if self.cleaned_data.get('phone_number') is None:
            raise ValidationError('No phone number provided')
        if len(self.cleaned_data.get('phone_number')) != 10:
            raise ValidationError('Please enter a valid phone number.')

        # the characters must be of type numbers, no alphas
        if not re.match('^[0-9]*$', self.cleaned_data.get('phone_number')):
            raise ValidationError('Please enter a valid phone number.')
        
        return self.cleaned_data

