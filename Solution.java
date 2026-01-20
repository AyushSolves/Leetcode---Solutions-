import java.util.Scanner;

class Solution 
{
    public int mySqrt(int x) 
    {
        if (x == 0 || x == 1) 
        {
            return x;
        }

        int low = 1, high = x;
        int ans = 0;
        
        while (low <= high) 
        {
            int mid = low + (high - low) / 2;
            long square = (long) mid * mid;   

            if (square == x) 
            {
                return mid;
            } 
            else if (square < x) 
            {
                ans = mid;        
                low = mid + 1;  
            } 
            else 
            {
                high = mid - 1;
            }
        }
        return ans;  
    }

    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
        Solution sol = new Solution();

        System.out.print("Enter a non-negative number: ");
        int x = sc.nextInt();

        int result = sol.mySqrt(x);

        System.out.println("Square root (rounded down) = " + result);

        sc.close();
    }
}
