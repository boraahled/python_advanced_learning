import json 

new_cards = {
    "Apple" : "تفاحة",
    "Book" : "كتاب",
    "Banana" : "موزة"
}

# with open("cards.json",mode="w",encoding="utf-8") as file :
#     json.dump(new_cards, file, indent = 4, ensure_ascii = False)

with open("cards.json", mode="r", encoding="utf-8") as file :
    save_data = json.load(file)

new_data = {"Divelopper":"مبرمج",
            "Orange":"برتقالة"}
save_data.update(new_data)

with open("cards.json" , mode="w" , encoding="utf-8") as file:
    json.dump(save_data,file,indent=4,ensure_ascii=False)
