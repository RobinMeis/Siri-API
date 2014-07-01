import http.server
import socketserver
import threading
import time
import os
os.chdir(os.path.dirname(os.path.realpath(__file__))) #Make sure to change the working directory to import html, css and pac file

class _Handler(http.server.SimpleHTTPRequestHandler):
    def __init__ (self, siri_api, *args):
        self.siri_api = siri_api
        http.server.SimpleHTTPRequestHandler.__init__(self, *args)
        
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
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
        
        
        #Decide whether a search or the style.css was requested
        if (path == "/style.css"):
            self.document = open('style.css', 'r').read()
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(self.document, "utf-8"))
        elif (path == "/proxy.pac"):
            self.document = open('proxy.pac', 'r').read()
            self.document = self.document.replace('<keyword>', self.siri_api.keyword.lower(), 1)
            self.document = self.document.replace('<google_domain>', self.siri_api.google_domain, 1)
            self.document = self.document.replace('<squid_host>', self.siri_api.squid.get_hostname(), 1)
            self.document = self.document.replace('<squid_port>', str(self.siri_api.squid.port), 1)
            self.send_response(200)
            self.send_header('Content-type', 'x-ns-proxy-autoconfig')
            self.end_headers()
            self.wfile.write(bytes(self.document, "utf-8"))
        elif (arguments["q"] != None):
            arguments["q"] = arguments["q"].replace(self.siri_api.keyword + '+', '', 1)
            arguments["q"] = arguments["q"].replace('+', ' ')
            command = commands(self)
            search(command).search(arguments["q"])
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes('Not found. Please visit <a href="https://github.com/HcDevel/Siri-API/wiki/_pages">https://github.com/HcDevel/Siri-API/wiki/_pages</a>', "utf-8"))

        return
        
    def log_message(self, format, *args): #Disable logging
        pass
        
    def log_error(self, format, *args):
        pass
    
class server:
    def __init__(self, siri_api):
        self.siri_api = siri_api #Parent SiriAPI class instance
        self.port = 3030
        self.hostname = None
        self.httpd = None
      
    #Hostname
    def set_hostname (self, hostname):
        if (isinstance(hostname, str)):
            self.hostname = hostname
            self.siri_api.hostname = hostname
        else:
            raise Exception("Hostname has to be a string")
            
    def get_hostname (self):
        return (self.hostname)
    
    #Port
    def set_port (self, port):
        if (isinstance(port, int)):
            self.port = port
        else:
            raise Exception("Port has to be an integer")
            
    def get_port (self):
        return (self.port)
        
    #Start server
    def start (self, force=False):
        if (self.hostname == None):
            raise Exception ("Hostname for the server has to be set")
        elif (self.siri_api.google_domain == None):
            raise Exception ("Google domain has to be set")
        else:
            if (self.httpd == None):
                exception = True
                tried = 0
                while (exception == True and (tried == 0 or force == True)): #Solves trouble in autostart mode (when network isn't ready)
                    tried += 1
                    try:
                        self.httpd = socketserver.TCPServer(('', self.port), lambda *args: _Handler(self.siri_api, *args))
                        threading.Thread(target=self.httpd.serve_forever).start()
                        print('Success: Server listening on port ' + str(self.port) + '...')
                        exception = False
                    except:
                        raise Exception ("Error: Webserver can't be started")
                        time.sleep (1)
            else:
                print ("Server is already running")
        
    #Stop server
    def stop (self):
        if (self.httpd != None):
            self.httpd.shutdown()
            self.httpd.server_close()
            self.httpd = None
            print ("Success: Server stopped")
        else:
            print ("Error: No running instance of the webserver found")

class server_old:
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