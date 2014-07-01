class actions:
    def __init__ (self, SiriAPI):
        self.SiriAPI = SiriAPI
        self.actions = []
        self.actions.append({'find': None, 'call': 'actions.error', 'case_sensitive': False})
        return
        
    def add (self, find, call, case_sensitive=True): #Add actions
        self.actions.append({'find': [find], 'call': call, 'case_sensitive': case_sensitive})
        return (len(self.actions) - 1)
        
    def modify (self, id, find, call, case_sensitive): #Modify actions by id
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
        
    def remove (self, id): #Remove actions by id
        if (id > 0): #Make it impossible to delete the not found rule
            try:
                del self.actions[id]
                return (True)
            except:
                return (False)
        else:
            return (False)
            
    def list (self): #List all actions
        return (self.actions)
