import array as ar
a=ar.array('b',[84,104,105,24,63])
a.extend([3,8,12,14])
a.insert(4,6)
b=ar.array("b",[3,8,9,4,6])
c=a+b
#print(c[2:6])

#for i in a:
#    print(i)

b=0
while b==5:
    print(c[a])
    b=b+1
    