"""
# What is hash table?
For arrays,search operation takes O(N) if index unknown. Search can be reduced to O(logN) in Balanced Binary Search Tree structure. With hashing it can be reduced to O(1).
Hashtable is a data structure implemented with an array. A structure that can map keys to values (index of array). A hash table uses a hash function to compute an index into an array of buckets or slots from which the values will be found.
So hash tables store the data values in array buckets

# What is hash function?
Hash-functions take the keys as input and calculate an index in the values array. So basically hash-functions map keys to array indexes.
Integer keys it is quite easy to generate an array index. Make sure the generated value will be valid. It must be within the range [0,arraySize-1]. We can transform the values with the modulo operator.
Strings as keys: transform the characters into integers based on the ASCII values. Every single character is represented by an integer.

# Collisions
Open addressing
chaining
Resixing

# Applications

"""
# Define hashtable object
class Hashtable(object):
    def __init__(self):
        self.size = 10
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def hashfunctions(self, key):
        sum = 0
        for pos in range(len(key)):
            sum = sum + ord(key[pos])
        return sum % self.size
    
    def put(self, key, data):
        index = self.hashfunctions(key)

        # in case of collison, the current keys[index] is not available
        while self.keys[index] is not None: 
            if self.keys[index] == key: # find the available slot
                self.values[index] = data # update the values array, overwrite
                return 
            index = (index+1) % self.size # generating a new index until get a available keys[index]
        
        # insert tge key and value into arrays
        self.keys[index] = key
        self.values[index] = data

    def get(self, key):
        # get the index from hashfunction
        index = self.hashfunctions(key)

        # it is possible that a new key was generated due to collision in put
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index+1) % self.size
        
        # self.keys[index] is all None in the keys array, means key is not present
        return None

if __name__ == "__main__":
    table = Hashtable()
    table.put("apple", 10)
    table.put("orange", 20)
    table.put("car", 30)
    table.put("table", 40)

    table.get('car')
    table.keys
    table.values
    table.hashfunctions('car')

# Dictionarys in python
dict = {"Joe": 14, 'Adam':27,'Gorden':52}
dict['Joe']  = 26
dict['Adam']
dict['Joe']

dict.items()
dict.values()

del dict['Adam']
dict
# insert and get values in O(1)