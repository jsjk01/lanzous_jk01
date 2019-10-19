'''
作者：天生魔心
项目创建时间：2019年10月18日 19:05:28
'''
from tkinter import *
win = Tk()
frma = Frame()
frmb = Frame()
frma.pack()
frmb.pack()
lblUname = Label(frma,text = '用户名',width = 10,fg = 'black')
etyUname = Entry(frma,width = 20)
lblUname.grid(row = 1,column = 1,pady = 2)
etyUname.grid(row = 1,column = 2,pady = 2)
lblPwd = Label(frma,text ='密  码',width = 10,fg = 'black')
etyPwd = Entry(frma,width = 20)
lblPwd.grid(row = 2,column = 1,pady = 2)
etyPwd.grid(row = 2,column = 2,pady = 2)
btnLogin = Button(frmb,text = '登  陆',width = 10)
btnReset = Button(frmb,text = '重  输',width = 10)
btnLogin.grid(row = 1,column = 1,padx = 5)
btnReset.grid(row = 1,column = 2,padx = 5)
win.title('蓝奏云网盘客户端')
win.geometry('280x90')
win.mainloop()