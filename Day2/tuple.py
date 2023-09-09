# t=(10,20,30)
# t[0]=t[0]*2 # gives error
# t=(11,22) # changing tuple it self

t=(11,22,[10,20,30])
print(t)

t[2].extend([100,200,300])
# list within tuple is still dynamic

print(t)