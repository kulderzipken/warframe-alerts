from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_twilio

def send_text(item):
    client = Client(account_sid, auth_token)
    my_msg = "{} is in Alert now!".format(item)

    client.messages.create(
        to=my_cell,
        from_=my_twilio,
        body=my_msg
    )

if __name__ = '__main__':
    pass