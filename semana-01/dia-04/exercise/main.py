users = [
    {
        "name": "Ana",
        "age": 16
    },
    {
        "name": "Julia",
        "age": 26
    },
    {
        "name": "João",
        "age": 28
    }
]

# A list containing only names
names = [user["name"] for user in users]
print(names)

# A list containing only 18+
eighten_or_more = [user["name"] for user in users if user["age"] >= 18]
print(eighten_or_more)

# Each of the ages multiplied by 2
ages_per_2 = [2*age["age"] for age in users]
print(ages_per_2)