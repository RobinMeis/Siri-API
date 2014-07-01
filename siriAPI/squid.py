class squid:
    def __init__(self, siri_api):
        self.siri_api = siri_api #Parent SiriAPI class instance
        self.port = 3128
        self.hostname = None
      
    #Hostname
    def set_hostname (self, hostname):
        if (isinstance(hostname, str)):
            self.hostname = hostname
        else:
            raise Exception("Hostname has to be a string")
            
    def get_hostname (self):
        if (self.hostname == None):
            return (self.siri_api.hostname)
        else:
            return (self.hostname)
    
    #Port
    def set_port (self, port):
        if (isinstance(port, int)):
            self.port = port
        else:
            raise Exception("Port has to be an integer")
            
    def get_port (self):
        return (self.port)
    
    def start (self):
        raise Exception ("This feature is not available in this version")