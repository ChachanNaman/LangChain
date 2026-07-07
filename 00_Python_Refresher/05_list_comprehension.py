# List Comprehension -> its a concise way of creating a list 
# creation : Operation -> then For loop -> then zero or more if or for loops

#Long Method
list1 = [1,2,3,4,5,5,6,7,8,9]
list2 = []
def square(lst):
    for i in lst:
        list2.append(i*i)
    return list2
print(square(list1))


#Easy way using List comprehension 
list3 = [i*i for i in list1 ]
print(list3)

list4 = [i*i for i in list1 if i%2==0]
print(list4)

