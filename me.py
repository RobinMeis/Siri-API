#Import required classes
from siriAPI.server import server
from siriAPI.keywords import keywords

#Set keywords
keywords = keywords()

server = server(keywords, "zimmer", ".google.co.uk")
server.start(True)
input("Press key to shutdown Siri-API")
server.stop()