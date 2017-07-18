import csv

def csv_soter():
	with open('b.csv') as csvfile:
		readCSV  = csv.reader(csvfile, delimiter=',')
		names=[]
		emails=[]

		for i in readCSV:
			email=i[0]
			name=i[1]

			emails.append(email)
			names.append(name)

	return(emails,names)
