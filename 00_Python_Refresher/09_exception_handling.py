#we handle exception by using try catch block

#Method-1
try:
    a=b
except:
    print("Something went wrong")


#Method-2 : using Exception class
#
#
try:
    a=b
except Exception as ex:
    print(ex) #will give the same exception statement that terminal gives usually-> not user friendly

#Exception can be derived into multiple types
#a=b is a type of NameError

#Method-3 : when you know what type of exception : Always place NameError on top of Exception , varna Exception execute hojaega

try:
    a=b
except NameError :
    print("user not defined var")
except Exception as ex:
    print("Something went wrong")

#try else block : 
try:
    a = int(input("Enter the number 1"))
    b = int(input("Enter the number 2"))
    c = a/b
    d = a*b
    e = a+b
except ZeroDivisionError: 
    print("dont enter the number 0")
except Exception as ex:
    print(ex)
else: #this block will get executed when there is no error , if exception there then else block not get excuted
    print(c)
    print(d)
    print(e)

#try else finally : 

try:
    a=b
except NameError :
    print("user not defined var")
except Exception as ex:
    print("Something went wrong")

#try else block : 
try:
    a = int(input("Enter the number 1"))
    b = int(input("Enter the number 2"))
    c = a/b
    d = a*b
    e = a+b
except ZeroDivisionError: 
    print("dont enter the number 0")
except Exception as ex:
    print(ex)
else: #this block will get executed when there is no error , if exception there then else block not get excuted
    print(c)
    print(d)
    print(e)
finally : #will get executed anyhow 
    print("Everything executed !")
