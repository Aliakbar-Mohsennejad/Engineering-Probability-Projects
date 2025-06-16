# -*- coding: utf-8 -*-
"""
Engineering Probability Project - Q3: Bus Delay Problem
Author: Aliakbar Mohsennejad
Date: 2023
"""

import numpy as np
import matplotlib.pyplot as plt

# ------------------------
# Parameters for delay
delay_min = 0      # Min delay in minutes
delay_max = 20     # Max delay in minutes
num_samples = 1000

# ------------------------
# Generate random delays (uniform distribution)
delays = np.random.uniform(delay_min, delay_max, num_samples)

# ------------------------
# Part 1 – Probability Calculations

# Case A: Person arrives at 12:00
prob_wait_more_than_5 = np.sum(delays > 5) / num_samples

# Case B: Person arrives at 12:10
# Person waits if delay is > 10+5 = 15 minutes
prob_late_arrival_waits_more_than_5 = np.sum(delays > 15) / num_samples

print(f"[Case A] Probability of waiting > 5 min (arrives at 12:00): {prob_wait_more_than_5:.3f}")
print(f"[Case B] Probability of waiting > 5 min (arrives at 12:10): {prob_late_arrival_waits_more_than_5:.3f}")

# ------------------------
# Part 2 – Plot histogram
plt.figure(figsize=(8, 5))
plt.hist(delays, bins=20, color='skyblue', edgecolor='black', density=True)
plt.title("Histogram of Random Bus Delays")
plt.xlabel("Delay (minutes)")
plt.ylabel("Probability Density")
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig("bus_delay_histogram.png")
plt.show()
