import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

# Betölti a .env fájlt
load_dotenv()

# Hozzáférés a környezeti változókhoz
host = os.getenv("MAIL_SMTP")
password = os.getenv("MAIL_PASSWORD")
username = os.getenv("MAIL_USERNAME")
port = os.getenv("MAIL_PORT", default=587)

sender_email = "kuldo@mailproba.com"
sender_name = "Küldő Neve"
receiver_email = "fogado@mailproba.com"
receiver_name = "Fogadó Neve"

# MIME üzenet létrehozása
message = MIMEMultipart()
message["Subject"] = "Teszt üzenet ékezetes karakterekkel"
message["From"] = f"{sender_name} <{sender_email}>"
message["To"] = f"{receiver_name} <{receiver_email}>"

# Az üzenet törzse UTF-8 kódolással
body = """
Szia!

Ez egy teszt e-mail üzenet magyar ékezetes karakterekkel:
árvíztűrő tükörfúrógép ÁRVÍZTŰRŐ TÜKÖRFÚRÓGÉP

Üdvözlettel,
A rendszer
"""

# A szöveget hozzáadjuk UTF-8 kódolással
message.attach(MIMEText(body, "plain", "utf-8"))

# Automatikusan lezárja a kapcsolatot, amikor nincs több utasítás
with smtplib.SMTP(host, port) as connection:
    connection.starttls()
    connection.login(user=username, password=password)
    #Levél kiküldés
    connection.sendmail(
        from_addr=sender_email,
        to_addrs=receiver_email,
        msg=message.as_string()
    )
