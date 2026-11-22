from tkinter import Tk , Label , Button ,Entry , END
from datetime import datetime

def calculate_age():
    age = int(entry.get())
    if age :
        calc_age = datetime.now().year - age
        label2.config(text=f"your age is {calc_age} years" ,fg="black",font=("Monospace" , 20))
        entry.delete(0,END)
    else:
        label2.config(text="please enter your age" ,fg="red",font=("Monospace" , 20))


root = Tk()
root.title("Quick AgeCalculator")
root.geometry("400x340")

label = Label(root,text="enter your birthday year")
entry = Entry(root,width=25,font=("Arial",14) ,fg="blue")
button = Button(root,text="Calculate",font=("Arial",10),fg="white",bg="green",command=calculate_age)
label2 = Label(root,text="")

label.pack(pady=10)
entry.pack(pady=10)
button.pack(pady=10)
label2.pack(pady=20)


root.mainloop()