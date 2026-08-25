# 06 — Random Sampling, Monte Carlo, and Limit Theorems

## Session preparation

Attempt the core exercises from [Session 5](../05_Conditional_Distributions_and_Dependence/README.md#exercises).

**Syllabus and input**

- [Random sampling](https://www.probabilitycourse.com/chapter8/8_1_1_random_sampling.php)
- [Law of Large Numbers](https://www.probabilitycourse.com/chapter7/7_1_1_law_of_large_numbers.php)
- [Central Limit Theorem](https://www.probabilitycourse.com/chapter7/7_1_2_central_limit_theorem.php)
- [Chapter 14: simulation using Python](https://www.probabilitycourse.com/chapter14/Chapter_14.pdf), selected sections

---

## Session focus

Random sampling connects probability models to computation. We use Python to generate i.i.d. samples, construct Monte Carlo estimates, and study their uncertainty. The LLN explains consistency; the CLT explains the approximate shape and scale of simulation error.

By the end of the session, you should be able to generate random samples, construct Monte Carlo estimators, calculate the mean and variance of a sample mean, and use the LLN and CLT appropriately.

---

## Exercises

#### Exercise 1 — Sampling distribution

Water samples have mean sulfate content \(7.48\) mg/L and standard deviation \(1.60\) mg/L. For an independent sample of size 10:

1. Find the mean and standard deviation of the sample mean.
2. Assuming normal observations, find \(P(6.49<\bar X<8.47)\).
3. Simulate the experiment and compare with the theoretical probability.

??? answer

    \(E[\bar X]=7.48\) and \(\operatorname{SD}(\bar X)=1.60/\sqrt{10}\). Standardise the two bounds using this standard deviation. A large simulation should agree up to Monte Carlo error.

#### Exercise 2 — CLT and sample size

Tree counts have mean 19.86 and standard deviation 23.65.

1. Find the standard error for sample sizes 8, 30, and 100.
2. Explain why the normal approximation is questionable for \(n=8\) if the population is strongly right-skewed.
3. Simulate a skewed distribution with the same approximate mean and compare the three sample-mean distributions.

#### Exercise 3 — Aggregate counts

Daily accident counts are independent \(\operatorname{Poisson}(10)\). Use the CLT to approximate the probability of more than 3800 accidents in 365 days. Compare with a simulation.

??? answer

    The annual sum has mean and variance 3650. With continuity correction, approximate \(P(S\ge3801)\) by \(P\bigl(Z>(3800.5-3650)/\sqrt{3650}\bigr)\).

#### Exercise 4 — Monte Carlo area

Estimate \(\pi\) by sampling points uniformly in \([-1,1]^2\). Report the estimate and an estimated Monte Carlo standard error for \(n=10^2,10^3,10^4,10^5\). Explain the observed \(1/\sqrt n\) rate.

#### Exercise 5 — Reproducible simulation

Estimate \(E[e^U]\) for \(U\sim\operatorname{Uniform}(0,1)\). Use a fixed random seed, state the estimator, compare with the exact value \(e-1\), and construct a plot of cumulative estimates against sample size.

#### Exercise 6 — Law of Large Numbers in action

Let \(X_i\) be independent Bernoulli variables with \(P(X_i=1)=0.3\).

1. Plot the running mean \(\bar X_n\) for \(n=1,\ldots,10{,}000\).
2. Repeat the experiment for 100 independent runs and compare the spread at \(n=10,100,1000,10{,}000\).
3. Estimate \(P(|\bar X_n-0.3|>0.02)\) for each sample size.
4. Explain what the LLN does and does not say about any single finite sample.

#### Exercise 7 — Sample means from a uniform population

Let \(X_1,\ldots,X_n\) be independent \(\operatorname{Uniform}(0,1)\) variables.

1. Find \(E[\bar X_n]\) and \(\operatorname{Var}(\bar X_n)\).
2. Use the CLT to approximate \(P(0.45<\bar X_{30}<0.55)\).
3. Simulate the sampling distribution for \(n=2,10,30\).
4. Compare the approximation with simulation and explain the effect of \(n\).

??? answer

    \(E[\bar X_n]=1/2\) and \(\operatorname{Var}(\bar X_n)=1/(12n)\). Standardise the bounds using standard error \(1/\sqrt{12n}\).

#### Exercise 8 — Accuracy of a rare-event estimate

Suppose a simulation estimates a probability \(p\approx0.001\) using the average of independent event indicators.

1. Find the approximate standard error when \(n=10^4,10^5,10^6\).
2. How large must \(n\) be for the standard error to be at most \(10^{-4}\)?
3. Simulate the estimator repeatedly and inspect the number of runs producing no observed events.
4. Explain why a large general-purpose sample size may still be inadequate for rare events.

??? answer

    The standard error is \(\sqrt{p(1-p)/n}\). Requiring it to be at most \(10^{-4}\) gives \(n\ge p(1-p)/10^{-8}\approx99{,}900\).
