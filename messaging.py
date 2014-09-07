''' 
Messaging module

Initiates a contact object and 2 class methods
Send messages to the contact, accepts payload from final_project.py
Reads messaging.cfg, a JSON file containing credential and API key info

'''

from twilio.rest import TwilioRestClient
import smtplib, json

class Contact():
    def __init__(self, name, sms_number, email_address, sign, language):
        self.name = name
        self.to = sms_number
        self.email = email_address
        self.sign = sign
        self.language = language
        config = open('messaging.cfg')
        credentials = json.load(config)
        global credentials 
    
    def send_sms(self,body):
        account_sid = credentials['sms']['account_sid']
        auth_token  = credentials['sms']['auth_token']
        client = TwilioRestClient(account_sid, auth_token)
        message = client.messages.create(body=body,
                to=self.to,                            
                from_="+16506845303")

    def send_email(self, subject, body):
        login = credentials['email']['email_login']
        password = credentials['email']['password']
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(login,password)
        message = 'Subject: %s\n\n%s' % (subject, body)
        server.sendmail('sasser.python.test@gmail.com',
                        self.email,
                        message)



    
