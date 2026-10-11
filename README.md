# Stock Portfolio Tracker

## Description

The Stock Portfolio Tracker is a simple Python application that calculates the total investment value of stocks using predefined stock prices. Users can enter stock symbols and quantities to calculate individual investment values and the total investment.

The program also provides an option to save portfolio details in a CSV file.

## Features

* Displays available stocks and their predefined prices.
* Accepts stock symbols and quantities from the user.
* Checks whether the entered stock symbol is available.
* Calculates the investment value for each stock.
* Calculates and displays the total investment value.
* Validates that the stock quantity is greater than zero.
* Saves portfolio details in a CSV file.
* Uses simple Python programming concepts.

## Technologies Used

* Python
* Dictionary and Lists
* Loops and Conditional Statements
* User Input and Output
* Basic Arithmetic Operations
* CSV File Handling

## Sample Stock Prices

| Stock Symbol | Price |
| ------------ | ----: |
| AAPL         |  $180 |
| TSLA         |  $250 |
| GOOGL        |  $150 |
| MSFT         |  $420 |
| AMZN         |  $190 |

Note: These are predefined sample prices, not live market prices.

## How to Run the Project

### Step 1: Install Python

Download Python from https://www.python.org/downloads/ if it is not already installed.

### Step 2: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Alternatively, download the repository from GitHub.

### Step 3: Open the Project

Open the project folder in Visual Studio Code.

### Step 4: Run the Program

Open the terminal and execute:

```bash
python stock_tracker.py
```

### Step 5: Enter Stock Details

1. Enter the number of different stocks.
2. Enter each stock symbol.
3. Enter the quantity.
4. View the individual investment values and total investment.
5. Choose `yes` to save the results to a CSV file.

## Example Calculation

* AAPL: 5 shares × $180 = $900
* TSLA: 2 shares × $250 = $500

**Total Investment = $1,400**

## Project Structure

```text
Stock-Portfolio-Tracker/
│
├── stock_tracker.py
├── README.md
├── .gitignore
└── output.png
```

The `stock_portfolio.csv` file is generated when the user chooses to save the results. It is excluded from Git tracking by `.gitignore`.

## Learning Outcomes

* Understanding dictionaries and lists in Python.
* Using loops and conditional statements.
* Performing basic arithmetic calculations.
* Handling CSV files.
* Building a simple command-line application.

## Author

Created as part of the CodeAlpha Python programming internship task.