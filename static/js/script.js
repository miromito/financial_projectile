function simulate() {
	// Collecting input values from the form
	const currentAge = document.getElementById("current_age").value;
	const targetAge = document.getElementById("target_age").value;
	const monthlyIncome = document.getElementById("salary_monthly_income").value;
	const monthlyExpenses = document.getElementById("monthly_expenses").value;
	const salaryTax = document.getElementById("salary_tax").value; // Ensure this input exists in your HTML
	const savings = document.getElementById("savings").value;
	const constructionTimeMonths = document.getElementById(
		"apartment_construction_time_months"
	).value;
	const blackDaySavingsTarget = document.getElementById(
		"black_day_savings_target"
	).value;
	const rentIncomePerApartment = document.getElementById(
		"rent_income_per_apartment"
	).value;
	const apartmentCost = document.getElementById("apartment_cost").value;
	const apartmentRepairCost = document.getElementById(
		"apartment_repair_cost"
	).value;

	// Making a POST request to the server with the collected data
	fetch("/simulate", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
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
			apartment_repair_cost: apartmentRepairCost,
		}),
	})
		.then((response) => response.json())
		.then((data) => {
			const resultsDiv = document.getElementById("results");
			resultsDiv.innerHTML = ""; // Clear previous results

			// Extract the last entry for total information
			const totalInfo = data.pop(); // Removes and returns the last item

			// Create total information display
			const summaryDiv = document.createElement("div");
			summaryDiv.className = "summary";

			// Loop over the keys in totalInfo
			for (let key in totalInfo) {
				// Create a new card for each key
				const cardHTML = `
        <div class="card card-stats">
            <div class="card-body">
                <div class="col">
                    <h5 class="card-title text-uppercase text-muted">${key}</h5>
                    <span class="h2 font-weight-bold color-blue count">${totalInfo[key]}</span>
                </div>
                
            </div>
        </div>
    `;

				// Append the new card to the summaryDiv
				summaryDiv.innerHTML += cardHTML;
			}

			// Create the details table
			const detailsDiv = document.createElement("div");
			detailsDiv.className = "limiter";

			const containerDiv = document.createElement("div");
			containerDiv.className = "container-table100";
			containerDiv.style.display = "none"; // Hide the table initially
			const wrapDiv = document.createElement("div");
			wrapDiv.className = "wrap-table100";
			const tableDiv = document.createElement("div");
			tableDiv.className = "table100 ver6 m-b-110";
			const table = document.createElement("table");
			table.dataset.verTable = "ver6";
			const thead = document.createElement("thead");
			thead.innerHTML = `<tr class="row100 head">
    <th class="column100 column1" data-column="column1">Age</th>
    <th class="column100 column2" data-column="column2">Total Savings</th>
    <th class="column100 column3" data-column="column3">Monthly Income - Expenses</th>
    <th class="column100 column4" data-column="column4">Rental Income</th>
    <th class="column100 column5" data-column="column5">Apts Owned</th>
    <th class="column100 column6" data-column="column6">Apts in Construction</th>
    <th class="column100 column7" data-column="column7">Mortgages Owned</th>
</tr>`;
			table.appendChild(thead);
			const tbody = document.createElement("tbody");
			data.forEach((item, index) => {
				const tr = document.createElement("tr");
				tr.className = "row100";
				tr.innerHTML = `<td class="column100 column1" data-column="column1">${item.Age}</td>
    <td class="column100 column2" data-column="column2">${item.Savings}</td>
    <td class="column100 column3" data-column="column3">${item["Monthly Income"]}</td>
    <td class="column100 column4" data-column="column4">${item["Rental Income"]}</td>
    <td class="column100 column5" data-column="column5">${item["Apartments Constructed Owned"]}</td>
    <td class="column100 column6" data-column="column6">${item["Apartments in Construction Owned"]}</td>
    <td class="column100 column7" data-column="column7">${item["Mortgages Owned"]}</td>`;
				tbody.appendChild(tr);
			});
			table.appendChild(tbody);
			tableDiv.appendChild(table);
			wrapDiv.appendChild(tableDiv);
			containerDiv.appendChild(wrapDiv);
			detailsDiv.appendChild(containerDiv);

			// Append both the summary and details to resultsDiv

			// Create the pill switch
			const pillSwitch = document.createElement("div");
			pillSwitch.className = "pill-switch";

			// Create the buttons
			const chartButton = document.createElement("button");
			chartButton.textContent = "Chart";
			chartButton.className = "active";
			const tableButton = document.createElement("button");
			tableButton.textContent = "Table";

			// Append the buttons to the pill switch
			pillSwitch.appendChild(chartButton);
			pillSwitch.appendChild(tableButton);

			// Add event listeners to the buttons
			chartButton.addEventListener("click", () => {
				chartButton.className = "active";
				tableButton.className = "";
				// Show the chart and hide the table
				chartDiv.style.display = "block";
				containerDiv.style.display = "none";
			});
			tableButton.addEventListener("click", () => {
				tableButton.className = "active";
				chartButton.className = "";
				// Show the table and hide the chart
				containerDiv.style.display = "block";
				chartDiv.style.display = "none";
			});

			// Append the summary card to resultsDiv
			resultsDiv.appendChild(summaryDiv);

			// Append the pill switch to resultsDiv
			resultsDiv.appendChild(pillSwitch);

			// Create the canvas for the chart
			const canvas = document.createElement("canvas");
			canvas.id = "savingsChart";

			// Append the chart and details table to resultsDiv
			resultsDiv.appendChild(canvas);
			resultsDiv.appendChild(detailsDiv);

			// Add event listeners to the buttons
			chartButton.addEventListener("click", () => {
				chartButton.className = "active";
				tableButton.className = "";
				// Show the chart and hide the table
				canvas.style.display = "block";
				detailsDiv.style.display = "none";
			});
			tableButton.addEventListener("click", () => {
				tableButton.className = "active";
				chartButton.className = "";
				// Show the table and hide the chart
				detailsDiv.style.display = "block";
				canvas.style.display = "none";
			});

			// Prepare the data for the chart
			const labels = data.map((item) => item.Age);
			const savingsData = data.map((item) => item.Savings);

			// Create the chart
			const ctx = document.getElementById("savingsChart").getContext("2d");

			// Create the gradient
			const gradient = ctx.createLinearGradient(0, 0, 0, 400);
			gradient.addColorStop(0, "#6a35ee");
			gradient.addColorStop(0.1424, "#9930ef");
			gradient.addColorStop(0.4956, "#5737ee");
			gradient.addColorStop(0.932, "#795ceb");

			new Chart(ctx, {
				type: "line",
				data: {
					labels: labels,
					datasets: [
						{
							label: "Savings",
							data: savingsData,
							backgroundColor: "#00000030", // Use the gradient here
							borderColor: gradient, // Use the gradient here
							tension: 0.1,
							pointStyle: false,
							fill: true,
						},
					],
				},
				options: {
					responsive: true,
					maintainAspectRatio: false,
					scales: {
						x: {
							title: {
								display: true,
								text: "Age",
								color: "#fff", // Light color for dark UI
							},
							grid: {
								color: "rgba(255, 255, 255, 0.1)", // Light color for dark UI
							},
							ticks: {
								color: "#fff", // Light color for dark UI
							},
						},
						y: {
							title: {
								display: true,
								text: "Savings",
								color: "#fff", // Light color for dark UI
							},
							grid: {
								color: "rgba(255, 255, 255, 0.1)", // Light color for dark UI
							},
							ticks: {
								color: "#fff", // Light color for dark UI
							},
						},
					},
					plugins: {
						legend: {
							labels: {
								color: "#fff", // Light color for dark UI
							},
						},
					},
				},
			});
		})
		.catch((error) => console.error("Error:", error));
}