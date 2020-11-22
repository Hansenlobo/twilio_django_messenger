from django.db import models
from twilio.rest import Client

# Create your models here.
class Score(models.Model):
    msg=models.CharField(max_length=100)
    ph=models.CharField(max_length=12)


    def __str__(self):
        return str(self.ph)

    def save(self, *args,**kwargs):
        ph=int(self.ph)
        account_sid = ''
        auth_token = ''
        client = Client(account_sid, auth_token)

        message = client.messages.create(
                                body=f'{self.msg}',
                                from_='+000000000',
                                to=f'+{self.ph}'
                            )

        print(message.sid)
        return super().save(*args,**kwargs) 