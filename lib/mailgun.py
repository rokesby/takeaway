# Prototype Twilio integration.

# https://www.twilio.com/docs/messaging/quickstart/python
# https://console.twilio.com/
# https://medium.com/@agarwalsrishti367/sending-sms-messages-with-twilio-and-python-91f78941d1c3



# Got problems with mailgun - https://help.mailgun.com/hc/en-us/articles/202464990-How-can-I-start-sending-email

from dotenv import load_dotenv
from pathlib import Path
import os
import requests
import logging

class SendMailer():
 
    def send_single_email(self, to_address: str, subject: str, message: str):

        load_dotenv()

        #dotenv_path = Path('/Users/reza/Code/takeaway/lib')
        #load_dotenv(dotenv_path=dotenv_path)


        # # Get the path to the directory this file is in
        # BASEDIR = os.path.abspath(os.path.dirname(__file__))
        # print ("The path is ***** : ", BASEDIR)
        # # Connect the path with your '.env' file name
        # load_dotenv(os.path.join(BASEDIR, '.env'))

        MAILGUN_KEY = os.getenv('MAILGUN_API_KEY')
        #key = os.environ.get('API_KEY')

        #print ("The key is => ", MAILGUN_KEY)



        # import os
        # from dotenv import load_dotenv

        logging.basicConfig(level=logging.INFO) # set log level
        load_dotenv() # for reading API key from `.env` file.

        # Subdomain - sandbox0269a106196242af8608bf502669c445

        # Sandbox API URL format: https://api.mailgun.net/v3/sandbox&lt;ID&gt;.mailgun.org/messages
        MAILGUN_API_URL = "https://api.mailgun.net/v3/sandbox0269a106196242af8608bf502669c445.mailgun.org/messages"
        FROM_EMAIL_ADDRESS = "sandbox0269a106196242af8608bf502669c445.mailgun.org"
        FROM_EMAIL_ADDRESS = "rezajugon@icloud.com"
        # authorised receivers, activcate account,

        try:
            api_key = os.getenv("MAILGUN_API_KEY") # get API-Key from the `.env` file
            resp = requests.post(MAILGUN_API_URL, auth=("api", api_key), data={"from": FROM_EMAIL_ADDRESS, "to": to_address, "subject": subject, "text": message})
        
            if resp.status_code == 200:
                # success
                logging.info(f"Successfully sent an email to '{to_address}' via Mailgun API.")
            else: # error
                logging.error(f"Could not send the email, reason: {resp.text}")
        except Exception as ex:
            logging.exception(f"Mailgun error: {ex}")

    
    # myMailer = SendMailer
    # myMailer.send_single_email("Reza <rezajugon@icloud.com>", "Single email test", "Testing Mailgun API for a single email")
