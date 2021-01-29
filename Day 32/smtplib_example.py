import smtplib
#Enter to email account configuration and set security to lowest

my_email = "test.for.smtplib90@gmail.com"
my_password = "smtplibtest01"

to_adress = "dtl15081986@gmail.com"

msg_subject = "Hello"
msg_body = "This is an email"
my_msg = f"Subject: {msg_subject}\n\n{msg_body}"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs=to_adress, 
        msg=my_msg
        )