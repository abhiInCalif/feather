# Create your views here.
# The following is property of Feather.com
# Created by Abhinav Khanna
from notifications.models import NotificationUser
from django.core.urlresolvers import reverse
from django.views.generic import CreateView
import forms

class CreateNotificationUserView(CreateView):

    model = NotificationUser
    template_name = 'create_notification_user.html'
    form_class = forms.NotificationUserForm

    def get_success_url(self):
        return reverse('notifications-user-create')
