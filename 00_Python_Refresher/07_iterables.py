#Iterables : the list we normal we go through is iterable 
#whole list will get initialised when created
lst = [1,2,3,4,5,6,7,8]
for i in lst : 
    print(i)
#means lst is iterable

print("\n")


#Iterator : storing iterable list in iterator -> iterator(iterable)
#and elements stored in iterator have not initialised space in memory , 
# soo have to access or retrieve elements using next() function
#only member inistialised in memory at a time
#used when lot of elements are there to store , but need only needed one at a time
list2 = iter(lst) #setted 
print(next(list2))
print(next(list2))
print(next(list2))
#if more next used then list elements then will throw error of stopping iteration 
#whereareas for loop handles exception of it of not throwing error

for i in list2:
    print(i)
