public class Solution 
{
    static int bad = 4;

    public boolean isBadVersion(int version) 
    {
        return version >= bad;
    }

    public int firstBadVersion(int n) 
    {
        int left = 1;
        int right = n;

        while (left < right) 
        {

            int mid = left + (right - left) / 2;

            if (isBadVersion(mid)) 
            {
                right = mid;
            } 
            else 
            {
                left = mid + 1;
            }
        }

        return left;
    }

    public static void main(String[] args) 
    {
        Solution sol = new Solution();

        int n = 5;
        System.out.println(sol.firstBadVersion(n));
    }
}