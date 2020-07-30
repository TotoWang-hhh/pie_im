print('Welcome to use Pie IM')
print('2020 By 人工智障')

import socket
import tkinter as tk
import os

print('==================================================')

def logIn():
    ip=enterIp.get()
    logInWin.destroy()
    global myip
    myip=ip
    print(ip)
    os.system("python ./chat.py %s"%(ip))
    exit()

logInWin=tk.Tk()
logInWin.geometry('360x360')
logInWin.resizable(0,0)
logInWin.title('Pie IM')
title=tk.Label(logInWin,text='Pie IM',font=('zpix',30),width=15,height=3,bg='blue',fg='white')
title.pack()
enterIpTip=tk.Label(logInWin,text='请输入对方的IP地址',font=('幼圆',15))
enterIpTip.pack(pady=20)
global login_enterIp
enterIp=tk.Entry(logInWin,width=40)
enterIp.pack()
btn=tk.Button(logInWin,text='登录',bd=2,font=('幼圆',15),command=logIn)
btn.pack(pady=25)
logInWin.mainloop()
