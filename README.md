# Financial Projection Model

## Overview
This project is like a guide to help you grow your savings by investing in houses. It's designed to show you how to handle your money from now until you retire, focusing on what you earn, what you spend, saving up, especially for emergencies (we call this "black day savings"), and earning extra from renting properties.

How It Works
Understanding Your Money: First, we figure out your monthly earnings and expenses. After setting aside a little for taxes, we calculate how much you can save.

Earning Rent: When a house you've invested in is ready, you can rent it out. This gives you more money each month to save or invest again.

Paying Off Houses: The program also helps manage loans taken to buy these houses. If you're in a good place with your savings, you can even think about getting more properties.

Investing in New Houses: You can buy new houses once you've paid off any loans and have saved enough—remembering to always keep a safety net of savings for tough times, known as "black day savings."

Tracking Progress: It keeps you updated on how much money you've saved, how much you're earning, how many houses you own, and your loans.

By planning wisely, saving for emergencies ("black day savings"), and investing in properties to rent, this plan helps you build a secure financial future. It's flexible, so you can adjust it based on your financial situation and goals.## Setup
To run this project, ensure you have Python 3.x installed on your system.

1. Clone the repository:
2. Navigate to the project directory:
3. Run the simulation:



## How to Use
#### Via flask:
1. Create virtual environment `python3 -v venv env`
2. Activate it `source env/bin/activate`
3. install dependencies `pip install -r requirements.txt`
4. run `python app.py`


#### Alternatively:
Modify the `main.py` file with your personal financial information including current age, target age, monthly income, expenses, and mortgages.
Then run 

`python backend/main.py`

## Parameters
To get the most out of this financial model, you'll start by setting some key information about your finances and goals. Here's what you need to know about each initial parameter:

current_age: This is your starting age. The model uses this to calculate how long it will simulate your financial growth, all the way up to your retirement.

target_age: Your retirement age or the age you want to reach a certain financial goal by. The model works out your finances from your current age to this age.

salary_monthly_income: How much money you make every month from your job or main income source, before taxes are taken out.

monthly_expenses: Your regular spending on things like food, housing, and bills. This does not include savings or investments.

apartment_construction_time: If you're planning to buy properties that need construction or significant repairs before they can be rented out, this is how long that process takes in months.

savings: How much money you already have saved up. This is your starting point for the model.

apartment_repair_cost: The cost to repair or prepare a property before it can be rented out.

mortgages: A list of your current or planned property loans. Each mortgage has details like the loan amount, whether it's been paid off, and how many months are left to pay it.

black_day_savings_target: The amount of money you want to keep saved for emergencies. It's your financial safety net.

apartment_cost: How much it costs to buy a new property outright. This helps the model decide when you can afford to buy more properties.

rent_income_per_apartment: The amount of money you expect to make each month from renting out a property.

income_tax: The percentage of your income that goes to taxes. This helps calculate your actual take-home pay.

Steps to Use the Model:
Fill in Your Info: Start by entering your personal financial information into the parameters of the Financial Model.

Simulate: Run the model to see how your financial situation could evolve from now until your target age. It'll show you how your savings might grow, when you could afford to invest in new properties, and how much you could earn from rentals.

Adjust and Experiment: Try changing the numbers to see how different decisions (like saving more each month or investing in more properties) could affect your financial future.

By understanding and adjusting these parameters, you can simulate different financial strategies to see which one might help you reach your goals. This tool is meant to help you plan ahead and make informed decisions about saving, spending, and investing.

The program will output your financial status at each interval considering your inputs.

## Contributing
Feel free to fork the project, make improvements, and submit pull requests. We're always looking to improve the simulation accuracy and features.
