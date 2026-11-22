import json 
from tkinter import Tk , Button , Label , Entry ,END ,messagebox

def search_word() :
    word = search_entry.get().strip().title()
    if not word :
        messagebox.showwarning(title="warning" , message="enter the word first!")
        return
    else:
        try:
            with open("cards.json","r",encoding="utf-8") as file :
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showwarning(title="File not found" , message="No saved word yet! Please add words first")
        except:
            messagebox.showwarning(title="Warning" , message="Error")
        else:
            if word in data :
                messagebox.showinfo(title="Info" , message=f"Meaning of {word} is : \n {data[word]}")
            else:
                messagebox.showwarning(title="Not Found" , message=f"{word} is not found in your dictionary!")
            search_entry.delete(0,END)



root = Tk()
root.title("safe your App")
root.geometry("420x300")

search_label = Label(root,text="search for a word in the dictionary:",font=("Monospace" , 14))
search_entry = Entry(root , font=("Arial" , 10),width=25)
search_button = Button(root ,text="Search Now" , font=("Monospace" , 14) , command=search_word)

search_label.pack(pady=10)
search_entry.pack(pady=10)
search_button.pack(pady=10)


root.mainloop()