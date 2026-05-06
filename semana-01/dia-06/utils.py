def parse_line(line):
    try:
        name, age = line.strip().split(",")
        if not name: 
            return { 
                "ok" : False,
                "error" : {
                    "code" : "INVALID_NAME",
                    "message" : "Name cannot be empty."
                }
            }
        age = int(age)
        return {
            "ok" : True,
            "data" : {
                "name" : name,
                "age" : age
            }
        }
    except ValueError:
        return {
            "ok" : False,
            "error" : {
                "code" : "INVALID_AGE",
                "message" : "Invalid age format. Age must be an integer."
            }
        }
    except Exception as e:
        return {
            "ok" : False,
            "error" : {
                "code" : "UNKNOWN_ERROR",
                "message" : str(e)
            }
        }
    
def is_adult(user):
    return user["age"] >= 18

def calculate_avarege_age(users):
    if not users:
        return 0
    total = sum(user["age"] for user in users)
    avarege = total / len(users)
    return avarege
