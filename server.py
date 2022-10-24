import socket
from tkinter import *
def send(listbox,entry):
    message=entry.get()
    listbox.insert('end',"Server:"+message)
    entry.delete(0,END)
    client.send(bytes(message, "utf-8"))

def receive(listbox):
    msg_from_client=client.recv(100)
    listbox.insert('end',"Client:"+msg_from_client.decode("utf-8"))

root=Tk()
entry=Entry()
entry.pack(side=BOTTOM)
listbox=Listbox(root)
listbox.pack()
button=Button(root,text="send", command= lambda :send(listbox,entry))
button.pack(side=BOTTOM)

r_button=Button(root,text="receive", command= lambda :receive(listbox))
r_button.pack(side=BOTTOM)
root.title("Server")
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST_NAME=socket.gethostname()
PORT=12346
s.bind((HOST_NAME,PORT))
s.listen(4)


client,address=s.accept()
# while True:
#     message=input("Server:")
#

root.mainloop()
