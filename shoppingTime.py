import datetime
import time

today = datetime.date.today()
f_today = today.strftime("%b %d,%Y")

b_price = 2.25
j_price = 1.25
t_price = 3.25

for i in "WELCOME TO JAS'S SHOPPING MALL":
    print(i, end="")
    time.sleep(1)

time.sleep(2)
print("\n")
print("\nPrice List for", f_today, "is:")
print("Bread : $2.25\nJam : $1.25\nButter:$3.25")

prices = {
    "Bread": b_price,
    "Jam": j_price,
    "Butter": t_price
}

while True:
    a = input("What would you like to buy today? Bread, Jam, Butter: ")
    if a in prices:
        break
    else:
        print(f"{a} is not a valid product. Please enter a valid product name.")

b = int(input("How many would you like to buy?"))
c = prices.get(a, 0) * b

print("Your total for today is", "$", c)
print("Thank you for shopping with us")
