import matplotlib.pyplot as plt
import numpy as np

# Generate data
x = np.linspace(0, 5, 100)  # Generating 100 data points from 0 to 5
y = np.exp(x)  # Exponential curve

# Create a figure and axis
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='Coolness', color='purple')

# Add labels and title
plt.xlabel('Time spent on Docker')
plt.ylabel('Coolness')
plt.title('Coolness of Hoklas people using Docker')

# Add a legend
plt.legend()

# Save the graph as a PNG image
plt.savefig('graph.png')
