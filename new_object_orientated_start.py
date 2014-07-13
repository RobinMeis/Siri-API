from siriAPI.siriAPI import siri_api
import json

def test(output, q, wildcards):
    print (q)
    output.use_chat_style(True)
    output.title("Siri API")
    output.incoming(q)
    output.outgoing("Hi")
    output.send()
    
def hello(output, q, wildcards):
    output.use_chat_style(True)
    output.title("Siri API")
    output.incoming(q)
    output.outgoing("Nice to meet you")
    output.send()
    
def dict(output, q, wildcards):
    output.use_chat_style(True)
    output.title("Dictionary")
    output.incoming(q)
    output.outgoing("I will look up this later")
    output.send()
    
def light(output, q, wildcards):
    if (wildcards[1] == "one"):
        id = 1
    elif (wildcards[1] == "two"):
        id = 2
    elif (wildcards[1] == "three"):
        id = 3
    elif (wildcards[1] == "four" or wildcards[1] == "for"):
        id = 4
    elif (wildcards[1] == "five"):
        id = 5
    elif (wildcards[1] == "six"):
        id = 6
    else:
        id = -1

    output.use_chat_style(True)
    output.title("Light Switch")
    output.incoming(q)
    if ((wildcards[0] == "on" or wildcards[0] == "off") and id > -1):
        output.outgoing("Okay, let's turn " + wildcards[0] + " lamp " + wildcards[1])
        output.send()
        output.request("http://zimmer:2525/remote/" + wildcards[0] + "?id=" + str(id)) #Only works in my setup
    else:
        output.outgoing("No such lamp available")
        output.send()

siri_api = siri_api()
siri_api.squid.set_hostname("zimmer")
siri_api.server.set_hostname ("zimmer")
siri_api.set_google_domain (".google.co.uk")
siri_api.set_yahoo_domain (".yahoo.com")
siri_api.set_keyword ("Siri")

def licht_an(output, q, wildcards):
    #Prozessverarbeitung
    receivers = json.loads(output.request("http://zimmer:2525/remote/list"))
    found = False
    for id, val in enumerate(receivers):
        if (receivers[val]['title'] == wildcards[0]):
            found = True
            output.request("http://zimmer:2525/remote/on?id=" + str(val))
         
    output.use_chat_style(True)
    output.title("Lichtschalter")
    output.incoming(q)
    
    if (found == False):
        output.outgoing("Diese Lampe kenne ich nicht")
    else:
        output.outgoing("Sehr gerne")

    output.send()
    
def licht_aus(output, q, wildcards):
    #Prozessverarbeitung
    receivers = json.loads(output.request("http://zimmer:2525/remote/list"))
    found = False
    for id, val in enumerate(receivers):
        if (receivers[val]['title'] == wildcards[0]):
            found = True
            output.request("http://zimmer:2525/remote/off?id=" + str(val))
         
    output.use_chat_style(True)
    output.title("Lichtschalter")
    output.incoming(q)
    
    if (found == False):
        if (wildcards[0] == "alles"):
            output.outgoing('Ich habe alles ausgeschaltet')
            output.request('http://zimmer:2525/remote/off?id=all')
        else:
            output.outgoing("Diese Lampe kenne ich nicht")
    else:
        output.outgoing("Sehr gerne")

    output.send()
    
siri_api.action.add([['hello', '*']], hello)
siri_api.action.add([['what does', '*', 'mean'], ['dictionary', '*']], dict)
siri_api.action.add([['schalte das', '*', 'an'], ['schalte die', '*', 'an'], ['schalte den', '*', 'an'], ['schalte das', '*', 'ein'], ['schalte die', '*', 'ein'], ['schalte den', '*', 'ein']], licht_an)
siri_api.action.add([['schalte das', '*', 'aus'], ['schalte die', '*', 'aus'], ['schalte den', '*', 'aus'], ['schalte das', '*', 'ab'], ['schalte die', '*', 'ab'], ['schalte den', '*', 'ab'], ['schalte', '*', 'ab'], ['schalte', '*', 'aus']], licht_aus)
siri_api.action.add([['turn', '*', 'lights', '*'], ['turn', '*', 'light', '*'], ['turn', '*', 'lamp', '*'], ['turn', '*', 'lemp', '*'], ['turn', '*', 'late', '*'], ['turn', '*', 'lead', '*']], light)

siri_api.server.start()
input("Press key to stop server\n")
siri_api.server.stop()