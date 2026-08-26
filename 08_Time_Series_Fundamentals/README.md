---
tags:
    - Time Series
    - Stationarity
    - Autocovariance
    - White Noise
    - Random Walk
---

<h1 align="center">Time-Series Fundamentals</h1>

A time series is one observed realisation of a discrete-time stochastic process. We study time dependence through lagged covariance and correlation and distinguish white noise, stationary processes, and random walks. The emphasis is probabilistic structure rather than a catalogue of statistical tests.

Strict and weak stationarity describe whether the law of the process is stable in time. Autocovariance and autocorrelation summarise linear dependence across lags. White noise is uncorrelated; a random walk is not stationary. Plots and sample ACFs are useful, but they mix model properties with sampling variation.

#### Key Concepts

- Realisation versus underlying process
- Strict and weak stationarity
- Autocovariance and autocorrelation
- White noise and random walks
- Sample ACF and its limitations

!!! tip "Learning Objectives"

    - Define strict and weak stationarity.
    - Calculate autocovariance and autocorrelation.
    - Recognise white noise and random-walk behaviour.
    - Use plots and sample ACFs cautiously.

<hr/>

### Session Preparation:

Review covariance and correlation from Session 5 and the distinction between a random variable and a random process from Session 7.

**Syllabus and input**

- [Basic concepts of random processes](https://www.probabilitycourse.com/chapter10/10_1_0_basic_concepts.php)
- [Stationary processes](https://www.probabilitycourse.com/chapter10/10_1_4_stationary_processes.php), through weak-sense stationarity

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

#### Exercise 4 — Dependence without trend

Construct two stationary processes with the same marginal \(N(0,1)\) distribution but different serial dependence. Simulate both and explain why a histogram cannot distinguish them.

#### Exercise 5 — Autocovariance from a short series

For the observations \(x=(2,4,3,7,6,8)\):

1. Calculate the sample mean.
2. Calculate the sample autocovariance at lags 0, 1, and 2 using denominator \(n\).
3. Convert the results to sample autocorrelations.
4. Compare your manual values with a Python implementation and document the denominator convention used by the software.

#### Exercise 6 — Random-phase sinusoid

Let \(X_t=A\cos(\omega t+U)\), where \(U\sim\operatorname{Uniform}(0,2\pi)\).

1. Find \(E[X_t]\).
2. Show that \(\operatorname{Cov}(X_t,X_{t+h})\) depends only on \(h\).
3. Determine whether the process is weakly stationary.
4. Simulate several realisations by drawing a new phase for each realisation.

??? answer

    Integration over the random phase gives \(E[X_t]=0\) and \(\gamma(h)=A^2\cos(\omega h)/2\). Hence the process is weakly stationary.

#### Exercise 7 — Filtering white noise

Let \(X_t=\varepsilon_t+0.6\varepsilon_{t-1}-0.2\varepsilon_{t-2}\), where \(\varepsilon_t\) is white noise with variance \(\sigma^2\).

1. Find the mean and variance of \(X_t\).
2. Find \(\gamma(1)\), \(\gamma(2)\), and \(\gamma(h)\) for \(|h|>2\).
3. Plot the theoretical ACF.
4. Simulate the process and compare its sample ACF with theory.

??? answer

    \(\gamma(0)=(1+0.6^2+0.2^2)\sigma^2=1.4\sigma^2\), \(\gamma(1)=(0.6-0.12)\sigma^2=0.48\sigma^2\), \(\gamma(2)=-0.2\sigma^2\), and later autocovariances are zero.
