class action:
    def __init__ (self, siri_api):
        self.siri_api = siri_api
        self.actions = []
        self.actions.append({'find': "hans", 'call': self.error, 'case_sensitive': False})
        return
        
    def add (self, find, call, case_sensitive=True): #Add action
        self.actions.append({'find': [find], 'call': call, 'case_sensitive': case_sensitive})
        return (len(self.actions) - 1)
        
    def modify (self, id, find, call, case_sensitive=True): #Modify action by id
        try:
            if (find == -1): #Keep old values if not overwritten
                find = self.actions[id]['find']
                
            if (call == -1):
                call = self.actions[id]['call']
                
            if (case_sensitive == -1):
                case_sensitive = self.actions[id]['case_sensitive']
                
            self.actions[id] = {'find': [find], 'call': call, 'case_sensitive': case_sensitive}
            return (True)
        except:
            return (False)
        
    def remove (self, id): #Remove action by id
        if (id > 0): #Make it impossible to delete the not found rule
            try:
                del self.actions[id]
                return (True)
            except:
                return (False)
        else:
            return (False)
            
    def list (self): #List all action
        return (self.actions)
        
    def error (self, q, wildcards_found): #Error message if not overwritten
        print ("error")