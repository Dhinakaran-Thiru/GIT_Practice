"""for i in range(0,6):
    print(i)
for i in range(0,11):
    print(i)"""
#print 2nd table using python
"""for i in range(0,11):
     print("98x",i,"=",i*98)"""
"""a=int(input())
b=int(input())
for i in range(a+1,b):
    print(i)"""
"""count=0
for i in range(1,11):
    if i%2==0:
        count=count+1
print(count)"""
li=[4,2,3,5,6,7,8,9,4,4,68,4,6,4,9,56]
unique=[]
duplicates=[]
for i in li:
    if i in unique:
        duplicates.append(i)
    else:
        unique.append(i)
for j in unique:
    count=1
    for x in duplicates:
        if j==x:
            count=count+1
    if count==2:
        print(j)
















