# Example: Given nums = [5, 1, 7, 8, 2], X = 5

nums = [5, 1, 7, 8, 2]
X = 5

print(f"{'Window':>15} {'Sum':>5} {'Length':>6} {'Avg':>6} {'X*Len':>7} {'Sum-X*Len':>10} {'Avg>=X?':>9}")

n = len(nums)
# Try every possible start/end for demonstration purposes
for start in range(n):
    for end in range(start, n):
        window = nums[start:end+1]
        window_sum = sum(window)
        window_len = end - start + 1
        avg = window_sum / window_len
        x_times_len = X * window_len
        excess = window_sum - x_times_len
        avg_good = "YES" if avg >= X else "NO"
        print(f"{str(window):>15} {window_sum:5} {window_len:6} {avg:6.2f} {x_times_len:7} {excess:10} {avg_good:>9}")