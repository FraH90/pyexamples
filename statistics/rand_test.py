import numpy as np
import matplotlib.pyplot as plt

# Generate random numbers
n = 100000  # Number of random numbers
random_uniform = np.random.rand(n)  # Uniform distribution
random_normal = np.random.randn(n)  # Normal (Gaussian) distribution

# Plotting the histograms
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Uniform distribution histogram
axs[0].hist(random_uniform, bins=50, density=True, alpha=0.7, color='blue')
axs[0].set_title('Uniform Distribution (rand)')
axs[0].set_xlabel('Random Number Value')
axs[0].set_ylabel('Probability Density')

# Normal distribution histogram
axs[1].hist(random_normal, bins=50, density=True, alpha=0.7, color='green')
axs[1].set_title('Normal Distribution (randn)')
axs[1].set_xlabel('Random Number Value')
axs[1].set_ylabel('Probability Density')

# Show plot
plt.tight_layout()
plt.show()
