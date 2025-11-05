scores = [("Essoh", -1),("Claude", 14),("Frederic", 5),]

for person in scores:
    print(person[1])


name = input("Your name : ")
price = int(input("enter your price: "))

print(f"Your name is {name} and your price is {price}")
print("Your name is {} and your price is {:.2f}".format(name, price))
