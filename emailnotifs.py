#! /usr/local/bin/python3

import sys, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

'''
note about setting up smtp server:
for host enter smtp.gmail.com.
Set the your username is yourgooglemailname@gmail.com
in gmail you must allow less secure apps under sign-in security
Connect to smtp.gmail.com on port 465, if you're using SSL. 
Connect on port 587 if you're using TLS.
'''

# please fill in below.
# alternatively, you may also call the send_email 
# function and supply the credentials
# todo: encrypt this password.

MY_ADDRESS = 'please fill in with your email address'
PASSWORD = 'please fill in with your password'
MY_PORT=587

def send_email(email,subject,message,my_address=MY_ADDRESS,my_password=PASSWORD,my_port=MY_PORT):
    # set up the SMTP server
    smtp_server = smtplib.SMTP(host='smtp.gmail.com', port=MY_PORT)
    smtp_server.starttls()
    smtp_server.login(MY_ADDRESS, PASSWORD)
    # create a message
    mymsg = MIMEMultipart()       
    # setup the parameters of the message
    mymsg['From']=MY_ADDRESS
    mymsg['To']=email
    mymsg['Subject']=subject
    # attach the message body
    mymsg.attach(MIMEText(message, 'plain'))
    # send the message from the server
    smtp_server.send_message(mymsg)
    del mymsg
    # end the SMTP session and shut-down connection
    smtp_server.quit()   


def main():
    while(1):
        email=input("enter email: \n")
        subject=input("enter subject: \n")
        message=input("enter message: \n")
        try:
            send_email(email,subject,message)
        except Exception as e:
            print( "Error: %s" % str(e) )
            sys.exit(1)
        else:
            print("successfully sent the following email:\n")
            print(email,message,)
            loop=input("send another email? (y)es or (n)o: \n")
            if loop != "y" or loop != "Y":
                break

if __name__ == '__main__':
    main()
