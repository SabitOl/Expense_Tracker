import csv
import re
import sys

print("Welcome to the Expense tracker!")

try:
    for i in range(4):
        amount = int(input("How much did you spend? "))
        category = (input("What did you spend the money on? For instance food, rent, etc. ")).strip()
        if not category.isalpha():
            print("Invalid category! The category should be a string/word")
            sys.exit()
        description = input("Enter description for your spending: ")
        date = input("Enter the date of your spending: ")
        if re.search(r"[a-zA-Z]", date):
            print("Invalid date! The date should be in numbers and symbols (eg. -, /) allowed")
            sys.exit()
        
        with open("storage.csv", "a", newline="") as file:
            actions = csv.DictWriter(file, fieldnames=["amount", "category", "description", "date"])
            actions.writerow({"amount": amount, "category": category, "description": description, "date": date})
                  
except ValueError:
    print(f"invalid input!")
    sys.exit()

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

     

