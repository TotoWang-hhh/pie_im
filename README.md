这个程序用多线程，实现设备之间的聊天，支持win10通知，欢迎下载
# 依赖的第三方库
win10toast
# 代码
## 将以下代码写入任意.py文件
```python
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
```
## 将以下代码写入chat.py
```python
import tkinter as tk
from tkinter import *
import tkinter.messagebox as msgbox
import time
import socket
import threading
import sys
from win10toast import ToastNotifier

udp_socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind((sys.argv[1],8080))

ip=sys.argv[1]
port=8081

def sendMsg():#发送消息
    print('doing:sendMsg()')
    msg=str(msgEnter.get('1.0',END))
    print(msg)
    print(type(msg))
    strMsg='我:'+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    print(strMsg)
    msgList.insert(END,strMsg+'\n','greencolor')#插入年月日
    msgList.insert(END,msg+'\n')#输入的内容,0.0表示文本开始
    msgList.insert(END,'\n')
    msgEnter.delete('1.0',END)#删除中间刚输入的内容
    udp_socket.sendto(msg.encode('utf-8'),(ip, port))

def recvMsg():
    while True:
        print('doing:recvMsg()')
        print('正在接收...')
        recv_data=udp_socket.recvfrom(8080)
        msg=recv_data[0].decode('utf-8')
        strMsg='对方:' + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        print(strMsg)
        msgList.insert(END,strMsg+'\n','greencolor')#插入年月日
        msgList.insert(END,msg+'\n')#输入的内容,0.0表示文本开始
        msgList.insert(END,'\n')
        toaster = ToastNotifier()
        toaster.show_toast(ip,msg)

win=tk.Tk()
win.geometry('480x560')
win.title(ip)
win.iconbitmap("./icons/icon-mini.ico")

msgList=tk.Text(win,font=('幼圆',13))
msgList.pack(fill=BOTH,expand=True)

sendBtn=tk.Button(win,text='发送',bd=2,font=('等线',15),height=2,command=sendMsg)
sendBtn.pack(fill=X,expand=True)

msgEnter=Text(win,width='1',font=('幼圆',13))
msgEnter.pack(fill=BOTH,expand=True,pady=0)

t1=threading.Thread(target=recvMsg,name='Pie IM消息接收服务')
t1.start()
win.mainloop()
```
