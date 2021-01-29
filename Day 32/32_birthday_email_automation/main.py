import datetime as dt
import pandas as pd
import random
import smtplib

now = dt.datetime.now()

data = pd.read_csv("100_days_of_python\Day 32\\32_birthday_email_automation\\birthdays.csv")
df = pd.DataFrame(data)
targets = {row['name']:row['email'] for index, row in df.iterrows() if row['month'] == now.month and row['day']}

letters = [
    '100_days_of_python\Day 32\\32_birthday_email_automation\letter_templates\letter_1.txt',
    '100_days_of_python\Day 32\\32_birthday_email_automation\letter_templates\letter_2.txt',
    '100_days_of_python\Day 32\\32_birthday_email_automation\letter_templates\letter_3.txt',
]

if len(targets) != 0:
    for person in targets:
        my_email = "test.for.smtplib90@gmail.com"
        my_password = "smtplibtest01"
        to_adress = targets[person]
        to_name = person

        letter_file = random.choice(letters)
        with open(letter_file) as file:
            letter = file.readlines()
            letter = [i.replace('[NAME]', to_name) for i in letter]
            letter = "".join(letter)

        msg_subject = f"Happy Birthday {to_name}!"
        msg_body = letter
        my_msg = f"Subject: {msg_subject}\n\n{msg_body}"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs=to_adress, 
                msg=my_msg)