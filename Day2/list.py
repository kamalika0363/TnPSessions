l=[11,12,13,14,15,16,17,18,19]
print(l)

# auto iteration---for
for item in l: 
    print(item)

for i in range(0, len(l),1): # indexed access
    print("At", i,"we have", l[i])

l2=l+[3,4,5] # used for appending list to other
print(l2)

l2=l*3
print(l2) # used for repeating

l=[11,22,33,44,55,66,77]
# multiply each number by 2
for items in range(0, len(l)):
    l[items]=l[items]*2
print(l)

# Slice                  
l[::-1] # temporary
l=l[::-1] # inplace overwrite                   
print(l)

# [start:end;step:step]
l=[10,20,30,40,50,60]
print(l[2:4])

print(sum(l))
print(len(l))
print(max(l))
print(min(l))


print(sorted(l))
print(l)

m = [[10,20],[30,40,50,60]]
# print(len(m)) #2
# print(len(m[1])) #4

for sublist in m:
    # print(sublist)
    for items in sublist:
        print(items)

# list comprehension
# expression for var in range
l=[x for x in range(10,101,10)]
print(l)        

a=[]
# a.append(int(input("enter a number: ")))
# print(a)
a=[11,12,13,14,15,16,17,18,19]
# # a.insert(-110, 2000)

a.extend([12])
print(a)


# flat the list
m2=[]
m = [[10,20],[30,40,50,60],[80,90,100]]

for sublist in m:
    for item in sublist:
        m2.append(item)

m3=[]
for sublist in m:
    m3.extend(sublist)
print(m3)
# m3.remove(50)    
m3.pop(0)        
print(m3)            

a= [55,11,22,44,33,66]
# sorted(a) # returns sorted list -> temporary
# print(a)

# print(a.sort()) # -> permanent

a[::-1]
a.reverse()
print(a)


