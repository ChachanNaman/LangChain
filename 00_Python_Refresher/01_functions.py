#Print Function
def even_odd(num):
    if num%2 == 0 :
        print("The number is even")
    else:
        print("The numer is odd")

even_odd(24)

#Return Function
def hello():
    return "Hello naman"
val = hello()
print(val)

#Positional Function 
def myself(name, age = 20):
    print("My name is {} and my age is {}".format(name, age))
myself("naman")
    # Here : name is positional argument 
    #        age is keyword argument


def hello(*args, **kwargs):
    print(args)
    print(kwargs)
list = ['krish', 'naman']
list1 = {'age' : 20 , 'dob' : 2005}
hello(list, list1)

#Function returning 2 values 
def evenoddsum(lst):
    evensum = 0
    oddsum = 0
    for i in lst:
        if i%2==0:
            evensum = evensum + i
        else : 
            oddsum = oddsum + i
    return evensum,oddsum
lst = [1,2,3,4,5,6,7]
sum = evenoddsum(lst)
print(sum)