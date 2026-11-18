---
tags:
    - Time Series
    - Stationarity
    - Autocovariance
    - White Noise
    - Random Walk
---

<h1 align="center">Time-Series Fundamentals</h1>

A time series is one observed realisation of a discrete-time stochastic process. As with the Markov chains of the previous sessions, we ask how the process depends on its past, but now we summarise that dependence through the mean function and the autocovariance and autocorrelation across lags. Two basic models serve as contrasting examples: white noise and the random walk.

Weak stationarity requires a constant mean and an autocovariance that depends only on the lag. White noise is stationary; a random walk is not, because its variance grows with time. A plot or a sample ACF of a single realisation mixes model properties with sampling variation, so it should be read with care.

#### Key Concepts

- Realisation versus underlying process
- Mean function, autocovariance, and autocorrelation
- Weak stationarity
- White noise and random walks
- Sample ACF and its limitations

!!! tip "Learning Objectives"

    - Define weak stationarity and check it for a simple model.
    - Calculate the mean function, autocovariance, and autocorrelation of a simple model.
    - Recognise white-noise and random-walk behaviour.
    - Calculate and interpret a sample ACF with caution.

<hr/>

### Session Preparation:

Review covariance and correlation from [Session 5](../05_Joint_Distributions_and_Dependence/README.md), stochastic processes and sample paths from [Session 7](../07_Stochastic_Processes_and_Poisson_Processes/README.md), and the stationary distribution of a Markov chain from [Session 9](../09_Markov_Chains_Long_Run_Behaviour/README.md). Stationarity of a time series asks a related question: when does the law of the process not change over time?

**Syllabus and input**

- [Chapter 10: Time-Series Fundamentals (PDF)](SMP1_26_chapter10_time_series.pdf){ download }, the main text for the session, with worked examples for the exercises
- [ProbabilityCourse 10.1.2: mean and correlation functions](https://www.probabilitycourse.com/chapter10/10_1_2_mean_and_correlation_functions.php)
- [ProbabilityCourse 10.1.4: stationary processes](https://www.probabilitycourse.com/chapter10/10_1_4_stationary_processes.php), through weak-sense stationarity

<hr/>

### Exercises

#### Exercise 1 — Classify the process

Let \(\varepsilon_t\) be i.i.d. with mean 0 and variance \(\sigma^2\). For each process, decide whether it is weakly stationary and justify your answer:

1. \(X_t=5+\varepsilon_t\)
2. \(X_t=t+\varepsilon_t\)
3. \(X_t=X_{t-1}+\varepsilon_t\), with \(X_0=0\)

??? answer

    The first is stationary white noise around mean 5. The second has a time-varying mean. The third has variance \(t\sigma^2\); neither of the last two is weakly stationary.

#### Exercise 2 — An MA(1) process

Let \(X_t=\varepsilon_t+\theta\varepsilon_{t-1}\).

1. Find its mean and variance.
2. Find \(\gamma(h)=\operatorname{Cov}(X_t,X_{t-h})\) for all lags.
3. Find the autocorrelation function.

??? answer

    The mean is 0 and variance is \((1+\theta^2)\sigma^2\). The autocovariance is \(\theta\sigma^2\) at lags \(\pm1\) and zero for \(|h|>1\). Divide by the variance to obtain the ACF.

#### Exercise 3 — Realisation versus model

Simulate 300 observations of white noise and of a random walk. For each, plot the series, rolling mean, rolling variance, and sample ACF. Explain which visual patterns are model properties and which may simply be sampling variation.

#### Exercise 4 — Autocovariance from a short series

For the observations \(x=(2,4,3,7,6,8)\):

1. Calculate the sample mean.
2. Calculate the sample autocovariance at lags 0, 1, and 2 using denominator \(n\).
3. Convert the results to sample autocorrelations.
4. Compare your manual values with a Python implementation and document the denominator convention used by the software.

??? answer

    The sample mean is 5. With denominator \(n=6\), \(\hat\gamma(0)=28/6\approx4.667\), \(\hat\gamma(1)=6/6=1\), and \(\hat\gamma(2)=8/6\approx1.333\), so \(\hat\rho(1)=6/28\approx0.214\) and \(\hat\rho(2)=8/28\approx0.286\). `statsmodels.tsa.stattools.acf` uses denominator \(n\) and the overall mean; `pandas.Series.autocorr` computes a Pearson correlation on the overlapping pairs and therefore gives different values.
