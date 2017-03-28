#!/usr/bin/python3
import requests,bs4,webbrowser,sys,time
sterm=' '.join(sys.argv[1:])
res=requests.get('https://www.google.co.in/search?q='+sterm)
res.raise_for_status()
bso=bs4.BeautifulSoup(res.text,"lxml")
linkeles=bso.select('.r a')
webbrowser.open('https://google.com'+linkeles[0].get('href'))
time.sleep(0.5) 
