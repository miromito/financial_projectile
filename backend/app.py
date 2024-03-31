from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from financial_model import FinancialModel

app = Flask(__name__)
CORS(app=app, resources={r"*": {"origins": "*"}})


@app.route('/simulate', methods=['POST'])
def simulate():
    data = request.json
    model = FinancialModel(
        current_age=int(data['current_age']),
        target_age=int(data['target_age']),
        salary_monthly_income=int(data['salary_monthly_income']),
        income_tax=float(data['salary_tax'])/100,
        monthly_expenses=int(data['monthly_expenses']),
        savings=int(data['savings']),
        apartment_construction_time=int(data['apartment_construction_time_months']),
        black_day_savings_target=int(data['black_day_savings_target']),
        rent_income_per_apartment=int(data['rent_income_per_apartment']),
        apartment_cost=int(data['apartment_cost']),
        apartment_repair_cost=int(data['apartment_repair_cost']),
        # Ensure you convert other numerical parameters similarly
    )

    results = model.simulate()  # Ensure your simulate method returns data
    response = jsonify(results)
    return response


if __name__ == '__main__':
    app.run(debug=True)
