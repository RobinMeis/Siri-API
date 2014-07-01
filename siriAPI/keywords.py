class keywords:
    def __init__ (self, SiriAPI):
        self.SiriAPI = SiriAPI
        self.keywords = []
        self.keywords.append({'find': None, 'call': 'keywords.error', 'case_sensitive': False})
        return
        
    def add (self, find, call, case_sensitive=True): #Add keywords
        self.keywords.append({'find': [find], 'call': call, 'case_sensitive': case_sensitive})
        return (len(self.keywords) - 1)
        
    def modify (self, id, find, call, case_sensitive): #Modify keywords by id
        try:
            if (find == -1): #Keep old values if not overwritten
                find = self.keywords[id]['find']
                
            if (call == -1):
                call = self.keywords[id]['call']
                
            if (case_sensitive == -1):
                case_sensitive = self.keywords[id]['case_sensitive']
                
            self.keywords[id] = {'find': [find], 'call': call, 'case_sensitive': case_sensitive}
            return (True)
        except:
            return (False)
        
    def remove (self, id): #Remove keywords by id
        if (id != 0): #Make it impossible to delete the not found rule
            try:
                del self.keywords[id]
                return (True)
            except:
                return (False)
        else:
            return (False)
            
    def list (self): #List all keywords
        return (self.keywords)
