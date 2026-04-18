# Version 2: Upgraded Python Project (Modular, Persistent, Extensible)

import json
import os
from datetime import datetime


class StorageManager:
    def __init__(self, filename="data.json"):
        self.filename = filename

    def load(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []

    def save(self, data):
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)


class Item:
    def __init__(self, name):
        self.name = name
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "name": self.name,
            "created_at": self.created_at
        }


class App:
    def __init__(self):
        self.storage = StorageManager()
        self.data = self.storage.load()

    def add_item(self, name):
        item = Item(name)
        self.data.append(item.to_dict())
        self.storage.save(self.data)
        print(f"Added: {name}")

    def remove_item(self, index):
        try:
            removed = self.data.pop(index - 1)
            self.storage.save(self.data)
            print(f"Removed: {removed['name']}")
        except (IndexError, ValueError):
            print("Invalid index")

    def search_items(self, keyword):
        results = [item for item in self.data if keyword.lower() in item["name"].lower()]
        if not results:
            print("No matching items found")
        else:
            print("Search Results:")
            for i, item in enumerate(results, start=1):
                print(f"{i}. {item['name']} (Created: {item['created_at']})")

    def display_items(self):
        if not self.data:
            print("No items available")
        else:
            print("\nItems:")
            for i, item in enumerate(self.data, start=1):
                print(f"{i}. {item['name']} (Created: {item['created_at']})")

    def run(self):
        while True:
            print("\n===== MENU =====")
            print("1. Add Item")
            print("2. Remove Item")
            print("3. View Items")
            print("4. Search Item")
            print("5. Exit")

            choice = input("Enter choice: ").strip()

            if choice == "1":
                name = input("Enter item name: ").strip()
                if name:
                    self.add_item(name)
                else:
                    print("Item name cannot be empty")

            elif choice == "2":
                self.display_items()
                try:
                    index = int(input("Enter item number to remove: "))
                    self.remove_item(index)
                except ValueError:
                    print("Please enter a valid number")

            elif choice == "3":
                self.display_items()

            elif choice == "4":
                keyword = input("Enter search keyword: ").strip()
                self.search_items(keyword)

            elif choice == "5":
                print("Exiting application...")
                break

            else:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    app = App()
    app.run()