#!/usr/bin/env python3

import requests as r
import re

api = {
	'base': 'http://en.wikipedia.org/w/index.php?action=raw&title='
}

#shows = ['The_Simpsons', 'The_Mick']
shows = ['The_Simpsons']

def get_url(show):
	return r.get(api['base']+show).text

def infobox(article):
	#return [line in article if '|' in line]
	result = ""
	for line in article:
		re.findall(r'|*',line)[0]
		#if re.findall(r'|', line)[0]:
			#result+=line+'\n'
	#return result

def main():
	for show in shows:
		data = get_url(show)
		data = infobox(data)
		print(data)


if __name__ == '__main__':
	main()