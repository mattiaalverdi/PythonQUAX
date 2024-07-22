import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, body, to_email, from_email, smtp_server, smtp_port, login, password):
    try:
        # Crea il messaggio
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        # Aggiungi il corpo del messaggio
        msg.attach(MIMEText(body, 'plain'))

        # Connessione al server SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(login, password)

        # Invia l'email
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()

        print(f"Email inviata con successo a {to_email}")

    except Exception as e:
        print(f"Errore durante l'invio dell'email: {e}")

if __name__ == "__main__":
# Configura i dettagli dell'email
    # for i in range(10): + str(i) + str(i*i+1)
    subject = "spamQUAX" 
    body = "mi scuso per l'errore, indirizzo email errato"
    to_email = "filippo.toffano@studenti.unipd.it"
    from_email = "quaxlegnaro@gmail.com"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587  # Porta per TLS
    login = "quaxlegnaro@gmail.com"
    password = "bsjp qzyf aqlh qjxh"
# Invia l'email
send_email(subject, body, to_email, from_email, smtp_server, smtp_port, login, password)
