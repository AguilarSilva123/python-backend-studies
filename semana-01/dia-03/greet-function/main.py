def greet(name): #define a function called greet that takes a parameter name
    return f"hello, {name}!" #return a string that says "hello, {name}!" where {name} is the value of the name parameter

user_name = input("What is your name? ") #ask the user for their name and store it in a variable called user_name
message = greet(user_name) #call the greet function with the user_name variable as an argument and store the result in a variable called message

print(message) #print the message variable to the console, which will display the greeting to the user