import numpy as np
# jerry ensure you use python not python3 to run this particular file. 


# Sample income data (in arbitrary units)
income_data = np.array([50, 100, 200, 400, 800, 1600, 3200])

# Define poverty lin
poverty_line = 300

# Poverty Headcount Ratio (PHR)
def calculate_phr(incomes, poverty_threshold):
    """
    Calculate Poverty Headcount Ratio.
    :param incomes: Array of income data.
    :param poverty_threshold: Poverty line.
    :return: PHR as a percentage.
    """
    below_poverty = incomes[incomes < poverty_threshold]
    phr = (len(below_poverty) / len(incomes)) * 100
    return phr

# Gini Coefficient
def calculate_gini(incomes):
    """
    Calculate the Gini Coefficient.
    :param incomes: Array of income data.
    :return: Gini coefficient.
    """
    sorted_incomes = np.sort(incomes)
    n = len(sorted_incomes)
    cumulative_income = np.cumsum(sorted_incomes)
    numerator = np.sum((2 * np.arange(1, n+1) - n - 1) * sorted_incomes)
    denominator = n * np.sum(sorted_incomes)
    gini = numerator / denominator
    return gini

# Calculations
phr = calculate_phr(income_data, poverty_line)
gini = calculate_gini(income_data)

# Output results
print(f"Poverty Headcount Ratio (PHR): {phr:.2f}%")
print(f"Gini Coefficient: {gini:.4f}")
