---
tags:
    - Discrete Random Variables
    - PMF
    - CDF
    - Bernoulli
    - Geometric
    - Binomial
    - Negative Binomial
    - Hypergeometric
    - Poisson
---

<h1 align="center">Discrete Random Variables</h1>

This session introduces random variables as numerical functions of outcomes and models their countable values using PMFs and CDFs. Expectation and variance are introduced as properties of a probability model rather than summaries calculated from an observed data sample. The central models are Bernoulli, geometric, binomial, negative binomial (Pascal), hypergeometric, and Poisson distributions.

A probability mass function assigns probability to each possible value; the CDF accumulates those probabilities. Expectation and variance follow from the PMF. Choosing a named distribution is a modelling step: a single trial, a fixed number of independent trials, waiting for the first success, waiting for a fixed number of successes, sampling without replacement, and counting events each point to a different family. The Poisson distribution is also used as an approximation to the binomial distribution under suitable conditions.

#### Key Concepts

- Random variables as numerical functions of outcomes
- Probability mass functions and CDFs
- Expectation and variance of a discrete random variable
- Bernoulli, geometric, binomial, negative binomial (Pascal), hypergeometric, and Poisson models
- Poisson approximation to the binomial distribution
- Matching a distribution to the assumptions of a problem

!!! tip "Learning Objectives"

    - Define a discrete random variable and identify its possible values.
    - Validate and use a PMF and construct its CDF.
    - Calculate and interpret expectation and variance as model properties.
    - Distinguish a single Bernoulli trial, a fixed number of trials, waiting for one or more successes, sampling without replacement, and count models.
    - Use a Poisson distribution as an approximation to a binomial distribution when appropriate.

<hr/>

### Session Preparation:

