for i in range(1,6,1):
    print('X'*i)

for i in range(7,0,-2):
    print('X'*i)

for i in range(5,0,-1):
    print(" "*(6-i),"X"*i)

# create cetner triangle of size n
# n entered by user

n=int(input("Enter n:"))
for i in range(1,n+1,1):
    if i%2==0:
        print(" "*(n-i),"X "*i)
    else:
        print(" "*(n-i),"# "*i)       

# ord('a') #returns ascii value
# chr(97) #returns character

for i in range(ord('P'),ord('T')+1):
    for j in range(ord('P'),i+1):
        print(chr(j),end="")
    print()

# for i in range(1,10):
#     print(i)
#     print()


# word triangle
# "python"
word=input("Enter: ")
for i in range(1, len(word)+1):
    print(word[:i])

# "kama" in "kamalika"
s="aeiou"
line = input("Enter: ").lower()
total = 0
for i in s:
    total += line.count(i)
    print(i,line.count(i))
print("total vowels: ", total)    

# count each character count in string in order
word="this is its"
sword=sorted(set(word))
sword.remove(" ")
line = input("Enter: ").lower()
total = 0
for i in sword:
    total += line.count(i)
    print(i,"--->",line.count(i))

# s="kamalika"
# print(s.center(30, "X"))

s="this is done by him"
print(s.replace("him", "her"))

s="12,234,567,8900"
slist=s.split(',')
print(slist)


# count number of words in line
print("Total word: ", len(input("Enter a line: ").split()))

#reverse line wordwise
# input: this is it
# output: it is this
# read line 
line = input("Enter a line: ")
# make list
rlist=line.split()
# reverse list
rlist.reverse()
# create a new string
rline=""
for word in rlist:
    rline=rline+" "+word
print("Reverse Line: ",rline)    

# print word count for each word in order for given line
# this is is this done

line=input("Enter a line to reverse: ")
wlist=(line.split())
for word in sorted(set(wlist)):
    print(word,"--->",wlist.count(word))