import smtplib, ssl


def send_mail(message):
    host = "smtp.gmail.com"
    port = 465
    username = "dev.solve.repeat@gmail.com"
    password = "uaebdeabihqzfvcl"
    receiver = "dev.solve.repeat@gmail.com"
    my_context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)



