import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 35]

# Create a line plot
plt.plot(x, y, marker='o')

plt.title('Simple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()
