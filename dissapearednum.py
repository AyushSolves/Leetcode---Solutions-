class Solution:
    def findDisappearedNumbers(self, nums):
        
        # Mark visited indices
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        
        # Collect missing numbers
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
        
        return result

if __name__ == "__main__":
    sol = Solution()

    nums1 = [4,3,2,7,8,2,3,1]
    nums2 = [1,1]

    print(sol.findDisappearedNumbers(nums1))  # [5, 6]
    print(sol.findDisappearedNumbers(nums2))  # [2]