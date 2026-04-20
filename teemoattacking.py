class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        if not timeSeries:
            return 0

        total = 0

        for i in range(len(timeSeries) - 1):
            gap = timeSeries[i + 1] - timeSeries[i]
            total += min(gap, duration)

        return total + duration

if __name__ == "__main__":
    sol = Solution()

    timeSeries = [1, 4]
    duration = 2
    print(sol.findPoisonedDuration(timeSeries, duration))  # Output: 4

    timeSeries = [1, 2]
    duration = 2
    print(sol.findPoisonedDuration(timeSeries, duration))  # Output: 3