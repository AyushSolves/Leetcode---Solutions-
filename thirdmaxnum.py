class Solution:
    def thirdMax(self, nums):
        
        first = second = third = None
        
        for num in nums:
            
            # Skip duplicates
            if num == first or num == second or num == third:
                continue
            
            if first is None or num > first:
                third = second
                second = first
                first = num
                
            elif second is None or num > second:
                third = second
                second = num
                
            elif third is None or num > third:
                third = num
        
        return third if third is not None else first

if __name__ == "__main__":
    sol = Solution()

    nums1 = [3, 2, 1]
    nums2 = [1, 2]
    nums3 = [2, 2, 3, 1]

    print(sol.thirdMax(nums1))  # 1
    print(sol.thirdMax(nums2))  # 2
    print(sol.thirdMax(nums3))  # 1