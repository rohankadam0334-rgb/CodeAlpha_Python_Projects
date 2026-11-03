prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 170
}

total = 0

n = int(input("Enter number of stocks: "))

for i in range(n):
    name = input("Enter stock name: ").upper()
    qty = int(input("Enter quantity: "))

    if name in prices:
        amount = prices[name] * qty
        total += amount
        print("Investment:", amount)
    else:
        print("Stock not found!")

print("Total Investment:", total)