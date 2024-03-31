from financial_model import FinancialModel

# Updated initial parameters based on the new script modifications
current_age = 33
target_age = 55

salary_monthly_income = 2500
monthly_expenses = 600

savings = 0
rental_income = 0
black_day_savings_target = 50000

apartment_construction_time_months = 48
rent_income_per_apartment = 500
apartment_cost = 48000
apartment_repair_cost = 12000

mortgages = [
    # {'amount': 22650, 'paid': False, "month_to_complete": 36}
]

financial_plan = FinancialModel(
    current_age=current_age,
    target_age=target_age,
    salary_monthly_income=salary_monthly_income,
    monthly_expenses=monthly_expenses,
    savings=savings,
    apartment_construction_time=apartment_construction_time_months,
    mortgages=mortgages,
    black_day_savings_target=black_day_savings_target,
    rent_income_per_apartment=rent_income_per_apartment,
    apartment_cost=apartment_cost,
    apartment_repair_cost=apartment_repair_cost,

)
print(financial_plan.simulate())
