from django.db import models
from twilio.rest import Client

# Create your models here.
class Score(models.Model):
    result=models.PositiveIntegerField()


    def __str__(self):
        return str(self.result)

    def save(self, *args,**kwargs):
        if self.result<70:
            account_sid = 'ID'
            auth_token = 'TOEKN'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                                body=f'Hi there! {self.result}',
                                from_='+00000000',
                                to='+000000000'
                            )

            print(message.sid)
        return super().save(*args,**kwargs) 