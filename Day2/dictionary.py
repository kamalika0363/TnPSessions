d={1: "One", 2: "Two", 3: "Three"}
print(d)

# # # # print(d[2])

# read a number and print in words
# 361----> three six one

d={1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 0: "Zero"}

print(d)

data=int(input("Enter a number: "))
rdata=0
while data>0:
    d=data%10
    data=data//10
    rdata=rdata*10+d
print(rdata)
while rdata>0:
    data=rdata%10
    rdata=rdata//10


l=[11,2,1,56,78,9,23,65,89,67,5,12,34,11,23]
# create 2 list one greater than avg and one lesser or equal

print("sum: ", sum(l))
avg = sum(l)/len(l)
print("avg: ", avg)

list_less=[]
list_greater=[]

for i in l:
    if i<avg:
        list_less.append(i)
    else:
        list_greater.append(i)
print("list_less: ",list_less)
print("list_greater: ",list_greater)            


# len(), pop(), append()
l=[11,22,33,44,55]
for i in range (len(l)):
    first = l.pop(0)
    l.append(first)
    last = l.pop()
    l.insert(0,last)
    print(l)

s=[1,2,3,4]
n=["bb","cc","dd","aa"]
s=sorted(s)
n=sorted(n)
mapped=dict(zip(s,n))
print(mapped)