Attempt the exercises from [Session 1](../01_Probability_Foundations/README.md#exercises).

**Syllabus and input**

- [Probability mass functions](https://www.probabilitycourse.com/chapter3/3_1_3_pmf.php)
- [Special discrete distributions](https://www.probabilitycourse.com/chapter3/3_1_5_special_discrete_distr.php)
- [Cumulative distribution functions](https://www.probabilitycourse.com/chapter3/3_2_1_cdf.php)
- [Expectation](https://www.probabilitycourse.com/chapter3/3_2_2_expectation.php)
- [Variance and standard deviation](https://www.probabilitycourse.com/chapter3/3_2_4_variance.php)

**Existing course material**

- [Session notes](https://drive.google.com/file/d/1OovTGgnYuL_G_5SUaI3L2ZUf1nDDLvRl/view?usp=sharing)
- [Recap and exercise notes](https://drive.google.com/file/d/1T39OfYneVpa9PzthqThTyzNCXej1FgKH/view?usp=sharing)
- [Session material](https://viaucdk-my.sharepoint.com/:f:/g/personal/rib_viauc_dk/EthiTapbBz1JrNRDVKsHTnkB2LPmmbKwlY22zvyaCJMI9Q?e=0ggVfo)

<hr/>

### Exercises

#### Exercise 1 — Password hits

A computer system uses passwords that are exactly six characters, and each character is one of the 26 letters (a-z) or 10 integers (0-9). Suppose that 10,000 users of the system have unique passwords. A hacker randomly selects, with replacement, 100,000 passwords from the potential set. A match to a user's password is called a hit.

1. What is the distribution of the number of hits?
2. What is the probability of no hits?
3. What are the mean and variance of the number of hits?

??? answer

    1. \(X\sim\operatorname{Binomial}(100{,}000,10{,}000/36^6)\).
    2. \(P(X=0)\approx0.6317\).
    3. \(E[X]\approx0.4594\) and \(\operatorname{Var}(X)\approx0.4594\).

#### Exercise 2 — Airline overbooking

An airline sells 125 tickets for a flight with 120 seats. Each passenger independently fails to appear with probability 0.10.

1. Find the probability that everyone who appears can take the flight.
2. Find the probability that the flight leaves with at least one empty seat.

??? answer

    1. \(P(X\le120)\approx0.9961\), where \(X\sim\operatorname{Binomial}(125,0.9)\) is the number of passengers who appear.
    2. \(P(X\le119)\approx0.9886\).

#### Exercise 3 — Video-game opponents

A player defeats each opponent independently with probability 0.8 and continues until the first defeat. Let \(X\) be the number of opponents contested.

1. What is the probability mass function of the number of opponents contested in a game?
2. What is the probability that a player defeats at least two opponents in a game?
3. What is the expected number of opponents contested in a game?
4. What is the probability that a player contests four or more opponents in a game?
5. What is the expected number of game plays until a player contests four or more opponents?

??? answer

    1. \(P(X=k)=0.8^{k-1}\cdot0.2\), for \(k=1,2,\ldots\).
    2. \(0.8^2=0.64\).
    3. \(E[X]=5\).
    4. \(0.8^3=0.512\).
    5. \(1/0.512\approx1.9531\).

#### Exercise 4 — Stars in space

The local density of stars is one star per 16 cubic light-years. Model counts in disjoint volumes as independent.

1. Find the probability of no stars in 16 cubic light-years.
2. Find the probability of at least two stars in that volume.
3. Find the volume needed for the probability of at least one star to exceed 0.95.

??? answer

    1. \(P(X=0)=e^{-1}\approx0.3679\).
    2. \(P(X\ge2)=1-2e^{-1}\approx0.2642\).
    3. At least 48 cubic light-years must be studied.

#### Exercise 5 — Lost data packets

A packet is lost independently with probability 0.01, and a message contains 100 packets.

1. What is the distribution of the number of packets in an e-mail message that must be resent? Include the parameter values.
2. What is the probability that at least one packet is resent?
3. What is the probability that two or more packets are resent?
4. What are the mean and standard deviation of the number of packets that are resent?
5. Simulate 10,000 e-mail messages and compare the simulated probabilities of at least one and at least two lost packets with the exact probabilities.

??? answer

    1. \(X\sim\operatorname{Binomial}(100,0.01)\).
    2. \(P(X\ge1)\approx0.6340\).
    3. \(P(X\ge2)\approx0.2642\).
    4. \(E[X]=1\) and \(\operatorname{SD}(X)=\sqrt{0.99}\approx0.995\).
    5. The simulated probabilities should approach \(0.6340\) and \(0.2642\), respectively.

#### Exercise 6 — Warranty failures

A manufacturer expects 2% of its units to fail during the warranty period. A sample of 500 independent units is followed.

1. What is the probability that none fail during the warranty period?
2. What is the expected number of failures during the warranty period?
3. What is the probability that more than two units fail during the warranty period?
4. Approximate the probabilities in parts 1 and 3 with a Poisson distribution, and compare the results with the exact binomial probabilities.

??? answer

    1. \(P(X=0)\approx0.0000\), where \(X\sim\operatorname{Binomial}(500,0.02)\).
    2. \(E[X]=10\).
    3. \(P(X>2)\approx0.9974\).
    4. Using \(Y\sim\operatorname{Poisson}(10)\), \(P(Y=0)\approx0.0000454\) and \(P(Y>2)\approx0.9972\). The corresponding exact binomial values are approximately \(0.0000410\) and \(0.9974\), so the approximation is close.

#### Exercise 7 — Recovery from a rare disease

The probability that a patient recovers from a rare blood disease is 0.4. Fifteen people are known to have contracted the disease.

1. What is the probability that at least 10 survive?
2. What is the probability that from 3 to 8 survive?
3. What is the probability that exactly 5 survive?
4. Find the mean and variance of the number who survive.

??? answer

    1. \(P(X\ge10)\approx0.0338\).
    2. \(P(3\le X\le8)\approx0.8778\).
    3. \(P(X=5)\approx0.1859\).
    4. \(E[X]=6\) and \(\operatorname{Var}(X)=3.6\).

#### Exercise 8 — Shipments containing defects

Each device is defective independently with probability 0.03. An inspector examines 20 devices from each of 10 shipments.

1. Find the probability that a particular inspected shipment contains at least one defective device.
2. State the distribution of the number of inspected shipments containing at least one defective device.
3. Find the probability that exactly three shipments contain at least one defective device.

??? answer

    1. For one shipment, \(P(X\ge1)=1-0.97^{20}\approx0.4562\).
    2. Let \(q=1-0.97^{20}\). Then \(Y\sim\operatorname{Binomial}(10,q)\), and \(P(Y=3)={10\choose3}q^3(1-q)^7\approx0.1602\).

#### Exercise 9 — Negative binomial model

Each inspected unit is acceptable independently with probability 0.8. Let \(X\) be the number of units inspected up to and including the fourth acceptable unit.

1. Identify the distribution of \(X\) and state its possible values.
2. Write its PMF.
3. Find \(P(X=6)\) and \(P(X\le6)\).
4. Find \(E[X]\) and \(\operatorname{Var}(X)\).

??? answer

    1. \(X\sim\operatorname{Pascal}(4,0.8)\), with \(R_X=\{4,5,6,\ldots\}\).
    2. \(P(X=k)={k-1\choose3}(0.8)^4(0.2)^{k-4}\), for \(k=4,5,6,\ldots\).
    3. \(P(X=6)=0.16384\) and \(P(X\le6)=0.90112\).
    4. \(E[X]=4/0.8=5\) and \(\operatorname{Var}(X)=4(0.2)/(0.8)^2=1.25\).

#### Exercise 10 — Designing an inspection sample

A company performs inspection on shipments from suppliers to detect nonconforming products. Assume that a lot contains 1,000 items and exactly 10 are nonconforming.

1. Using a binomial model with \(p=0.01\), what sample size is needed so that the probability of selecting at least one nonconforming item is at least 0.90?
2. If the items are sampled without replacement, write the exact hypergeometric probability of selecting at least one nonconforming item in a sample of size \(n\).
3. Find the smallest sample size that gives a probability of at least 0.90 under the hypergeometric model, and compare it with the binomial result.

??? answer

    1. The binomial model requires a sample size of at least 230.
    2. The exact probability is \(1-\frac{{990\choose n}}{{1000\choose n}}\).
    3. The hypergeometric model requires a sample size of at least 205. Sampling without replacement increases the chance of finding a nonconforming item because the lot contains exactly 10 such items.

#### Exercise 11 — Valid PMF

Let

\[
P(X=k)=\frac{c}{3^k},\qquad k=1,2,\ldots
\]

1. Find \(c\) so that this is a valid PMF.
2. Find \(P(X\in\{2,4,6\})\).
3. Find \(P(X\ge3)\).

??? answer

    1. Since \(\sum_{k=1}^{\infty}c/3^k=c/2=1\), \(c=2\).
    2. \(P(X\in\{2,4,6\})=182/729\).
    3. \(P(X\ge3)=1/9\).

The notebook [ex1.ipynb](ex1.ipynb) can be used as a starting point for discrete-distribution calculations.
