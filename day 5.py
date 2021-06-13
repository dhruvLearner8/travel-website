'''class Demo:
    def myfunction(self):
        print("this is myfunction of class")
    def show(self,name):
        print('name is',name)
    def sum(self,n1,n2):
        ans=n1+n2
        print("ans is",ans)
    def __init__(self) -> None:
        print('this is demo class')
    def __init__(self,name) -> None:
        print('name is',name)
#d1=Demo()
d1=Demo('trushit')
d1.myfunction()
d1.show('trushit')
d1.sum(20,30)

class Demo1:
    name=''
    def fucn1(self):
        print('this is normal method')
    def func2(self,n):
        self.name=n
    def show(self):
        print('name is',self.name)

d2=Demo1()
d2.fucn1()
d2.func2('trushit')
d2.show()

class Demo3:
    name=''
    def __init__(self,n1) -> None:
        self.name=n1
    def show(self):
        print('name is',self.name)
d3=Demo3('trushit patel')
d3.show()

class Demo4:
    num1=0
    num2=0
    def __init__(self,n1,n2) -> None:
        self.num1=n1
        self.num2=n2
    def show(self):
        ans = self.num1 + self.num2
        print('ans is',ans)
d4=Demo4(10,20)
d4.show()
class parent:
    def func1(self):
        print('this is from parent class')
class child(parent):
    def func2(self):
        print('this is from child class')

d1 = child()
d1.func1()
d1.func2()
class parent:
    def __init__(self) -> None:
        print('this is constructor of parent class')
    def func1(self):
        print('this is from parent class')
class child(parent):
    def __init__(self) -> None:
        print('this is constructor of child class')
    def func2(self):
        print('this is from child class')
d1=child()
d1.func1()
d1.func2()

class demo1:
    def __init__(self) -> None:
        print('this is default demo class constructor')
    def func1(self):
        print('this is demo1/parent clas method')
class demo2(demo1):
    def __init__(self) -> None:
        print('this is child/demo2 class constructor')
    def func2(self):
        print('this is child/demo2 class method')
class demo3(demo2):
    def func3(self):
        print('this is method of demo3 class')

d1=demo3()
d1.func1()
d1.func2()
d1.func3()

class demo1:
    def __init__(self) -> None:
        print('this is default demo1 class constructor')
    def func1(self):
        print('this is demo1/parent clas method')
class demo2:
    def __init__(self) -> None:
        print('this is child/demo2 class constructor')
    def func2(self):
        print('this is child/demo2 class method')
class demo3(demo1,demo2):
    def func3(self):
        print('this is method of demo3 class')
d1=demo3()
d1.func1()
d1.func2()
d1.func3()

class demo1:
    def __init__(self) -> None:
        print('this is default demo1 class constructor')
    def func1(self):
        print('this is demo1/parent clas method')
class demo2(demo1):
    def __init__(self) -> None:
        print('this is child/demo2 class constructor')
    def func2(self):
        print('this is child/demo2 class method')
class demo3(demo1):
    def func3(self):
        print('this is method of demo3 class')
d1=demo2()
d1.func1()
d1.func2()

d2=demo3()
d2.func1()
d2.func3()

class demo1:
    def __init__(self) -> None:
        print('this is default demo1 class constructor')
    def func1(self):
        print('this is demo1/parent clas method')
class demo2:
    def __init__(self) -> None:
        print('this is child/demo2 class constructor')
    def func2(self):
        print('this is child/demo2 class method')
class demo3(demo1,demo2):
    def func3(self):
        print('this is method of demo3 class')
class demo4(demo3):
    def func4(self):
        print('hybrid inheritance/this is method of demo4 class')
d1=demo4()
d1.func1()
d1.func2()
d1.func3()
d1.func4()
'''
class demo:
    def func1(self,n1,n2):
        ans=n1+n2
        print('ans is',ans)
    def func1(self,n1,n2,n3):
        ans=n1+n1+n3
        print('ans is',ans)
d1=demo()
#d1.func1(10,20)
d1.func1(10,20,30)

