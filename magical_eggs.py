# Project 3 - Magical eggs and floors
# Project Members: 1. Tanyah Madondo, 2. Perfect Masiiwa, 3. Collin Munateyi
# Date: 11/18/2025

def magical_eggs(eggs, floors):
    # dp[i][j]  = minimum number of drops in the worst case
    # first[i][j] = floor to throw from first when we have i eggs and j floors
    dp = [[0] * (floors + 1) for _ in range(eggs + 1)]
    first = [[0] * (floors + 1) for _ in range(eggs + 1)]

    # Base case: with 1 egg, we can only do linear search from floor 1 up
    for j in range(1, floors + 1):
        dp[1][j] = j
        first[1][j] = 1   # start at floor 1 and go up

    # Fill table for i >= 2 eggs
    for i in range(2, eggs + 1):
        for j in range(1, floors + 1):
            best = float('inf')
            best_k = 1
            # Try dropping first egg from floor k
            for k in range(1, j + 1):
                worst_case = 1 + max(dp[i-1][k-1], dp[i][j-k])
                if worst_case <= best:
                    best = worst_case
                    best_k = k
            dp[i][j] = best
            first[i][j] = best_k

    # Return both: min drops and the optimal first floor
    return dp[eggs][floors], first[eggs][floors]


def input_eggs_number_and_floor():
    eggs = int(input("Enter number of eggs: "))
    floors = int(input("Enter number of floors: "))
    return eggs, floors

def main():
    eggs, floors = input_eggs_number_and_floor()
    min_attempts, first_floor = magical_eggs(eggs, floors)
    print("Drop the first egg from floor:", first_floor)
    print("Minimum number of attempts:", min_attempts)

main()
