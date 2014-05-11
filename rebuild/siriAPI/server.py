import http.server
import socketserver
import threading
import time
import os

#from search import search

os.chdir(os.path.dirname(os.path.abspath(__file__))) # Set working directory to path of server.py

class _Handler(http.server.SimpleHTTPRequestHandler):
    def __init__ (self, squid_hostname, squid_port, google_domain, keyword, *args):
        self.squid_hostname = squid_hostname
        self.squid_port = squid_port
        self.google_domain = google_domain
        self.keyword = keyword
        http.server.SimpleHTTPRequestHandler.__init__(self, *args)
        
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        print ("hi head")

    def do_GET(self):
        print (self.keyword)
        parts = self.path.split("?") #Extract requested file and get parameters from path
        path = parts[0]
        print ("hi get")
        
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
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(self.document, "utf-8"))
        elif (path == "/proxy.pac"):
            self.document = open('proxy.pac', 'r').read()
            self.document = self.document.replace('<keyword>', self.keyword.lower(), 1)
            self.document = self.document.replace('<google_domain>', self.google_domain, 1)
            self.document = self.document.replace('<squid_host>', self.squid_hostname, 1)
            self.document = self.document.replace('<squid_port>', str(self.squid_port), 1)
            self.send_response(200)
            self.send_header('Content-type', 'x-ns-proxy-autoconfig')
            self.end_headers()
            self.wfile.write(bytes(self.document, "utf-8"))
        elif (arguments["q"] != None):
            arguments["q"] = arguments["q"].replace(self.keyword + '+', '', 1)
            arguments["q"] = arguments["q"].replace('+', ' ')
            command = commands(self)
            search(command).search(arguments["q"])
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes('Not found. Please visit <a href="https://github.com/HcDevel/Siri-API/wiki/_pages">https://github.com/HcDevel/Siri-API/wiki/_pages</a>', "utf-8"))

        return

class server:
    def __init__ (self, keywords=None, squid_hostname=None, google_domain=None, keyword="Siri", port=3030, squid_port=3128):
        self.httpd = None
        if (keywords == None or squid_hostname == None or google_domain == None):
            print ('Error: server() has the following syntax: (keywords, squid_hostname, google_domain, keyword="Siri", port=3030, squid_port=3128)')
            return
        else:
            self.keywords = keywords
            self.squid_hostname = squid_hostname
            self.google_domain = google_domain
            self.keyword = keyword
            self.port = port
            self.squid_port = squid_port
            
    def start (self, force=False):
        if (self.httpd == None):
            exception = True
            tried = 0
            while (exception == True and (tried == 0 or force == True)): #Solves trouble in autostart mode (when network isn't ready)
                tried += 1
                try:
                    #self.httpd = socketserver.TCPServer(('', self.port), _Handler)
                    self.httpd = socketserver.TCPServer(('', self.port), lambda *args: _Handler(self.squid_hostname, self.squid_port, self.google_domain, self.keyword, *args))
                    threading.Thread(target=self.httpd.serve_forever).start()
                    print('Success: Server listening on port ' + str(self.port) + '...')
                    exception = False
                except:
                    print ("Error: Webserver can't be started")
                    time.sleep (1)
        else:
            print ("Server is already running")
        
    def stop (self):
        if (self.httpd != None):
            self.httpd.shutdown()
            self.httpd.server_close()
            self.httpd = None
            print ("Success: Server stopped")
        else:
            print ("Error: No running instance of the webserver found")