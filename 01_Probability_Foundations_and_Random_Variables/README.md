---
tags:
    - Probability
    - Sample Space
    - Conditional Probability
    - Bayes
    - Random Variables
---

<h1 align="center">Probability Foundations and Random Variables</h1>

This session establishes the language used throughout the course: experiments, sample spaces, events, probability measures, conditioning, independence, and random variables. Expectation and variance are introduced as properties of a model rather than sample summaries.

We represent a random experiment with a sample space and events, then apply probability rules, conditional probability, the law of total probability, and Bayes' theorem. Independence is distinguished from mutually exclusive events. A random variable assigns a numerical value to each outcome, and its expectation and variance describe the model, not a data sample.

#### Key Concepts

- Experiments, sample spaces, and events
- Probability rules, conditional probability, and Bayes' theorem
- Independence versus mutually exclusive events
- Random variables
- Expectation and variance as model properties

!!! tip "Learning Objectives"

    - Represent a random experiment using a sample space and events.
    - Apply probability rules, conditional probability, total probability, and Bayes' theorem.
    - Distinguish independence from mutually exclusive events.
    - Define a random variable and interpret its expectation and variance.

<hr/>

### Session Preparation:

There are no exercises due before the first class. Review the [prerequisites](../00_Prerequisites/README.md), especially sets, combinatorics, and basic probability.

**Syllabus and input**

- [Chapter 1 introduction](https://www.probabilitycourse.com/chapter1/1_0_0_introduction.php)
- [Probability axioms](https://www.probabilitycourse.com/chapter1/1_3_2_probability.php)
- [Conditional probability](https://www.probabilitycourse.com/chapter1/1_4_0_conditional_probability.php)
- [Bayes' rule](https://www.probabilitycourse.com/chapter1/1_4_3_bayes_rule.php)

**Existing course material**

- [Session notes](https://drive.google.com/file/d/1oqEy7sINksGCfdytv_O8qIZ0FoVEyWjz/view?usp=drive_link)
- [Session material](https://viaucdk-my.sharepoint.com/:f:/g/personal/rib_viauc_dk/EuOeq6E9sg9Jjf5n_qCeM80B4uonPufDX4RnR0nFz3EdMg?e=dRNi7T)

<hr/>

### Exercises

#### Exercise 1 — Probability tree

Heart failures are due to natural occurrences (87%) or outside factors (13%). Outside factors are related to induced substances (73%) or foreign objects (27%). Natural occurrences are caused by arterial blockage (56%), disease (27%), or infection (17%).

1. Find the probability that a failure is due to an induced substance.
2. Find the probability that a failure is due to disease or infection.

??? answer

    1. \(0.13\cdot0.73=0.0949\).
    2. \(0.87(0.27+0.17)=0.3828\).

#### Exercise 2 — Event algebra

Let \(P(A)=0.4\), \(P(B)=0.7\), and \(P(A\cup B)=0.9\).

1. Find \(P(A\cap B)\).
2. Find \(P(A^c\cap B)\).
3. Find \(P(A-B)\).
4. Find \(P(A^c\cup B)\).

??? answer

    1. \(0.4+0.7-0.9=0.2\).
    2. \(0.7-0.2=0.5\).
    3. \(0.4-0.2=0.2\).
    4. \(1-P(A-B)=0.8\).

#### Exercise 3 — Bayes' theorem

An IT company receives 40% of its circuit boards from supplier 1 and 60% from supplier 2. The defect rates are 5% and 3%, respectively.

1. Find the probability that a randomly chosen board is defective.
2. Given that a board is defective, find the probability that it came from supplier 1.

??? answer

    1. \(P(D)=0.4(0.05)+0.6(0.03)=0.038\).
    2. \(P(S_1\mid D)=0.4(0.05)/0.038\approx0.5263\).

#### Exercise 4 — Conditional probability

For a scheduled flight, \(P(D)=0.83\) is the probability of departing on time, \(P(A)=0.82\) is the probability of arriving on time, and \(P(D\cap A)=0.78\).

1. Find \(P(A\mid D)\).
2. Find \(P(D\mid A)\).
3. Find \(P(A\mid D^c)\).

??? answer

    1. \(0.78/0.83\approx0.9398\).
    2. \(0.78/0.82\approx0.9512\).
    3. \((0.82-0.78)/(1-0.83)\approx0.2353\).

#### Exercise 5 — A first random variable

Let \(X\) be the number of sixes obtained in three independent rolls of a fair die.

1. State the possible values of \(X\).
2. Find the probability of each value.
3. Find \(E[X]\) and \(\operatorname{Var}(X)\).

??? answer

    \(X\sim\operatorname{Binomial}(3,1/6)\). Thus \(R_X=\{0,1,2,3\}\), \(P(X=k)={3\choose k}(1/6)^k(5/6)^{3-k}\), \(E[X]=1/2\), and \(\operatorname{Var}(X)=5/12\).

#### Exercise 6 — Keyboard failures

Computer keyboard failures are caused by faulty electrical connections (12%) or mechanical defects (88%). Mechanical defects are loose keys (27%) or improper assembly (73%). Electrical defects are defective wires (35%), improper connections (13%), or poorly welded wires (52%).

1. Draw a probability tree.
2. Find the probability that a failure is caused by loose keys.
3. Find the probability that a failure is caused by an improper connection or a poorly welded wire.
4. Given that the failure is electrical, find the probability that it is caused by a defective wire.

??? answer

    The answers are \(0.88(0.27)=0.2376\), \(0.12(0.13+0.52)=0.078\), and \(0.35\), respectively.

#### Exercise 7 — Sample space and complements

Two teams play a football match. Let \(a\), \(b\), and \(d\) denote that team A wins, team B wins, or the match is drawn. Suppose \(P(a)=0.50\) and \(P(d)=0.25\).

1. Write the sample space and its power set.
2. Find \(P(b)\).
3. Find the probability that team A does not win.
4. Define two non-trivial events and determine whether they are mutually exclusive.

??? answer

    \(S=\{a,b,d\}\), \(P(b)=0.25\), and \(P(A\text{ does not win})=P(\{b,d\})=0.50\). Mutual exclusivity depends on the events chosen and requires an empty intersection.

#### Exercise 8 — Three suppliers and Bayes' rule

A batch contains 50% Western Digital, 30% Toshiba, and 20% Seagate hard drives. The defect rates for Toshiba and Seagate are both 2%, while 3% of the entire batch is defective.

1. Find the defect rate for Western Digital drives.
2. Construct a supplier-by-quality contingency table for a batch of 1,000 drives.
3. Given that a drive is defective, find the probability that it came from Seagate.
4. Given that a drive is not defective, find the probability that it came from Western Digital.

??? answer

    Total probability gives \(0.03=0.5p+0.3(0.02)+0.2(0.02)\), so \(p=0.04\). There are 20, 6, and 4 defective drives from Western Digital, Toshiba, and Seagate. Thus \(P(S\mid D)=4/30\) and \(P(W\mid D^c)=480/970\).
