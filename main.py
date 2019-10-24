import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os


print("--------------------Mention the Sender adress--------------------")

sender_adr = input()

print("Whats your password")
password = input()

print("--------------------Mention the reciever adress-------------------")
reciever_adr = input()

print("Tell me the subject of the mail: ")

subject = input()

print("Whats the content(body) of your mail")
body = input()

msg = MIMEMultipart()

msg['From'] = sender_adr

msg['To'] = reciever_adr

msg['Subject'] = subject

msg.attach(MIMEText(body, 'plain'))

filename = "Papa_Plant.odt"

attachment = open("Papa_Plant.odt", "rb")

p = MIMEBase('application', 'octet-steam')
p.set_payload((attachment).read())

encoders.encode_base64(p)

p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(p) 
  
s = smtplib.SMTP('smtp.gmail.com', 587) 

s.starttls() 

s.login(sender_adr, password) 
  

text = msg.as_string() 
  
s.sendmail(sender_adr, reciever_adr, text) 
print("Done")
s.quit() 



