def even(num):
    if num%2==0:
        return True
lst = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(even, lst)))

#using lambda - easier
print(list(filter(lambda num:num%2==0,lst)))

#map function gives about all and filter function gives about reuired only
