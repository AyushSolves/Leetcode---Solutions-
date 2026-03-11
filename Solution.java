import java.util.*;

public class Solution {

    public int[] countBits(int n) {

        int[] ans = new int[n + 1];

        for (int i = 1; i <= n; i++) {
            ans[i] = ans[i >> 1] + (i & 1);
        }

        return ans;
    }

    public static void main(String[] args) {

        Solution sol = new Solution();

        int n = 5;

        int[] result = sol.countBits(n);

        System.out.println(Arrays.toString(result));
    }
}