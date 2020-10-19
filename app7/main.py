# App: Uses an API (Twilio) to send out 
# Text Messages on an interval

# Need imports
import random
import time
import schedule

from twilio.rest import Client
from twilio_credentials import cellphone, twilio_number, twilio_account, twilio_token

# Array that has pre-built messages to send
SMS_MESSAGES_FOR_SPOUSE = ["I'm going to be late, eat dinner without me",
                           "Boss asked me to do some work, will be late",
                           "Got stuck in traffic will be a while"]

# Send Message
def send_message(quotes_list=SMS_MESSAGES_FOR_SPOUSE):
    account_sid = twilio_account
    auth_token = twilio_token
    body = quotes_list[random.randint(0, len(quotes_list)- 1)]

    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body=body,
            from_=twilio_number,
            to=cellphone
        )

    print(message.sid)

# Schedule the messages or use cronjobs
# Use Python 3.8 application would be constantly running
# or We could use cronjobs to set at a specific internval

# Python Pros - self-contained if it doesn't fire app not running
# Cronjobs = can be complicated to setup

schedule.every().wednesday.at("17:15").do(send_message,SMS_MESSAGES_FOR_SPOUSE)

#test

schedule.every(1).minutes.do(send_message,SMS_MESSAGES_FOR_SPOUSE)
# Loop system if we want to continue running the program or

while True:
    schedule.run_pending()
    time.sleep(5)
