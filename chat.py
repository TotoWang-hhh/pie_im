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
