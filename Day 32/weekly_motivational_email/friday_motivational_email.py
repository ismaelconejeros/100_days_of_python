import smtplib
import datetime as dt
import random


with open(r'C:\Users\isma\Desktop\VSC\\100_days_of_python\\100_days_of_python\Day 32\weekly_motivational_email\quotes.txt') as quotes:
    data = quotes.readlines()
    data = [i.replace("\n", "") for i in data]

my_email = "test.for.smtplib90@gmail.com"
my_password = "smtplibtest01"
to_adress = "dtl15081986@gmail.com"

msg_subject = "It's friday, I'm in love"
msg_body = random.choice(data)
my_msg = f"Subject: {msg_subject}\n\n{msg_body}"

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 4:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=to_adress, 
            msg=my_msg
            )
