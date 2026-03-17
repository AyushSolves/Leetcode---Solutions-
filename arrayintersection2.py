class Solution:
    def intersect(self, nums1, nums2):
        
        freq = {}
        
        for num in nums1:
            freq[num] = freq.get(num, 0) + 1
        
        result = []
        
        for num in nums2:
            if num in freq and freq[num] > 0:
                result.append(num)
                freq[num] -= 1
        
        return result


if __name__ == "__main__":
    sol = Solution()

    nums1 = [1,2,2,1]
    nums2 = [2,2]
    print("Output:", sol.intersect(nums1, nums2)) 

    nums3 = [4,9,5]
    nums4 = [9,4,9,8,4]
    print("Output:", sol.intersect(nums3, nums4)) 