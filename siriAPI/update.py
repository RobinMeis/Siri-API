import time
import urllib.request

class update: #DONT WORRY! IT IS NOT USED IN THE CURRENT VERSION
    def __init__ (self):
        #Configuration area
        self.check_for_updated = True #Check for updates. By default true. It is secure since the update file is hosted on GitHub servers
        self.update_url = 'https://raw.githubusercontent.com/HcDevel/Siri-API/gh-pages/update.txt' #Update file is hosted on GitHub servers
        self.update_period = 86400 #Update period in seconds. By default 1 day (=86400 seconds)
        
        #DONT CHANGE ANYTHING BELOW THIS COMMAND!
        self.this_version = '1.2.0'
        self.update_information = {'newer': False, 'version': None, 'notes': None, 'auto': True}
        
        self.check()
        
    def check(self):
        if (self.last_update + self.update_period < time.time()):
            self.last_update = time.time()
            f = urllib.request.urlopen(self.update_url)
            print(f.read())
            
    def do(self):
        if (self.update_information != None):
            
    def server(self): #Returns information to the server.py
        
    
test = update()