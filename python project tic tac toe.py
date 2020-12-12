#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import*
import tkinter.messagebox
root=Tk()
root.geometry("1337x723")
root.title("tic tac toe")
root.configure(background="cadet blue")
tops=Frame(root,bg="cadet blue",pady=2,width=1350,height=100,relief=RIDGE)
tops.grid(row=0,column=0)
title=Label(tops,font=("arial",50,"bold"),text="tic tac toe game",bd=21,bg="cadet blue",fg="cornsilk",justify=CENTER)
tops.grid(row=0,column=0)
MainFrame=Frame(root,bg="powder blue",padx=10,pady=2,width=1350,height=600,relief=RIDGE)
MainFrame.grid(row=1,column=0)

LeftFrame=Frame(MainFrame,bg="powder blue",bd=10,pady=2,padx=10,width=750,height=500,relief=RIDGE)
LeftFrame.pack(side=LEFT)
RightFrame=Frame(MainFrame,bg="brown",bd=10,padx=10,pady=2,width=560,height=500,relief=RIDGE)
RightFrame.pack(side=RIGHT)
RightFrame1=Frame(RightFrame,bg="green",bd=10,padx=10,pady=2,width=560,height=200,relief=RIDGE)
RightFrame1.grid(row=0,column=0)
RightFrame2=Frame(RightFrame,bg="khaki",bd=10,padx=10,pady=2,width=560,height=200,relief=RIDGE)
RightFrame2.grid(row=1,column=0)

playerX=IntVar()
playerO=IntVar()

playerX.set(0)
playerO.set(0)

buttons=StringVar()
click=True
def checker(buttons):
    global click
    if(buttons["text"]=="" and click==True):
        buttons["text"]= "X"
        click=False 
        scorekeeper()
    elif (buttons["text"]=="" and click==False):
        buttons["text"]="O"
        click=True 
        scorekeeper()
