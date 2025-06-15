# -*- coding: utf-8 -*-
"""
Galton Board Simulation - Engineering Probability Project
Author: Aliakbar Mohsennejad
Date: 2023
"""

import random
import matplotlib.pyplot as plt


def simulate_galton_board(height: int, balls: int) -> list:
    """
    Simulates a Galton board where balls fall randomly through pegs.

    Parameters:
    height (int): Number of levels in the Galton board
    balls (int): Total number of balls to drop

    Returns:
    list: Number of balls collected in each container/bin
    """
    bins = [0] * (height + 1)

    for _ in range(balls):
        position = 0
        for _ in range(height):
            position += random.randint(0, 1)
        bins[position] += 1

    return bins


def plot_histogram(bins: list):
    """
    Plots a histogram showing the distribution of balls.

    Parameters:
    bins (list): List of bin counts
    """
    plt.figure(figsize=(10, 5))
    plt.bar(range(len(bins)), bins, color='skyblue', edgecolor='black')
    plt.title("Galton Board Simulation")
    plt.xlabel("Bin Index")
    plt.ylabel("Number of Balls")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig("galton_board_histogram.png")
    plt.show()


if __name__ == '__main__':
    HEIGHT = 20   # Number of levels in the Galton board
    BALLS = 300   # Number of balls dropped

    results = simulate_galton_board(HEIGHT, BALLS)
    plot_histogram(results)
