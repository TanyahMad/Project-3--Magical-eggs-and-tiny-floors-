import time
import csv
import matplotlib.pyplot as plt

def build_dp(eggs, floors):
    """
    dp[i][j] = min number of attempts in the worst case
               with i eggs and j floors.
    """
    dp = [[0] * (floors + 1) for _ in range(eggs + 1)]

    # base case: 1 egg -> j attempts
    for j in range(1, floors + 1):
        dp[1][j] = j

    for i in range(2, eggs + 1):
        for j in range(1, floors + 1):
            best = float("inf")
            # try dropping from every floor k
            for k in range(1, j + 1):
                worst = 1 + max(dp[i - 1][k - 1], dp[i][j - k])
                if worst < best:
                    best = worst
            dp[i][j] = best

    return dp


def time_dp(eggs, floors):
    """
    Time the DP for a given number of eggs and floors.
    Returns time in microseconds.
    """
    start = time.perf_counter()
    build_dp(eggs, floors)
    end = time.perf_counter()
    return (end - start) * 1_000_000.0  # microseconds



# 1) Measure times for floors 6..99 for eggs = 1,2,4,6

def measure_range(eggs_list, floor_start, floor_end):
    floors = list(range(floor_start, floor_end + 1))
    timings = {e: [] for e in eggs_list}

    for e in eggs_list:
        print(f"Measuring for {e} eggs...")
        for f in floors:
            t = time_dp(e, f)
            timings[e].append(t)
    return floors, timings


# 2) Save big table: eggs-floor-table.csv

def save_eggs_floor_table(filename, floors, timings, eggs_list):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        header = ["floor"] + [f"eggs_{e}" for e in eggs_list]
        writer.writerow(header)

        for idx, floor in enumerate(floors):
            row = [floor]
            for e in eggs_list:
                row.append(timings[e][idx])
            writer.writerow(row)

# 3) Save summary: new_experimental_results.csv
#    for floors 10, 100, 1000, 10000 and eggs = 1,2

def save_summary_table(filename):
    floors = [10, 100, 1000, 10000]
    eggs_list = [1, 2]

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["floor", "eggs_1", "eggs_2"])

        for floor in floors:
            row = [floor]
            for e in eggs_list:
                t = time_dp(e, floor)
                row.append(t)
            writer.writerow(row)

# 4) Plot runtime graph: runtime_plot.png

def plot_timings(floors, timings, eggs_list, out_file="runtime_plot.png"):
    plt.figure(figsize=(8, 5))

    for e in eggs_list:
        plt.plot(floors, timings[e], label=f"n = {e}")

    plt.xlabel("floors")
    plt.ylabel("time (microseconds)")
    plt.title("Runtime of Egg-Drop DP Algorithm")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(out_file, dpi=300)
    plt.close()

# Main

if __name__ == "__main__":
    eggs_list = [1, 2, 4, 6]
    floor_start = 6
    floor_end = 99

    floors, timings = measure_range(eggs_list, floor_start, floor_end)

    # 1) full table for the big CSV
    save_eggs_floor_table("eggs-floor-table.csv", floors, timings, eggs_list)

    # 2) small summary table (10,100,1000,10000)
    save_summary_table("new_experimental_results.csv")

    # 3) graph image
    plot_timings(floors, timings, eggs_list, "runtime_plot.png")

    print("Done. Files generated:")
    print("  - eggs-floor-table.csv")
    print("  - new_experimental_results.csv")
    print("  - runtime_plot.png")
