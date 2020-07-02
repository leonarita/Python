senders_email = "void.naoki@gmail.com"
senders_passwd = ""
reciever_email = "void.naoki@gmail.com"
message = "Hello, there"


def func1():
    import smtplib
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(senders_email, senders_passwd)
    s.sendmail(senders_email, reciever_email, message)
    s.quit()


def func2():
    import re
    normal_text = "hello, there. My email is helloworld@gmail.com"
    pattern = re.compile("[a-zA-Z0-9] + \@[a-zA-Z0-9] + \.[a-zA-Z] +")
    email = pattern.findall(normal_text)
    print(email)


#func1()
func2()