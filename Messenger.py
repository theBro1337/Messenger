from Tkinter import *
from threading import *
import time
import socket
ip1 = "192.168.43.155"
port1 = 5001
Chats = "Chats"
def send():
    ip = "192.168.43.155"
    port = 5000
    message = tb1.get("1.0",END)
    tb1.delete('1.0',END)
    L3 = Label(root, text=message, bg="white",fg="black",font="Belinda 12")
    L3.place(x=650,y=620)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    if True:
        sock.send(message)
def callsign():
    sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock1.connect((ip1, port1))
    while True:
        sock1.send("Debabrata")
#def caller():
    #t = Timer(1, callsign)
    #t.daemon = True
    #t.start()
def signup():
    username = tb2.get("1.0",END)
    password = tb4.get("1.0",END)
    print username
    print password
    file1 = open(".config1.txt", "w1")
    file1.write(username)
file1 = open(".config1.txt", "r")
username = file1.read()
file2 = open(".config2.txt", "r")
password = file2.read()
#please use database instead
#it is a temporary solution
if not file1:
    print"gotohell"
else:
    root = Tk()
    root.title("Messenger")
    root.geometry("800x700")
    root.configure(bg="white")
    frame1 = Frame(root, width=300,height=700,bg="#252e3e")
    frame1.place(x=0,y=0)
    frame2 = Frame(root, width=300,height=50,bg="#343b4a",bd=2,highlightbackground="white",highlightthickness=1,highlightcolor="white")
    frame2.place(x=0,y=0)
    L1 = Label(frame2,text=Chats,bg="#343b4a",fg="white",font="Belinda 12 bold")
    L1.place(x=120,y=10)
    frame3 = Frame(root, width=455,height=30,bg="white",highlightthickness=1,highlightbackground="#00ffff",highlightcolor="#00ffff")
    frame3.place(x=300,y=668)
    frame4 = Frame(root, width=600,height=50,bg="white",highlightthickness=1,highlightbackground="#00ffff",highlightcolor="#00ffff")
    frame4.place(x=300,y=0)
    L2 = Label(frame4, text="Debabrata",bg="white",fg="black",font="Belinda 12 bold")
    L2.place(x=180,y=10)
    tb1 = Text(frame3,bd=0,highlightthickness=1,highlightbackground="#00ffff",highlightcolor="#00ffff",width=50,height=2,font="Lato")
    tb1.place(x=0,y=0)
    photo1 = PhotoImage(file="icon3.png")
    bt1 = Button(root, image=photo1,bd=0,bg="white",highlightthickness=0,highlightbackground="#00ffff",highlightcolor="#00ffff",command=send)
    bt1.image = photo1
    bt1.place(x=755,y=660)
    root.mainloop()
