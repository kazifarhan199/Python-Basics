import csv

with open('b.csv') as csvfile:
	readCSV  = csv.reader(csvfile, delimiter='|')

	dates=[]
	colors=[]

	for r in readCSV:
		color= r[3]
		date = r[0]

		dates.append(date)
		colors.append(color)
	try:												#the try an exception statement
		what_color=input('which color ? ')
		color_index=colors.index(what_color.lower())		# '.lower' is used to convert to lower case

		the_date=dates[color_index]
		print(the_date)

	except Exception as e:								#there are other errors like NameError,etc
		print(e)										#rather than Exception

#print('''Sarya IS A bad girl							#multiline print()
#but she is good too :)''')
