# import numpy as np
# import matplotlib.pyplot as plt
# import csv

# # Read data from CSV
# def load_data_from_csv(filename):
#     data_points = []
#     with open(filename, 'r') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             x = float(row[0])
#             y = float(row[1])
#             data_points.append([x, y])
#     return np.array(data_points)

# # Main program
# data = load_data_from_csv('linear_data.csv')

# if len(data) < 2:
#     print("At least two points are required for linear regression.")
# else:
#     # Separate into X and Y
#     X = data[:, 0]
#     Y = data[:, 1]

#     # Calculate slope and intercept
#     mean_x = np.mean(X)
#     mean_y = np.mean(Y)

#     numerator = np.sum((X - mean_x) * (Y - mean_y)) 
#     denominator = np.sum((X - mean_x)**2)
#     beta = numerator / denominator

#     alpha = mean_y - beta * mean_x

#     # Output
#     print(f"Alpha (Intercept): {alpha:.2f}")
#     print(f"Beta (Slope): {beta:.2f}")
#     print(f"Linear Regression Equation: y = {beta:.2f}x + {alpha:.2f}")

#     # Plot
#     x_range = np.linspace(X.min(), X.max(), 100)
#     y_pred = alpha + beta * x_range
    
#     plt.figure(figsize=(8, 5))
#     plt.scatter(X, Y, color='blue', label='Data Points')
#     plt.plot(x_range, y_pred, color='red', label='Regression Line')
#     plt.title("Linear Regression")
#     plt.xlabel("X")
#     plt.ylabel("Y")
#     plt.legend()
#     plt.grid(True)
#     plt.show()

# Data
experience = [3, 8, 9, 13, 3, 6, 11, 21, 1, 16]
salary = [30, 57, 64, 72, 36, 43, 59, 90, 20, 83]
# Step 1: Calculate means
n = len(experience)
mean_x = sum(experience) / n
mean_y = sum(salary) / n
# Step 2: Calculate slope (m) and intercept (c)
numerator = sum((experience[i] - mean_x) * (salary[i] - mean_y) for i in
range(n))
denominator = sum((experience[i] - mean_x) ** 2 for i in range(n))
m = numerator / denominator
c = mean_y - m * mean_x
# Step 3: Predict salary for 10 years of experience
x_new = 10
y_pred = m * x_new + c
# Output
print("Slope (m):", m)
print("Intercept (c):", c)
print("Predicted Salary for 10 years experience:", y_pred)