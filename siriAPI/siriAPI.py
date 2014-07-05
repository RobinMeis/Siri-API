import os

from .squid import squid
from .server import server
from .action import action
from .search import search

class siri_api:
    def __init__ (self):
        #Userdefined variables
        self.hostname = None
        self.google_domain = None
        
        #Predefined variables
        self.keyword = "Siri"
        self.port = 3030
        self.case_sensitive = False
        
        #Initialize class instances of subclasses
        self.squid = squid(self)
        self.server = server(self)
        self.action = action(self)
        self.search = search(self)
        
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
        
    #Case sensitive
    def set_case_sensitive (self, value): #If you want SiriAPI to be case sensitive set to True
        if (isinstance(value, bool)):
            self.case_sensitive = value
        else:
            raise Exception('Value has to be a boolean')

    def get_case_sensitive (self):
        return (self.case_sensitive)
        
    