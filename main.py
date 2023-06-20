

import smtplib

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kaiserjaey@gmail.com','duhiyllyuimdzpcr')
    server.sendmail('kaiserjaey@gmail.com',to,content)
    server.close()


if __name__ == '__main__':
    try:
        content = input('Type your text \n')
        to = input('receiver\'s email \n')
        sendEmail(to, content)
        print('Email sent successfully')
    except Exception as e:
        print(e)
        print('Email not sent')