import json 

contacts = {
    "ahmed" : "0679833829",
    "sara" : "0748338229",
    "nora" : "0684399374"
}

with open("practice_json_file.json",mode="w") as file :
    json.dump(contacts,file,indent=4)

with open("practice_json_file.json",mode="r") as file :
    contact = json.load(file)


new_contact = {
    "omar" : "0747843456",
    "otman" : "0655577488",
    "hassan" : "0584895839"
    }
contact.update(new_contact)

with open("practice_json_file.json","w") as file :
    json.dump(contact,file,indent=4)
