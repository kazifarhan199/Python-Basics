import os 
import time
import re

a=os.getcwd()			#get current working directory
print(a)
b=input('Where to go next? ')

c=re.sub(r'\\',r'\\\\',b)		#can also use re.sub('\\\\','\\\\\\\\',whatever)
os.chdir(c)				#change working directery

print(os.getcwd())

os.mkdir('The name of new directory')			#make directory
time.sleep(4)
os.rename('The name of new directory','new name')	#As rename has path and name to move 
time.sleep(4)									#it to other directory just change the path
												#eg:"os.rename(old//path//a,new//path//a)"

os.rmdir('new name')								#Remove directory
												
