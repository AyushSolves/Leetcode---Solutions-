import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        
        while n % 3 == 0:
            n //= 3
        
        return n == 1

    def isPowerOfThreeFast(self, n: int) -> bool:
       
        return n > 0 and 1162261467 % n == 0

if __name__ == "__main__":
    sol = Solution()
    
    test_cases = [27, 0, -1, 9, 45]
    
    print("Results:")
    for val in test_cases:
        result = sol.isPowerOfThree(val)
        print(f"Input: n = {val} -> Output: {result}")