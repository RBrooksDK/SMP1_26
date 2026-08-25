# 03 — Continuous Random Variables

## Session preparation

Attempt the core exercises from [Session 2](../02_Discrete_Random_Variables/README.md#exercises) and review basic integration from the [prerequisites](../00_Prerequisites/README.md).

**Syllabus and input**

- [Continuous random variables and distributions](https://www.probabilitycourse.com/chapter4/4_1_0_continuous_random_vars_distributions.php)
- [Functions of a continuous random variable](https://www.probabilitycourse.com/chapter4/4_1_3_functions_continuous_var.php)
- [Uniform distribution](https://www.probabilitycourse.com/chapter4/4_2_1_uniform.php)
- [Exponential distribution](https://www.probabilitycourse.com/chapter4/4_2_2_exponential.php)
- [Normal distribution](https://www.probabilitycourse.com/chapter4/4_2_3_normal.php)

**Existing course material**

- [Recap notes](https://drive.google.com/file/d/1bfSGEXCjWAhseYAkICVakgEmtgMJUtBy/view?usp=sharing)
- [Session notes, part 1](https://drive.google.com/file/d/1-MKzwovM7uHrSUQ_XBe1NczVT2ssdbKd/view?usp=sharing)
- [Session material](https://viaucdk-my.sharepoint.com/:f:/g/personal/rib_viauc_dk/Ev_P59eY9qJOiDMwGkdri9ABxzovHXJiHdLP432519F7vQ?e=gwTShz)

---

## Session focus

The ideas from discrete variables are transferred from sums to integrals. We work with PDFs, CDFs, expectation, variance, transformations, and the uniform, exponential, and normal distributions.

By the end of the session, you should be able to:

- validate a PDF and derive a CDF;
- calculate interval probabilities, expectation, and variance using integrals;
- select and interpret common continuous models;
- transform a single continuous random variable.

---

## Exercises

#### Exercise 1 — Reading a CDF

Let \(T\) be the time in hours to complete a job, with

\[
F_T(t)=\begin{cases}0,&t<0,\\ t^2/16,&0\le t\le4,\\1,&t>4.\end{cases}
\]

1. Find \(P(T\le1)\).
2. Find \(P(T>2)\).
3. Find \(P(1\le T\le3)\).
4. Find the PDF of \(T\).

??? answer

    The probabilities are \(1/16\), \(3/4\), and \(1/2\). Differentiating the CDF gives \(f_T(t)=t/8\) for \(0<t<4\), and zero otherwise.

#### Exercise 2 — From PDF to CDF

Let

\[
f(x)=\begin{cases}cx^4,&-1\le x\le1,\\0,&\text{otherwise}.\end{cases}
\]

1. Determine \(c\).
2. Derive the CDF.
3. Find \(P(-1/2<X<1/2)\), \(E[X]\), and \(\operatorname{Var}(X)\).

??? answer

    Normalisation gives \(c=5/2\). On \([-1,1]\), \(F(x)=(x^5+1)/2\). Symmetry gives \(E[X]=0\); \(P(-1/2<X<1/2)=1/32\), and \(\operatorname{Var}(X)=E[X^2]=5/7\).

#### Exercise 3 — Counts and waiting times

A server receives requests according to a rate of 25 requests per second.

1. Find the probability of no requests in 10 ms.
2. Find the probability of more than two requests in 10 ms.
3. Let \(T\) be the time between requests. Find \(P(T\le0.01)\) and \(P(T>0.1)\).

??? answer

    Counts over 0.01 seconds are \(\operatorname{Poisson}(0.25)\). Waiting time is \(\operatorname{Exponential}(25)\), so the last two answers are \(1-e^{-0.25}\) and \(e^{-2.5}\).

#### Exercise 4 — Exam-time model

The time \(X\), in hours, needed to complete an exam has density

\[
f(x)=\begin{cases}q(x^2+x),&0\le x\le3,\\0,&\text{otherwise}.\end{cases}
\]

1. Find \(q\) and the CDF.
2. Find the probabilities of finishing before one hour, between one and two hours, and after two hours.
3. Find \(E[X]\) and \(\operatorname{Var}(X)\).

??? answer

    Normalisation gives \(q=2/27\). For \(0\le x\le3\), \(F(x)=\frac{2}{27}(x^3/3+x^2/2)\). Use this CDF for the interval probabilities and integration for the moments.

#### Exercise 5 — A symmetric polynomial density

Let

\[
f(x)=\begin{cases}c(1-x^2),&-1<x<1,\\0,&\text{otherwise}.\end{cases}
\]

1. Find \(c\).
2. Derive the CDF on the complete real line.
3. Find \(P(X\le1/2)\) and \(P(X>-1/4)\).
4. Find \(E[X]\) and \(\operatorname{Var}(X)\), using symmetry where possible.

??? answer

    Normalisation gives \(c=3/4\). Symmetry gives \(E[X]=0\), and integration gives \(E[X^2]=1/5\). On \([-1,1]\), integrate \((3/4)(1-t^2)\) from \(-1\) to \(x\) to obtain the CDF.

#### Exercise 6 — Finite and infinite expectations

For each density, verify that it integrates to one and determine \(E[X]\):

1. \(f_1(x)=\frac14xe^{-x/2}\), for \(x>0\);
2. \(f_2(x)=5x^{-2}\), for \(x>5\).

Explain why a valid probability distribution need not have a finite mean.

??? answer

    The first density is Gamma with shape 2 and scale 2, so \(E[X]=4\). For the second, \(\int_5^\infty x(5x^{-2})\,dx=5\int_5^\infty x^{-1}\,dx=\infty\).

#### Exercise 7 — Memorylessness

The lifetime \(T\) of a component is exponentially distributed with mean 500 hours.

1. Find \(P(T>600)\).
2. Given that the component has survived 400 hours, find \(P(T>600\mid T>400)\).
3. Compare part 2 with the probability that a new component survives 200 hours.
4. Simulate 100,000 lifetimes and verify the memoryless property empirically.

??? answer

    The rate is \(1/500\). The answers are \(e^{-600/500}\) and \(e^{-200/500}\). The latter equals \(P(T>200)\), illustrating memorylessness.
