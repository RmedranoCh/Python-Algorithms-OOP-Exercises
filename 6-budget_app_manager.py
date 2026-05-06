
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category_instance):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category_instance.name}")
            category_instance.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):

        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:

            desc = f"{item['description'][:23]:<23}"
            amt = f"{item['amount']:>7.2f}"
            items += f"{desc}{amt}\n"
        
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

def create_spend_chart(categories):

    res = "Percentage spent by category\n"

    spent = []
    for cat in categories:
        s = sum(-item['amount'] for item in cat.ledger if item['amount'] < 0)
        spent.append(s)
    
    total = sum(spent)

    percs = [int((s / total) * 100 // 10) * 10 for s in spent]

    for i in range(100, -1, -10):
        res += str(i).rjust(3) + "| "
        for p in percs:
            res += "o  " if p >= i else "   "
        res += "\n"

    res += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = max(len(cat.name) for cat in categories)
    names = [cat.name.ljust(max_len) for cat in categories]
    
    for i in range(max_len):
        res += "     "
        for name in names:
            res += name[i] + "  "

        if i < max_len - 1:
            res += "\n"

    return res

def interactive_menu():
    categories = {}

    while True:
        print("\n--- BUDGET APP ---")
        print("1. Create Category (e.g. Food)")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. View Status and Chart")
        print("6. Exit")
        
        option = input("Select an option: ")

        if option == "1":
            name = input("Category name: ")
            categories[name] = Category(name)
            print(f"Category '{name}' created.")

        elif option == "2":
            cat = input("To which category?: ")
            if cat in categories:
                amount = float(input("Amount to deposit: "))
                desc = input("Description: ")
                categories[cat].deposit(amount, desc)
            else:
                print("Category does not exist.")

        elif option == "3":
            cat = input("From which category?: ")
            if cat in categories:
                amount = float(input("Amount to withdraw: "))
                desc = input("Description: ")
                categories[cat].withdraw(amount, desc)
            else:
                print("Category does not exist.")

        elif option == "4":
            source = input("Source category: ")
            destination = input("Destination category: ")
            if source in categories and destination in categories:
                amount = float(input("Amount to transfer: "))
                categories[source].transfer(amount, categories[destination])
            else:
                print("One or both categories do not exist.")

        elif option == "5":
            for cat in categories.values():
                print("\n" + str(cat))
            if categories:
                print("\n" + create_spend_chart(list(categories.values())))

        elif option == "6":
            print("Exiting...")
            break

if __name__ == "__main__":
    interactive_menu()