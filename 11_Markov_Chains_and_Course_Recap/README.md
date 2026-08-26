---
tags:
    - Markov Chains
    - Stationary Distribution
    - Model Selection
    - Course Recap
---

<h1 align="center">Markov Chains and Course Recap</h1>

The final session consolidates Markov-chain analysis and connects the major course ideas: conditional probability, dependence, simulation, processes, long-run behaviour, and probabilistic prediction. Class time is primarily used for problem solving and model selection.

A Markov chain, a Poisson process, a stationary time series, and a simple random sample answer different questions. The last meeting practises choosing among them, checking assumptions, and moving between probability rules, distributions, simulation, and process models.

#### Key Concepts

- Classification of states and stationary versus limiting distributions
- Recursion with the law of total probability
- Choosing among binomial, Poisson-process, time-series, random-walk, and Markov models
- Long-run behaviour and absorption
- Connecting probability, simulation, and stochastic processes

!!! tip "Learning Objectives"

    - Use classification of states, recursion, and stationary distributions on a Markov chain.
    - Choose a model from the course and state the assumptions that make it appropriate.
    - Estimate a probability by Monte Carlo simulation and report uncertainty.
    - Move between probability rules, distributions, simulation, and process models.

<hr/>

### Session Preparation:

Attempt the exercises from [Session 10](../10_Markov_Chains/README.md#exercises) and identify the two course topics you most need to revisit.

**Syllabus and input**

- [Classification of states](https://www.probabilitycourse.com/chapter11/11_2_4_classification_of_states.php)
- [The law of total probability and recursion](https://www.probabilitycourse.com/chapter11/11_2_5_using_the_law_of_total_probability_with_recursion.php)
- [Stationary and limiting distributions](https://www.probabilitycourse.com/chapter11/11_2_6_stationary_and_limiting_distributions.php)
- [Session exercises: Problems 10](https://drive.google.com/file/d/13m9g-jfVpG9yaxR9CF6aEza6ObSWXNEW/view?usp=sharing)
- [Session material](https://viaucdk-my.sharepoint.com/:f:/g/personal/rib_viauc_dk/Enaype9j_R1DvUKrGId_u3kBW9qq69kr6D5UwdyKBCCAjg?e=d32pBn)

<hr/>

### Exercises

#### Exercise 1 — Web-service states

A service is in state Normal, Degraded, or Down. Construct a plausible transition matrix satisfying the following one-step statements: a normal service remains normal with probability 0.92; a degraded service goes down with probability 0.10; and a down service recovers to degraded with probability 0.60. Choose and justify the remaining probabilities.

1. Draw the transition diagram.
2. Calculate the distribution after 5 steps from Normal.
3. Find a stationary distribution.
4. Simulate 10,000 steps and compare empirical state frequencies with the stationary distribution.

#### Exercise 2 — Select the model

For each situation, choose a binomial distribution, Poisson process, stationary time-series model, random walk, or Markov chain. State the assumptions that make the model appropriate and one way the assumptions could fail.

1. Failed requests among 200 independent API calls.
2. Arrival times of support tickets.
3. Hourly CPU load fluctuating around a stable level with serial dependence.
4. A user's movement among pages of an application.
5. A cumulative account balance driven by independent daily shocks.

#### Exercise 3 — Simulation and uncertainty

Choose one model from the course and estimate a non-trivial probability by Monte Carlo simulation. Include:

1. the mathematical model and target probability;
2. reproducible Python code;
3. an analytical result when available;
4. a Monte Carlo standard error;
5. a discussion of model assumptions and limitations.

#### Exercise 4 — Long-run service availability

Use the transition matrix constructed in Exercise 1.

1. Determine whether the chain is irreducible and aperiodic.
2. Find its stationary distribution.
3. Interpret the long-run proportions of time in Normal, Degraded, and Down.
4. Change one transition probability to represent an improved repair process and quantify the effect on long-run availability.

#### Exercise 5 — An absorbing release process

A software change moves among Review, Testing, Released, and Rejected with transition matrix

\[
P=\begin{pmatrix}
0.3&0.6&0&0.1\\
0.2&0.3&0.4&0.1\\
0&0&1&0\\
0&0&0&1
\end{pmatrix}.
\]

1. Identify transient and absorbing states.
2. Starting in Review, find the probability of eventual release.
3. Find the expected number of steps until absorption.
4. Verify both results by simulation.

#### Exercise 6 — One dataset, competing models

An API log records one-minute request counts, mean response times, and a categorical health state for 30 days.

1. Propose a Poisson-process model for the request counts.
2. Propose a stationary time-series model for response time.
3. Propose a Markov-chain model for health state.
4. State two assumptions for each model and design one diagnostic check for each assumption.
5. Explain why the three variables should not automatically be modelled independently.

#### Exercise 7 — Integrated probability calculation

Requests arrive as a Poisson process with rate 20 per minute. Each request independently fails with probability 0.03 when the service is Normal and 0.15 when it is Degraded. During a ten-minute interval, assume the service state is fixed and is Normal with probability 0.8.

1. Find the conditional distribution of failed requests in each service state.
2. Find the unconditional probability of no failed requests.
3. Given that no failures were observed, find the probability that the service was Normal.
4. Simulate the full hierarchical model and verify the analytical results.

??? answer

    Thinning gives Poisson means \(20(10)(0.03)=6\) and \(20(10)(0.15)=30\). Hence \(P(F=0)=0.8e^{-6}+0.2e^{-30}\), and Bayes' rule gives \(P(N\mid F=0)=\frac{0.8e^{-6}}{0.8e^{-6}+0.2e^{-30}}\).

### Course checklist

You should now be able to move between four representations of uncertainty:

- probability rules and conditional reasoning;
- distributions of single and multiple random variables;
- simulation and limit-theorem approximations;
- stochastic-process models for dependence over time.
