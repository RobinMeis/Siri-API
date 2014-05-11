#Import required classes
import siriAPI.server
import siriAPI.keywords

#Set keywords
keywords = keywords()

server = server(keywords, "zimmer", ".google.co.uk")
server.start(True)
input("Press key to shutdown Siri-API")
server.stop()