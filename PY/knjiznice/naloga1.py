import math

import matplotlib.pyplot as plt

# Generate x values from -2π to 2π with step π/8
step = math.pi / 8
start = -2 * math.pi
end = 2 * math.pi + step

x = []
current = start
while current <= end:
    x.append(current)
    current += step

# Compute y = sin(x) for each x
y = [math.sin(val) for val in x]

# Plotting
plt.scatter(x, y)
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.title("Naloga 9:")
plt.show()
