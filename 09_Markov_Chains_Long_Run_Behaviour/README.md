---
tags:
    - Markov Chains
    - Stationary Distribution
    - Absorption
    - Classification of States
---

<h1 align="center">Markov Chains: Long-Run Behaviour</h1>

This session follows a Markov chain over many steps. Where does the chain end up, how long does it take to get there, and what fraction of time does it spend in each state? Conditioning on the first step turns these questions into systems of linear equations.

Classification of states decides which long-run questions make sense. In a chain with absorbing states, we calculate absorption probabilities and expected absorption times by recursion with the law of total probability. In an irreducible and aperiodic chain, the stationary distribution is also the limiting distribution and gives the long-run proportion of time spent in each state. Simulation checks every analytical result.

#### Key Concepts

- Classification of states, periodicity, and irreducibility
- Recursion with the law of total probability
- Absorption probabilities and expected absorption times
- Stationary versus limiting distributions
- Long-run proportions of time and their simulation

!!! tip "Learning Objectives"

    - Classify the states of a Markov chain and identify closed classes.
    - Use first-step analysis to find absorption probabilities and expected absorption times.
    - Decide when a stationary distribution is also a limiting distribution.
    - Interpret stationary probabilities as long-run proportions and verify them by simulation.

<hr/>

### Session Preparation:

Attempt the exercises from [Session 8](../08_Markov_Chains/README.md#exercises).

**Syllabus and input**

- [Classification of states](https://www.probabilitycourse.com/chapter11/11_2_4_classification_of_states.php)
- [The law of total probability and recursion](https://www.probabilitycourse.com/chapter11/11_2_5_using_the_law_of_total_probability_with_recursion.php)
- [Stationary and limiting distributions](https://www.probabilitycourse.com/chapter11/11_2_6_stationary_and_limiting_distributions.php)

<hr/>

### Exercises

#### Exercise 1 — Web-service states

A service is in state Normal, Degraded, or Down. Construct a plausible transition matrix satisfying the following one-step statements: a normal service remains normal with probability 0.92; a degraded service goes down with probability 0.10; and a down service recovers to degraded with probability 0.60. Choose and justify the remaining probabilities.

1. Draw the transition diagram.
2. Calculate the distribution after 5 steps from Normal.
3. Find a stationary distribution.
4. Simulate 10,000 steps and compare empirical state frequencies with the stationary distribution.

#### Exercise 2 — Long-run service availability

Use the transition matrix constructed in Exercise 1.

1. Determine whether the chain is irreducible and aperiodic.
2. Find its stationary distribution.
3. Interpret the long-run proportions of time in Normal, Degraded, and Down.
4. Change one transition probability to represent an improved repair process and quantify the effect on long-run availability.

#### Exercise 3 — An absorbing release process

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
