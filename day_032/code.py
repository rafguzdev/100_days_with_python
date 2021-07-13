import smtplib
import datetime as dt
import random

my_email = 'mateusz40000@gmail.com'
password = '*********'

now = dt.datetime.now()
if now.weekday() == 1: 
    with open('quotes.txt', 'r', encoding="utf8") as f:
        quote = random.choice(list(f)).strip()
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs='rafguzdev@gmail.com',
                                msg=f'Subject:Motivation\n\n{quote.encode("utf-8")}.'
                                )
