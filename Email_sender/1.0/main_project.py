
def main(from_the_person,passward,subject_of_mail,Email_message):
	import smtplib
	import csv_reader
	this_is_exceptiion_indicator=0

	#csv imports
	emails=csv_reader.csv_soter()[0]
	names=csv_reader.csv_soter()[1]

	#basic smtp
	try:
		mail=smtplib.SMTP('smtp.gmail.com',587)

		mail.ehlo()
		mail.starttls()
		mail.ehlo()

	except Exception as e:
		import Sender_show
		this_is_exceptiion_indicator=1
		Sender_show.internet_problem()

	if this_is_exceptiion_indicator==0:
		try:
			my_email=from_the_person
			passa=passward
			mail.login(my_email,passa)
		except Exception as e:
			import Sender_show
			this_is_exceptiion_indicator=2
			Sender_show.login_problem()

	if this_is_exceptiion_indicator!=2 or this_is_exceptiion_indicator!=2:
		try:
			for i in range(len(names)):
				subjec=subject_of_mail
				text=names[i]+' \n'+str(Email_message)
				message = 'Subject: {}\n\n{}'.format(subjec, text)
				mail.sendmail(my_email,emails[i],message)
				persenr=((i+1)*100/len(names))
				print(str(persenr)+' Persenr complete')
		except Exception as e:
			import Sender_show
			this_is_exceptiion_indicator=3		
			Sender_show.file_problem_or_unknown_problem()

		mail.close()

if __name__ == '__main__':
	main('Your e-mail','Your passward','Subject','Message')
