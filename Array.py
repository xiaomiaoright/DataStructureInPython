"""
# Array in Python : List
# What is Array?
A collection of elements each identified by an array index or key. Items can be of different types in python

# What is properties of array?
store data of same type
Random access with Keys
multiD arrays
Dynamic array (size change)

# Applications
Lookuptables
Hashtables
heaps

# Advantages

# Disadvantages
# Operations
Add
Remove

"""
numberArr = [1,2,3,4]

# Random indexing -- O(1) get items with index
print(numberArr[2])


# Update values give index -- O(1)
numberArr[2] = 60
numberArr[3] = 'apple'



# Tranverse through array -- O(n)
for num in numberArr:
    print(num)

for i in range(len(numberArr)):
    print(numberArr[i])

# Slicing array
print(numberArr[2:4])

# Linear  Search O(N)
# Insert a value in the beginning of array
