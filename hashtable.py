class Hash:
    def __init__(self,size):
        self.tab = {}
        self.max_size = size

    def hash_function(self, key):
        v = int(key)
        return v % self.max_size
    
    def full(self):
        return len(self.tab) == self.max_size
    
    def print(self):
        for i in self.tab:
            print("Hash[%d] = " %i, end="")
            print(self.tab[i])

    def delete(self, key):
        pos = self.find(key)
        if pos != -1:
            del self.tab[pos]
            print("%d position data erased" %pos)
        else:
            print("Item not found")

    def find(self, key):
        pos = self.hash_function(key)
        if self.tab.get(pos) == None:
            return -1
        if self.tab[pos] == key:
            return pos
        return -1
    
    def insert(self,item):
        if self.full():
            print('The hash table has reached its size limit')
            return
        pos = self.hash_function(item)
        if self.tab.get(pos) == None:
            self.tab[pos] = item
            print("inserted hash[%d]" %pos)
        else:
            print("-> A collision occurred at position %d" %pos)


hash_size = 7
tab = Hash(hash_size)
print(" Hashtable without collisions (%d itens) " %hash_size)

for i in range(0,hash_size,1):
    print("\nInserted element %d" %(i + 1))

    item = input("Provide integer numeric value:")
    tab.insert(item)

item = input("\n - Enter integer numeric value to search: ")
pos = tab.find(item)

if(pos == -1):
    print('Item not found')
else:
    print("Item found at position: ", pos)

item = input("\n - Enter integer numeric value to delete:")
tab.delete(item)

print("\nprinting...")
tab.print()
print("\n")    
