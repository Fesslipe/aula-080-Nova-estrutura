import requests
from flask import current_app

def send_simple_message(subject, body):
    return requests.post(
        f"https://api.mailgun.net/v3/{current_app.config['MAILGUN_DOMAIN']}/messages",
        auth=("api", current_app.config['MAILGUN_API_KEY']),
        data={"from": current_app.config['FROM_EMAIL'],
              "to": current_app.config['TO_EMAILS'],
              "subject": subject,
              "text": body}
    )
