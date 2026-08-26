---
tags:
    - Markov Chains
    - Transition Matrix
    - Stationary Distribution
    - Classification of States
---

<h1 align="center">Markov Chains</h1>

Markov chains model state-based systems in which the next state is conditionally independent of the earlier past given the current state. We connect conditional probability, matrices, stochastic processes, and simulation.

A chain is specified by a state space and a transition matrix. Path probabilities multiply along a route; multi-step probabilities come from powers of the matrix. Communicating classes, transience, and recurrence organise the long-run picture, and a stationary distribution describes the equilibrium occupancy of an irreducible class.

#### Key Concepts

- Markov property, state space, and transition matrix
- Path and multi-step probabilities
- Communicating classes, transience, and recurrence
- Stationary distributions
- Absorption in closed classes

!!! tip "Learning Objectives"

    - Define a state space and transition matrix.
    - Calculate path and multi-step probabilities.
    - Identify communicating classes.
    - Calculate and interpret a stationary distribution.

<hr/>

### Session Preparation:

Review conditional probability, matrix multiplication, and the idea of a discrete-time process.

**Syllabus and input**

- [ProbabilityCourse 11.2.1: discrete-time Markov chains](https://www.probabilitycourse.com/chapter11/11_2_1_introduction.php)
- [State-transition matrix and diagram](https://www.probabilitycourse.com/chapter11/11_2_2_state_transition_matrix_and_diagram.php)
- [State probability distributions](https://www.probabilitycourse.com/chapter11/11_2_3_probability_distributions.php)
- [Classification of states](https://www.probabilitycourse.com/chapter11/11_2_4_classification_of_states.php)

**Existing course material**

[Recap notes](https://drive.google.com/file/d/1GJYl8qMMGcRZ7FD0qTif7jJazdyUPuQr/view?usp=sharing)

[Session notes](https://drive.google.com/file/d/1AyY6nKHnY9f9Tl9siholsRkop_BbB2Fv/view?usp=sharing)

[Session material](https://viaucdk-my.sharepoint.com/:f:/g/personal/rib_viauc_dk/EuqNIuAYAltDmfXlB9l-DpMBTP5g7G1XrHFCqcXim9OfNQ?e=IMjqf3)

<hr/>

### Exercises

<style type="text/css">
    ol { list-style-type: lower-alpha; }
</style>

#### Exercise 1 — Paths and transitions

Consider the Markov chain with three states, $S=\{1,2,3\}$, that has the following transition matrix

$$
P=\left[\begin{array}{ccc}
\frac{1}{2} & \frac{1}{4} & \frac{1}{4} \\
\frac{1}{3} & 0 & \frac{2}{3} \\
\frac{1}{2} & \frac{1}{2} & 0
\end{array}\right]
$$

1. Draw the state transition diagram for this chain.
2. If we know $P\left(X_1=1\right)=P\left(X_1=2\right)=\frac{1}{4}$, find $P\left(X_1=3, X_2=2, X_3=1\right)$.

???answer
    <ol start="2">
        <!-- element b -->
        <li style> 1/12 </li>
    </ol>

#### Exercise 2

Consider the Markov chain in the figure below. There are two recurrent classes, $R_1=\{1,2\}$, and $R_2=\{5,6,7\}$.

<img src="src/Ex2_1.png">

1. Assuming $X_0=3$, find the probability that the chain gets absorbed in $R_1$.
2. Find the expected time (number of steps) until the chain gets absorbed in $R_1$ or $R_2$. More specifically, let $T$ be the absorption time, i.e., the first time the chain visits a state in $R_1$ or $R_2$, so find $E\left[T \mid X_0=3\right]$

???answer
    1. $a_3=\frac{5}{7}$
    2. $t_3=\frac{12}{7}$

#### Exercise 3

Consider the following Markov chain

<img src="src/Ex3_1.png">

1. Is this chain irreducible?
2. Is this chain aperiodic?
3. Find the stationary distribution for this chain.
4. Is the stationary distribution a limiting distribution for the chain?

???answer
    1. yes
    2. yes
    3. $\pi_1 \approx 0.457, \pi_2 \approx 0.257, \pi_3 \approx 0.286$
    4. yes

#### Exercise 4

Consider the following Markov chain

<img src="src/Ex4_1.png">

Assume $X_0=1$, and let $R$ be the first time that the chain returns to state 1 . Find $E\left[R \mid X_0=1\right]$.

???answer
    $\frac{8}{3}$

#### Exercise 5 — A two-state reliability chain

A component is either Working or Failed. During each hour, a working component fails with probability 0.02, while a failed component is repaired with probability 0.30.

1. Construct the transition matrix and diagram.
2. Starting in Working, find the probability of being Failed after 2 and 10 hours.
3. Find the stationary distribution.
4. Interpret the stationary failure probability operationally.

??? answer

    With state order \((W,F)\), \(P=\begin{pmatrix}0.98&0.02\\0.30&0.70\end{pmatrix}\). The stationary distribution satisfies \(0.02\pi_W=0.30\pi_F\), giving \((\pi_W,\pi_F)=(15/16,1/16)\).

#### Exercise 6 — Classification of states

Consider

\[
P=\begin{pmatrix}
1&0&0&0\\
0.2&0.5&0.3&0\\
0&0&0.6&0.4\\
0&0&0.1&0.9
\end{pmatrix}.
\]

1. Draw the transition diagram.
2. Identify the communicating classes.
3. Classify states as transient or recurrent.
4. Identify all closed classes and stationary distributions.

??? answer

    State 1 is an absorbing closed class. States 3 and 4 form another closed irreducible class. State 2 is transient because it can leave for either closed class and cannot be revisited from them. Each closed class supports a stationary distribution.

#### Exercise 7 — Estimating a transition matrix

An observed state sequence is

\[
A,A,B,A,C,C,B,C,C,A,B,B,C,A,A.
\]

1. Count all observed one-step transitions.
2. Estimate the transition matrix by row-normalising the counts.
3. State which rows have the greatest estimation uncertainty and why.
4. Simulate a sequence of length 100 from the fitted chain and compare transition frequencies.
