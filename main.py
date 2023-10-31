import smtplib
import datetime as dt
import random
import config

sender_email = config.sender_email
recipient_email = config.recipient_email
password_email = config.password_email

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quotes:
        quotes_list = quotes.readlines()
        quote_for_today = random.choice(quotes_list)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password_email)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=recipient_email,
            msg=f"Subject:It's gonna be a great day!\n\n{quote_for_today}"
        )





