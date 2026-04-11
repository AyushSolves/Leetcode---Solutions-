class Solution:
    def findComplement(self, num):
        mask = 1
        
        # create mask with all bits = 1 (same length as num)
        while mask <= num:
            mask <<= 1
        
        mask -= 1
        
        return num ^ mask

if __name__ == "__main__":
    sol = Solution()

    num = 5
    print(sol.findComplement(num))  # Output: 2

    num = 1
    print(sol.findComplement(num))  # Output: 0