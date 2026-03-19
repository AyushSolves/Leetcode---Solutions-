class Solution:
    def guessNumber(self, n: int) -> int:
        
        left, right = 1, n

        while left <= right:
            mid = (left + right) // 2
            res = guess(mid)

            if res == 0:
                return mid
            elif res == -1:
                right = mid - 1
            else:
                left = mid + 1

pick = 6

def guess(num):
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0


if __name__ == "__main__":
    sol = Solution()

    n = 10
    print("Picked number:", sol.guessNumber(n))  # 6