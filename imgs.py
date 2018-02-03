import urllib.request 
from bs4 import BeautifulSoup
import os

url = input('enter a url')
location=input('Enter location')
headers = {}
headers['User-Agent'] =  'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
req=urllib.request.Request(url,headers=headers)
resp = urllib.request.urlopen(req)
page = BeautifulSoup(resp,'html.parser')

j=0

for i in page.findAll('img'):
	img = i.get('data-src')
	names = i.get('alt')+str(j)
	j+=1
	if (img!=None):
		file=open(location+'/'+names+'.png','wb')
		if(img[0]=='/'):
			img='http://www.lamalinks.com/'+img
		file.write(urllib.request.urlopen(img).read())
		print('done')
		file.close()

print(os.getcwd())