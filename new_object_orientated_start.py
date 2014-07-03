from siriAPI.siriAPI import siri_api

class hans:
    def vader(self, q, zes):
        print ("Ja Klasse!")
        
def test(q, found):
    print (q)

dumm = hans()
siri_api = siri_api()
siri_api.server.set_hostname ("localhost")
siri_api.set_google_domain (".google.de")
siri_api.set_keyword ("Siri")
siri_api.action.add("hans", test)
#siri_api.action.modify(0, "no", test)
siri_api.server.start()
input("Press key to stop server")
siri_api.server.stop()