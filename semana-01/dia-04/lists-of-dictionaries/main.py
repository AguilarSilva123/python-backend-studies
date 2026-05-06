users = [
    {
        "name": "Julia Bianca",
        "age": 26,
        "sex": "female",
        "height": 1.63
    },
    {
        "name": "João Vitor",
        "age": 28,
        "sex": "male",
        "height": 1.75
    },
    {
        "name": "Anorina",
        "age": 70,
        "sex": "female",
        "height": 1.60
    },
    {
        "name": "Edilaine",
        "age": 46,
        "sex": "female",
        "height": 1.60
    },
    {
        "name": "Davi",
        "age": 15,
        "sex": "male",
        "height": 1.55
    }
]

for user in users:
    if user["age"] >= 18:
        print(user["name"])