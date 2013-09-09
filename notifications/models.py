from django.db import models

# Create your models here.
class NotificationUser(models.Model):
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return self.phone_number
