---
tags:
    - Joint Distributions
    - Marginal Distributions
    - Conditional Distributions
    - Independence
---

<h1 align="center">Joint Distributions</h1>

A single random variable describes one aspect of an experiment. Joint distributions describe several quantities simultaneously and make dependence visible. We construct joint, marginal, and conditional distributions in both discrete and continuous settings.

A joint PMF or joint PDF must be validated, then summed or integrated to obtain marginals. Conditioning restricts attention to a slice of the joint model. Independence means the joint factors into a product of marginals; a glance at the support or at a table of zeros is often enough to rule it out. Probabilities over regions in the plane are areas or sums over the corresponding cells.

#### Key Concepts

- Joint PMFs and joint PDFs
- Marginal and conditional distributions
- Probabilities over two-dimensional regions
- Independence of two random variables
- Discrete tables and continuous supports

!!! tip "Learning Objectives"

    - Validate and use a joint PMF or joint PDF.
    - Derive marginal and conditional distributions.
    - Calculate probabilities over regions in two dimensions.
    - Determine whether two random variables are independent.

<hr/>

### Session Preparation:

Attempt the core exercises from [Session 3](../03_Continuous_Random_Variables/README.md#exercises).

**Syllabus and input**

- [Introduction to joint distributions](https://www.probabilitycourse.com/chapter5/5_1_0_joint_distributions.php)
- Discrete joint distributions: [joint PMF](https://www.probabilitycourse.com/chapter5/5_1_1_joint_pmf.php), [joint CDF](https://www.probabilitycourse.com/chapter5/5_1_2_joint_cdf.php), and [conditioning and independence](https://www.probabilitycourse.com/chapter5/5_1_3_conditioning_independence.php)
- Continuous joint distributions: [joint PDF](https://www.probabilitycourse.com/chapter5/5_2_1_joint_pdf.php), [joint CDF](https://www.probabilitycourse.com/chapter5/5_2_2_joint_cdf.php), and [conditioning and independence](https://www.probabilitycourse.com/chapter5/5_2_3_conditioning_independence.php)

**Existing course material**

- [Recap notes](https://drive.google.com/file/d/11-lAHXLQO_PRv2xqHwjoZv66-PY9X-9x/view?usp=sharing)
- [Session notes](https://drive.google.com/file/d/1oUHWdzQZa62bTqsmLe_eRts7OpOEhFgJ/view?usp=sharing)
- [Session material](https://viaucdk-my.sharepoint.com/:f:/g/personal/rib_viauc_dk/EoKqqy67NdBBk7Qnug21TH4BXHHtg2jlNNSF45_H9n7feg?e=3dBknY)

<hr/>

### Exercises

#### Exercise 1 — Joint PMF table

The joint PMF of \(X\) and \(Y\) is:

| \(y\backslash x\) | 1 | 2 | 3 |
| --- | ---: | ---: | ---: |
| 5 | \(1/12\) | 0 | 0 |
| 6 | \(2/12\) | 0 | \(2/12\) |
| 7 | \(2/12\) | \(1/12\) | \(2/12\) |
| 8 | 0 | \(2/12\) | 0 |

1. Find the marginal PMFs of \(X\) and \(Y\).
2. Find \(E[X]\), \(E[Y]\), and \(E[XY]\).
3. Determine whether \(X\) and \(Y\) are independent.
4. Find \(p_{X\mid Y}(x\mid6)\).

??? answer

    \(p_X=(5/12,3/12,4/12)\) and \(p_Y=(1/12,4/12,5/12,2/12)\) for the listed values. Moreover, \(E[X]=23/12\), \(E[Y]=20/3\), and \(E[XY]=155/12\). The variables are not independent. Given \(Y=6\), \(X=1\) and \(X=3\) each have probability \(1/2\).

#### Exercise 2 — Probability as area

Choose \((A,B)\) uniformly in the unit square. What is the probability that

\[
AX^2+X+B=0
\]

has real solutions?

<div style="text-align: center;">
  <img src="src/ex7.png" width="220" alt="Unit square for Exercise 2">
</div>

??? answer

    The discriminant condition is \(1-4AB\ge0\). The required area is \(\frac14+\frac14\ln4\approx0.5966\). See the [extended solution](src/Solution7.pdf).

#### Exercise 3 — A finite joint model

Let

\[
C=\{(x,y)\mid x,y\in\mathbb Z,\ x^2+|y|\le2\},
\]

and choose \((X,Y)\) uniformly from \(C\).

1. List the points in \(C\).
2. Construct the joint and marginal PMFs.
3. Find the conditional PMF of \(X\) given \(Y=1\).
4. Determine whether \(X\) and \(Y\) are independent.

??? answer

    There are 11 points: five with \(x=0\) and three for each of \(x=-1\) and \(x=1\). Each has probability \(1/11\). Given \(Y=1\), \(X\) is uniform on \(\{-1,0,1\}\). The variables are not independent because the possible values of \(Y\) depend on \(X\).

#### Exercise 4 — Joint PDF

Let

\[
f_{X,Y}(x,y)=\begin{cases}
\frac12e^{-x}+\frac{cy}{(1+x)^2},&x\ge0,\ 0\le y\le1,\\
0,&\text{otherwise}.
\end{cases}
\]

1. Find \(c\).
2. Find \(P(0\le X\le1,0\le Y\le1/2)\).
3. Derive the marginal PDF of \(X\).

??? answer

    Normalisation gives \(c=1\). Integrate the joint PDF over the requested rectangle for part 2. The marginal is \(f_X(x)=\frac12e^{-x}+\frac{1}{2(1+x)^2}\) for \(x\ge0\).

#### Exercise 5 — A second joint PMF

The joint PMF of \(X\) and \(Y\) is:

| \(y\backslash x\) | 4 | 5 | 7 |
| --- | ---: | ---: | ---: |
| -3 | \(k\) | 0 | 0 |
| -1 | \(2/10\) | 0 | \(k\) |
| 0 | \(1/10\) | 0 | \(4/10\) |
| 5 | 0 | \(k\) | 0 |

1. Find \(k\) and both marginal PMFs.
2. Find \(E[X]\), \(E[Y]\), and \(E[XY]\).
3. Find \(P(X<6,Y<0)\).
4. Determine whether \(X\) and \(Y\) are independent.

??? answer

    Normalisation gives \(3k+0.7=1\), so \(k=0.1\). Use row and column sums for the marginals. Since the table contains zero-probability cells whose marginal products are positive, the variables are not independent.

#### Exercise 6 — An infinite discrete joint model

Let

\[
p_{X,Y}(k,l)=\frac{1}{2^{k+l}},\qquad k,l=1,2,\ldots
\]

1. Verify that this is a valid joint PMF.
2. Find the marginal PMFs.
3. Determine whether \(X\) and \(Y\) are independent.
4. Find \(P(X^2+Y^2\le10)\).

??? answer

    Each marginal is \(P(X=k)=2^{-k}\), and the joint PMF factors into the product of the marginals. The admissible pairs in part 4 are \((1,1),(1,2),(2,1),(2,2),(1,3),(3,1)\), giving probability \(11/16\).

#### Exercise 7 — A triangular support

Suppose \(f_{X,Y}(x,y)=c(x+y)\) on \(x\ge0\), \(y\ge0\), and \(x+y\le1\), and is zero elsewhere.

1. Sketch the support and find \(c\).
2. Derive both marginal PDFs.
3. Find \(P(X+Y\le1/2)\).
4. Determine whether \(X\) and \(Y\) are independent.

??? answer

    Integrating over the triangle gives \(c=3\). For \(0\le x\le1\), \(f_X(x)=\int_0^{1-x}3(x+y)\,dy\), with an analogous expression for \(f_Y\). The triangular support alone rules out independence.
