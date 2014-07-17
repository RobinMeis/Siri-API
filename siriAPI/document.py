#################################################################################
# This class generates HTML or HTTP output.                                     #
# The HTML output shows a chat windows in Apples Messages Style                 #
# The HTTP output can be used to redirect the browser to another website or app #
#                                                                               #
#                      Please read the documentation at                         #
#  https://github.com/HcDevel/Siri-API/wiki/Customize-commands#use-chat-style   # TODO Refer to right article
#################################################################################

import urllib.request

class document: #Class to generate the (HTML) output
    def __init__ (self, connection):
        self.connection = connection
        self.response = 200
        self.header = ['Content-type', 'text/html']
        self.document = ''
        self.chat_style = None
        self.sent = False
        
    def use_chat_style (self, value):
        self.response = 200
        if (value == True):
            self.chat_style = True
            self.response = 200
            self.header = ['Content-type', 'text/html']
            self.document = open('style.html', 'r').read()
        else:
            self.chat_style = False
            self.response = 200
            self.header = ['Content-type', 'text/html']
            
    def redirect (self, target): #Redirects to a HTTP target. Generated HTML will be deleted and locked
        self.chat_style = False
        self.document = ''
        self.response = 302
        self.header = ["Location", target]
            
    def title (self, text): #Generates a title bar
        if (self.chat_style == True):
            self.document = self.document.replace('<replace_with_document_class_dont_remove>', '<div class="header"><div class="title">' + text + '</div></div><replace_with_document_class_dont_remove>')
        else:
            raise Exception ('You need to enable chatstyle whith output.use_chat_style(true) first')
            
    def incoming (self, text): #Creates a text box displaying an incoming message
        if (self.chat_style == True):
            self.document = self.document.replace('<replace_with_document_class_dont_remove>', '<div class="message"><div class="style incoming">' + text + '</div></div><replace_with_document_class_dont_remove>')
        else:
            raise Exception ('You need to enable chatstyle whith output.use_chat_style(true) first')
            
    def outgoing (self, text): #Creates a text box displaying an outgoing message
        if (self.chat_style == True):
            self.document = self.document.replace('<replace_with_document_class_dont_remove>', '<div class="message"><div class="style outgoing">' + text + '</div></div><replace_with_document_class_dont_remove>')
        else:
            raise Exception ('You need to enable chatstyle whith output.use_chat_style(true) first')
            
    def message_full_width (self, text, background_color='#23afed', font_color='black'): #Create a message with full screen width. Set color in HTML notation
        if (self.chat_style == True):
            self.document = self.document.replace('<replace_with_document_class_dont_remove>', '<div class="message"><div class="full_width" style="background-color:' + background_color + '; color:' + font_color + ';">' + text + '</div></div><replace_with_document_class_dont_remove>')
        else:
            raise Exception ('You need to enable chatstyle whith output.use_chat_style(true) first')
            
    def error (self, text):
        self.message_full_width (text, '#ed4423', 'white')

            
    def request (self, url): #Sends a HTTP request (useful for HTTP APIS). If you don't need the response, you can do this after calling send. This will decrease loading time in the browser
        f = urllib.request.urlopen(url)
        return(f.read().decode('utf-8'))
            
    def send (self): #Send the answer to the browser
        self.sent = True
        self.connection.send_response(self.response)
        self.connection.send_header(self.header[0], self.header[1])
        self.connection.end_headers()
        
        if (self.response != 302):
            self.document = self.document.replace ('<replace_with_document_class_dont_remove>', '') #Remove reference mark before sending
            self.connection.wfile.write(bytes(self.document, "utf-8"))
