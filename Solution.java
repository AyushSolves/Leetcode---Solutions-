
public class Solution 
{

    public boolean isUgly(int n) 
    {

        if (n <= 0) 
        {
            return false;
        }

        int[] factors = {2, 3, 5};

        for (int factor : factors) 
        {
            while (n % factor == 0) 
            {
                n /= factor;
            }
        }

        return n == 1;
    }

    public static void main(String[] args) 
    {

        Solution sol = new Solution();

        int n1 = 6;
        int n2 = 1;
        int n3 = 14;

        System.out.println("Input: " + n1 + " -> " + sol.isUgly(n1)); // true
        System.out.println("Input: " + n2 + " -> " + sol.isUgly(n2)); // true
        System.out.println("Input: " + n3 + " -> " + sol.isUgly(n3)); // false
    }
}