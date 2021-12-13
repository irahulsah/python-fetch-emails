# Python 3.8.0
from email import message
import smtplib
import time
import imaplib
import email
import traceback 
import csv
# f = open('/intern.csv', 'w')

# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------
ORG_EMAIL = "@everestwalk.com" 
FROM_EMAIL = "info" + ORG_EMAIL 
FROM_PWD = "info@dmin!123" 
SMTP_SERVER = "mail.privateemail.com" 
SMTP_PORT = 993

def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')

        # writer = csv.writer(f)

        data = mail.search(None, 'ALL')
        mail_ids = data[1]
        id_list = mail_ids[0].split()   
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])

        for i in range(latest_email_id,first_email_id, -1):
            data = mail.fetch(str(i), '(RFC822)' )
            
            for response_part in data:
                arr = response_part[0]
                if isinstance(arr, tuple):
                    msg = email.message_from_string(str(arr[1],'utf-8'))
                    email_subject = msg['subject']
                    date = msg['Date']
                    email_from = msg['from']
                    print(msg,'the message is')
                    save_pdf(msg)
                    # writer.writerow({'email':email_from,"subject":email_subject,"message":msg})
                    # print('From : ' + email_from + '\n')
                    # print('Subject : ' + email_subject + '\n')
                    # print('msg : ' , msg )
            # print(data,'the iterm are ');
    except Exception as e:
        traceback.print_exc() 
        print(str(e))
intern = [];
def save_pdf(msg):
    for part in msg.walk():
        if part.get_content_type() == 'application/pdf':
        # When decode=True, get_payload will return None if part.is_multipart()
        # and the decoded content otherwise.
            payload = part.get_payload(decode=True)

        # Default filename can be passed as an argument to get_filename()
            filename = part.get_filename()
            print(filename,'the filename is');

        # Save the file.
            if payload and filename:
                intern.append({'email':msg['from'],"subject":msg['subject'],"date":msg['Date'],"attchment":filename})
                with open(filename, 'wb') as f:
                    f.write(payload)

read_email_from_gmail()
save_files()