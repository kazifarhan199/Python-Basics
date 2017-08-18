from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget

class apple(Widget):
	pass

class simple(App):
	def build(self):
		
		return apple()

simple().run()