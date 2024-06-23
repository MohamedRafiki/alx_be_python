month_income = int(input("Enter your monthly income: "))
month_expences = int(input("Enter your total monthly expences: "))
month_saving = month_income - month_expences
print(f"Your monthly savings are ${month_saving}.")
projected_savings = month_saving * 12 + (month_saving * 12 * 0.05)
print(f"Projected savings after one year, with interest, is: ${int(projected_savings)}.")
