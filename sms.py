# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACd6c58243ab007611fa74b86e5dd33c32'
auth_token = '99472456738013b5a4244c2b873fc8ce'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Te amo mi amor hermosos, eres mi Regalito de  DIOS.",
                     from_='+12058787187',
                     to='+573187636255'
                 )

print(message.sid)