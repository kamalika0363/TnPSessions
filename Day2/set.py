a={1,2,3,4}
b={3,4,5,6}
print(a|b)
print(a+b)
print(a-b)
print(b-a)

all={1,2,3,4,5,6,7,8,9,10}
d={1,4,9}
s={1,7,8}
b={1,4,6}

print("Taken in all: ", d&s&b)
print("Not part of anything: ", all-d-s-b)

s=set()
print(s,type(s))
s.add(100)
s.add(200)
s.add(300)
s.add(100)
print(s)

s.remove(100)
print(s)
s.discard(100) # does not gives error
print(s)


l = [11,22,11,33,44,22,22,66,77,99,22,11,22,33]
# print count of each unique element in sorted order
# l = {11,22,11,33,44,22,22,66,77,99,22,11,22,33}
ul=sorted(set(l))
print("Sorted unique list: ",ul)
for i in ul:
    print(i,"--->", l.count(i))   

