# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACd9e10ecb26c44647b719f430ae745ca8'
auth_token = 'fed85f51ab308395d06337686a9cc72b'
client = Client(account_sid, auth_token)

def message(text):
    from_number = '+12028834384'
    to_number = '+31624852983'
    
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
