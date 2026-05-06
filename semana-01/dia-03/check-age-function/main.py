def check_age(age):
    if(age>18):
        return "Access allowed"
    else:
        return "Access denied"
    
user_age = int(input("Enter your age: "))
result = check_age(user_age)

print(result)
