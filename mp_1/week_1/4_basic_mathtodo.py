"""
Lets do a basic math problem
"""

# perform all of the following mathematical operations and print the results in between

# set a constant tax rate of 20%
TAX_RATE = .20

# ask a user what their profit was for the quarter
quarter_profit = int(input("How much money did you make in the first quarter?: "))

# deduct the tax rate from the profit and print the result
tax_expense = quarter_profit * TAX_RATE
quarter_after_taxes = quarter_profit - tax_expense
print("The company paid $%.2f in taxes" %tax_expense)

# split that profit evenly amongst 7 share holders
shareholder_value = quarter_after_taxes / 7

# print out what each shareholder will receive from the profit
print("Each shareholder will receive $%.2f" %shareholder_value)

# extra credit: find the remainder of 112 divided by 3