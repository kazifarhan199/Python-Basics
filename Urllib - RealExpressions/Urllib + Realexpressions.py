import urllib.request
import urllib.parse
import re

url = 'https://pythonprogramming.net'

value={'q':'python3'}
data=urllib.parse.urlencode(value)
data=data.encode('utf-8')
headers={}
headers['User-Agent'] =  'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
resp=urllib.request.Request(url,headers=headers)
main=urllib.request.urlopen(resp)
opt=main.read()

paragrphs = re.findall(r'<p>(.*?)</p>',str(opt))    #'<p>(.*?)</p>' to find values betwee<p> and </p> which is .*? (this combination means everything)

for ea in paragrphs:
	print(ea)
