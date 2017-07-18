from tkinter import *
import main_project

def sender():
	from_this_person=ee_mail_from.get()
	your_passward=passward_yours.get()
	your_subject=esubject.get()
	texta=emessage.get("0.0",END)
	main_project.main(from_this_person , your_passward ,your_subject, texta)

root=Tk()

le_mail_from=Label(width=20,height=2,text='E-mail')
le_mail_to=Label(width=20,height=2,text='Passward')
lsubject=Label(width=20,height=2,text='Subject')
lmessage=Label(width=20,height=2,text='Message')

le_mail_from.grid(row=1,column=1)
le_mail_to.grid(row=2,column=1)
lsubject.grid(row=3,column=1)
lmessage.grid(row=4,column=1)

ee_mail_from=Entry(width=60)
passward_yours=Entry(width=60)
esubject=Entry(width=60)
emessage=Text(width=45,height='15')
scrollb =Scrollbar(command=emessage.yview,width=2)
emessage['yscrollcommand'] = scrollb.set

ee_mail_from.focus()

ee_mail_from.grid(row=1,column=2)
passward_yours.grid(row=2,column=2)
esubject.grid(row=3,column=2)
emessage.grid(row=4,column=2,columnspan=2)
scrollb.grid(row=4,column=3)

sent_button=Button(text='Sent',command=sender,width=40,height=2,bg='green')
sent_button.grid(row=5,column=2)

plabel=Label(width=10)
plabel.grid(row=6,column=2)

root.mainloop()
