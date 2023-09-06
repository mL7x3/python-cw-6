# write your code here
person = {
           "name": "mubarak" ,
            "age" : "14" ,
           "hobbies" : "programer"
       }
print(person["name"])
print(person["age"])

person["age"] = "15"
person["country"] = "Kuwait"

print(f"hi my name is {person['name']}, iam {person['age']}, iam from {person['country']}, i hobe to be a {person['hobbies']} ")
print(f"{person}")



person.get("Sciences")

def check_hobbies(person):
    if person["hobbies"] >= 3 :
        print("wow you are amazing")