#A finance calculator to enable user to calculate their savings over a one month period
monthly_income_string = input("Enter your monthly income: ")
monhtly_income = int(monthly_income_string)

monthly_expenses_string = input("Enter your monhtly expenses: ")
monthly_expenses = int(monthly_expenses_string)

monthly_savings = monhtly_income - monthly_expenses|float

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print("Your monthly savings are $", monthly_savings)
print("Projected savings, after one year, with interest, is: $", projected_savings)