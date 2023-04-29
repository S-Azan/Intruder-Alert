import keys
from twilio.rest import Client

client = Client(keys.account_sid, keys.auth_token)


def send_sms():
    client.messages.create(
        body="Intruder Alert - Unauthorized entry!",
        from_=keys.twilio_number,
        to=keys.target_number
    )
