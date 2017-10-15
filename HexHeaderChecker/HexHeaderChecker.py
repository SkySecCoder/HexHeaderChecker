#!/usr/bin

import os
import sys
import optparse

def main():	
	xxdExist=os.path.exists("/usr/bin/xxd")
	tempFilename="VVTw4TstYB.txt"
	parser = optparse.OptionParser("usage %prog [-f <Name of file>]")
	parser.add_option('-f', dest='fname', type='string',help='Specify file whose header is to be checked')
	(options, args) = parser.parse_args()
	if ((options.fname == None)):
		parser.print_help()
	else:
		nameOfFile = options.fname
		if xxdExist:
			os.system("xxd "+nameOfFile+" | grep 00000000: > "+tempFilename)
			f=open(tempFilename,"r")
			myType = f.readline()
			f.close()
			os.remove(tempFilename)
			myTypeRefined = myType[10:19]
			myTypeRefined = myTypeRefined.upper()
			checkType(myTypeRefined)
		else:
			print("XXD not installed")
def checkType(data):
	i=0
	allTypes = {"jpeg":"FFD8 FFE0",
			"zip":"504B 0304",
			"wmv":"3026 B275",
			"Word":"D0CF 11E0",
			"tgz":"1F9D 9070",
			"pdf":"2550 4446",
			"mp3v1":"4944 332E",
			"mp3v2":"4944 3303"
			}
	for key in allTypes:
		if allTypes[key]==data:
			print("[+] This is a "+key+" file...")
			i=1
			break
	if i==0:
		print("[-] File format not recognized.")

if __name__=="__main__":
	main()
