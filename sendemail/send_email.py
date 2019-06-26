import smtplib
#import config

def send_email(to_address,subject,msg):
    EMAIL_ADDRESS = 'automail.msconstructions@gmail.com'
    PASSWORD = 'RMurugan@123'
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(EMAIL_ADDRESS,PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject,msg)
        server.sendmail(EMAIL_ADDRESS,to_address,message)
        server.quit()
        print('Success!, Message Sent to {}'.format(to_address))
    except:
        print('Error: Message Not Sent!')

