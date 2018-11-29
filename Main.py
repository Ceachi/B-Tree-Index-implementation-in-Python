from BTree import *
"""
The following application is an example for using B-Tree index.
We are going to have, an sorted array with a fixed size.
Based on this array we will create a B-Tree.
The scope is to find a specific key in the array using the B-tree.

Observation:
- a node in the B-tree is <key, value>
where key =  is the key we are looking for
and value = is the page number where the key exist

Database = is just a simple array in this example

author: Ceachi Bogdan
"""
class Main:
    DATABASE_SIZE = 100
    database = [None] * DATABASE_SIZE # just the sorted array where we will try to find the keys
    pageSize = 4 # we divide the array into dimensions of pageSize
    btree = Btree()
    key = 19  # we are trying to find this key in the database array
    def run(self):
        self.constructDatabase()
        self.printDatabase()
        self.constructInitialBTree()
        print(" We are trying to find the position of key = ", self.key, "in the array")
        print("Page number where the key might exist = ", self.btree.search(self.key))
        pos = self.btree.search(self.key) # after the search of the key in B-Tree, we get the pageNumber where the key exist
        print("Position of the key in array is =", self.binarySearch(self.database, pos, pos+self.pageSize-1, self.key))

    def printDatabase(self):
        print(" The array we full of keys is :")
        print(self.database)

    """"
        here we construct the sorted array
    """
    def constructDatabase(self):
        startFromNumber = 6
        self.database = [(startFromNumber + i) for i in range(self.DATABASE_SIZE)]

    """
        Here we are construct the B-Tree based on the populated array
        every node in the B-Tree is <key,value>
        where value = is the page where the key might exist in the array
        
        We divide the array into dimensions of pageSize
    """
    def constructInitialBTree(self):
        global pos
        pos = 0
        for i in range(self.DATABASE_SIZE):
            if(i%self.pageSize == 0):
                pos = i
            #print(self.database[i], pos)
            self.add(self.database[i], pos)

    def add(self, key, value):
        self.btree.insert(key, value)

    def binarySearch(self, arr, l, r, x):
        if r >= l:
            mid = int(l + (r - l) / 2)
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                return self.binarySearch(arr, l, mid - 1, x)
            else:
                return self.binarySearch(arr, mid + 1, r, x)
        else:
            return -1

program = Main()
program.run()