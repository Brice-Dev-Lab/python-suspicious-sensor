# Suspicious Sensor Analysis  
*A Probability, Statistics, and Monte Carlo Engineering Exercise*

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![Status](https://img.shields.io/badge/status-in%20progress-orange)
![Focus](https://img.shields.io/badge/focus-probability%20%7C%20statistics%20%7C%20MCMC-informational)
![Simulation](https://img.shields.io/badge/simulation-Monte%20Carlo-darkgreen)
![Domain](https://img.shields.io/badge/domain-infrastructure%20analytics-critical)
![Math](https://img.shields.io/badge/math-statistics%20%26%20bayesian%20reasoning-purple)
![Data](https://img.shields.io/badge/data-synthetic%20sensor%20dataset-lightgrey)
![Difficulty](https://img.shields.io/badge/level-intermediate-red)

A probability, statistics, and Monte Carlo simulation exercise centered around infrastructure pressure monitoring and operational uncertainty.

This project explores:
- descriptive statistics,
- z-scores,
- probability distributions,
- Monte Carlo simulation,
- Bayesian reasoning,
- and engineering interpretation of infrastructure sensor data.

Because eventually every infrastructure system starts behaving strangely at 2 AM and someone has to decide whether it is:
- instrumentation noise,
- operational drift,
- hydraulic instability,
- or the opening scene of a capital improvement project.

---

# Scenario

A water utility installs a pressure sensor on a transmission main feeding a lift station.

Engineers originally believed the system pressure followed a normal distribution:

```text
μ = 72 psi
σ = 4 psi
```

However, operators begin observing signs of abnormal pressure instability.

A synthetic sensor dataset has been provided to investigate:
- pressure variability,
- potential outliers,
- operational excursions,
- and system uncertainty.

---

# Dataset Overview

The dataset includes:
- timestamped pressure readings,
- normal operational fluctuations,
- gradual drift behavior,
- low-pressure excursions,
- high-pressure anomalies,
- and possible outlier conditions.

The dataset was intentionally designed to resemble realistic infrastructure operations rather than perfectly clean textbook statistics.

Because real infrastructure systems are messy, noisy, and deeply committed to violating assumptions.

---

# Learning Objectives

This exercise introduces concepts related to:

- Descriptive statistics
- Sample variance and standard deviation
- Z-score analysis
- Probability distributions
- Statistical inference
- Monte Carlo simulation
- Bayesian reasoning
- Infrastructure risk interpretation
- Engineering uncertainty

---

# Topics Explored

## Statistics

- Mean
- Variance
- Standard deviation
- Outlier detection
- Distribution behavior

---

## Probability

- Normal distributions
- Z-score calculations
- Tail probabilities
- Event likelihood estimation

---

## Monte Carlo Simulation

- Random sampling
- Synthetic data generation
- Probability estimation
- Confidence intervals
- Histogram analysis

---

## Bayesian / MCMC Concepts

- Posterior estimation
- Parameter uncertainty
- Sampling methods
- Distribution inference
- Probabilistic reasoning

---

# Suggested Workflow

Possible analysis steps include:

1. Load and inspect the dataset
2. Compute descriptive statistics
3. Visualize pressure distributions
4. Calculate z-scores
5. Identify anomalies and excursions
6. Estimate probability thresholds
7. Perform Monte Carlo simulations
8. Explore Bayesian estimation concepts
9. Interpret operational infrastructure risk

---

# Suggested Python Libraries

Common libraries that may be useful:

```python
numpy
pandas
scipy
matplotlib
seaborn
```

Additional tools may include:
- arviz
- pymc
- jupyter
- statsmodels

---

# Example Questions

## Statistical Questions

- Does the data appear normally distributed?
- Are there significant outliers?
- Is the system mean shifting over time?

---

## Engineering Questions

- Are high-pressure events operationally significant?
- Could low-pressure excursions indicate service risk?
- Is additional monitoring required?
- Would pressure transients justify infrastructure upgrades?

---

## Simulation Questions

- What is the probability of pressure exceeding 80 psi?
- How often would low-pressure conditions occur?
- How sensitive are results to changes in variance?

---

# Potential Extensions

Future project extensions may include:

- Time-series forecasting
- Sensor anomaly detection
- Infrastructure reliability modeling
- Bayesian parameter estimation
- Markov Chain Monte Carlo (MCMC)
- Predictive maintenance analytics
- Hydraulic system simulation
- Risk scoring pipelines

---

# Repository Notes

This exercise intentionally blends:
- infrastructure engineering,
- statistics,
- simulation,
- and probabilistic systems thinking.

The objective is not merely to calculate numbers, but to interpret uncertainty in a realistic operational context.

Because engineering is rarely about finding a perfect answer.

It is usually about determining whether the system is failing slowly enough to survive the budget cycle.