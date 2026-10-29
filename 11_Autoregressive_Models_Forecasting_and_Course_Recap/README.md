---
tags:
    - AR(1)
    - Stationarity
    - Forecasting
    - Model Selection
    - Course Recap
---

<h1 align="center">Autoregressive Models, Forecasting, and Course Recap</h1>

We introduce the AR(1) model as a simple dependent process that can be simulated, analysed, and used for forecasting. Forecasts are conditional distributions, not single guaranteed values. We derive the stationary mean, variance, ACF, multi-step forecast, and forecast uncertainty. The second half of the session connects the models of the course.

Stationarity of AR(1) requires \(|\phi|<1\). Like a Markov chain, an AR(1) process depends on the past only through the current value, so a forecast conditions on the latest observation and steps the recursion forward. Recursive forecasts revert toward the stationary mean, while forecast variance grows with the horizon toward the stationary variance. Updating a forecast after a new observation is just restarting the recursion from the new state.

A Markov chain, a Poisson process, a stationary time series, and a simple random sample answer different questions. The recap practises choosing among them, checking assumptions, and moving between probability rules, distributions, simulation, and process models.

#### Key Concepts

- The AR(1) recursion and its stationarity condition
- Stationary mean, variance, and ACF
- Multi-step conditional means and forecast variance, including forecast updating
- Mean reversion
- Choosing among binomial, Poisson-process, time-series, random-walk, and Markov models

!!! tip "Learning Objectives"

    - Analyse and simulate an AR(1) process.
    - Determine when an AR(1) process is stationary.
    - Calculate and update recursive forecasts and their forecast variance.
    - Choose a model from the course and state the assumptions that make it appropriate.
    - Estimate a probability by Monte Carlo simulation and report uncertainty.

<hr/>

### Session Preparation:

Attempt the core exercises from [Session 10](../10_Time_Series_Fundamentals/README.md#exercises). Be able to calculate covariance, condition on an observed value, and state the Markov property from [Session 8](../08_Markov_Chains/README.md). Identify the two course topics you most need to revisit.

**Syllabus and input**

- [Chapter 11: Autoregressive Models and Forecasting (PDF)](SMP1_26_chapter11_ar_forecasting.pdf){ download }, the main text for the session, with worked examples for the exercises
- [ProbabilityCourse: stationary processes](https://www.probabilitycourse.com/chapter10/10_1_4_stationary_processes.php) as the probability foundation

<hr/>

### Exercises

#### Exercise 1 — AR(1) properties

Let \(X_t=c+\phi X_{t-1}+\varepsilon_t\), where \(\varepsilon_t\) is white noise with variance \(\sigma^2\).

1. State the stationarity condition.
2. Derive the stationary mean and variance.
3. Find the lag-\(h\) autocorrelation.

??? answer

    For \(|\phi|<1\), the mean is \(c/(1-\phi)\), the variance is \(\sigma^2/(1-\phi^2)\), and \(\rho(h)=\phi^{|h|}\).

#### Exercise 2 — Recursive forecast

For \(X_t=2+0.7X_{t-1}+\varepsilon_t\), \(\operatorname{Var}(\varepsilon_t)=4\), and \(X_{20}=10\):

1. Find the one-, two-, and five-step conditional means.
2. Find their forecast variances.
3. Explain the limiting forecast as the horizon increases.

??? answer

    The stationary mean is \(20/3\). The \(h\)-step mean is \(20/3+0.7^h(10-20/3)\), and variance is \(4\sum_{j=0}^{h-1}0.7^{2j}\). Both approach the stationary moments.

#### Exercise 3 — Simulation study

Simulate AR(1) series with \(\phi=-0.8,0,0.8,1\). Compare their paths and sample ACFs. Which cases are stationary, and how does the sign of \(\phi\) appear in the data?

#### Exercise 4 — Forecast distributions

Simulate 5,000 future paths from the AR(1) model in Exercise 2, all starting at \(X_{20}=10\). Compare empirical forecast intervals at horizons 1–10 with the theoretical normal forecast intervals. Discuss how uncertainty changes with the horizon.

#### Exercise 5 — Mean reversion and half-life

For a stationary AR(1) process, deviations from the stationary mean evolve in expectation as \(\phi^h(X_t-\mu)\).

1. Derive the horizon at which the expected deviation has been reduced by one half.
2. Calculate this half-life for \(\phi=0.2,0.6,0.9\).
3. Explain what happens when \(\phi<0\).
4. Simulate the three positive-\(\phi\) cases after the same initial shock.

??? answer

    Solve \(|\phi|^h=1/2\), giving \(h=\log(1/2)/\log|\phi|\). For negative \(\phi\), deviations alternate in sign while their magnitudes decay when \(|\phi|<1\).

#### Exercise 6 — Forecast updating

Suppose \(X_t=5+0.8(X_{t-1}-5)+\varepsilon_t\), with \(\varepsilon_t\sim N(0,1)\), and \(X_{20}=8\).

1. Produce forecasts for times 21–23.
2. At time 21, the observed value is \(X_{21}=6\). Update the forecasts for times 22–23.
3. Compare the original and updated forecasts.
4. Explain which information the innovation at time 21 contributes to later forecasts.

??? answer

    Before observing time 21, the conditional means are \(5+0.8^h(8-5)\). After observing \(X_{21}=6\), restart the recursion from 6, so the new forecasts are \(5+0.8^h(6-5)\) for \(h=1,2\).
### Course recap exercises

#### Exercise 7 — Select the model

For each situation, choose a binomial distribution, Poisson process, stationary time-series model, random walk, or Markov chain. State the assumptions that make the model appropriate and one way the assumptions could fail.

1. Failed requests among 200 independent API calls.
2. Arrival times of support tickets.
3. Hourly CPU load fluctuating around a stable level with serial dependence.
4. A user's movement among pages of an application.
5. A cumulative account balance driven by independent daily shocks.


#### Exercise 8 — Simulation and uncertainty

Choose one model from the course and estimate a non-trivial probability by Monte Carlo simulation. Include:

1. the mathematical model and target probability;
2. reproducible Python code;
3. an analytical result when available;
4. a Monte Carlo standard error;
5. a discussion of model assumptions and limitations.


#### Exercise 9 — One dataset, competing models

An API log records one-minute request counts, mean response times, and a categorical health state for 30 days.

1. Propose a Poisson-process model for the request counts.
2. Propose a stationary time-series model for response time.
3. Propose a Markov-chain model for health state.
4. State two assumptions for each model and design one diagnostic check for each assumption.
5. Explain why the three variables should not automatically be modelled independently.


#### Exercise 10 — Integrated probability calculation

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
