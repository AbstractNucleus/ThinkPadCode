import tkinter as tkinter
from tkinter import *
import subprocess

adminPassword = '1234'

#Main screen
def appWindow():
    base = Tk()
    base.geometry('1200x800')

    #Exit button
    def exitApp():
        base.destroy()
    Button(base,text=f'Quit',command=exitApp).pack()

    #Confirmation buttons
    def confirm1():
        cWin1 = Tk()
        cWin1.attributes('-type','dialog')
        cWin1.geometry(f'200x100')
        Label(cWin1,text='Are you sure?').pack()

        #Functions
        def updateCode():
            scpCode1 = 'urxvt -hold -e scp -r -P 666 /home/teryxeon/Documents/Code/ teryxeon@188.150.156.25:/home/teryxeon/Documents'
            subprocess.check_output(['bash','-c',scpCode1])
        #def getCode():
            #scpCode2 = 'urxvt -hold -e scp -r -P 666 teryxeon@188.150.156.25:/home/teryxeon/Documents/Code/ /home/teryxeon/Documents'
            #subprocess.check_output(['bash','-c',scpCode2])
        #def sshConnect():
            #code = "tilix -e ssh teryxeon@188.150.156.25 -p 666"
            #subprocess.check_output(['bash','-c',code])

        #Confirmation buttons
        def cancel():
            cWin1.destroy()
        def ok():
            cWin1.destroy()
            updateCode()
        Button(cWin1,text='Cancel',command=cancel).pack()
        Button(cWin1,text='Ok',command=ok).pack()

    #Buttons
    updateCodeButton = Button(base,text='Update code to server',command=confirm1)
    updateCodeButton.pack()

    #getCodeButton = Button(base,text='Get code from server',command=getCode)
    #getCodeButton.pack()

    #connectSsh = Button(base,text='Connect via ssh',command=sshConnect)
    #connectSsh.pack()



#Login window
def login():
    root = Tk()
    root.attributes('-type','dialog')
    root.geometry("300x120")
    pwdbox = Entry(root,show=f'*')
    Label(root,text='Enter master password:').pack()
    def onpwdentry(esv):
        password = pwdbox.get()
        if password == adminPassword:
            root.destroy()
            appWindow()
        else:
            h = Label(fg="red",text='Wrong password, try again!')
            h.pack()
    def onpwdclick():
        password = pwdbox.get()
        if password == adminPassword:
            root.destroy()
            appWindow()
        else:
            h = Label(fg='red',text='Wrong password, try again!')
            h.pack()
    pwdbox.pack()
    pwdbox.bind('<Return>', onpwdentry)
    Button(root,command=onpwdclick,text='LOGIN').pack()
    root.mainloop()


login()
