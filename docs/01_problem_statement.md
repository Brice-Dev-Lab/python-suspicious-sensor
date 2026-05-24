# The Suspicious Sensor  
*A Probability, Statistics, and Monte Carlo Exercise*

---

# Scenario

A water utility installs a pressure sensor on a transmission main feeding a lift station.

The engineers believe the pressure fluctuations follow a normal distribution:

```text
μ = 72 psi
σ = 4 psi
```

However, after several months, operators suspect the system may actually be experiencing abnormal pressure instability.

You collect the following observed pressure readings (psi):

see `data/raw/pressure_readings.csv` for data.

Your task is to investigate whether the system still appears consistent with the original assumptions.

Because infrastructure systems never simply behave quietly and respectfully for decades. That would apparently violate the laws of engineering.

---

# Part A — Basic Statistics

Compute the following:

1. Sample mean
2. Sample variance
3. Sample standard deviation

---

# Part B — Z-Scores

For each observation, compute the z-score using:

```text
z = (x - μ) / σ
```

Questions:
- Which values appear unusual?
- Does `81 psi` look like a potential outlier?

---

# Part C — Probability Thinking

Assuming the original distribution is correct:

```text
X ~ N(72, 4²)
```

Estimate:

1. Probability that pressure exceeds `80 psi`
2. Probability that pressure falls below `65 psi`

You may use:
- z-tables,
- Python,
- SciPy,
- or approximation reasoning.

---

# Part D — MCMC / Monte Carlo Connection

Suppose you do **not** know the true mean pressure anymore.

You now want to estimate the unknown system mean using simulation methods.

Conceptual Questions:

1. Why might Monte Carlo methods help here?
2. Why might sampling from a posterior distribution be useful?
3. What advantages would Bayesian estimation provide over a single-point estimate?

---

# Part E — Infrastructure Engineering Interpretation

Assume:
- pressures above `80 psi` increase risk of pipe stress,
- pressures below `65 psi` increase risk of inadequate service.

Questions:
- Which condition is operationally more dangerous?
- Would occasional excursions matter?
- What additional data would you want before making engineering recommendations?

---

# Bonus Mode — Monte Carlo Simulation

Implement a simple Monte Carlo simulation:

1. Generate `100,000` synthetic pressure readings
2. Estimate:
   - probability of exceeding `80 psi`,
   - expected pressure,
   - confidence intervals,
   - histogram behavior.

Then compare:
- analytical probability
vs
- simulated probability.

Because eventually every sufficiently advanced infrastructure problem becomes:

> “We should probably simulate this 100,000 times and hope the pipes survive.”

---

# Suggested Python Libraries

You may optionally use:

```python
numpy
scipy
matplotlib
pandas
seaborn
```

---

# Suggested Extensions

Possible future extensions include:

- Bayesian parameter estimation
- Posterior distribution visualization
- Markov Chain Monte Carlo sampling
- Time-series pressure analysis
- Infrastructure risk scoring
- Reliability modeling
- Sensor anomaly detection
- Predictive maintenance modeling

---

# Learning Objectives

This exercise introduces concepts related to:

- Probability distributions
- Descriptive statistics
- Standardization using z-scores
- Statistical inference
- Monte Carlo simulation
- Bayesian reasoning
- Infrastructure risk interpretation
- Engineering uncertainty

---

# Deliverables

Suggested outputs:
- handwritten derivations,
- Jupyter notebook analysis,
- probability calculations,
- visualization plots,
- simulation results,
- engineering interpretation summary.

Because the real challenge in engineering is not producing numbers.

It is determining whether the numbers are quietly lying to you.