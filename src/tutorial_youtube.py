import urllib.request 
import urllib.parse
import re 

url = 'https://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&format=xmlfm&titles=The%20Simpsons&rvsection=0'
#url = 'http://pythonprogramming.net'
values = {'s': 'basics',
			'submit': 'search'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request (url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

#print(respData)

paragraphs = re.findall(r"=(.*?)\\n", str(respData))
for eachP in paragraphs:
	print(eachP)

