# 09 — Autoregressive Models and Probabilistic Forecasting

## Session preparation

Attempt the core exercises from [Session 8](../08_Time_Series_Fundamentals/README.md#exercises). Be able to calculate covariance and condition on an observed value.

**Syllabus and input**

- [ProbabilityCourse: stationary processes](https://www.probabilitycourse.com/chapter10/10_1_4_stationary_processes.php) as the probability foundation
- Session notes on autoregressive models, recursive forecasting, and forecast distributions

---

## Session focus

We introduce the AR(1) model as a simple dependent process that can be simulated, analysed, and used for forecasting. Forecasts are conditional distributions, not single guaranteed values. We derive the stationary mean, variance, ACF, multi-step forecast, and forecast uncertainty.

By the end of the session, you should be able to analyse and simulate an AR(1) process, determine when it is stationary, calculate recursive forecasts and forecast variance, and evaluate assumptions using residuals.

---

## Exercises

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

Simulate 5,000 future paths from a fitted AR(1) model starting at the same final observation. Compare empirical forecast intervals at horizons 1–10 with the theoretical normal forecast intervals. Discuss how uncertainty changes with the horizon.

#### Exercise 5 — Mean reversion and half-life

For a stationary AR(1) process, deviations from the stationary mean evolve in expectation as \(\phi^h(X_t-\mu)\).

1. Derive the horizon at which the expected deviation has been reduced by one half.
2. Calculate this half-life for \(\phi=0.2,0.6,0.9\).
3. Explain what happens when \(\phi<0\).
4. Simulate the three positive-\(\phi\) cases after the same initial shock.

??? answer

    Solve \(|\phi|^h=1/2\), giving \(h=\log(1/2)/\log|\phi|\). For negative \(\phi\), deviations alternate in sign while their magnitudes decay when \(|\phi|<1\).

#### Exercise 6 — Estimating an AR(1) coefficient

For the centred observations

\[
x=(-1.2,-0.7,-0.4,0.1,0.5,0.3,0.8,0.6),
\]

1. Estimate \(\phi\) by regressing \(x_t\) on \(x_{t-1}\) without an intercept.
2. Calculate the fitted innovations.
3. Estimate the innovation variance.
4. Compare the estimated \(\phi\) with the lag-1 sample autocorrelation and explain why they need not be identical in a short sample.

#### Exercise 7 — Forecast updating

Suppose \(X_t=5+0.8(X_{t-1}-5)+\varepsilon_t\), with \(\varepsilon_t\sim N(0,1)\), and \(X_{20}=8\).

1. Produce forecasts for times 21–23.
2. At time 21, the observed value is \(X_{21}=6\). Update the forecasts for times 22–23.
3. Compare the original and updated forecasts.
4. Explain which information the innovation at time 21 contributes to later forecasts.

??? answer

    Before observing time 21, the conditional means are \(5+0.8^h(8-5)\). After observing \(X_{21}=6\), restart the recursion from 6, so the new forecasts are \(5+0.8^h(6-5)\) for \(h=1,2\).
