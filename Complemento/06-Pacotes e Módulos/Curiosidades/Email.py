import smtplib

sender_mail = input("Enter your gmail: ")
receivers_mail = input("Enter receivers gmail: ")

message = """From: From Person %s
To: To Person %s
Subject: Sending SMT e-mail
This is a test e-mail message.
""" % (sender_mail, receivers_mail)

try:
    password = input('Enter your password: ')
    smtpObj = smtplib.SMTP('gmail.com', 587)
    smtpObj.login(sender_mail, password)
    smtpObj.sendmail(sender_mail, receivers_mail, message)
    print("Sucessfully sent mail")
except Exception:
    print("Error: unable to send email")
