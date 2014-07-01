class action:
    def __init__ (self, SiriAPI):
        self.SiriAPI = SiriAPI
        self.action = []
        self.action.append({'find': None, 'call': 'action.error', 'case_sensitive': False})
        return
        
    def add (self, find, call, case_sensitive=True): #Add action
        self.action.append({'find': [find], 'call': call, 'case_sensitive': case_sensitive})
        return (len(self.action) - 1)
        
    def modify (self, id, find, call, case_sensitive): #Modify action by id
        try:
            if (find == -1): #Keep old values if not overwritten
                find = self.action[id]['find']
                
            if (call == -1):
                call = self.action[id]['call']
                
            if (case_sensitive == -1):
                case_sensitive = self.action[id]['case_sensitive']
                
            self.action[id] = {'find': [find], 'call': call, 'case_sensitive': case_sensitive}
            return (True)
        except:
            return (False)
        
    def remove (self, id): #Remove action by id
        if (id > 0): #Make it impossible to delete the not found rule
            try:
                del self.action[id]
                return (True)
            except:
                return (False)
        else:
            return (False)
            
    def list (self): #List all action
        return (self.action)
