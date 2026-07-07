#Playing with {} and .format 

def hello(name, age):
    return "Hello your name is {} and age is {}".format(name,age)
print(hello("naman",20))

#Using temp vars 
def hello1(name, age):
    return "Hello your name is {name1} and age is {age1}".format(age1 = age, name1=name)
print(hello1("satwik", 76))