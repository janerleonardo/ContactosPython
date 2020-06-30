# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACd6c58243ab007611fa74b86e5dd33c32'
auth_token = '99472456738013b5a4244c2b873fc8ce'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              from_='whatsapp:+14155238886',
                              body='Hello, there!',
                              to='whatsapp:+573166280358'
                          )

print(message.sid)