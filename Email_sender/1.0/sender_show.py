from tkinter import  *

def internet_problem():
	master=Tk()
	master.geometry('485x35+420+150')
	mainlabel=Label(master,text='Check Your internet connection',bg='red')
	mainlabel.config(font=("Courier", 20))
	mainlabel.pack()
	master.mainloop()

def login_problem():
	master=Tk()
	master.geometry('485x35+420+150')
	mainlabel=Label(master,text='Email or Passward is incorrect',bg='red')
	mainlabel.config(font=("Courier", 20))
	mainlabel.pack()
	master.mainloop()	


def file_problem_or_unknown_problem():
	master=Tk()
	master.geometry('1340x70+10+150')
	mainlabel=Label(master,text=' There is a problem in your file Plase check if file has the format of Email,name   ',bg='red')
	Second=Label(master,text=' if wanna change the format contact Support for an update at farhankazi43@gmail.com ',bg='red')
	mainlabel.config(font=("Courier", 20))
	mainlabel.pack()
	Second.config(font=("Courier", 20))
	Second.pack()
	master.mainloop()		
