from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
#kivy.require("1.10.0")

class login_screen(GridLayout):
	def __init__(self,**kwargs):
		super(login_screen,self).__init__(**kwargs)
		self.cols=2

		self.add_widget(Label(text="Name: "))
		self.username=TextInput(multiline=False)
		self.add_widget(self.username)

		self.add_widget(Label(text="Passward: "))
		self.password=TextInput(multiline=False,password=True)
		self.add_widget(self.password)


class kivy_app(App):
	def build(self):
		return login_screen()



if __name__=="__main__":
	kivy_app().run()
