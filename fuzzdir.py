#!/usr/bin/python

import requests, os, sys, argparse
from colorama import Fore, Back, Style, init
init(autoreset=True)

parser = argparse.ArgumentParser(prog='FuzzDir', description='Find directories')
parser.add_argument("--url", help="URL", type=str, required=True, metavar='The URL')
parser.add_argument("--proxy", help="Set proxy", type=str, metavar='Proxy')
parser.add_argument("--useragent", help="Set User Agent", type=str, metavar='User Agent', default='Firefox')
parser.add_argument("--dic", help="The path where the txt file is located", type=str, default='common.txt', metavar='File Path')
args = parser.parse_args()
	
def readFile(filePath):
	CURSOR_UP_ONE = '\x1b[1A'
	ERASE_LINE = '\x1b[2K'
	if os.path.exists(filePath):
		with open(filePath, 'r') as item:
			try:
				for line in item:

					url = 	args.url+'/'+line
					
					request = requests.Session()

					if args.proxy:
						request.proxies = '{"http": "'+args.proxy+'"}'

					if args.useragent:
						request.headers = "{'user-agent': '"+args.useragent+"'}"

					try:

						response = request.get(url)
						response.close()
						code = response.status_code 						
						#command = "curl -I " + url + " 2>/dev/null | head -n 1 | cut -d$' ' -f2"					

						if code == 200:
							print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
							print( Fore.GREEN + "FOUND -  Status Code: " + str(code) + ' --- Path: '+ url  )
						else:						
							print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
							print("Checking - Status Code: " + str(code) + " Path: "+ line ),
					except Exception as e:
						print e
													
			except Exception as e:
				print e

			print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
	else:
		print "File not Found"
	
def main(args):

	if (len(sys.argv) < 2) | (len(sys.argv) > 8):
		sys.exit('Invalid number of parameters, use -h for help')

	print("===================================================================================================")
	print("                 	    Finding possible paths in "+args.url+"                                    ")
	print("===================================================================================================")
	print('')
	readFile(args.dic)
	print("===================================================================================================")

if __name__ == '__main__':
	main(args)
	sys.exit()