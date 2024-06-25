import smtplib
import datetime as dt
import random
sender_email = "sender email"
sender_app_password = "App password"

reciver_email = "reciver emamil"

weekday = dt.datetime.now().weekday()



if weekday == 0:
    with open ("quotes.txt") as file:
        quotes = file.readlines()
        quote = random.choice(quotes)
    try:
        # Establishing a connection to the SMTP server
        with smtplib.SMTP("smtp.gmail.com", 587) as connection: # Specify the port
            connection.starttls()  # Secure the connection
            connection.login(user=sender_email, password=sender_app_password)
            connection.sendmail(from_addr=sender_email, to_addrs=reciver_email, msg=f"Subject:Quote of the Day\n\n{quote}")  # Including subject line
        print("Email sent successfully")
    except Exception as e:
        print(f"An error occurred: {e}")

else:
    print("Today is not Monday. No email will be sent.")



