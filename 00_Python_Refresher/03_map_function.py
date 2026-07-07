def evenodd(num):
    if num%2==0:
        print("the number {} is EVEN".format(num))
    else:
        print("the number {} is ODD".format(num))

lst = [1,2,3,4,5,6,7,8,9]

#Iterating is difficult by using For loop better to use map function
#map(parameter, iterable)
list(map(evenodd, lst))