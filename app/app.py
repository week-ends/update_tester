#! /usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '1.0'

import os
import requests
import zipfile
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image, ImageOps
_AppName_ = 'UpdateTestApp'


window = Tk()
window.title(_AppName_)
window.geometry("400x400")
window.resizable(False, False)

# 배경화면
wall = PhotoImage(file="img/logo.png")
wall_label = Label(window, image=wall)
wall_label.place(x=1, y=1)


def close():
    window.quit()
    window.destroy()


def aboutme():
    toplevel = Toplevel()
    toplevel.title('About Me')
    toplevel.geometry("250x100")

    label = Label(toplevel, text='The Current Version is\n'+__version__)
    label.pack()


def newVersion():
    data = requests.get('http://127.0.0.1:5000/version',
                        allow_redirects=True).content
    return float(data)


def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)


try:
    # data = urllib2.urlopen(
    #     'http://192.168.116.128:81/py_autoupdate/version').read()
    data = requests.get('http://127.0.0.1:5000/version',
                        allow_redirects=True).content
    print(data)
    if float(data) > float(__version__):
        messagebox.showinfo('Software Update', 'Update Available!')
        mb = messagebox.askquestion(
            _AppName_+' '+str(__version__), 'Do you want to setup ' + _AppName_ + ' ' + str(newVersion())+'?')
        if mb == 'yes':
            # data = urlopen('http://127.0.0.1:5000/download').read()
            # print(data)

            # 다운로드 서버 접속
            r = requests.get('http://127.0.0.1:5000/download',
                             allow_redirects=True)
            # 다운로드
            update_file = '1.1.zip'
            open(update_file, 'wb').write(r.content)
            dirname = os.path.dirname(os.path.abspath(__file__))
            try:
                # 압축풀기
                with zipfile.ZipFile(update_file) as zf:
                    zf.extractall()
                    print("Uncompress Succeeded")
                # 업데이트 파일 삭제
                os.remove(update_file)

                messagebox.showinfo('Software Update',
                                    'The Update Succeeded!\n This program will restart.')

                # 프로그램 재시작
                restart_program()

            except Exception as e:
                print("Uncompress Failed", e)
                messagebox.showerror('Software Update',
                                     'The Update Failed!')
            finally:
                os.remove(update_file)
        elif mb == 'no':
            pass
    else:
        # messagebox.showinfo('Software Update',
        #                     'No Updates are Avalible.')
        print('No Updates are Avalible.')
except Exception as e:
    messagebox.showwarning('Software Update',
                           'Unable to Check for Update')

menubar = Menu(window)

# 메뉴 바 속성
menu_1 = Menu(menubar, tearoff=0, activebackground='red')
menu_1.add_command(label="Open", state="disable")
menu_1.add_command(label="Save", state="disable")
menu_1.add_separator()
menu_1.add_command(label="Close", command=close)
menubar.add_cascade(label="File", menu=menu_1)

menu_2 = Menu(menubar, tearoff=0)
menu_2.add_radiobutton(label="About Me", command=aboutme)
menubar.add_cascade(label="About", menu=menu_2)

# 윈도우 창에 메뉴 등록
window.config(menu=menubar)

window.mainloop()
print('Window Close')
