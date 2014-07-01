from siriAPI.siriAPI import siri_api

siri_api = siri_api()
siri_api.server.set_hostname ("localhost")
siri_api.set_google_domain (".google.de")
siri_api.set_keyword ("Siri")
siri_api.server.start()
input("Press key to stop server")
siri_api.server.stop()