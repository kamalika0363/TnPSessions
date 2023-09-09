# Data structures
 - Partially Mutable 
### Python's primitive DS

1. list
2. tuple
3. set {data}
4. dictionary {no data}

- Default Heterogeneous (One can store any type of data)

## Which data structures will you use and why?

1. list [duplicate,index access, dynamic]
2. tuple (duplicate, index access, static)
3. set {no dulicate, no index access, dynamic}
4. dictionary {key based (key: no duplicate, value: duplicate)}

## When to use

1. list -> Array
2. tuple -> python uses maximum for security
3. set -> filteration
4. dictionary -> mapping the data

# List -> n elements

### Types

1. list.append
2. list.extend
3. list.insert
4. list.remove(x)
5. list.pop([i]) -> if not declared removes last element
6. list.clear()
7. list.index(x)
8. list.count(x)
9. list.sort() -> sorts in place
10. list.reverse()

# Questions

1. reverse a list
2. create a list using list comprehension
3. create a sequence of elements in data structure

# Tuple

- does not support item assignment

# Set
1. union
2. intersection
3. symmetric 
4. difference

- set can be auto iterative but cannot be accessed by index
- sets are not ordered

### Types
1. add(data)
2. update(set)
3. remove(data)
4. discard(data) -> remove add without any error


## IMP Methods 
1. Zip

# Strings

1. capitalize() -> This is capital
2. title() -> This Is Title
3. upper()
4. lower()
5. swapcase()
6. count(str,beg=0,end=len(string))
7. find -> INDEX
8. rfind -> answers from right but does not returns negative index
9. index 
10. center
11. ljust
12. rjust
13. replace(old,new[,max])
### Slicing
- s[:3] 0 to 2 index


# Error Handling
1. error -> any state which one cant have normal flow of code
2. exception -> is report of error
3. exception handling -> trying to continue either alternate or normal flow of code in presence of error