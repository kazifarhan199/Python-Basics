import tkinter as tk
from functools import partial

root=tk.Tk()

def apple(n):
	print('Hello '+str(n))

button = list()
for i in range(4):
    button.append(tk.Button(root, text='karirano', command=partial(apple, i)))
    button[-1].grid(row=0,column=i)

root.mainloop()