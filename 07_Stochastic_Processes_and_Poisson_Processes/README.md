# 07 — Stochastic Processes and Poisson Processes

## Session preparation

Review the Poisson and exponential distributions and the LLN from Sessions 2, 3, and 6.

**Syllabus and input**

- [Basic concepts of random processes](https://www.probabilitycourse.com/chapter10/10_1_0_basic_concepts.php)
- [Basic concepts of the Poisson process](https://www.probabilitycourse.com/chapter11/11_1_2_basic_concepts_of_the_poisson_process.php)
- [Merging and splitting Poisson processes](https://www.probabilitycourse.com/chapter11/11_1_3_merging_and_splitting_poisson_processes.php)

**Existing course material**

- [Session notes](https://drive.google.com/file/d/1gTaiww6T_lyrVKNU7E93SkhK3ITO3ojL/view?usp=sharing)
- [Session material](https://viaucdk-my.sharepoint.com/:f:/g/personal/rib_viauc_dk/EpMa2OpoQTRLjtQWiM9qhugBXvJkRWuUGK7-4SuiycEDYQ?e=Fg6B41)

---

## Session focus

A stochastic process is a collection of random variables indexed by time. We distinguish a distribution at one time from dependence across time, then study the Poisson counting process through stationary independent increments and exponential interarrival times.

By the end of the session, you should be able to describe a process through its state space and time index, calculate probabilities for Poisson-process increments and arrival times, combine or thin Poisson processes, and simulate event histories.

---

## Exercises

#### Exercise 1 — Server arrivals

Requests arrive as a Poisson process with rate 25 per second.

1. Find the distribution of the number of requests in 200 ms.
2. Given 7 requests in one second, find the distribution of the number arriving in the first 200 ms.
3. Find the probability that the third request arrives before 100 ms.

??? answer

    The count is \(\operatorname{Poisson}(5)\). Conditional on 7 arrivals in one second, the first-interval count is \(\operatorname{Binomial}(7,0.2)\). The third arrival time is \(\operatorname{Gamma}(3,25)\), equivalently calculate \(P(N(0.1)\ge3)\).

#### Exercise 2 — Superposition and thinning

Independent high- and low-priority requests arrive at rates 4 and 10 per minute.

1. Describe the combined process.
2. Find the probability that the next request is high priority.
3. If each low-priority request is cached independently with probability 0.3, describe the cached-request process.

??? answer

    The combined process has rate 14. The next request is high priority with probability \(4/14\). Thinning gives a Poisson process of cached requests with rate 3 per minute.

#### Exercise 3 — Independent increments

For a rate-2 process, let \(X=N(3)-N(1)\) and \(Y=N(4)-N(2)\). Find \(E[X]\), \(E[Y]\), and \(\operatorname{Cov}(X,Y)\). Explain why the overlap matters.

??? answer

    Both means are 4. The intervals overlap from time 2 to 3, so the shared increment has variance \(2\cdot1=2\); hence \(\operatorname{Cov}(X,Y)=2\).

#### Exercise 4 — Simulation

Simulate 100 realisations of a rate-3 Poisson process on \([0,10]\) using exponential interarrival times. Plot five paths and compare the empirical mean and variance of \(N(10)\) with theory.

#### Exercise 5 — Arrival times conditional on the count

Customers arrive according to a Poisson process with rate 6 per hour. Given that exactly four customers arrive during one hour:

1. Find the probability that exactly two arrived during the first 30 minutes.
2. Find the probability that all four arrived during the final 15 minutes.
3. Simulate the four conditional arrival times and compare their ordered values with four ordered uniform observations on \([0,1]\).

??? answer

    Conditional on the total count, arrivals independently fall into subintervals according to their relative lengths. Thus the first count is \(\operatorname{Binomial}(4,1/2)\), and the probability in part 2 is \((1/4)^4\).

#### Exercise 6 — Time to the fifth event

Failures occur as a Poisson process with rate 2 per day. Let \(T_5\) be the time of the fifth failure.

1. Identify the distribution of \(T_5\).
2. Find its mean and variance.
3. Express \(P(T_5\le2)\) as both a Gamma probability and a Poisson count probability.
4. Verify the equivalence numerically.

??? answer

    \(T_5\) has a Gamma distribution with shape 5 and rate 2, so its mean is \(5/2\) and variance \(5/4\). Also, \(P(T_5\le2)=P(N(2)\ge5)\), where \(N(2)\sim\operatorname{Poisson}(4)\).

#### Exercise 7 — Splitting an incident stream

Incidents arrive at rate 12 per hour. Independently, 50% are classified as minor, 35% as major, and 15% as critical.

1. Describe the three classified counting processes.
2. Find the probability of at least one critical incident in 30 minutes.
3. Given that 10 incidents occurred in one hour, find the conditional distribution of the three class counts.
4. Simulate the split processes and empirically check their pairwise independence without conditioning on the total.

??? answer

    Thinning gives independent Poisson processes with rates 6, 4.2, and 1.8 per hour. Part 2 is \(1-e^{-0.9}\). Conditional on a total of 10, the class counts are multinomial with probabilities \((0.50,0.35,0.15)\).
