class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, string):
        return sum(ord(char) for char in string)

    def add(self, key, value):
        hash_index = self.hash(key)
        if hash_index not in self.collection:
            self.collection[hash_index] = {}
        self.collection[hash_index][key] = value

    def remove(self, key):
        hash_index = self.hash(key)
        if hash_index in self.collection:
            if key in self.collection[hash_index]:
                del self.collection[hash_index][key]
            
    def lookup(self, key):
        hash_index = self.hash(key)
        if hash_index in self.collection and key in self.collection[hash_index]:
            return self.collection[hash_index][key]
        return None

def hash_table_manager():
    table = HashTable()
    
    while True:
        print("\n--- HASH TABLE MANAGER ---")
        print("1. Add element (add)")
        print("2. Search element (lookup)")
        print("3. Remove element (remove)")
        print("4. View internal state (collection)")
        print("5. Exit")
        
        option = input("Select an option: ")

        if option == "1":
            key = input("Enter the key: ")
            value = input("Enter the value: ")
            table.add(key, value)
            print(f"'{key}' successfully added.")

        elif option == "2":
            key = input("Enter the key to search for: ")
            result = table.lookup(key)
            if result is not None:
                print(f"Value found: {result}")
            else:
                print("Key does not exist.")

        elif option == "3":
            key = input("Enter the key to remove: ")
            table.remove(key)
            print(f"Removal attempt for '{key}' completed.")

        elif option == "4":
            print("\nInternal structure (hash indices):")
            print(table.collection)

        elif option == "5":
            print("Exiting...")
            break

if __name__ == "__main__":
    hash_table_manager()