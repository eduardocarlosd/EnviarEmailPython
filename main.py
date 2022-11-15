import email
import smtplib

msg = email.message_from_string('''Mensagem''') # Mensagem
msg['From'] = "eduardocarlosbsi@outlook.com"
msg['To'] = "eduardocarlosds1@gmail.com"
msg['Subject'] = "Assunto" # assunto

s = smtplib.SMTP("smtp.office365.com",587)
s.ehlo()
s.starttls()
s.ehlo()
s.login('eduardocarlosbsi@outlook.com', 'geqfjsnpnrmopzsi')

s.sendmail("eduardocarlosbsi@outlook.com", "eduardocarlosds1@gmail.com", msg.as_string())

s.quit()