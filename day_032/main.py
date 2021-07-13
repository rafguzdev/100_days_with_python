# Extra Hard Starting Project #
import random
import smtplib
import pandas as pd
import datetime

my_email = 'mateusz40000@gmail.com'
password = '*********'

# Check if today matches a birthday in the birthdays.csv
df = pd.read_csv('birthdays.csv')
data = df.to_dict('records')
now = datetime.datetime.now()
day = now.day
month = now.month
for parent in data:
    birth_day = parent['day']
    birth_month = parent['month']
    who = parent['name']
    if day == birth_day and month == birth_month:
        print(f'dzis urodziny ma: {who}')
        i = random.randint(1, 3)
        with open(f'letter_templates/letter_{i}.txt') as f:
            letter = str(f.read())
            letter = letter.replace('[NAME],', who)
            email = parent['email']
            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email,
                                    to_addrs=email,
                                    # to_addrs='rafguzdev@gmail.com',
                                    msg=f'Subject:Birthday!\n\n{letter}.'
                                    )
