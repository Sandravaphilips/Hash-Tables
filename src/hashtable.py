# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)
        linked_pair = self.storage[index]
        if linked_pair is None:
            self.storage[index] = LinkedPair(key, value)
        else: 
            previous = linked_pair
            while linked_pair is not None:
                previous = linked_pair
                linked_pair = linked_pair.next
                if previous.key == key:
                    previous.value = value
                    break
            else: 
                previous.next = LinkedPair(key, value)

            
            



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        linked_pair = self.storage[index]
        previous = None
        linked_pair_index = index
            
        while linked_pair and linked_pair.key != key:
            previous = linked_pair
            linked_pair = linked_pair.next

        if linked_pair is None:
            print("There's no such key in our storage!")     
        else:
            if previous is None:
                self.storage[index] = None
            else:
                previous.next = previous.next.next
                
            


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        linked_pair = self.storage[index]
        while linked_pair is not None:
            if linked_pair.key == key:
                break
            else:
                linked_pair = linked_pair.next
            

        if linked_pair is None:
            return None
        return linked_pair.value


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        new_hashtable = HashTable(self.capacity*2)
        for i in self.storage:
            if i is not None:
                previous = i
                while previous is not None:
                    new_hashtable.insert(previous.key, previous.value)
                    previous = previous.next

        self.storage = new_hashtable.storage
        self.capacity *= 2



if __name__ == "__main__":
    ht = HashTable(8)

    ht.insert("key-0", "val-0")
    ht.insert("key-1", "val-1")
    ht.insert("key-2", "val-2")
    ht.insert("key-3", "val-3")
    ht.insert("key-4", "val-4")
    ht.insert("key-5", "val-5")
    ht.insert("key-6", "val-6")
    ht.insert("key-7", "val-7")
    ht.insert("key-8", "val-8")
    ht.insert("key-9", "val-9")

    ht.remove("key-9")
    ht.remove("key-8")
    ht.remove("key-7")
    ht.remove("key-6")
    ht.remove("key-5")
    ht.remove("key-4")
    ht.remove("key-3")
    ht.remove("key-2")
    ht.remove("key-1")
    ht.remove("key-0")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("key-0"))
    print(ht.retrieve("key-1"))
    print(ht.retrieve("key-2"))
    print(ht.retrieve("key-3"))
    print(ht.retrieve("key-4"))
    print(ht.retrieve("key-5"))
    print(ht.retrieve("key-6"))
    print(ht.retrieve("key-7"))
    print(ht.retrieve("key-8"))
    print(ht.retrieve("key-9"))

    # Test resizing
    # old_capacity = len(ht.storage)
    # ht.resize()
    # new_capacity = len(ht.storage)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    print("")
