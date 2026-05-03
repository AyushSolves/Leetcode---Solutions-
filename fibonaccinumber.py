class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        a, b = 0, 1

        for i in range(2, n + 1):
            a, b = b, a + b

        return b

if __name__ == "__main__":
    sol = Solution()
    print(sol.fib(2))  # 1
    print(sol.fib(3))  # 2
    print(sol.fib(4))  # 3