![warframe](https://user-images.githubusercontent.com/32396421/41535981-7fae1e7a-7304-11e8-9387-52c91962f01f.jpg)
# intro
Warframe is a third-person, co-op focused action game.
In warframe there are time-limited alerts that grant you certain items.
There are websites and mobile apps where alerts can be watched but this is boring and time consuming.
So this script is made to watch the warframe alerts and looks for the item you want.
When the desired item is in alert an email and a text message is sent with gmail and twilio.

# warframe-alerts
mails and text warframe alerts from items you want!
The parse_warframe.py script parses this website : https://deathsnacks.com. Then it checks wether the item I want is in alert or not. Every time a wanted item is in the list send_emails.py and send_sms.py are used to send the information.

for this you will need to set-up your own gmail smtp adress and a twilio account for text messages.Put the credentials from these accounts in a separate credentials.py file.

# example credentials file:

account_sid= 'akjamjamjamjamjdfihihiofa484e848'

auth_token= '7558qsf4a484e8af8ae4fe84af8'

my_cell = '+11244477879'

my_twilio = '+8464864884'

my_email = 'example_email@gmail.com'

my_passord = 'examplepassword'

# future plans
- fine-tune it so it won't send same alerts twice (now this is kinda solved with time.sleep())

- expand this to work for multiple users that want different items

- turn this into a webapp
