import numpy as np

# Sample income data
income_data = np.array([50, 100, 200, 400, 800, 1600, 3200])
poverty_line = 300  # Define poverty line

# Poverty Headcount Ratio (PHR)
calculate_phr = lambda incomes, threshold: (np.sum(incomes < threshold) / len(incomes)) * 100

# Gini Coefficient
def calculate_gini(incomes):
    sorted_incomes = np.sort(incomes)
    n = len(sorted_incomes)
    cumulative_income = np.cumsum(sorted_incomes)
    lorenz_area = np.sum(cumulative_income) / cumulative_income[-1]
    gini = (2 * lorenz_area / n) - (n + 1) / n
    return gini

# Calculations
phr = calculate_phr(income_data, poverty_line)
gini = calculate_gini(income_data)

# Results
print(f"Poverty Headcount Ratio (PHR): {phr:.2f}%")
print(f"Gini Coefficient: {gini:.4f}")
