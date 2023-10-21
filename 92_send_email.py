import smtplib

sender = ""
receiver = ""
password = "" # mot de passe d'application (smtp)
subject = "Python email test"
body = "Hello from python"


# header
message = f"""From: {sender}
To: {receiver}
Subject: {subject}
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
  server.login(sender, password)
  print("Logged in...")

  server.sendmail(sender, receiver, message)
  print("Email has been sent")

except smtplib.SMTPAuthenticationError:
  print("unable to sign in")