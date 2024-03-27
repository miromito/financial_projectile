from financial_model import FinancialModel

# Initial parameters
current_age = 33
target_age = 55
salary_monthly_income = 5300
monthly_expenses = 2300
mortgages = [{'amount': 22650, 'paid': False}]

# Create a FinancialModel instance and simulate the financial plan
financial_plan = FinancialModel(current_age, target_age, salary_monthly_income, monthly_expenses, mortgages)
financial_plan.simulate()
