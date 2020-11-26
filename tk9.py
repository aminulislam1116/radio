from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("455x233")
root.title('Radio button')

##
def order():
    tmsg.showinfo("Order received", f"We have received your order for {var.get()}. Thanks for ordering")

var = IntVar()
#####
Label(root,text='Whar you like to sir',font='lucida 19 bold',justify=LEFT,padx=14).pack()

radio=Radiobutton(root,text='Dosa',padx=14,variable=var,value=1).pack(anchor="w")
radio=Radiobutton(root,text='Idly',padx=14,variable=var,value=2).pack(anchor="w")
radio=Radiobutton(root,text='Pratha',padx=14,variable=var,value=3).pack(anchor="w")
radio=Radiobutton(root,text='somosa',padx=14,variable=var,value=4).pack(anchor="w")
Button(root,text='Get dolar',pady=10,command=order).pack()


root.mainloop()