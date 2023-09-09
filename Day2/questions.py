# LEVEL 1
# keep accepting elements from user till blank is given
# add all element in list
# print sum of all elements

list = []
while True:
    data=input("Enter:")
    if data=="":
        break
    list.append(float(data))
print("Sum is:",sum(list))    

# LEVEL 2
# keep accepting elements from user till blank is given
# add all element in list
# print sum of all elements
# print all elements > the average of all elements

list = []
while True:
    data=input("Enter:")
    if data=="":
        break
    list.append(float(data))
avg=sum(list)/len(list)
for i in list:
    if i>avg:
        print(i)   


