from siriAPI.siriAPI import siri_api
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

siri_api.server.set_hostname ("localhost")
siri_api.set_google_domain (".google.de")
siri_api.set_keyword ("Siri")


#self.keywords.append({'find': [['turn', '*', 'lights', '*'], ['turn', '*', 'light', '*'], ['turn', '*', 'lamp', '*'], ['turn', '*', 'lemp', '*'], ['turn', '*', 'late', '*'], ['turn', '*', 'lead', '*']], 'call': 'light'})
#self.keywords.append({'find': [['what does', '*', 'mean'], ['dictionary', '*']], 'call': 'dict'})


siri_api.action.add([['hello', '*']], hello)
siri_api.action.add([['what does', '*', 'mean'], ['dictionary', '*']], dict)
siri_api.action.add([['turn', '*', 'lights', '*'], ['turn', '*', 'light', '*'], ['turn', '*', 'lamp', '*'], ['turn', '*', 'lemp', '*'], ['turn', '*', 'late', '*'], ['turn', '*', 'lead', '*']], light)

siri_api.server.start()
input("Press key to stop server")
siri_api.server.stop()