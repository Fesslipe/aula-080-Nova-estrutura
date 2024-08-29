import requests

def send_simple_message(subject, body):
    MAILGUN_DOMAIN = 'x'  # Substitua pelo seu domínio Mailgun
    MAILGUN_API_KEY = 'x'  # Substitua pela sua chave API Mailgun
    FROM_EMAIL = 'Excited User <x>'  # Substitua pelo e-mail do remetente
    TO_EMAILS = ['x', 'x', 'x']  # Substitua pelos e-mails destinatários

    response = requests.post(
        f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
        auth=("api", MAILGUN_API_KEY),
        data={
            "from": FROM_EMAIL,
            "to": ", ".join(TO_EMAILS),
            "subject": subject,
            "text": body
        }
    )
    
    if response.status_code == 200:
        print("Email enviado com sucesso!")
    else:
        print(f"Falha ao enviar o e-mail: {response.status_code}")
        print(response.text)
    
    return response
