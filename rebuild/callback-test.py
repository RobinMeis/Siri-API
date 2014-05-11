class Foo:
	def __init__(self):
		self.callback = None
		
	def callback(self):
		self.callback()

		
def eineFunktion():
	print("Hallo Welt")

		
meinFoo = Foo()
meinFoo.callback = eineFunktion # wichtig keine () dadurch wird die Funktion nicht ausgeführt, sondern als zeiger übergeben
meinFoo.callback()
