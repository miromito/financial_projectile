class FinancialModel:
    def __init__(self,
                 current_age: int,
                 target_age: int,
                 salary_monthly_income: int,
                 monthly_expenses: int,
                 apartment_construction_time: int,
                 savings: int,
                 rental_income: int,
                 apartment_repair_cost: int,
                 mortgages,
                 black_day_savings_target: int,
                 apartment_cost: int,
                 rent_income_per_apartment: int,
                 ):
        self.current_age = current_age
        self.target_age = target_age
        self.salary_monthly_income = salary_monthly_income
        self.monthly_expenses = monthly_expenses
        self.savings = savings
        self.rental_income = rental_income
        self.mortgages = mortgages
        self.apartments_owned = 0
        self.apartments_repair_time = 0
        self.apartment_cost = apartment_cost
        self.apartment_first_payment = self.apartment_cost * 0.3
        self.apartment_repair_cost = apartment_repair_cost
        self.rent_income_per_apartment = rent_income_per_apartment
        self.black_day_savings = black_day_savings_target
        self.apartment_construction_time = apartment_construction_time
        self.monthly_savings_goal = self.salary_monthly_income - self.monthly_expenses
        self.months_until_target_age = (self.target_age - self.current_age) * 12

    def simulate(self):
        for month in range(self.months_until_target_age):
            self.update_rental_income()
            self.calculate_monthly_finances(month)
            self.process_mortgages()
            self.check_for_new_apartment()
            self.print_financial_status(month)

    def update_rental_income(self):
        if self.apartments_repair_time != 0:
            if self.apartments_repair_time < 6:
                self.apartments_repair_time += 1
            else:
                self.rental_income += self.rent_income_per_apartment
                self.apartments_repair_time = 0

    def calculate_monthly_finances(self, month):
        current_month_income = (self.salary_monthly_income - self.salary_monthly_income * 0.1) + self.rental_income
        month_savings = current_month_income - self.monthly_expenses
        self.savings += month_savings

    def process_mortgages(self):
        for mortgage in self.mortgages:
            if not mortgage['paid']:
                mortgage_payment = ((self.apartment_cost - self.apartment_first_payment)
                                    / self.apartment_construction_time)
                mortgage['amount'] -= min(mortgage_payment, mortgage['amount'])
                self.savings -= mortgage_payment
                mortgage['month_to_complete'] -= 1
                if mortgage['amount'] == 0 and mortgage['month_to_complete'] <= 0:
                    mortgage['paid'] = True
                break  # Pay one mortgage at a time

    def check_for_new_apartment(self):
        if all(m['paid'] for m in self.mortgages):
            if self.savings - self.black_day_savings > self.apartment_cost:
                self.purchase_apartment(cash_purchase=True)
            elif self.savings >= self.apartment_first_payment + self.apartment_repair_cost:
                self.purchase_apartment()

    def purchase_apartment(self, cash_purchase=False):
        if cash_purchase:
            self.savings -= self.apartment_cost
            self.mortgages.append({'amount': 0, 'paid': True, "month_to_complete": 48})
        else:
            self.savings -= (self.apartment_first_payment + self.apartment_repair_cost)
            self.apartments_repair_time = 1
            self.mortgages.append(
                {'amount': self.apartment_cost - self.apartment_first_payment, 'paid': False, "month_to_complete": 48})

    def print_financial_status(self, month):
        print(
            f'Age: {self.current_age + month // 12}, '
            f'Savings: {self.savings}, '
            f'income: {(self.salary_monthly_income - self.salary_monthly_income * 0.1) + self.rental_income}, '
            f'Rental Income: {self.rental_income}, '
            f'Apartments constructed owned: {len([x for x in self.mortgages if x["paid"] and x["month_to_complete"] <= 0])}, '
            f'Apartments in construction owned: {len([x for x in self.mortgages if x["paid"] and x["month_to_complete"] > 0])}, '
            f'Mortgages owned: {len([x for x in self.mortgages if not x["paid"]])}, '
            f'Apartment repair time: {self.apartments_repair_time}, '
        )
