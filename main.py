
# importing tkinter
from tkinter import *
# importing random
import random
num=random.randint(1,50)
print(num)

# GUI work start here 
root=Tk()
root.minsize(500,500)
root.maxsize(500,500)
root.title(" BY IMRAN RAEENI")

# SETUP for GUI 
root.config(bg="white")
l0 = Label(root, text="THE GUESS GAME",font=20)
l0.place(x=170, y=10)
ln = Label(root, text="BETWEEN [1,50] ",font=30,border=5,bg="white")
ln.place(x=170, y=60)
i = Entry(root,background="blue",font=20,border=10)
i.place(x=150, y=100)
count=0



# define sub function :
def sub():
    global count
    if (int(i.get())!= num):

        count = count + 1
        l2 = Label(root, text=f"COUNTER : {count}", bg="red",font=6)
        l2.place(x=200, y=350)
        #check wether the number is greater or smaller
        if (int(i.get()) < num):
            l3 = Label(root, text=f"RE-ENTER GREATER THAN {int(i.get())}", bg="yellow",width=33)
            l3.place(x=150, y=280)
        else:
            l3 = Label(root, text=f"RE-ENTER LESS   THAN {int(i.get())}", bg="yellow", width=33)
            l3.place(x=150, y=280)
    else:
        l = Label(root, text="YOU WIN", bg="green", width=50)
        l.place(x=100, y=230)
        l4 = Label(root, bg="white",width=33)
        l4.place(x=150, y=280)

b=Button(root,text="SUBMIT",width=33,command=sub)
b.place(x=150,y=180)
exit=Button(root,text="EXIT",width=33,bg="red",command=root.destroy)
exit.place(x=150,y=450)
root.mainloop()