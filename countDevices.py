import urllib2
import xml.etree.ElementTree as ET
import sys
import os
import time
import datetime

ip_address = "" 
apiKey = ""
startTime = time.time()
filePath = os.path.join('C:/', 'CountDevices' + datetime.datetime.now().strftime("_%m-%d-%y_%S") + '.txt')
logString =  "*****Script started*****"

def getTime(): #Gets the current time and formats it
	time = datetime.datetime.now().strftime("%m-%d-%y %H:%M:%S")
	return time

def setLog(logString): #Logs to a file and appends newlines
	with open(filePath, 'a') as logFile:
		logFile.write(getTime() + " : " + logString + '\n')

def print_menu():       ## Design menu
    print 30 * "-" , "MENU" , 30 * "-"
    print "1. Item 1"
    print "2. Item 2"    
    print "3. Exit"
    print 67 * "-"
  
loop = True      
  
while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = input("Enter your choice [1-3]: ")
     
    if choice==1:     
        print "Corp Panorama has been selected"
        ip_address = "x.x.x.x"
        apiKey = "&key=APIKEY"
        loop=False
    elif choice==2:
        print "EMS Panorama has been selected"
        ip_address = "x.x.x.x"
        apiKey = "&key=APIKEY"
        loop=False
    elif choice==3:
        print "Menu 5 has been selected"
        loop=False 
    else:
        raw_input("Wrong option selection. Enter any key to try again..")

def GetAllHosts(): #Returns a list hostnames of every host in Panorama. 
	try:
		cmd = '&cmd=<show><devices><all></all></devices></show>'
		url = 'https://'+ ip_address +'/api/?type=op'+ apiKey + cmd
		response = urllib2.urlopen(url) #Basically a curl
		html = response.read() #Read the curl and assign it to string variable
		logString = "HTML accessed : " + url
		setLog(logString)
	except:
		logString = "Invalid credentials or IP address. Check username and password"
		setLog(logString)

	contents = ET.fromstring(html) #import the xml through a string

	deviceList = []
	for item in contents.findall('./result/devices/entry/hostname'):
				#print item.attrib['name']
				#deviceList.append(item.attrib['name'])
				deviceList.append(item.text)
				#logString = item.attrib['name']
				#logString = "Added " + logString + " to Device List"
				#setLog(logString)

	return deviceList;

def GetAllConnectedHosts(): #Returns a list hostnames of every host that is connected in Panorama.
	try:
		cmd = '&cmd=<show><devices><connected></connected></devices></show>'
		url = 'https://'+ ip_address +'/api/?type=op'+ apiKey + cmd
		response = urllib2.urlopen(url) #Basically a curl
		html = response.read() #Read the curl and assign it to string variable
		logString = "HTML accessed : " + url
		setLog(logString)
	except:
		logString = "Invalid credentials or IP address. Check username and password"
		setLog(logString)

	contents = ET.fromstring(html) #import the xml through a string

	deviceList = []
	for item in contents.findall('./result/devices/entry/hostname'):
				#print item.attrib['name']
				#deviceList.append(item.attrib['name'])
				deviceList.append(item.text)
				#logString = item.attrib['name']
				#logString = "Added " + logString + " to Device List"
				#setLog(logString)

	return deviceList;


allHostsList = GetAllHosts()
allConnectedList = GetAllConnectedHosts()
allHosts = len(allHostsList)
allConnected = len(allConnectedList)
print ""
print "Corp Panorama - Total Devices : " + str(allHosts) #len counts how many items are in the list
print "Corp Panorama - Actual Connected : " + str(allConnected)
print ""
