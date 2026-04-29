# Logistic Sequences

A Python-based project for exploring and visualizing the **Logistic Map**, a polynomial mapping of degree 2 often used to illustrate how complex, chaotic behavior can arise from very simple non-linear dynamical equations.

## Overview

This repository contains tools to:
1.  **Compute Sequences**: Generate data points for the logistic map defined by the recurrence relation:
    $p_{n+1} = k \cdot p_n \cdot (1 - p_n)$
2.  **Visualize Results**: Create line plots showing the evolution of $p$ over discrete iterations for various initial conditions ($p_0$) and growth rates ($k$).

## Repository Structure

- `compute.py`: The main script that calculates sequences for a predefined set of $p$ and $k$ values and exports them to `runs.csv`.
- `graphs.py`: Reads the computed data and generates graphs using Matplotlib.
- `runs.csv`: The generated dataset containing iterations for multiple parameter combinations.
- `graphs/`: Directory containing exported PNG plots of the sequences.
- `LatexPresentation.pdf`: A LaTeX presentation detailing the results of these experiments.

## Parameters

The current configuration explores:
- **$p_0$ values**: `0.6572, 0.5, 0.892, 0.121, 0.9932, 0.893, 0.891`
- **$k$ values**: `1.964343, 1.2345, 2.7852, 3.321, 3.4729, 3.8342`
- **Iterations**: 100 steps per sequence.

## Example Output

The plots illustrate different behaviors of the logistic map, ranging from convergence to a fixed point to periodic oscillations and chaotic fluctuations, depending on the value of $k$.
