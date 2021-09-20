# sendemail.py
# this programme sends an email via gmail
# Author Fatima Zeino

import smtplib

username = 'fatimaprog2021@gmail.com'
password = 'fatima@2021'
toemail = 'fatemazeno.fz@gmail.com'
massege = 'hi this an test email'

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

server.login(username,password)
server.sendmail(username, toemail, massege)

print ("Done")