---
tags:
    - Discrete Random Variables
    - PMF
    - CDF
    - Binomial
    - Poisson
---

<h1 align="center">Discrete Random Variables</h1>

This session introduces random variables as numerical functions of outcomes and models their countable values using PMFs and CDFs. Expectation and variance are introduced as properties of a probability model rather than summaries calculated from an observed data sample. The central models are Bernoulli, binomial, geometric, hypergeometric, and Poisson distributions.

A probability mass function assigns probability to each possible value; the CDF accumulates those probabilities. Expectation and variance follow from the PMF. Choosing a named distribution is a modelling step: repeated independent trials, waiting times, sampling without replacement, and counts each point to a different family. Python is used to simulate the chosen model.

#### Key Concepts

- Random variables as numerical functions of outcomes
- Probability mass functions and CDFs
- Expectation and variance of a discrete random variable
- Bernoulli, binomial, geometric, hypergeometric, and Poisson models
- Matching a distribution to the assumptions of a problem
- Simulation of a discrete random variable

!!! tip "Learning Objectives"

    - Define a discrete random variable and identify its possible values.
    - Validate and use a PMF and construct its CDF.
    - Calculate and interpret expectation and variance as model properties.
    - Distinguish repeated independent trials, waiting-time models, sampling without replacement, and count models.
    - Simulate a discrete random variable in Python.

<hr/>

### Session Preparation:

