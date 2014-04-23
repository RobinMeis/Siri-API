class search:
	def __init__ (self, command):
		self.command = command
		
	def search (self, q): #search for matching
		for keywords in self.command.keywords[:]:
			for keyword in keywords['find'][:]:
				if (isinstance(keyword, list) == False):
					if (keyword == q):
						getattr(self.command, keywords['call'])(q, None)
						return
				else:
					found = True
					have_to_follow = True
					cursor = 0
					wildcard_counter = -1
					wildcard_start = 0
					wildcard_end = -1
					wildcards_found = {}
					for search in keyword[:]:
						if (search == '*'):
							wildcard_counter += 1
							have_to_follow = False
							wildcard_start = cursor
						else:
							position = q.find(search)
							
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
							
							if (keyword[-1] == "*" and keyword[-2] == search):
								print (cursor)
								wildcards_found[wildcard_counter + 1] = q[cursor:]
								wildcard_counter += 1
								
					if (found == True):
						getattr(self.command, keywords['call'])(q, wildcards_found)
						return
						
		getattr(self.command, "no_action")(q, None)