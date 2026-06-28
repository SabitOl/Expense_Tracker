import csv

amount = int(input("How much did you spend? "))
category = input("On what did you spend the money? For instance food, rent, etc. ")
description = input("Enter description for your spending: ")
date = input("Enter the date of your spending: ")

with open("storage.csv", "a", newline="") as file:
    actions = csv.DictWriter(file, fieldnames=["amount", "category", "description", "date"])
    actions.writerow({"amount": amount, "category": category, "description": description, "date": date})

def main():
    my_total = total_amount()
    print(f"The total sum of money you spent is ${my_total}")

def total_amount():
    total = 0
    with open("storage.csv", "r") as file:
        reader = csv.DictReader(file)
        for amt in reader:
            amounts = int(amt["amount"])
            total += amounts
        return total
     
main()

