# 🚌 Bus Delay Simulation – Engineering Probability Project (Q3)

This simulation analyzes a bus arrival delay scenario, where the delay is modeled by a **uniform distribution** over a fixed time interval.

---

## 🧠 Problem Description

- Buses are expected to arrive at 12:00.
- Due to random traffic, they may arrive with a delay uniformly distributed between 0 and 20 minutes.
- What is the probability that a person has to wait **more than 5 minutes**?

Two scenarios:
1. **Person arrives at 12:00** → wait if delay > 5
2. **Person arrives at 12:10** → wait if delay > 15

---

## 📊 Output

The simulation:
- Generates 1000 random delays.
- Calculates probabilities for both cases.
- Plots a histogram of the sampled delay data.

### 🖼️ Histogram Example:

![Bus Delay Histogram](./bus_delay_histogram.png)

---

## 📤 Console Output Example

- [Case A] Probability of waiting > 5 min (arrives at 12:00): 0.75
- [Case B] Probability of waiting > 5 min (arrives at 12:10): 0.25

