class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''
    
    def __init__(self, name, number):
        self.name = name
        self.number = number
    def __str__(self):
        return f"{self.name}: {self.number}"

class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''
   
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''
    
    def __init__(self, size):
        self.size = size
        self.data = [None] * size
    
    def hash_function(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.size
    
    def insert(self, key, value):
        index = self.hash_function(key)
        current =  self.data[index]
        if self.data[index] is None:
            self.data[index] = Node(key, value)
            return
        while current: 
            if current.key == key:
                current.value = value
                return
            if current.next is None: 
                break
            current = current.next
        current.next = Node(key, value)

    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None
        
    def print_table(self):
        for i in range(self.size):
            current = self.data[i]
            if current is None:
                print(f"Index {i}: Empty")
            else:
                contacts = []
                while current:
                    contacts.append(str(current.value))
                    current = current.next
                print(f"Index {i}: {contacts}")
# Test your hash table implementation here.  

table = HashTable(5)
table.insert("Joe", Contact("Joe", "111-111-1111"))
table.insert("Eve", Contact("Eve", "222-222-2222"))
table.insert("Huck", Contact("Huck", "333-333-3333"))
table.insert("Kevin", Contact("Kevin", "444-444-4444"))
table.insert("Jack", Contact("Jack", "555-555-5555"))
table.print_table()

table.insert("Amy", Contact("Amy", "111-222-3333"))
table.insert("May", Contact("May", "222-333-1111")) 
table.print_table()

table.insert("Huck", Contact("Huck", "999-444-9999"))
table.print_table()

table.search("Chris")
table.search("Joe")

'''
A hash table is the optimal structure for fast contact lookups due to its average O(1) 
time complexity for search operations. Unlike linear searches through lists (O(n)) or 
balanced tree traversals (O(log n)), hash tables use a hash function to compute direct
 array indices from keys, enabling near-instantaneous access to contact data. This makes it 
 ideal for applications requiring frequent searches, such as contact directories where users 
 expect immediate results when searching for names.

Collisions were handled using separate chaining with linked lists. When multiple keys hash 
to the same index (e.g., "Amy" and "May" both hashing to index 5), we maintain a linked list 
at that array position. Each node contains the key-value pair and a pointer to the next node. 
The insert method traverses the chain to update existing contacts or append new ones, while 
search operations scan the chain for matching keys.

Engineers should choose hash tables over lists when dealing with large datasets requiring 
frequent lookups, as lists degrade to O(n) searches. Hash tables outperform trees when data 
ordering isn't critical, since they provide faster average access times without the overhead 
of maintaining balance. However, hash tables require careful size selection to minimize 
collisions and may use more memory than lists. For our contact management system, the hash 
table's constant-time lookups provide the responsive performance users expect when searching 
through thousands of contacts.
'''