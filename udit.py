# Version 1: Simple Python Project Template (OOP-based)
# You can extend this later with more features

class App:
    def __init__(self):
        self.data = []

    def add_item(self, item):
        self.data.append(item)
        print(f"Added: {item}")

    def remove_item(self, item):
        if item in self.data:
            self.data.remove(item)
            print(f"Removed: {item}")
        else:
            print("Item not found")

    def display_items(self):
        if not self.data:
            print("No items available")
        else:
            print("Items:")
            for i, item in enumerate(self.data, start=1):
                print(f"{i}. {item}")

    def run(self):
        while True:
            print("\n1. Add Item")
            print("2. Remove Item")
            print("3. View Items")
            print("4. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                item = input("Enter item: ")
                self.add_item(item)

            elif choice == "2":
                item = input("Enter item to remove: ")
                self.remove_item(item)

            elif choice == "3":
                self.display_items()

            elif choice == "4":
                print("Exiting...")
                break

            else:
                print("Invalid choice")


if __name__ == "__main__":
    app = App()
    app.run()