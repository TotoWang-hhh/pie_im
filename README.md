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
 1 import tkinter as tk
 2 from tkinter import *
 3 import tkinter.messagebox as msgbox
 4 import time
 5 import socket
 6 import threading
 7 import sys
 8 from win10toast import ToastNotifier
 9 
10 udp_socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
11 udp_socket.bind((sys.argv[1],8080))
12 
13 ip=sys.argv[1]
14 port=8081
15 
16 def sendMsg():#发送消息
17     print('doing:sendMsg()')
18     msg=str(msgEnter.get('1.0',END))
19     print(msg)
20     print(type(msg))
21     strMsg='我:'+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
22     print(strMsg)
23     msgList.insert(END,strMsg+'\n','greencolor')#插入年月日
24     msgList.insert(END,msg+'\n')#输入的内容,0.0表示文本开始
25     msgList.insert(END,'\n')
26     msgEnter.delete('1.0',END)#删除中间刚输入的内容
27     udp_socket.sendto(msg.encode('utf-8'),(ip, port))
28 
29 def recvMsg():
30     while True:
31         print('doing:recvMsg()')
32         print('正在接收...')
33         recv_data=udp_socket.recvfrom(8080)
34         msg=recv_data[0].decode('utf-8')
35         strMsg='对方:' + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
36         print(strMsg)
37         msgList.insert(END,strMsg+'\n','greencolor')#插入年月日
38         msgList.insert(END,msg+'\n')#输入的内容,0.0表示文本开始
39         msgList.insert(END,'\n')
40         toaster = ToastNotifier()
41         toaster.show_toast(ip,msg)
42 
43 win=tk.Tk()
44 win.geometry('480x560')
45 win.title('test title')
46 win.iconbitmap("./icons/icon-mini.ico")
47 
48 msgList=tk.Text(win,font=('幼圆',13))
49 msgList.pack(fill=BOTH,expand=True)
50 
51 sendBtn=tk.Button(win,text='发送',bd=2,font=('等线',15),height=2,command=sendMsg)
52 sendBtn.pack(fill=X,expand=True)
53 
54 msgEnter=Text(win,width='1',font=('幼圆',13))
55 msgEnter.pack(fill=BOTH,expand=True,pady=0)
56 
57 t1=threading.Thread(target=recvMsg,name='Pie IM消息接收服务')
58 t1.start()
59 win.mainloop()
 
