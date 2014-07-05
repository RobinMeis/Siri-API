class search:
    def __init__ (self, siri_api):
        self.siri_api = siri_api
        
    def search (self, q, output): #search for matching
        if (self.siri_api.case_sensitive == False): #case sensitive or not?
            q_search = q.lower()
        else:
            q_search = q
            
        self.output = output
        for keywords in self.siri_api.action.actions[:]: #Complicated search algorithm ;)
            for keyword in keywords['find'][:]:
                for find in keyword[:]:
                    if (isinstance(find, list) == False):
                        if (find == q):
                            return (keywords['call'](self.output, q, None))
                            return
                    else:
                        found = True
                        have_to_follow = True
                        cursor = 0
                        wildcard_counter = -1
                        wildcard_start = 0
                        wildcard_end = -1
                        wildcards_found = {}
                        for search in find[:]:
                            if (search == '*'):
                                wildcard_counter += 1
                                have_to_follow = False
                                wildcard_start = cursor
                            else:
                                position = q.find(search, cursor)
                                
                                if (position == cursor):
                                    cursor += len(search) + 1
                                    wildcard_end = position
                                elif (position > cursor and have_to_follow == False):
                                    
                                    cursor = position + len(search) + 1
                                    have_to_follow = True
                                    wildcard_end = position - 1
                                else:
                                    found = False
                                    break
                                
                                if (wildcard_end > -1):
                                    wildcards_found[wildcard_counter] = q[wildcard_start:wildcard_end]
                                    wildcard_start = 0
                                    wildcard_end = 0
                                
                                if (find[-1] == "*" and find[-2] == search):
                                    wildcards_found[wildcard_counter + 1] = q[cursor:]
                                    wildcard_counter += 1
                                    
                                    
                        if (found == True):
                            return (keywords['call'](self.output, q, wildcards_found))
                            return
                        
        return (self.siri_api.action.actions[0]['call'](self.output, q, None))
        return