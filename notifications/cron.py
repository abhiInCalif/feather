# This file contains logic for the cron job
# associated with this app
# Mainly will be used to send sms notifications to people
# Autho: Abhinav Khanna
from django_cron import CronJobBase
from django_cron import Schedule
from django.core.mail import send_mail
from googlevoice import Voice
from notifications.models import NotificationUser
from twilio.rest import TwilioRestClient

import imaplib
import email

class NotificationCronJob(CronJobBase):
    RUN_EVERY_MIN = 1 # We want it to run every minute so that its always up to date

    schedule = Schedule(run_every_mins=RUN_EVERY_MIN)
    code = 'notifications.send_sms'

    # define login credentials for voice
    user = 'princetonfeather@gmail.com'
    password = 'GoodWhenDrunk'

    # login to the google account once per instantiation,
    # rather than once per do....
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login('princetonfeather@gmail.com', 'GoodWhenDrunk')

    def do(self):
        # the code that will be done each iteration of the cron job
        # get the mail and check for the most recent unread email
        print 'reached do'
        mail = self.mail
        mail.list()
        mail.select('inbox')
        result, data = mail.search(None, '(UNSEEN)')
        for num in data[0].split(' '):
            typ, data = mail.fetch(num, '(RFC822)')
            msg = email.message_from_string(data[0][1])
            # we need to extract out the subject line
            # and send it through google sms
            subject = msg['subject']
            self.send_twilio_sms(subject)

    def send_twilio_sms(self, message):
        account_sid = 'ACca04b88e42ffc740570c9270dbb46ec4'
        auth_token = '0b81c57e9ba3d60130829910db94200a' 
        client = TwilioRestClient(account_sid, auth_token)
        user_list = NotificationUser.objects.filter()

        for u in user_list:
            print 'pushing sms through twilio'
            msg = client.sms.messages.create(body=message, to=u.phone_number, from_='+16505219069')
            # log the message id in the console
            print msg.sid

    def send_google_voice_message(self, message):
        # Sends the google voice message
        voice = Voice()
        voice.login(self.user, self.password)

        # Pull in all the user objects and us all the phone_numbers
        user_list = NotificationUser.objects.filter()
        for u in user_list:
            print 'pushing sms'
            try:
                voice.send_sms(u.phone_number, message)
            except:
                # do nothing really
                print 'flooding error occured'
                # switch self.user and self.password to a diff account
                if self.user is 'abhi1994@gmail.com':
                    self.user = 'princetonfeather@gmail.com'
                    self.password = 'GoodWhenDrunk'
                else:
                    self.user = 'abhi1994@gmail.com'
                    self.password = 'good2dad'

    def get_first_text_block(self, email_message_instance):
        maintype = email_message_instance.get_content_maintype()
        if maintype == 'multipart':
            for part in email_message_instance.get_payload():
                if part.get_content_maintype() == 'text':
                    return part.get_payload()
        elif maintype == 'text':
            return email_message_instance.get_payload()