Attempt the exercises from [Session 1](../01_Probability_Foundations/README.md#exercises).

**Syllabus and input**

- [Probability mass functions](https://www.probabilitycourse.com/chapter3/3_1_3_pmf.php)
- [Special discrete distributions](https://www.probabilitycourse.com/chapter3/3_1_5_special_discrete_distr.php)
- [Cumulative distribution functions](https://www.probabilitycourse.com/chapter3/3_2_1_cdf.php)

**Existing course material**

- [Recap and exercise notes](https://drive.google.com/file/d/1xX9-A1fTUsaXV-mFlmRYR4fRoQcoszrX/view?usp=sharing)
- [Session notes](https://drive.google.com/file/d/1LJ8Nu0D1PLLB1FF1jTsLK50HGLhl1EtG/view?usp=sharing)
- [Session material](https://viaucdk-my.sharepoint.com/:f:/g/personal/rib_viauc_dk/EthiTapbBz1JrNRDVKsHTnkB2LPmmbKwlY22zvyaCJMI9Q?e=0ggVfo)

<hr/>

### Exercises

#### Exercise 1 — From outcomes to a distribution

Let \(X\) be the number of sixes obtained in three independent rolls of a fair die.

1. State the possible values of \(X\).
2. Find the PMF of \(X\).
3. Find \(E[X]\) and \(\operatorname{Var}(X)\).
4. Explain which assumptions make a binomial model appropriate.

??? answer

    \(X\sim\operatorname{Binomial}(3,1/6)\). Thus \(R_X=\{0,1,2,3\}\), \(P(X=k)={3\choose k}(1/6)^k(5/6)^{3-k}\), \(E[X]=1/2\), and \(\operatorname{Var}(X)=5/12\). The three trials have two relevant outcomes, use the same success probability, and are independent.

#### Exercise 2 — Valid PMF

Let \(P(X=k)=c/3^k\) for \(k=1,2,\ldots\).

1. Find \(c\).
2. Find \(P(X\in\{2,4,6\})\).
3. Find \(P(X\ge 3)\).

??? answer

    Since \(\sum_{k=1}^{\infty}c/3^k=c/2=1\), \(c=2\). The remaining probabilities are \(182/729\) and \(1/9\), respectively.

#### Exercise 3 — Binomial model

An airline sells 125 tickets for a flight with 120 seats. Each passenger independently fails to appear with probability 0.10.

1. Find the probability that everyone who appears can take the flight.
2. Find the probability that the flight leaves with at least one empty seat.

??? answer

    Let \(X\sim\operatorname{Binomial}(125,0.9)\) be the number appearing. Calculate \(P(X\le120)\) and \(P(X\le119)\), respectively.

#### Exercise 4 — Geometric model

A player defeats each opponent independently with probability 0.8 and continues until the first defeat. Let \(X\) be the number of opponents contested.

1. Find the PMF of \(X\).
2. Find \(P(X\ge4)\).
3. Find \(E[X]\).

??? answer

    \(X\sim\operatorname{Geometric}(0.2)\) when the terminal defeat is counted. Thus \(P(X=k)=0.8^{k-1}0.2\), \(P(X\ge4)=0.8^3\), and \(E[X]=5\).

#### Exercise 5 — Poisson counts

The local density of stars is one star per 16 cubic light-years. Model counts in disjoint volumes as independent.

1. Find the probability of no stars in 16 cubic light-years.
2. Find the probability of at least two stars in that volume.
3. Find the volume needed for the probability of at least one star to exceed 0.95.

??? answer

    For volume \(v\), \(X\sim\operatorname{Poisson}(v/16)\). The answers are \(e^{-1}\), \(1-2e^{-1}\), and any \(v>-16\ln(0.05)\approx47.93\).

#### Exercise 6 — Model and simulate

A packet is lost independently with probability 0.01, and a message contains 100 packets.

1. State the distribution of the number of resent packets.
2. Find the probability that at least one packet is resent.
3. Simulate 10,000 messages and compare the simulated frequency with the exact result.

??? answer

    \(X\sim\operatorname{Binomial}(100,0.01)\), so \(P(X\ge1)=1-0.99^{100}\approx0.6340\). A simulation should approach this value as the number of messages grows.

#### Exercise 7 — Warranty failures

A manufacturer expects 2% of its units to fail during the warranty period. A sample of 500 independent units is followed.

1. State the distribution of the number of failures.
2. Find the probability that none fail.
3. Find the expected number and standard deviation of failures.
4. Find the probability that more than two units fail.
5. Assess whether a Poisson approximation is reasonable and compare the two results.

??? answer

    \(X\sim\operatorname{Binomial}(500,0.02)\), with \(E[X]=10\) and \(\operatorname{SD}(X)=\sqrt{9.8}\). Use \(P(X>2)=1-P(X\le2)\). The approximation \(X\approx\operatorname{Poisson}(10)\) is reasonable because \(n\) is large and \(p\) is small.

#### Exercise 8 — Shipments containing defects

Each device is defective independently with probability 0.03. An inspector examines 20 devices from each of 10 shipments.

1. Find the probability that a particular inspected shipment contains at least one defective device.
2. State the distribution of the number of inspected shipments containing at least one defective device.
3. Find the probability that exactly three shipments contain at least one defective device.
4. Simulate the complete two-level experiment and compare with the analytical result.

??? answer

    For one shipment, \(q=1-0.97^{20}\). The number of affected shipments is \(Y\sim\operatorname{Binomial}(10,q)\), so \(P(Y=3)={10\choose3}q^3(1-q)^7\).

#### Exercise 9 — Designing an inspection sample

A lot contains a small proportion \(p=0.01\) of nonconforming products. Items are sampled independently using a binomial approximation.

1. Find the smallest sample size \(n\) for which the probability of observing at least one nonconforming item is at least 0.90.
2. Repeat for target probabilities 0.95 and 0.99.
3. Explain how the answer changes if sampling is without replacement from a lot of only 200 items.

??? answer

    Solve \(1-(1-p)^n\ge q\), or \(n\ge \log(1-q)/\log(1-p)\), and round up. For \(q=0.90\), the minimum is \(230\). A small finite lot requires a hypergeometric rather than binomial model.

The notebook [ex1.ipynb](ex1.ipynb) can be used as a starting point for discrete-distribution calculations.
