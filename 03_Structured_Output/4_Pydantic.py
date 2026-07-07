from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name : str
    age : Optional[int] = None  #if theres no value specified in age then print none
    mail : EmailStr
    cgpa : float = Field(gt=0, lt=10, default = 5, description='A decimal value of a student cgpa')
new_student = {'name' : 'naman', 'age' : '23', 'mail' : 'abc@gmail.com', 'cgpa' : 8}
#it will throw if i type integer in name as it is string 
student = Student(**new_student)


print(student)
print(student.name)

#converting student into dict 
student_dict = dict(student)
print(student_dict['age'])

#converting student into json 
student_json = student.model_dump_json()
print(student_json)



