def myfunction():
    print('name is trushit')

myfunction()
myfunction()

def myfunction(name):
    print('hello wolrd')
    print('name is',name)

myfunction('trushit')

def myfunction(name):
    print('hello wolrd')
    return name*2

y=myfunction('trushit')
print('value is',y)

def myfunction():
    n1 = 10
    name='trushit'
    return name,n1

x,y=myfunction()
print('value is',x)
print('value is',y)

def calsum(n1=100,n2=200):
    print(n1+n2)
calsum()
calsum(10,20)


def calsum(n1,n2):
    print(n1+n2)
calsum(n2=10,n1=20)

def sum(*n1):
    sum=0
    for i in n1:
        sum+=i
    print(sum)
sum(20,10,30)
sum(50,40)

def sum(**n1):
    for i,j in n1.items():
        print(i,j)
sum(name='trushit',last='patel')

import demo

demo.myfunction()
z=demo.myfunction2('trushit')
print(z)