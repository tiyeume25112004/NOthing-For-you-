#import library
import requests
import re

headers = {'User-Agent': 'YOu_aR3_Cr4cID-43242oijd',
	       'Date': '2018',
	       'DNT': '3',
	       'Accept-Language': 'sv-SE'
	       }

r = requests.get('{HOST}:{PORT}', headers=headers)
p = re.compile('XAmPP\{.*\}')
flag = p.findall(r.text)[0]
print(flag)
