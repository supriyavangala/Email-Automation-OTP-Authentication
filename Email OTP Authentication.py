#Email Automation OTP Authentication
import random
import math
import smtplib#simple mail transfer protocol libraray

digits = "0123456789"
OTP = ""

for i in range(6):
    OTP += digits[math.floor(random.random()*10)]
otp = OTP + " is your otp"
msg = otp

s = smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("your_email@gmail.com
","your_app_password
")
user="your_email@gmail.com"
email = input("enter the mail which you want to send otp:\n")
s.sendmail(user,email,msg)
while True:
    a = input("enter the otp")
    if a == OTP:
        print("otp is correct")
    else:
        print("wrong otp")
