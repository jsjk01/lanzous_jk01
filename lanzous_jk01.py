'''
作者：天生魔心
项目创建时间：2019年10月18日 19:05:28
'''
from tkinter import *
win = Tk()
label1 = Label(win,text='Hellp Python!')
btn1 = Button(win,text='click')
label1.pack()
btn1.pack()
win.title('蓝奏云网盘客户端')
win.geometry('300x200')
win.mainloop()