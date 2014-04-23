import http.server
import socketserver
import threading
import time

from commands import commands
from search import search

######################
# Configuration area #
######################

squid_hostname = "zimmer" # Hostname or IP address of the server which is running squid proxy
squid_port = 3128 # Port of squid (change only if you changed it in squid configuration)
google_domain = ".google.co.uk" # Domain of "the" Google which is opened from your language. Consult readme for more information
keyword = "Siri" # By default this is siri. You can change this to any other (well recognized) keyword, CASE SENSITIVE!!!

######################

class Handler(http.server.SimpleHTTPRequestHandler):
	def do_HEAD(self):
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()

	def do_GET(self):
		global squid_hostname
		global squid_port
		global google_domain
		global keyword
		
		parts = self.path.split("?") #Extract requested file and get parameters from path
		path = parts[0]
		
		#Extract variables from get parameters
		try:
			arguments = {}
			arguments["q"] = None #Variable for search request. Default None to prevent errors if no search request was started
			if (len(parts) > 1):
				raw_arguments = parts[1].split("&")
				for raw_argument in raw_arguments[:]:
					argument = raw_argument.split("=", 1)
					arguments[argument[0]] = argument[1]
		except:
			print ("No get parameters")
		
		print (path)
		
		#Decide wether a search or the style.css was requested
		if (path == "/style.css"):
			self.document = open('style.css', 'r').read()
			self.send_header('Content-type', 'text/html')
			self.send_response(200)
			self.end_headers()
			self.wfile.write(bytes(self.document, "utf-8"))
		elif (path == "/proxy.pac"):
			self.document = open('proxy.pac', 'r').read()
			self.document = self.document.replace('<keyword>', keyword.lower(), 1)
			self.document = self.document.replace('<google_domain>', google_domain, 1)
			self.document = self.document.replace('<squid_host>', squid_hostname, 1)
			self.document = self.document.replace('<squid_port>', str(squid_port), 1)
			self.send_header('Content-type', 'x-ns-proxy-autoconfig')
			self.send_response(200)
			self.end_headers()
			self.wfile.write(bytes(self.document, "utf-8"))
		elif (arguments["q"] != None):
			arguments["q"] = arguments["q"].replace(keyword + '+', '', 1)
			arguments["q"] = arguments["q"].replace('+', ' ')
			command = commands(self)
			search(command).search(arguments["q"])

		return

port = 3030
print ("Starting Server...")

exception = True
while (exception == True): #Solves trouble in autostart mode (when network isn't ready)
	try:
		#(Try) to start webserver
		httpd = socketserver.TCPServer(('', port), Handler)
		threading.Thread(target=httpd.serve_forever).start()
		print('Server listening on port ' + str(port) + '...')
		exception = False
	except:
		print ("Error: Webserver can't be started")
		time.sleep (1)

input ("Press enter to exit")
print ("Shutting down server ...")
httpd.shutdown()
httpd.server_close()
