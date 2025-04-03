import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt

# Data
x = np.array([5, 7, 10, 12, 15, 19])
y = np.array([10, 13, 18, 22, 27, 31])

# Calculate regression
mean_x, mean_y = np.mean(x), np.mean(y)
numerator = np.sum((x - mean_x) * (y - mean_y))
denominator = np.sum((x - mean_x) ** 2)
m = numerator / denominator
c = mean_y - m * mean_x

# Calculate predictions and R-squared
predictions = m * x + c
ss_res = np.sum((y - predictions) ** 2)
ss_tot = np.sum((y - mean_y) ** 2)
r_squared = 1 - (ss_res / ss_tot)

print(f"Linear formula: Y = {m:.4f}X + {c:.4f}")
print(f"R-squared: {r_squared:.4f}")

# Create and save plot
plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='blue', label='Actual Data')
plt.plot(x, predictions, color='red', label=f'Regression Line (R²={r_squared:.2f})')
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Linear Regression Analysis')
plt.legend()
plt.grid(True)
plt.savefig('regression_plot.png', bbox_inches='tight')
print("Plot saved as 'regression_plot.png'")
