##################### Extra Hard Starting Project ######################
# imports
import datetime as dt
import pandas as pd
import random
import smtplib

sender_email = "sender email"
sender_app_password = "App password"



today = dt.datetime.now()
today_tuple = (today.month,today.day)

data = pd.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"],data_row["day"]): data_row for (index,data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter:
        content = letter.read()
        content = content.replace("[NAME]", birthday_person["name"])

    try:
        # Establishing a connection to the SMTP server
        with smtplib.SMTP("smtp.gmail.com", 587) as connection: # Specify the port
            connection.starttls()  # Secure the connection
            connection.login(user=sender_email, password=sender_app_password)
            connection.sendmail(
                from_addr=sender_email, 
                to_addrs=birthday_person["email"], 
                msg=f"Subject:Happy Birthday\n\n{content}")  # Including subject line
        print("Email sent successfully")
    except Exception as e:
        print(f"An error occurred: {e}")
        