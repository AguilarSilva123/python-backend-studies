with open("data.txt", "r") as file: # open the file in read mode 
    lines = file.readlines() # read all lines and store them in a list

print(lines)