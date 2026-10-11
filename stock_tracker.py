
# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = []
total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")
print("\nAvailable Stocks:")

for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

# Take input from the user
n = int(input("\nHow many different stocks do you want to add? "))

for i in range(n):
    stock_name = input("\nEnter stock symbol: ").upper()

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

        price = stock_prices[stock_name]
        investment = price * quantity
        total_investment += investment

        portfolio.append(
            [stock_name, quantity, price, investment]
        )

        print("Stock added successfully!")
        print("Investment value: $", investment)

    else:
        print("Stock not available!")

# Display portfolio
print("\n===== YOUR PORTFOLIO =====")
print("Stock\tQuantity\tPrice\tInvestment")

for item in portfolio:
    print(f"{item[0]}\t{item[1]}\t\t${item[2]}\t${item[3]}")

print("\nTotal Investment: $", total_investment)

# Save results in a CSV file
save = input("\nDo you want to save the result? (yes/no): ").lower()

if save == "yes":
    import csv

    with open("stock_portfolio.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(
            ["Stock", "Quantity", "Price", "Investment"]
        )

        writer.writerows(portfolio)

        writer.writerow(
            ["", "", "Total Investment", total_investment]
        )

    print("Portfolio saved to stock_portfolio.csv")

print("\nThank you for using Stock Portfolio Tracker!")