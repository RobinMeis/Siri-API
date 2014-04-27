#################################################################################
# This class generates HTML or HTTP output.                                     #
# The HTML output shows a chat windows in Apples Messages Style                 #
# The HTTP output can be used to redirect the browser to another website or app #
#                                                                               #
#                      Please read the documentation at                         #
#  https://github.com/HcDevel/Siri-API/wiki/Customize-commands#use-chat-style   #
#################################################################################

import urllib.request

class document: #Class to generate the (HTML) output
	def __init__ (self, connection, chat_style=True):
		self.connection = connection
		self.chat_style = chat_style
		
		self.response = 200
		self.header = ['Content-type', 'text/html']
		if (self.chat_style == True):
			self.document = open('style.html', 'r').read()
		else:
			self.document = ""
			
	def title (self, text): #Generates a title bar
		print ("Title: ")
		if (self.chat_style == True):
			print (text)
			self.document = self.document.replace('<replace_with_document_class_dont_remove>', '<div class="header"><div class="title">' + text + '</div></div><replace_with_document_class_dont_remove>')
			
	def incoming (self, text): #Creates a text box displaying an incoming message
		if (self.chat_style == True):
			self.document = self.document.replace('<replace_with_document_class_dont_remove>', '<div class="message"><div class="style incoming">' + text + '</div></div><replace_with_document_class_dont_remove>')
			
	def outgoing (self, text): #Creates a text box displaying an outgoing message
		if (self.chat_style == True):
			self.document = self.document.replace('<replace_with_document_class_dont_remove>', '<div class="message"><div class="style outgoing">' + text + '</div></div><replace_with_document_class_dont_remove>')
			
	def redirect (self, target): #Redirects to a HTTP target. Generated HTML will be deleted and locked
		self.chat_style = False
		self.document = ''
		self.response = 302
		self.header = ["Location", target]
		
	def request (self, url): #Sends a HTTP request (useful for HTTP APIS). If you don't need the response, you can do this after calling send. This will decrease loading time in the browser
		f = urllib.request.urlopen(url)
		return(f.read().decode('utf-8'))
			
	def send (self): #Send the answer to the browser
		self.connection.send_response(self.response)
		self.connection.send_header(self.header[0], self.header[1])
		self.connection.end_headers()
		
		if (self.response != 302):
			self.document = self.document.replace ('<replace_with_document_class_dont_remove>', '') #Remove reference mark before sending
			self.connection.wfile.write(bytes(self.document, "utf-8"))
