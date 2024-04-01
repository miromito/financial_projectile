function simulate() {
    // Collecting input values from the form
    const currentAge = document.getElementById('current_age').value;
    const targetAge = document.getElementById('target_age').value;
    const monthlyIncome = document.getElementById('salary_monthly_income').value;
    const monthlyExpenses = document.getElementById('monthly_expenses').value;
    const salaryTax = document.getElementById('salary_tax').value; // Ensure this input exists in your HTML
    const savings = document.getElementById('savings').value;
    const constructionTimeMonths = document.getElementById('apartment_construction_time_months').value;
    const blackDaySavingsTarget = document.getElementById('black_day_savings_target').value;
    const rentIncomePerApartment = document.getElementById('rent_income_per_apartment').value;
    const apartmentCost = document.getElementById('apartment_cost').value;
    const apartmentRepairCost = document.getElementById('apartment_repair_cost').value;

    // Making a POST request to the server with the collected data
    fetch('/simulate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            current_age: currentAge,
            target_age: targetAge,
            salary_monthly_income: monthlyIncome,
            salary_tax: salaryTax,
            monthly_expenses: monthlyExpenses,
            savings: savings,
            apartment_construction_time_months: constructionTimeMonths,
            black_day_savings_target: blackDaySavingsTarget,
            rent_income_per_apartment: rentIncomePerApartment,
            apartment_cost: apartmentCost,
            apartment_repair_cost: apartmentRepairCost
        }),
    })
    .then(response => response.json())
    .then(data => {
        const resultsDiv = document.getElementById('results');
        resultsDiv.innerHTML = ''; // Clear previous results

        // Extract the last entry for total information
        const totalInfo = data.pop(); // Removes and returns the last item

        // Create total information display
        const summaryDiv = document.createElement('div');
        summaryDiv.className = 'summary';
        summaryDiv.innerHTML = `<h2>Total Information</h2>
            <p>Age: ${totalInfo.Age}</p>
            <p>Savings: ${totalInfo.Savings}</p>
            <p>Monthly Income after Tax: ${totalInfo['Monthly Income']}</p>
            <p>Rental Income: ${totalInfo['Rental Income']}</p>
            <p>Apts Constructed: ${totalInfo['Apartments Constructed Owned']}</p>
            <p>Apts In Construction: ${totalInfo['Apartments in Construction Owned']}</p>
            <p>Total Value (30% increase for apts): ${totalInfo['Total Value']}</p>
`;

        // Create the details table
        const detailsDiv = document.createElement('div');
        detailsDiv.className = 'details';
        const table = document.createElement('table');
        table.className = 'results-table';
        const thead = document.createElement('thead');
        thead.innerHTML = `<tr>
                <th>Age</th>
                <th>Total Savings</th>
                <th>Monthly Income after Tax</th>
                <th>Rental Income</th>
                <th>Apts Owned</th>
                <th>Apts in Construction</th>
                <th>Mortgages Owned</th>
            </tr>`;
        table.appendChild(thead);
        const tbody = document.createElement('tbody');
        data.forEach(item => {
            const tr = document.createElement('tr');
            tr.innerHTML = `<td>${item.Age}</td>
                <td>${item.Savings}</td>
                <td>${item['Monthly Income']}</td>
                <td>${item['Rental Income']}</td>
                <td>${item['Apartments Constructed Owned']}</td>
                <td>${item['Apartments in Construction Owned']}</td>
                <td>${item['Mortgages Owned']}</td>`;
            tbody.appendChild(tr);
        });
        table.appendChild(tbody);
        detailsDiv.appendChild(table);

        // Append both the summary and details to resultsDiv
        resultsDiv.appendChild(summaryDiv);
        resultsDiv.appendChild(detailsDiv);
    })
    .catch(error => console.error('Error:', error));
}