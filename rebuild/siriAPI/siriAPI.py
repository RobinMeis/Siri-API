import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))
print (os.getcwd())
from siriAPI.squid import squid #TODO make it universal!
from siriAPI.server import server
from siriAPI.keywords import keywords

class siri_api:
    def __init__ (self):
        #Userdefined variables
        self.hostname = None
        self.google_domain = None
        
        #Predefined variables
        self.keyword = "Siri"
        self.port = 3030
        
        #Initialize class instances of subclasses
        self.squid = squid(self)
        self.server = server(self)
        self.keywords = keywords(self)
        
    #Google domain of your country
    def set_google_domain (self, google_domain):
        if (isinstance(google_domain, str)):
            self.google_domain = google_domain
        else:
            raise Exception("Google domain has to be a string")
            
    def get_google_domain (self):
        return (self.google_domain)
        
    #Keyword
    def set_keyword (self, keyword):
        if (isinstance(keyword, str)):
            self.keyword = keyword
        else:
            raise Exception("Keyword has to be a string")
    
    def get_keyword (self):
        return (self.keyword)
        
    