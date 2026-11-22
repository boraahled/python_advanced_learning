from tkinter import Tk , Button , Label , Entry ,END

def say_hello():
    name = entry.get()
    if name :
        greating_name.config(text=f"hello {name}! welcome to tkinter",fg="green")
        entry.delete(0,END)
    else:
        greating_name.config(text="please enter your name",fg="red")


window = Tk()
window.title("first program GUI")
window.geometry("400x320")

lable1 = Label(window,text="enter your name" , font=("Monospace" , 12))
entry = Entry(window,font=("Monospace" , 11),width=25)
button = Button(window,text="click here" ,font=("Arial" , 10),bg="blue",fg="white",command= say_hello)
greating_name = Label(window,text="waiting for your name ..." , font=("Arial" , 20))

lable1.pack(pady=10)
entry.pack(pady=10)
button.pack(pady=10)
greating_name.pack(pady=20)

window.mainloop()