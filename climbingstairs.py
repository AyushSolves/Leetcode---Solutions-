class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1
        if n == 2:
            return 2

        prev2 = 1  
        prev1 = 2  

        for i in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current

        return prev1

if __name__ == "__main__":
    sol = Solution()

    n = 5

    print("Number of steps:", n)
    result = sol.climbStairs(n)
    print("Number of distinct ways to climb:", result)
