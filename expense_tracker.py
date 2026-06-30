import csv
import re
import sys

print("Welcome to the Expense tracker!")

while True:
    try:
        while True:
            amount = int(input("How much did you spend? "))
            category = (input("What did you spend the money on? For instance food, rent, etc. ")).strip()
            if re.search(r"[0-9]", category):
                print("Invalid category! The category should be a string/word")
                break
            description = input("Enter description for your spending: ")
            date = input("Enter the date of your spending: ")
            if re.search(r"[a-zA-Z]", date):
                print("Invalid date! The date should be in numbers and symbols (eg. -, /) allowed")
                break
            
            with open("storage.csv", "a", newline="") as file:
                actions = csv.DictWriter(file, fieldnames=["amount", "category", "description", "date"])
                actions.writerow({"amount": amount, "category": category, "description": description, "date": date})
            
            print("Write 'exit'")
                  
    except ValueError:
        print(f"invalid input!")

    def main():
        total = 0
        with open("storage.csv", "r") as file:
            reader = csv.DictReader(file)
            for amt in reader:
                amounts = int(amt["amount"])
                total += amounts
            print(f"The total sum of money you spent is ${total}")


if __name__ == "__main__":
    main()

     

