class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

# size should be prime to prevent collise [https://www.quora.com/Learning-programming-Why-should-hash-functions-use-a-prime-number-modulus#:~:text=Because%20a%20prime%20number%20avoids,any%20number%20works%20as%20modulus.]


    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash  
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if(self.data_map[index] is None):
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for item in self.data_map[index]:
                if item[0] == key:
                    return item[1]
        return None
    
    def keys(self):
        all_Keys = []
        for box in self.data_map:
            if box is not None:
                for pair in box:
                    all_Keys.append(pair[0])
        return all_Keys;

    def print_table(self):
        for i, val in enumerate(self.data_map): 
            print(i, ": ", val)

        
my_hash_table = HashTable()

my_hash_table.print_table()



"""
    EXPECTED OUTPUT:
    ----------------
    0 :  None
    1 :  None
    2 :  None
    3 :  None
    4 :  None
    5 :  None
    6 :  None

"""