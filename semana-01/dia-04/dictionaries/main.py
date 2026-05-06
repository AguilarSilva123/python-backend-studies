user = { # the struct user contains name, midle name, last name, age and status from user
    "name": "João",
    "middle_name": "Vitor Aguilar",
    "last_name": "Silva Assis",
    "age": "28",
    "active": True
}

print(user["name"]) # print user name 

user["email"] = "joao_vitor@gmail.com" # add a new indo in user: email

for key, value in user.items(): # print all info from user and your respectives keys
    print(key, value)