---
tags:
    - Continuous Random Variables
    - Transformations
    - Exponential
    - Normal
    - Memorylessness
---

<h1 align="center">Continuous Random Variables II: Models and Transformations</h1>

This session builds on PDFs, CDFs, and moments by transforming continuous random variables and selecting models that fit common stories. The exponential distribution describes waiting times, while the normal distribution describes symmetric variation and later provides the reference model for the central limit theorem.

For a transformation $Y=g(X)$, first determine the possible values of $Y$. The CDF method is the safest general starting point, while the change-of-variables formula is efficient when $g$ is differentiable and monotone. For named distributions, the parameter and its units must be interpreted as part of the model.

#### Key Concepts

- Support under a transformation
- The CDF method and monotone change of variables
- Exponential waiting times and memorylessness
- Normal models, standardisation, and the standard normal CDF
- Model selection and interpretation of parameters

!!! tip "Learning Objectives"

    - Find the distribution of a monotone transformation of one continuous random variable.
    - Calculate and interpret exponential waiting-time probabilities.
    - Apply the memoryless property appropriately.
    - Standardise a normal random variable and calculate probabilities and quantiles.
    - Distinguish uniform, exponential, and normal modelling assumptions.

<hr/>

### Session Preparation:

Attempt the core exercises from [Session 3](../03_Continuous_Random_Variables/README.md#exercises). In particular, be comfortable moving between PDFs and CDFs and calculating expectation by integration.

**Syllabus and input**

- [Functions of a continuous random variable](https://www.probabilitycourse.com/chapter4/4_1_3_functions_continuous_var.php)
- [Exponential distribution](https://www.probabilitycourse.com/chapter4/4_2_2_exponential.php)
- [Normal distribution](https://www.probabilitycourse.com/chapter4/4_2_3_normal.php)

**Existing course material**

- [Session notes](https://drive.google.com/file/d/1FiEaxaq-pDUw7vvVdzoD_SsxRCY5z1lw/view?usp=sharing)
- [Recap and exercise notes](https://drive.google.com/file/d/1G7XfakWQwW6NklFLE7GY2WWV9Lp-WIXh/view?usp=sharing)
- [Session material](https://viaucdk-my.sharepoint.com/:f:/g/personal/rib_viauc_dk/Ev_P59eY9qJOiDMwGkdri9ABxzovHXJiHdLP432519F7vQ?e=gwTShz)

<hr/>

### Exercises

#### Exercise 1 - A transformation

Let

\[
f_X(x)=\begin{cases}\frac{5}{32}x^4,&0\le x\le2,\\0,&\text{otherwise},\end{cases}
\qquad Y=X^2.
\]

1. Find the support and CDF of $Y$.
2. Find the PDF of $Y$.
3. Find $E[Y]$ directly using LOTUS and by integrating with the PDF of $Y$.

??? answer

    The support is $[0,4]$. For $0\le y\le4$,

    \[
    F_Y(y)=P(X\le\sqrt y)=\frac{y^{5/2}}{32},
    \qquad
    f_Y(y)=\frac{5y^{3/2}}{64}.
    \]

    The CDF is zero below 0 and one above 4; the PDF is zero outside $[0,4]$. Both expectation calculations give $E[Y]=E[X^2]=20/7$.

#### Exercise 2 - Counts and waiting times

A server receives requests according to a rate of 25 requests per second.

1. Find the probability of no requests in 10 ms.
2. Find the probability of more than two requests in 10 ms.
3. Let $T$ be the time between requests. Find $P(T\le0.01)$ and $P(T>0.1)$.
4. Find the mean and standard deviation of $T$, in seconds.

??? answer

    Counts over 0.01 seconds have a $\operatorname{Poisson}(0.25)$ distribution. Thus $P(N=0)=e^{-0.25}$ and

    \[
    P(N>2)=1-e^{-0.25}\left(1+0.25+\frac{0.25^2}{2}\right).
    \]

    The waiting time is $\operatorname{Exponential}(25)$, so the next two probabilities are $1-e^{-0.25}$ and $e^{-2.5}$. Both the mean and standard deviation are $1/25=0.04$ seconds.

#### Exercise 3 - Memorylessness

The lifetime $T$ of a component is exponentially distributed with mean 500 hours.

1. Find $P(T>600)$.
2. Given that the component has survived 400 hours, find $P(T>600\mid T>400)$.
3. Compare part 2 with the probability that a new component survives 200 hours.
4. Simulate 100,000 lifetimes and verify the memoryless property empirically.

??? answer

    The rate is $1/500$. The answers to the first two parts are $e^{-600/500}=e^{-1.2}$ and $e^{-(600-400)/500}=e^{-0.4}$. The second probability equals $P(T>200)$, illustrating memorylessness. In the simulation, compare the proportion exceeding 600 among observations already exceeding 400 with the overall proportion exceeding 200.

#### Exercise 4 - Normal probabilities and a quantile

Suppose $X\sim N(100,10^2)$.

1. Find $P(X\le85)$.
2. Find $P(90\le X\le115)$.
3. Find the 95th percentile of $X$.
4. State clearly whether your table or software returns $P(Z\le z)$ or the area between $0$ and $z$.

??? answer

    Standardisation gives $z=-1.5$ in part 1, so the probability is approximately $0.0668$. Part 2 is

    \[
    \Phi(1.5)-\Phi(-1)=0.9332-0.1587=0.7745.
    \]

    With $z_{0.95}\approx1.6449$, the 95th percentile is $100+10(1.6449)\approx116.45$. The stated convention must agree with the values used; throughout these exercises, $\Phi(z)=P(Z\le z)$.

#### Exercise 5 - Choosing a continuous model

For each situation, choose a uniform, exponential, or normal model and explain the decisive assumption.

1. A position is selected at random along a two-metre cable, with equal-length segments equally likely.
2. Requests arrive independently at a constant average rate, and $X$ is the waiting time to the next request.
3. A measurement error is the combined effect of many small, roughly symmetric disturbances.
4. Explain one reason why each selected model could fail in practice.

??? answer

    The natural choices are uniform, exponential, and normal, respectively. The decisive assumptions are equal probability per unit length, a constant event rate with memoryless waiting time, and approximately symmetric additive variation. The models can fail if positions are spatially biased, arrival rates vary or arrivals interact, or the errors are skewed, heavy-tailed, bounded, or affected by outliers.
