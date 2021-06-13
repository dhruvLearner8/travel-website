############################## USER INPUT ##############################
'''name = input('enter name:')
print("name is:",name)
##############################
n1 = input('enter num1:')
n2 = input('enter num2:')
ans = n1+n2
print('sum is:',ans)
##############################
n1 = int(input('enter num1:'))
n2 = int(input('enter num2:'))
ans = n1+n2
print('sum is:',ans)'''
############################## CONDITIONAL STATEMENTS ##############################
n1 = 20
n2 = 10
if n1>n2 :
    print('n1 is greater')
if n2>n1 :
    print('n2 is greater')
else:
    print('both are equal')
    ''' logic problem'''
##############################
n1 = 20
n2 = 10
if n1>n2 :
    print('n1 is greater')
if n2>n1 :
    print('n2 is greater')
##############################
n1 = 20
n2 = 10
if n1>n2 :
    print('n1 is greater')
elif n2>n1 :
    print('n2 is greater')
else:
    print('both are equal')
##############################
n1 = 20
n2 = 20
if n1>n2 :
    print('n1 is greater')
elif n2>n1 :
    print('n2 is greater')
else:
    print('both are equal')
##############################
n1 = 20
n2 = 100
if n1>n2 :
    print('n1 is greater')
elif n2>n1 :
    print('n2 is greater')
else:
    print('both are equal')
##############################
n1 = 10
if n1>=0:
    if n1 == 0:
        print('n1 is zero')
    else:
        print('n1 is positive')
else:
    print('n1 is negative')
############################## LOOPS ##############################
i=1
while i<=10 :
    print('value is ',i)
    i+=1
##############################
for i in 'hello':
    print(i)
##############################
li = [10,20,'trushit']
print(li)
for i in li:
    print(i)
##############################
for i in range(10):
    print('value is',i)
for j in range(1,5):
    print('value is',j)
for k in range(1,10,2):
    print('value is',k)
##############################
li = [10,20,'trushit']
print(li)
for i in li:
    print(i)
for j in range(len(li)):
    print('value is',li[j])
##############################
li = [10,20,'trushit']
print(li)
for i in li:
    print(i)
for j in range(len(li)):
    print('value is',li[j])
else:
    print('loop end...')
##############################
for i in range(10):
    if i%2==0:
        continue
    print('value is',i)
##############################
i=0
while i<=10:
    print('value is',i)
    i+=1
    if i>=5:
        break
##############################
li = [10,20,'trushit']
print(li)
for i in li:
    print(i)
for j in range(len(li)):
    print('value is',li[j])
else:
    pass