import smtplib
import csv_reader

#content='Example email stuff hear'

mail=smtplib.SMTP('smtp.gmail.com',587) #server , port

#helo - for SNTP
#ehlo - for extended SNTP

mail.ehlo()

TEXT='Ha ha ha'
SUBJECT='I am Farhan'

message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

#TLS mode - transport layer security
mail.starttls()

mail.login('Kazifarhan199@gmail.com','Firefox10@')

mail.sendmail('kazifarhan199@gmail.com','farhankazi43@gmail.com',message)

mail.close()
