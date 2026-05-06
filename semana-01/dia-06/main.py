from utils import parse_line, is_adult, calculate_avarege_age

users = [] 
errors = 0

with open("data.txt", "r") as file: 
    for line in file:
        result = parse_line(line) 
        if result["ok"]:
            users.append(result["data"])
        else:
            print(f"Erro {result["error"]["code"]}: {result["error"]["message"]}")
            errors += 1
            

adults = [user for user in users if is_adult(user)]

average_age = calculate_avarege_age(users)

print(f"Total valid users: {len(users)}")
print(f"Total invalid lines: {errors}")
print(f"Adults: {len(adults)}")
for adult in adults:
    print(f"{adult['name']} is an adult.")
print(f"Avarege age: {average_age:.2f}")