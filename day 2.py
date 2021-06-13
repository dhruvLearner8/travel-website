################## VARIABLES IN PYTHON ##################
n1 = 10
n2 = 10.5
name = "trushit"
print(n1)
print("vale of n2 is ",n2)
print("nmae is ",name)
##############################
name = "trushit patel"
print(name)
#assigning diff vale
name = "_truxxhit"
print(name)
##############################
a,b,c = 10, 10.5 , "Trushit patel"
print("value of a is ",a)
print("value of b is ",b)
print("value of c is ",c)
##############################
a=b=c=4
print("value of a is ",a)
print("value of b is ",b)
print("value of c is ",c)
##############################
n1,n2,name =10,10.5, "trushit"
print(n1)
print("vale of n2 is ",n2)
print("nmae is ",name)
##############################
n1=n2=name =10
print(n1)
print("vale of n2 is ",n2)
print("nmae is ",name)
################## DATA TYPES IN PYTHON ##################
n2 = 10.5
print("n2 is ",n2,type(n2))
n2 = 10
print("n2 is ",n2 , type(n2))
n2 = 10 + 2j
print("n2 is ",n2 ,type(n2))
print("n2 is ", isinstance(n2,complex))
print("n2 is ", isinstance(n2, int))
##############################
name = "trushitpatel"
print("name is "+name)
print(name[2])
print(name[1:6])
print(name[1:])
print(name[:7])
print(name+" says hello ")
##############################
name = [10,20,30.5,'trushit']
print(name)
print(type(name))
print(name[2])
print(name[1:3])
print(name[1:])
print(name[:3])
##############################
name = (10,20,30.5,'trushit')
#name[1]=40 this will show error
print(name)
print(type(name))
print(name[2])
print(name[1:3])
print(name[1:])
print(name[:3])
##############################
name = [10,20,30.5,'trushit']
print(name)
name[1]=40.7
print(name)
print(type(name))
print(name[2])
print(name[1:3])
print(name[1:])
print(name[:3])
##############################
d={10:'trushit', 'a1':100, 20:200 }
print(d)
print(type(d))
print(d[10])
print(d['a1'])
print(d[20])