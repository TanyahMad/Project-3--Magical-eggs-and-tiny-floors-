Magical Eggs & Tiny Floors
Dynamic Programming Solution to the Egg Drop Problem
This project implements an optimal strategy for solving the Egg Drop Problem, also known as the Magical Eggs and Tiny Floors puzzle.
Given m eggs and n floors, the goal is to determine:
The first floor from which to drop an egg
The minimum number of drops needed in the worst case
The solution uses Dynamic Programming, computes the full DP table, and recovers the optimal first drop floor.

Features
Computes the minimum worst-case number of drops
Outputs the optimal first floor to drop from
Works for any number of eggs and floors
Includes experimental runtime measurements
Plot of runtime vs floors for multiple egg counts
Clean and documented Python implementation

How the Algorithm Works
Let:
dp[i][j] = minimum number of drops needed with i eggs and j floors
first[i][j] = best first floor to drop from for that state
For every floor k (1 to j):
If the egg breaks, we check below → dp[i-1][k-1]
If the egg survives, we check above → dp[i][j-k]
Worst-case cost of dropping from floor k:
1+max(dp[i−1][k−1], dp[i][j−k])
We choose the k that minimizes this value and store it in first[i][j].
This gives both:
The optimal first drop floor
The minimal worst-case number of attempts

Run the program:
python3 magical_eggs.py
Enter the number of eggs and floors

Experimental Runtime Analysis
We measured runtime for:
Eggs = 1, 2, 4, 6
Floors = 1 to 100

Observations
1 egg → linear growth (simple scan)
≥2 eggs → quadratic growth due to the 3 nested loops
