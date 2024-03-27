class FinancialModel:
    def __init__(self, current_age, target_age, salary_monthly_income, monthly_expenses, mortgages):
        self.current_age = current_age
        self.target_age = target_age
        self.salary_monthly_income = salary_monthly_income
        self.monthly_expenses = monthly_expenses
        self.mortgages = mortgages
        self.savings = 0
        self.rental_income = 0
        self.apartments_repair_time = 0

    @staticmethod
    def calculate_months_until_target_age(current_age, target_age):
        """Calculate months until target age."""
        return (target_age - current_age) * 12

    @staticmethod
    def update_rental_income(rental_income, apartments_repair_time, rent_income_per_apartment):
        """Update rental income based on apartment repair time."""
        if apartments_repair_time == 8:  # Apartment repair completed
            return rental_income + rent_income_per_apartment
        return rental_income

    @staticmethod
    def update_savings(savings, income, expenses):
        """Update savings after income and expenses."""
        return savings + (income - expenses)

    @staticmethod
    def pay_mortgage(mortgages, savings):
        """Pay off one mortgage at a time."""
        for mortgage in mortgages:
            if not mortgage['paid']:
                mortgage_payment = min(3000, mortgage['amount'])
                mortgage['amount'] -= mortgage_payment
                savings -= mortgage_payment
                if mortgage['amount'] == 0:
                    mortgage['paid'] = True
                break  # Pay one mortgage at a time
        return savings

    @staticmethod
    def can_afford_new_apartment(savings, first_payment, repair_cost):
        """Check if the user can afford a new apartment."""
        return savings >= first_payment + repair_cost

    def print_financial_status(self):
        """Print the financial status of the individual."""
        apartments_owned = len([x for x in self.mortgages if x["paid"]])
        age = self.current_age + self.calculate_months_until_target_age(self.current_age, self.target_age) // 12
        print(f'Age: {age}, Savings: {self.savings}, Rental Income: {self.rental_income}, '
              f'Apartments owned: {apartments_owned}, Apartment repair: {self.apartments_repair_time}')

    def simulate(self):
        """Simulate the financial plan over time."""
        months_until_target = self.calculate_months_until_target_age(self.current_age, self.target_age)
        apartment_first_payment, apartment_repair_cost = 15000, 12000

        for month in range(months_until_target):
            self.rental_income = self.update_rental_income(self.rental_income, self.apartments_repair_time, 500)
            self.apartments_repair_time = min(self.apartments_repair_time + 1, 36) if self.apartments_repair_time else 0
            income_after_tax = self.salary_monthly_income * 0.9 + self.rental_income
            self.savings = self.update_savings(self.savings, income_after_tax, self.monthly_expenses)
            self.savings = self.pay_mortgage(self.mortgages, self.savings)

            if all(m['paid'] for m in self.mortgages) and self.can_afford_new_apartment(self.savings, apartment_first_payment, apartment_repair_cost):
                self.savings -= (apartment_first_payment + apartment_repair_cost)
                self.apartments_repair_time = 1
                self.mortgages.append({'amount': 30000, 'paid': False})

            self.print_financial_status()
