# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from config import account_sid, auth_token, from_number, to_number

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure

client = Client(account_sid, auth_token)

def message(text):

    
    try:
        client.messages \
                .create(
                     body=str(text),
                     from_=from_number,
                     to=to_number
                 )
        print(f"Send SMS to {to_number}: '{text}'")
    except Exception as e:
        print(e)
