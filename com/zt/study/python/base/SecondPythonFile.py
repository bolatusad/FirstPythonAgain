#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
import tkinter.messagebox as messagebox
import mysql.connector


# pass
def hello(a):
    pass


# hello(1)


# 返回多个值
def returnMultiValue(a, b):
    a += 1
    b += 2
    return a, b


# print(returnMultiValue(1, 1)[0])


# 默认参数
def default_param(a, b=2):
    a += 1
    b += 1
    print(a)
    print(b)


# default_param(1)
# default_param(1, 3)


# 切片
# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# print(L[2:3])

# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()
#
#     def createWidgets(self):
#         self.helloLabel = Label(self, text='Hello, world!')
#         self.helloLabel.pack()
#         self.quitButton = Button(self, text='Quit', command=self.quit)
#         self.quitButton.pack()


# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()
#
#     def createWidgets(self):
#         self.nameInput = Entry(self)
#         self.nameInput.pack()
#         self.alertButton = Button(self, text='Hello', command=self.hello)
#         self.alertButton.pack()
#
#     def hello(self):
#         name = self.nameInput.get() or 'world'
#         messagebox.showinfo('Message', 'Hello, %s' % name)


# app = Application()
# # 设置窗口标题:
# app.master.title('Hello World')
# # 主消息循环:
# app.mainloop()

conn = mysql.connector.connect(user='root', password='123456', database='bbkim')
cursor = conn.cursor()

print(cursor)

cursor.execute('select * from account ')
values = cursor.fetchall()
print(values)
cursor.close()