import socket
from tkinter import *
def send(listbox,entry):
    message=entry.get()
    listbox.insert('end',"Client:"+message)
    entry.delete(0,END)
    s.send(bytes(message, "utf-8"))
    receive(listbox)

def receive(listbox):
    message=s.recv(100)
    listbox.insert('end',"Server:"+message.decode("utf-8"))

root=Tk()
entry=Entry()
entry.pack(side=BOTTOM)
listbox=Listbox(root)
listbox.pack()
button=Button(root,text="send", command= lambda :send(listbox,entry))
button.pack(side=BOTTOM)

r_button=Button(root,text="receive", command= lambda :receive(listbox))
r_button.pack(side=BOTTOM)
root.title("Client")
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST_NAME=socket.gethostname()
PORT=12346
s.connect((HOST_NAME,PORT))
# while True:
#     m=s.recv(100)
#     print("Server:" +m.decode("utf-8"))
#     msg_to_snd=input("Client:")
    # s.send(bytes(msg_to_snd,"utf-8"))

root.mainloop()