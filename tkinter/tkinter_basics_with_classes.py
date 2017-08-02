from tkinter import *
from PIL import Image, ImageTk

def Q(self):
		master.destroy()


class Window(Frame):
	def __init__(self, root = None):
		Frame.__init__(self,root)
		self.root=root
		self.__initwindow()

	def __initwindow(self):
		self.root.title('My window')
		self.pack(fill=BOTH,expand=1)
		
		#button=Button(self,text='Quit',command=self.quit)
		#button.grid(row=0,column=0)

		menu=Menu(self.root)
		self.root.config(menu=menu)

		file=Menu(menu)				#Use 'tearoff=0' or 'tearoff=False' to remove the lines (---) from menue
		file.add_command(label='Save')
		file.add_command(label='Exit',command=self.quit)
		menu.add_cascade(label='File',menu=file)
		edit=Menu(menu)
		edit.add_command(label='Show imang',command=self.showimage)
		edit.add_command(label='Show txt',command=self.showtext)
		menu.add_cascade(label='Edit',menu=edit)

	def showimage(self):
		load=Image.open('images.jpg')
		render=ImageTk.PhotoImage(load)
		img=Label(self,image=render)
		img.image=render
		img.grid(row=0,column=0)

	def showtext(self):
		text=Label(self,text='this is label')
		text.grid(row=1,column=0)

	def quit(self):
		exit()

master=Tk()
root.iconbitmap('file.ico')
master.bind('<Control-w>',Q)
master.geometry('250x250')

app=Window(master)

master.mainloop()
