import json
from tkinter import Tk , Label ,Button, Entry ,END,messagebox

CARDS_FILE = "flashCard.json"

def save_card():
    question = entry_q.get().strip().lower()
    answer = entry_a.get().strip().lower()
    if not question or not answer:
        messagebox.showwarning(title="warrning",message="please enter your flash card",icon="warning")
        return
    else:
        cards = {question : answer}
        try :
            with open(CARDS_FILE , "r" , encoding="utf-8") as file :
                data = json.load(file)

        except FileNotFoundError:
            with open(CARDS_FILE , "w" , encoding="utf-8") as file :
                json.dump(cards , file , indent=4 , ensure_ascii= False)

        except :
            messagebox.showerror(title="error" , message="please try again" , icon="error")

        else :
            data.update(cards)
            with open(CARDS_FILE , "w" , encoding="utf-8") as file :
                json.dump(data , file , indent=4 , ensure_ascii= False)

            messagebox.showinfo(title="Saved",message=f"Saved card '{question}' successfully!",icon="info")

        entry_a.delete(0,END)
        entry_q.delete(0,END)


root = Tk()
root.title("Flash Cards Game")
root.geometry("480x520")

# =============== partie 1 =====================

title = Label(root,text="Add a new flashcards" , font=("Monospace",17,"bold"))

question = Label(root,text="Question or English Word :" , font=("Monospace",12))
entry_q = Entry(root , width=30 , font=("Monospace",14) ,fg="gray")

answer = Label(root,text="Correct Answer or Meaning :" , font=("Monospace",12))
entry_a = Entry(root , width=30 , font=("Monospace",14) ,fg="gray")

save_button = Button(root , text="save Flash Card" , bg="blue" ,fg="white" , font=("Arial" , 12 , "bold") , command=save_card)
line = Label(root,text="___________________________________________" , font=("Monospace",12))

title.pack(pady=10)
question.pack(pady=10)
entry_q.pack(pady=10)
answer.pack(pady=10)
entry_a.pack(pady=10)
save_button.pack()
line.pack(pady=5)

# ====================== partie 2 ===========================

score = question = Label(root,text="score : 0" , font=("Monospace",10,"bold"))
generate_question = Label(root,text="click new quetion to start" , font=("Monospace",12))
entry_question = Entry(root , width=30 , font=("Monospace",12))

button_answer = Button(root , text="Cheek Answer" , bg="blue" ,fg="white" , font=("Arial" , 12 , "bold"))
button_question = Button(root , text="New Question" , bg="blue" ,fg="white" , font=("Arial" , 12 , "bold"))

score.pack(pady=5)
generate_question.pack(pady=5)
entry_question.pack(pady=5)
button_answer.pack(pady=5)
button_question.pack(pady=5)







root.mainloop()