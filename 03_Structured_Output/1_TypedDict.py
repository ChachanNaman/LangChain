from typing import TypedDict

class Person(TypedDict):
    name:str
    age:int

#now to make new dict from class 
new_person : Person = {'name' : 'naman' , 'age' : 19}

print(new_person)