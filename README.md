# Email Automation with OTP Authentication

This project demonstrates how to send a **One-Time Password (OTP)** via email using Python’s `smtplib` library. It generates a random 6-digit OTP, sends it to the recipient’s email, and verifies the OTP entered by the user.

---

## Features
- Generates a **6-digit numeric OTP**.
- Sends OTP securely via **Gmail SMTP server**.
- Prompts the user to enter the OTP for verification.
- Validates whether the entered OTP matches the generated one.

---

## Requirements
- Python 3.x
- Gmail account with **App Passwords** enabled (for authentication)
- Libraries:
  - `random`
  - `math`
  - `smtplib`

---

## Setup Instructions

1. **Clone or download** this project.
2. Ensure you have Python installed:
   ```bash
   python --version
   ```
3. Replace the following in the script:
   - "your_email@gmail.com" → your Gmail address
   - `your_app_password` → your Gmail **App Password** (not your regular password).
     - To generate an App Password:
       - Go to [Google Account Security](https://myaccount.google.com/security).
       - Enable **2-Step Verification**.
       - Create an **App Password** for "Mail".
4. Run the script:
   ```bash
   python otp_auth.py
   ```
---

## Code Explanation

### OTP Generation
```python
digits = "0123456789"
OTP = ""
for i in range(6):
    OTP += digits[math.floor(random.random()*10)]
```
- Generates a random 6-digit OTP using digits `0-9`.

### Email Sending
```python
s = smtplib.SMTP("smtp.gmail.com", 587)
s.starttls()
s.login("your_email@gmail.com", "your_app_password")
s.sendmail(user, email, msg)
```
- Connects to Gmail’s SMTP server.
- Logs in using your credentials.
- Sends the OTP to the recipient.

### OTP Verification
```python
while True:
    a = input("enter the otp")
    if a == OTP:
        print("otp is correct")
    else:
        print("wrong otp")
```
- Continuously asks the user to enter the OTP.
- Validates against the generated OTP.

---

## Security Notes
- **Never hardcode your real Gmail password** in the script. Use **App Passwords**.
- Avoid sharing your credentials in public repositories.
- For production, consider using secure libraries like `python-dotenv` to store credentials.

---

## Example Output
```
enter the mail which you want to send otp:
recipient@example.com
enter the otp: 123456
otp is correct
```
