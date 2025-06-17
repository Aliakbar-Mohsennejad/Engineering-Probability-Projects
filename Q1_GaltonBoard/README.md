#  Galton Board Simulation – Engineering Probability Project (Q1)

This project simulates a **Galton board** (or bean machine), a classic example of how the **binomial distribution** and **normal distribution** arise from random binary outcomes.

---

##  Problem Description

The Galton board contains several layers of pins. Each ball falls through the layers, bouncing either left or right with equal probability at each pin. This simulation calculates where each ball ends up and visualizes the final distribution of balls in the containers below.

---

##  Inputs

- `h`: Number of rows/pins (height of the board)
- `b`: Number of balls to simulate

These values can be modified in the script. For the current run:
```python
h = 20
b = 300
