monthly_income = int(input("Enter your monthly income: "))
monthly_expences = int(input("Enter your total monthly expences: "))
monthly_savings = monthly_income - monthly_expences
print(f"Your monthly savings are ${monthly_savings}.")
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"Projected savings after one year, with interest, is: ${int(projected_savings)}.")
