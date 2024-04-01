class FinancialModel:
    def __init__(self,
                 current_age: int,
                 target_age: int,
                 salary_monthly_income: int,
                 monthly_expenses: int,
                 apartment_construction_time: int,
                 savings: int,
                 apartment_repair_cost: int,
                 black_day_savings_target: int,
                 apartment_cost: int,
                 rent_income_per_apartment: int,

                 mortgages=None,
                 income_tax: float = 0.02,
                 ):
        if mortgages is None:
            mortgages = []
        self.current_age = current_age
        self.target_age = target_age
        self.salary_monthly_income = salary_monthly_income
        self.monthly_expenses = monthly_expenses
        self.income_tax = income_tax
        self.savings = savings
        self.mortgages = mortgages
        self.apartment_cost = apartment_cost

        self.apartment_repair_cost = apartment_repair_cost
        self.rent_income_per_apartment = rent_income_per_apartment
        self.black_day_savings = black_day_savings_target
        self.apartment_construction_time = apartment_construction_time

        self.monthly_savings_goal = self.salary_monthly_income - self.monthly_expenses
        self.apartment_first_payment = self.apartment_cost * 0.3
        self.months_until_target_age = (self.target_age - self.current_age) * 12

        self.rental_income = 0
        self.apartments_owned = 0
        self.apartments_repair_time = 6

    def simulate(self):
        results = []
        for month in range(self.months_until_target_age):
            self.update_rental_income()
            self.calculate_monthly_finances()
            self.process_mortgages()
            self.check_for_new_apartment()

            apartments_constructed_owned = len(
                [x for x in self.mortgages if x["paid"] and x["month_to_complete"] <= 0])
            apartments_in_construction_owned = len(
                [x for x in self.mortgages if x["paid"] and x["month_to_complete"] > 0])
            total_value = round(
                (apartments_in_construction_owned + apartments_constructed_owned) * self.apartment_cost + self.savings)

            # Collecting data instead of printing
            month_result = {
                'Age': self.current_age + month // 12,
                'Savings': round(self.savings),
                'Monthly Income': round(self.current_month_income),
                'Rental Income': self.rental_income,
                'Apartments Constructed Owned': apartments_constructed_owned,
                'Apartments in Construction Owned': apartments_in_construction_owned,
                'Mortgages Owned': len([x for x in self.mortgages if not x["paid"]]),
                'Total Value': f"{total_value:,}$"}
            results.append(month_result)

        return results

    def update_rental_income(self):
        for mortgage in self.mortgages:
            if not mortgage["rented"]:
                self.process_mortgage_for_rental_income(mortgage)

    def process_mortgage_for_rental_income(self, mortgage):
        # If the apartment is ready to be rented, mark it as rented and increase income
        if mortgage['ready_for_rent']:
            self.mark_mortgage_as_rented(mortgage)
        # Otherwise, if the apartment is under repair, process the repair time
        elif mortgage['ready_for_repair']:
            self.update_mortgage_repair_time(mortgage)

    def mark_mortgage_as_rented(self, mortgage):
        mortgage['rented'] = True
        self.rental_income += self.rent_income_per_apartment

    @staticmethod
    def update_mortgage_repair_time(mortgage):
        # Check if the repair time is over
        if mortgage['month_to_repair'] == 0:
            mortgage['ready_for_rent'] = True
        else:
            mortgage['month_to_repair'] -= 1

    def calculate_monthly_finances(self):
        self.current_month_income = (
                (self.salary_monthly_income - self.salary_monthly_income * self.income_tax)
                + self.rental_income)
        month_savings = self.current_month_income - self.monthly_expenses
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
                    mortgage['ready_for_repair'] = True
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
            self.mortgages.append({
                'amount': 0,
                'paid': True,
                "month_to_complete": self.apartment_construction_time,
                "ready_for_repair": False,
                "ready_for_rent": False,
                "rented": False,
                "month_to_repair": 6
            })
        else:
            self.savings -= (self.apartment_first_payment + self.apartment_repair_cost)
            self.mortgages.append(
                {
                    'amount': self.apartment_cost - self.apartment_first_payment,
                    'paid': False,
                    "month_to_complete": self.apartment_construction_time,
                    "ready_for_repair": False,
                    "ready_for_rent": False,
                    "rented": False,
                    "month_to_repair": 6
                })

    def print_financial_status(self, month):
        print(
            f'Age: {self.current_age + month // 12}, '
            f'Savings: {self.savings}, '
            f'income: {self.current_month_income} '
            f'Rental Income: {self.rental_income}, '
            f'Apartments constructed owned: {len([x for x in self.mortgages if x["paid"] and x["month_to_complete"] <= 0])}, '
            f'Apartments in construction owned: {len([x for x in self.mortgages if x["paid"] and x["month_to_complete"] > 0])}, '
            f'Mortgages owned: {len([x for x in self.mortgages if not x["paid"]])}, '
        )
