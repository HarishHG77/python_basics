from tkinter import *
form=Tk()
form.geometry('500x500')
lblregno=Label(form,text='register number')
lblregno.grid(row=0,column=0)
etregno=Entry(form,width=20)
etregno.grid(row=0,column=1)
form.mainloop()