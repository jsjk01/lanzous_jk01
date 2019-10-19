'''
作者：天生魔心
项目创建时间：2019年10月18日 19:05:28
'''
from tkinter import *
import tkinter.messagebox
#创建应用程序窗口
win = Tk()
varName = StringVar()
varName.set('')
varPwd = StringVar()
varPwd.set('')
#创建用户名标签
labelName = Label(text = '用户名',justify = RIGHT)
labelName.place(x = 20,y = 5,width = 80,height = 20)
#创建文本框，同时设置关联的变量
entryName = Entry(win,textvariable = varName)
entryName.place(x = 110,y = 5,width = 80,height = 20)
#创建用户密码标签
labelPwd = Label(text = '密   码',justify = RIGHT)
labelPwd.place(x = 20,y = 30,width = 80,height = 20)
#创建密码文本框，同时设置关联的变量
entryPwd = Entry(win,show = '*',textvariable = varPwd)
entryPwd.place(x = 110,y = 30,width = 80,height = 20)
#用户信息
users = {'zhang3':'a12','admin':'12345','li4':'abc'}
def login(): #登录按钮事件处理函数
    #获取用户名和密码
    name = entryName.get()
    pwd = entryPwd.get()
    flag = False
    for item in users:
        if item == name and users[item] == pwd:
            flag = True
    if flag == True:
        tkinter.messagebox.showinfo(title = '登录信息',message = '登录成功')
    else:
        tkinter.messagebox.showinfo(title = '登录信息',message = '用户名或密码有误，请重新输入或找回密码')
def cancel():
    varName.set('')
    varPwd.set('')
#创建按钮组件，同时设置按钮事件处理函数
buttonOk = Button(win,text = '登  录',command = login)
buttonOk.place(x = 60,y = 60,width = 50,height = 20)
buttonCancel = Button(win,text = '重  置',command = cancel)
buttonCancel.place(x = 120,y = 60,width = 50,height = 20)
win.title('蓝奏云网盘客户端')
win.geometry('280x90')
win.mainloop()