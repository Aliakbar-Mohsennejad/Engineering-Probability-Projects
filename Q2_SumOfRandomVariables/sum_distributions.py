# -*- coding: utf-8 -*-
"""
Engineering Probability Project - Q2: Sum of Random Variables
Author: Aliakbar Mohsennejad
Date: 2023
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon, uniform
from math import factorial

def plot_sum_distributions(distribution, name, lam=1, sample_size=10000):
    plt.figure(figsize=(12, 8))

    for idx, n in enumerate(range(2, 15, 2), 1):
        plt.subplot(3, 3, idx)

        if distribution == 'exponential':
            samples = np.sum(np.random.exponential(scale=1/lam, size=(sample_size, n)), axis=1)
        elif distribution == 'uniform':
            samples = np.sum(np.random.uniform(0, 1, size=(sample_size, n)), axis=1)
        else:
            raise ValueError("Unsupported distribution type.")

        plt.hist(samples, bins=50, density=True, alpha=0.7, label=f'n = {n}')
        plt.title(f'{name} Sum for n = {n}')
        plt.xlabel('Value')
        plt.ylabel('Density')
        plt.grid(True)

    plt.tight_layout()
    plt.savefig(f"{name.lower()}_sum_distribution.png")
    plt.show()


if __name__ == "__main__":
    plot_sum_distributions(distribution='exponential', name='Exponential', lam=1)
    plot_sum_distributions(distribution='uniform', name='Uniform')
