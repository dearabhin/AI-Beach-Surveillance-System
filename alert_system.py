import smtplib
from twilio.rest import Client

def send_email_alert():
    sender_email = "your_email@example.com"
    receiver_email = "alert_receiver@example.com"
    password = "your_password"

    message = """\
    Subject: Beach Alert

    A person has crossed the danger zone on the beach."""

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        print("Alert email sent!")
    except Exception as e:
        print(f"Error: {e}")

def send_sms_alert():
    account_sid = "your_account_sid"
    auth_token = "your_auth_token"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="A person has crossed the danger zone on the beach.",
        from_="+1234567890",
        to="+0987654321"
    )
    print(f"SMS sent: {message.sid}")
