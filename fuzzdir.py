#!/usr/bin/python

import requests, os, sys, argparse
from colorama import Fore, Back, Style, init
init(autoreset=True)

parser = argparse.ArgumentParser(prog='FuzzDir', description='Find directories')
parser.add_argument("--url", help="URL", type=str, required=True, metavar='The URL')
parser.add_argument("--dic", help="The path where the txt file is located", type=str, default='common.txt', metavar='File Path')
args = parser.parse_args()
	
def readFile(filePath):
	if os.path.exists(filePath):
		with open(filePath, 'r') as item:
			try:
				for line in item:
					request = requests.get(args.url+'/'+line)
					if request.status_code == 200:
						print( Fore.GREEN + "Status Code: " + str(request.status_code) + ' ------------ Path: '+ line)
			except Exception as e:
				print e
	else:
		print "File not Found"
	
def main(args):

	if (len(sys.argv) < 2) | (len(sys.argv) > 4):
		sys.exit('Invalid number of parameters, use -h for help')

	print("=========================================================================")
	print("                 Finding possible paths in "+args.url+ "                 ")
	print("=========================================================================")
	readFile(args.dic)
	print("=========================================================================")

if __name__ == '__main__':
	main(args)
	sys.exit()
