from tkinter import *
import csv
from tkinter import ttk
import datetime

date=[]
name=[]
transition=[]
amount=[]
new_name=''
new_transition=''

class window1(Frame):
	def __init__(self,root=None):
		Frame.__init__(self,root)
		self.root=root
		self.root.geometry('600x400')

		self.root.bind('<Control-w>',self.Quit)
		self.root.bind('<Control-n>',self.Add_transation)
		self.root.iconbitmap('F:\\Project Not\\bank_building.ico')
		self.menu_window1()
		self.page_window1()

	def menu_window1(self):
		menu=Menu(self.root)
		self.root.config(menu=menu)

		file=Menu(menu,tearoff=False)
		file.add_command(label='New Transation',command=self.Add_transation)
		file.add_separator()
		file.add_command(label='quit',command=lambda:exit())
		menu.add_cascade(label='File',menu=file)


	def Add_transation(self,event=True):
		self.takeinput()

	def new_transition_fill(self):

		global new_name,new_transition
		todays_date=datetime.date.today()
		try:
			New_amount=int(amount[-1])+int(new_transition)
		except:
			New_amount=int(new_transition)

		a=open('b.csv','a')
		a.write('\n'+str(todays_date)+'|'+(new_name.upper())+'|'+new_transition+'|'+str(New_amount))
		a.close()
		self.get_previous_saved_file()
		self.show(1,0)
	
	def takeinput(self):
		master=Tk()
		master.iconbitmap('F:\\Project Not\\paper.ico')
		ttk.Label(master,text='Transition type').grid(row=0,column=0)
		ttk.Label(master,text='Amount').grid(row=1,column=0)
		e_name=ttk.Entry(master)
		e_name.grid(row=0,column=1)
		e_transition=ttk.Entry(master)
		e_transition.grid(row=1,column=1)
		ttk.Button(master,width=20,text='Set New Transition',command=lambda:self.transition_button(e_name,e_transition,master)).grid(row=2,column=1)

	def transition_button(self,e_name,e_transition,master):
		global new_name
		global new_transition

		new_name=e_name.get()
		new_transition=e_transition.get()
		name.append(e_name)
		transition.append(e_transition)
		self.new_transition_fill()
		master.destroy()

	def page_window1(self):
		self.get_previous_saved_file()
		Label(text="------------Date-------------------Transition name------------Transition Ammount----------------Balance---------").grid(row=0,column=0,columnspan=7)
		self.show(1,0)

	def show(self,x,y):
		global date
		global name
		global amount
		
		for i in range(len(date)):
			ai=ttk.Label(text='             '+date[-i-1],width=20).grid(row=x,column=y)
			bi=ttk.Label(text=name[-i-1],width=20).grid(row=x,column=y+2)
			ci=ttk.Label(text=transition[-i-1],width=20).grid(row=x,column=y+4)
			di=ttk.Label(text='	'+amount[-i-1],width=20).grid(row=x,column=y+6)
			x+=1
	
		for i in range(30):
			Label(text='|',width=1).grid(row=i,column=y+1)
			Label(text='-',width=1).grid(row=i,column=y+3)
			Label(text='|',width=1).grid(row=i,column=y+5)

	def Deleat(self,a,b,c,d,e):
		a.destroy()
		b.destroy()
		c.destroy()
		d.destroy()
		e.destroy()

	def get_previous_saved_file(self):
		global date
		global name
		global transition
		global amount

		with open('b.csv') as csvfile:
			readCSV  = csv.reader(csvfile, delimiter='|')
			date=[]
			name=[]
			transition=[]
			amount=[]

			for i in readCSV:

				dates = i[0]
				names = i[1]
				transitions=i[2]
				amounts = i[3]

				date.append(dates)
				name.append(names)
				transition.append(transitions)
				amount.append(amounts)

	def Quit(self,root=None):
		self.root.destroy()

root=Tk()
window1(root)
root.mainloop()
	
