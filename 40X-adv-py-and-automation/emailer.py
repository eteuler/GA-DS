import smtplib
from secret import password

s = smtplib.SMTP('smtp.gmail.com', 587)
#s = smtplib.SMTP('smtp-mail.oulook.com', 587)

s.ehlo()
s.starttls()

s.login("eteuler@gmail.com", password)

s.sendmail(
    "eteuler@gmail.com"
    "email@gmail.com"
    "Subject: Sending email from Python Script\n Hey whats up?"
)
