
import smtplib
def sendEmail(sender_email, password, to, subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)

        message = f'From: {sender_email}\nTo: {to}\nSubject: {subject}\n\n{msg}'
        print(message)

        server.sendmail(sender_email, to, message)
        server.quit()
        print("Email Sent")
    except Exception as eg:
    
        print("Some Error Occured")

    try:
        if __name__ == '__main__':
            SENDER_EMAIL= "priyanshisingh.ap97@gmail.com"
            PASSWORD = "Arpit@2019"
            TO = "priyanshisingh.ap97@gmail.com"
            SUBJECT = "Just having fun"
            MESSAGE = "hey dawg! it's my first Email"
            sendEmail(SENDER_EMAIL, PASSWORD, TO, SUBJECT, MESSAGE)
    except Exception as eg:
        pass
