import os
passkey = ""
'''id=os.popen("vcgencmd otp_dump | grep '28:'").read()
id=id.strip()
print(id)
wlan=os.popen('ethtool --show-permaddr wlan0').read()
wlan=wlan.strip()
print(wlan)'''

id = "28:d402234e"

def menu(passkey):
	while(True):
		if(passkey=="ccnet"):
			while(True):
				os.system("clear")
				print("Welcome to CCThinClient !!")
				print("\n")
				print("1 - Config Display")
				print("2 - Config IP / Subnet / DNS")
				print("3 - Connect to Server")
				n = input("Enter your choice : ")

				if(n=="1"):
					os.system("sudo nano /boot/config.txt")
				elif(n=="2"):
					os.system("sudo nano /etc/dhcpcd.conf")
				elif(n=="3"):
							#print("StartX - 3")
					os.system("startx")
				else:
					print("Invalid Input, please try again.")
					quit()
					
		else:
			passkey = ""
			print("Invalid Password, please try again.")
			passkey = input("Enter your password : ")
		
		


if(id=="28:d402234e"):
	passkey = input("Enter your password : ")
	menu(passkey)


else:
	print("Licence Violation !! Contact CC Network Solutions @ www.ccnet.in")
#	print("Invalid Password")3