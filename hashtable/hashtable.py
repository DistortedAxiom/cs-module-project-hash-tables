class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None] * capacity
        self.size = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.size / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here

        hash = 5381
        for x in key:
            hash = ((hash << 5) + hash) + ord(x)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here

        # Get a hash value from a key and setting it as an index to be accessed
        # Get the list in the table at that index

        index = self.hash_index(key)
        node = self.table[index]

        # If the "node" / "key, value" is None, we can create a new HashTableEntry at that location
        # Increase the size (number of items) inside the array
        # If the load factor is greater than 0.7, we want to double the number of slots to prevent it from being too "full"

        if node is None:
            self.table[index] = HashTableEntry(key, value)
            self.size += 1
            if self.get_load_factor() > 0.7:
                self.resize(len(self.table) * 2)

        # If there's something already (which is a linked list node due to our previous condition), execute the below loop

        else:
            #We will iterate through the loop until the pointer reaches the end (None)
            while node is not None:
                # If the node hash value is the same as the one that is being added
                if node.key == key:
                    #If the node key is the same as the key input, we will override the current value of the node key
                    node.value = value
                    return node.value
            #Else, insert key, value at the head of the linked list slot that is empty
            if node is None:
                next_value = self.table[index]
                self.table[index] = HashTableEntry(key, value)
                self.table[index].next = next_value
                self.size += 1
                if self.get_load_factor() > 0.7:
                    self.resize(len(self.table) * 2)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here

        # Get the hash index of key

        index = self.hash_index(key)
        node = self.table[index]


        while node:
            # Search the list for key
            if node.key == key:
                #Delete the node from list
                self.table[index] = node.next
                self.size -= 1
                return node
            else:
                return None


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """

        # Get the index of the key and list inside the table for that index
        index = self.hash_index(key)
        node = self.table[index]

        # If the node is none, return none
        if node is None:
            return None
        else:
            # Search the list for that key
            while node:
                # If found return the value
                if node.key == key:
                    return node.value
            return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        old_table = self.table
        self.table = [None] * new_capacity
        self.capacity = new_capacity

        for ll in old_table:
            node = ll
            while node:
                self.put(node.key, node.value)
                node = node.next




if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")

