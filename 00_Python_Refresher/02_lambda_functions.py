#Lambda Function : is an anonymus function , a function with no name , can only works when there is only one value in return 

#Normal return function 
def addition(a,b):
    return a+b
val = addition(4,3)
print(val)

#Lambda return function
addition = lambda a,b : a+b
val1 = addition(22,33)
print(val1)

even = lambda c : c%2==0
val2 = even(12)
print(val2)

