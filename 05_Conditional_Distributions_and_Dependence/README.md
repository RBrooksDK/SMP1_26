# 05 — Conditional Distributions and Dependence

## Session preparation

Attempt the core exercises from [Session 4](../04_Joint_Distributions/README.md#exercises).

**Syllabus and input**

- [Conditional expectation](https://www.probabilitycourse.com/chapter5/5_1_5_conditional_expectation.php)
- [Conditioning and independence for continuous random variables](https://www.probabilitycourse.com/chapter5/5_2_3_conditioning_independence.php)
- [Functions of two continuous random variables](https://www.probabilitycourse.com/chapter5/5_2_4_functions.php)
- [Covariance and correlation](https://www.probabilitycourse.com/chapter5/5_3_1_covariance_correlation.php)
- [Sums of random variables](https://www.probabilitycourse.com/chapter6/6_1_2_sums_random_variables.php)

**Existing course material**

- [Recap exercises](https://drive.google.com/file/d/15LXt_ODdG0qUIhZmrPiXvwHjChZpQwCH/view?usp=sharing)
- [Session notes](https://drive.google.com/file/d/1oUHWdzQZa62bTqsmLe_eRts7OpOEhFgJ/view?usp=sharing)
- [Session material](https://viaucdk-my.sharepoint.com/:f:/g/personal/rib_viauc_dk/EnYOFBJCZ-hNtWAfipCS0pUB6xsNt8lOW1fDyq_l_vNqUg?e=BSqiaH)

---

## Session focus

This session develops the quantitative tools for dependence. Conditional expectation summarises how one variable changes with another, while covariance and correlation describe linear dependence. Transformations and sums connect joint probability to later work with sampling, time series, and stochastic processes.

By the end of the session, you should be able to:

- calculate and interpret conditional expectation and variance;
- apply the laws of total expectation and total variance;
- calculate covariance and correlation and explain their limitations;
- obtain distributions or moments of transformations and sums.

---

## Exercises

#### Exercise 1 — Conditional moments

Continue with the uniform model on

\[
C=\{(x,y)\mid x,y\in\mathbb Z,\ x^2+|y|\le2\}.
\]

1. Find \(E[XY^2]\).
2. Find \(E[X\mid Y=1]\) and \(\operatorname{Var}(X\mid Y=1)\).
3. Find \(E[X\mid |Y|\le1]\) and \(E[X^2\mid |Y|\le1]\).

??? answer

    Symmetry gives \(E[XY^2]=0\). Given \(Y=1\), \(X\) is uniform on \(\{-1,0,1\}\), so the conditional mean is 0 and the variance is \(2/3\). Conditioning on \(|Y|\le1\) gives a uniform \(3\times3\) grid; the last two answers are 0 and \(2/3\).

#### Exercise 2 — Conditional density

Suppose

\[
f_{Y\mid X}(y\mid x)=xe^{-xy},\qquad y>0.
\]

1. Find \(P(Y<2\mid X=2)\).
2. Find \(E[Y\mid X=2]\).

??? answer

    Given \(X=2\), \(Y\sim\operatorname{Exponential}(2)\). The answers are \(1-e^{-4}\) and \(1/2\).

#### Exercise 3 — Transformation

Let

\[
f_X(x)=\begin{cases}\frac{5}{32}x^4,&0\le x\le2,\\0,&\text{otherwise},\end{cases}
\qquad Y=X^2.
\]

1. Find the CDF of \(Y\).
2. Find the PDF of \(Y\).
3. Find \(E[Y]\) directly and by using \(E[X^2]\).

??? answer

    For \(0\le y\le4\), \(F_Y(y)=y^{5/2}/32\) and \(f_Y(y)=5y^{3/2}/64\). Both approaches give \(E[Y]=20/7\).

#### Exercise 4 — Covariance and correlation

The joint PMF is:

|  | \(Y=0\) | \(Y=1\) | \(Y=2\) |
| --- | ---: | ---: | ---: |
| \(X=0\) | \(1/6\) | \(1/4\) | \(1/8\) |
| \(X=1\) | \(1/8\) | \(1/6\) | \(1/6\) |

1. Find \(\operatorname{Cov}(X,Y)\).
2. Find \(\rho(X,Y)\).
3. Explain why a small correlation does not imply independence.

??? answer

    \(E[X]=11/24\), \(E[Y]=1\), and \(E[XY]=1/2\), so \(\operatorname{Cov}(X,Y)=1/24\). The correlation is \(2\sqrt3/\sqrt{1001}\approx0.1095\). The joint PMF still differs from the product of the marginals.

#### Exercise 5 — Sums and simulation

Let \(X_1,\ldots,X_n\) have common mean \(\mu\), variance \(\sigma^2\), and pairwise covariance \(c\). Define \(S_n=\sum_iX_i\).

1. Find \(E[S_n]\) and \(\operatorname{Var}(S_n)\).
2. What changes when the variables are independent?
3. Simulate both an independent and a positively correlated example in Python and compare the spread of \(S_n\).

??? answer

    \(E[S_n]=n\mu\) and \(\operatorname{Var}(S_n)=n\sigma^2+n(n-1)c\). Independence sets \(c=0\), giving variance \(n\sigma^2\). Positive dependence makes the sum substantially more variable.

#### Exercise 6 — Covariance after transformation

Let \(X\) and \(Y\) be independent standard normal random variables and define

\[
Z=11-X+X^2Y,\qquad W=3-Y.
\]

1. Expand \(\operatorname{Cov}(Z,W)\) using linearity.
2. Identify which terms vanish because of independence or zero means.
3. Find \(\operatorname{Cov}(Z,W)\).
4. Explain why the nonlinear term \(X^2Y\) still contributes.

??? answer

    Constants contribute nothing. Independence gives \(\operatorname{Cov}(X,Y)=0\), while \(\operatorname{Cov}(X^2Y,Y)=E[X^2]E[Y^2]=1\). Because \(W=3-Y\), \(\operatorname{Cov}(Z,W)=-1\).

#### Exercise 7 — Total expectation and total variance

A request is routed to a fast server with probability 0.7 and a slow server with probability 0.3. Conditional response times are exponential with means 20 ms and 80 ms, respectively. Let \(T\) be the response time and \(S\) the selected server.

1. Find \(E[T\mid S]\) and \(\operatorname{Var}(T\mid S)\).
2. Use the law of total expectation to find \(E[T]\).
3. Use the law of total variance to find \(\operatorname{Var}(T)\).
4. Find \(P(S=\text{slow}\mid T>100)\).

??? answer

    \(E[T]=0.7(20)+0.3(80)=38\) ms. Use \(\operatorname{Var}(T)=E[\operatorname{Var}(T\mid S)]+\operatorname{Var}(E[T\mid S])\). Bayes' rule gives \(P(S=\text{slow}\mid T>100)=\frac{0.3e^{-100/80}}{0.7e^{-100/20}+0.3e^{-100/80}}\).

#### Exercise 8 — Sum of two uniforms

Let \(X\) and \(Y\) be independent \(\operatorname{Uniform}(0,1)\) variables and define \(S=X+Y\).

1. Derive the PDF of \(S\) by convolution.
2. Derive the CDF of \(S\) geometrically from the unit square.
3. Find \(P(0.5<S<1.5)\).
4. Simulate \(S\) and compare its histogram with the theoretical PDF.

??? answer

    The PDF is \(f_S(s)=s\) for \(0<s<1\), \(f_S(s)=2-s\) for \(1\le s<2\), and zero otherwise. Symmetry gives \(P(0.5<S<1.5)=3/4\).
