import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = "insert email here"
MY_EMAIL_PASSWORD = "insert password here"

# Identify day and month of current day
current_day = dt.datetime.now().day
current_month = dt.datetime.now().month

# Read csv birthdays with pandas
data = pandas.read_csv("birthdays.csv")

birthdays_dict = data.to_dict(orient="records")

for item in birthdays_dict:
    birthday_day = item["day"]
    birthday_month = item["month"]
    birthday_person = item["name"]
    person_email = item["email"]

    if current_day == birthday_day and current_month == birthday_month:
        file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
        with open(file_path) as letter_file:
            contents = letter_file.read()
            contents = contents.replace("[NAME]", birthday_person)

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_EMAIL_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=person_email,
                msg=f"Subject: Happy Birthday!\n\n{contents}")
