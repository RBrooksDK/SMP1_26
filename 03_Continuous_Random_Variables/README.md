---
tags:
    - Continuous Random Variables
    - PDF
    - CDF
    - Expectation
    - Variance
    - Uniform
---

<h1 align="center">Continuous Random Variables I: Foundations</h1>

The ideas from discrete random variables now move from sums to integrals. This session develops the common language used by every continuous model: support, cumulative distribution functions, probability density functions, interval probabilities, expectation, variance, and the law of the unconscious statistician.

A density is not itself a probability. Probabilities are areas obtained by integrating the PDF, while the CDF records the accumulated probability up to a point. The uniform distribution provides a simple running model in which interval probabilities are proportional to interval length.

#### Key Concepts

- Support and the distinction between density and probability
- CDFs, PDFs, and interval probabilities
- Normalising a proposed density
- Expectation, variance, and LOTUS via integrals
- The continuous uniform distribution

!!! tip "Learning Objectives"

    - Validate a PDF and derive a CDF.
    - Recover a PDF from a differentiable CDF.
    - Calculate interval probabilities using either a PDF or a CDF.
    - Calculate expectation and variance using integrals.
    - Use and interpret a continuous uniform model.

<hr/>

### Session Preparation:

Attempt the core exercises from [Session 2](../02_Discrete_Random_Variables/README.md#exercises) and review basic integration from the [prerequisites](../00_Prerequisites/README.md).

**Syllabus and input**

- [Continuous random variables and distributions](https://www.probabilitycourse.com/chapter4/4_1_0_continuous_random_vars_distributions.php)
- [Probability density functions](https://www.probabilitycourse.com/chapter4/4_1_1_pdf.php)
- [Expected value and variance](https://www.probabilitycourse.com/chapter4/4_1_2_expected_val_variance.php)
- [Uniform distribution](https://www.probabilitycourse.com/chapter4/4_2_1_uniform.php)

**Existing course material**

- [Session notes](https://drive.google.com/file/d/1pJzZ3zuWmTWrpJ-tnzG1CE04hdlNwoUN/view?usp=sharing)
- [Recap and exercise notes](https://drive.google.com/file/d/15QrOe1fh9mv6WumlpLBZrV7U8wh_AWvH/view?usp=sharing)
- [Session material](https://viaucdk-my.sharepoint.com/:f:/g/personal/rib_viauc_dk/Ev_P59eY9qJOiDMwGkdri9ABxzovHXJiHdLP432519F7vQ?e=gwTShz)

<hr/>

### Exercises

#### Exercise 1 - Reading a CDF

Let $T$ be the time in hours to complete a job, with

\[
F_T(t)=\begin{cases}0,&t<0,\\ t^2/16,&0\le t\le4,\\1,&t>4.\end{cases}
\]

1. Find $P(T\le1)$.
2. Find $P(T>2)$.
3. Find $P(1\le T\le3)$.
4. Find the PDF of $T$.

??? answer

    The probabilities are $1/16$, $3/4$, and $1/2$. Differentiating the CDF gives $f_T(t)=t/8$ for $0<t<4$, and zero otherwise. Values assigned to the PDF at the endpoints do not affect any probability.

#### Exercise 2 - From PDF to CDF

Let

\[
f(x)=\begin{cases}cx^4,&-1\le x\le1,\\0,&\text{otherwise}.\end{cases}
\]

1. Determine $c$.
2. Derive the CDF on the complete real line.
3. Find $P(-1/2<X<1/2)$, $E[X]$, and $\operatorname{Var}(X)$.

??? answer

    Normalisation gives $c=5/2$. The CDF is

    \[
    F(x)=\begin{cases}
    0,&x<-1,\\
    (x^5+1)/2,&-1\le x\le1,\\
    1,&x>1.
    \end{cases}
    \]

    Symmetry gives $E[X]=0$. Moreover, $P(-1/2<X<1/2)=1/32$ and $\operatorname{Var}(X)=E[X^2]=5/7$.

#### Exercise 3 - A uniform delivery-time model

Suppose a delivery time $X$, measured in minutes, is uniformly distributed on $[10,22]$.

1. Write the PDF and CDF of $X$.
2. Find $P(X\le15)$, $P(12\le X\le18)$, and $P(X=15)$.
3. Find $E[X]$ and $\operatorname{Var}(X)$.

??? answer

    The density is $1/12$ on $[10,22]$, and the CDF is $0$ below 10, $(x-10)/12$ on $[10,22]$, and $1$ above 22. The probabilities are $5/12$, $1/2$, and $0$. The mean is $16$ and the variance is $(22-10)^2/12=12$.

#### Exercise 4 - Exam-time model

The time $X$, in hours, needed to complete an exam has density

\[
f(x)=\begin{cases}q(x^2+x),&0\le x\le3,\\0,&\text{otherwise}.\end{cases}
\]

1. Find $q$ and the CDF.
2. Find the probabilities of finishing before one hour, between one and two hours, and after two hours.
3. Find $E[X]$ and $\operatorname{Var}(X)$.

??? answer

    Normalisation gives $q=2/27$. For $0\le x\le3$,

    \[
    F(x)=\frac{2x^3}{81}+\frac{x^2}{27},
    \]

    with $F(x)=0$ below 0 and $F(x)=1$ above 3. The three probabilities are $5/81$, $23/81$, and $53/81$. Finally, $E[X]=13/6$, $E[X^2]=51/10$, and $\operatorname{Var}(X)=73/180$.

#### Exercise 5 - A symmetric polynomial density

Let

\[
f(x)=\begin{cases}c(1-x^2),&-1<x<1,\\0,&\text{otherwise}.\end{cases}
\]

1. Find $c$.
2. Derive the CDF on the complete real line.
3. Find $P(X\le1/2)$ and $P(X>-1/4)$.
4. Find $E[X]$ and $\operatorname{Var}(X)$, using symmetry where possible.

??? answer

    Normalisation gives $c=3/4$. For $-1\le x\le1$,

    \[
    F(x)=\frac12+\frac{3x}{4}-\frac{x^3}{4},
    \]

    with $F(x)=0$ below $-1$ and $F(x)=1$ above $1$. The probabilities are $27/32$ and $175/256$. Symmetry gives $E[X]=0$, and integration gives $\operatorname{Var}(X)=E[X^2]=1/5$.

#### Exercise 6 - Finite and infinite expectations

For each density, verify that it integrates to one and determine $E[X]$:

1. $f_1(x)=\frac14xe^{-x/2}$, for $x>0$;
2. $f_2(x)=5x^{-2}$, for $x>5$.

Explain why a valid probability distribution need not have a finite mean.

??? answer

    Both densities integrate to one. The first density is Gamma with shape 2 and scale 2, so $E[X]=4$. For the second,

    \[
    \int_5^\infty x(5x^{-2})\,dx=5\int_5^\infty x^{-1}\,dx=\infty.
    \]

    A finite total probability therefore does not guarantee a finite first moment.