def scorekeeper():
    if(button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X"):
        button1.configure(background="green")
        button2.configure(background="green")
        button3.configure(background="green")
        n=float(playerX.get())
        score=(n+1)
        playerX.set(score)
        tkinter.messagebox.showinfo("winner","x")
    if(button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X"):
        button4.configure(background="purple")
        button5.configure(background="purple")
        button6.configure(background="purple")
        n=float(playerX.get())
        score=(n+1)
        playerX.set(score)
        tkinter.messagebox.showinfo("winner","x")
    if(button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X"):
        button7.configure(background="blue")
        button8.configure(background="blue")
        button9.configure(background="blue")
        n=float(playerX.get())
        score=(n+1)
        playerX.set(score)
        tkinter.messagebox.showinfo("winner","x")
    if(button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X"):
        button3.configure(background="green")
        button5.configure(background="green")
        button7.configure(background="green")
        n=float(playerX.get())
        score=(n+1)
        playerX.set(score)
        tkinter.messagebox.showinfo("winner","x")
    if(button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X"):
        button1.configure(background="red")
        button5.configure(background="red")
        button9.configure(background="red")
        n=float(playerX.get())
        score=(n+1)
        playerX.set(score)
        tkinter.messagebox.showinfo("winner","x")
    if(button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X"):
        button1.configure(background="blue")
        button4.configure(background="blue")
        button7.configure(background="blue")
        n=float(playerX.get())
        score=(n+1)
        playerX.set(score)
        tkinter.messagebox.showinfo("winner","x")
    if(button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X"):
        button2.configure(background="blue")
        button5.configure(background="blue")
        button8.configure(background="blue")
        n=float(playerX.get())
        score=(n+1)
        playerX.set(score)
        tkinter.messagebox.showinfo("winner","x")
    if(button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X"):
        button3.configure(background="purple")
        button6.configure(background="purple")
        button9.configure(background="purple")
        n=float(playerX.get())
        score=(n+1)
        playerX.set(score)
        tkinter.messagebox.showinfo("winner","x")
        
        
    if(button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O"):
        button1.configure(background="blue")
        button2.configure(background="blue")
        button3.configure(background="blue")
        n=float(playerO.get())
        score=(n+1)
        playerO.set(score)
        tkinter.messagebox.showinfo("winner","O")
    if(button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O"):
        button4.configure(background="yellow")
        button5.configure(background="yellow")
        button6.configure(background="yellow")
        n=float(playerO.get())
        score=(n+1)
        playerO.set(score)
        tkinter.messagebox.showinfo("winner","O")
    if(button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O"):
        button7.configure(background="red")
        button8.configure(background="red")
        button9.configure(background="red")
        n=float(playerO.get())
        score=(n+1)
        playerO.set(score)
        tkinter.messagebox.showinfo("winner","O")
    if(button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O"):
        button3.configure(background="blue")
        button5.configure(background="blue")
        button7.configure(background="blue")
        n=float(playerO.get())
        score=(n+1)
        playerO.set(score)
        tkinter.messagebox.showinfo("winner","O")
    if(button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O"):
        button1.configure(background="purple")
        button5.configure(background="purple")
        button9.configure(background="purple")
        n=float(playerO.get())
        score=(n+1)
        playerO.set(score)
        tkinter.messagebox.showinfo("winner","O")
    if(button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O"):
        button1.configure(background="purple")
        button5.configure(background="purple")
        button9.configure(background="purple")
        n=float(playerO.get())
        score=(n+1)
        playerO.set(score)
        tkinter.messagebox.showinfo("winner","O")
    if(button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O"):
        button1.configure(background="yellow")
        button4.configure(background="yellow")
        button7.configure(background="yellow")
        n=float(playerO.get())
        score=(n+1)
        playerO.set(score)
        tkinter.messagebox.showinfo("winner","O")
    if(button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O"):
        button2.configure(background="red")
        button5.configure(background="red")
        button8.configure(background="red")
        n=float(playerO.get())
        score=(n+1)
        playerO.set(score)
        tkinter.messagebox.showinfo("winner","O")
    if(button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O"):
        button3.configure(background="blue")
        button6.configure(background="blue")
        button9.configure(background="blue")
        n=float(playerO.get())
        score=(n+1)
        playerO.set(score)
        tkinter.messagebox.showinfo("winner","O")
    if(button1["text"]!="" and button2["text"]!="" and button3["text"]!="" and button4["text"]!="" and button5["text"]!="" and button6["text"]!="" and button7["text"]!="" and button8["text"]!="" and button9["text"]!=""):
        tkinter.messagebox.showinfo("opps","Game Draw")
def col():
    button1.configure(background="gainsboro")
    button2.configure(background="gainsboro")
    button3.configure(background="gainsboro")
    button4.configure(background="gainsboro")
    button5.configure(background="gainsboro")
    button6.configure(background="gainsboro")
    button7.configure(background="gainsboro")
    button8.configure(background="gainsboro")
    button9.configure(background="gainsboro")
    
def r():
    col()
    button1["text"]=""
    button2["text"]=""
    button3["text"]="" 
    button4["text"]=""
    button5["text"]=""
    button6["text"]=""
    button7["text"]=""
    button8["text"]=""
    button9["text"]=""
def newgame():
    col()
    playerX.set(0)
    playerO.set(0)
    button1["text"]=""
    button2["text"]=""
    button3["text"]="" 
    button4["text"]=""
    button5["text"]=""
    button6["text"]=""
    button7["text"]=""
    button8["text"]=""
    button9["text"]=""

TPlayerX=Label(RightFrame1,font=("arial",40,"bold"),text="playerX:",padx=2,pady=2,bg="cadet blue")
TPlayerX.grid(row=0,column=0,sticky=S+N+E+W)
TxtPlayerX=Entry(RightFrame1,font=("arial",40,"bold"),bd=2,fg="black",textvariable=playerX,width=14,justify=LEFT)
TxtPlayerX.grid(row=0,column=1)
    
TPlayerO=Label(RightFrame1,font=("arial",40,"bold"),text="playerX:",padx=2,pady=2,bg="cadet blue")
TPlayerO.grid(row=1,column=0,sticky=S+N+E+W)
TxtPlayerO=Entry(RightFrame1,font=("arial",40,"bold"),bd=2,fg="black",textvariable=playerO,width=14,justify=LEFT)
TxtPlayerO.grid(row=1,column=1)

btnreset=Button(RightFrame2,text="reset",font=("times 26 bold"),height=1,width=20,bg="pink",command=r)
btnreset.grid(row=2,column=0,padx=6,pady=11)

btnnewgame=Button(RightFrame2,text="new Game",font=("times 26 bold"),height=1,width=20,bg="gray",command=newgame)
btnnewgame.grid(row=3,column=0,padx=6,pady=10)

button1=Button(LeftFrame,text="",font=("times 26 bold"),height=3,width=8,bg="gainsboro",command=lambda:checker(button1))
button1.grid(row=1,column=0,sticky=S+N+E+W)

button2=Button(LeftFrame,text="",font=("times 26 bold"),height=3,width=8,bg="gainsboro",command=lambda:checker(button2))
button2.grid(row=1,column=1,sticky=S+N+E+W)

button3=Button(LeftFrame,text="",font=("times 26 bold"),height=3,width=8,bg="gainsboro",command=lambda:checker(button3))
button3.grid(row=1,column=2,sticky=S+N+E+W)

button4=Button(LeftFrame,text="",font=("times 26 bold"),height=3,width=8,bg="gainsboro",command=lambda:checker(button4))
button4.grid(row=2,column=0,sticky=S+N+E+W)

button5=Button(LeftFrame,text="",font=("times 26 bold"),height=3,width=8,bg="gainsboro",command=lambda:checker(button5))
button5.grid(row=2,column=1,sticky=S+N+E+W)

button6=Button(LeftFrame,text="",font=("times 26 bold"),height=3,width=8,bg="gainsboro",command=lambda:checker(button6))
button6.grid(row=2,column=2,sticky=S+N+E+W)

button7=Button(LeftFrame,text="",font=("times 26 bold"),height=3,width=8,bg="gainsboro",command=lambda:checker(button7))
button7.grid(row=3,column=0,sticky=S+N+E+W)

button8=Button(LeftFrame,text="",font=("times 26 bold"),height=3,width=8,bg="gainsboro",command=lambda:checker(button8))
button8.grid(row=3,column=1,sticky=S+N+E+W)

button9=Button(LeftFrame,text="",font=("times 26 bold"),height=3,width=8,bg="gainsboro",command=lambda:checker(button9))
button9.grid(row=3,column=2,sticky=S+N+E+W)

root.mainloop()



# In[ ]:




