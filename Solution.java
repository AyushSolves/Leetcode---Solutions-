import java.util.*;

public class Solution {

    public int findContentChildren(int[] g, int[] s) {

        Arrays.sort(g); // greed factors
        Arrays.sort(s); // cookie sizes

        int i = 0; // child pointer
        int j = 0; // cookie pointer

        while (i < g.length && j < s.length) {

            if (s[j] >= g[i]) {
                i++; // child satisfied
            }
            j++; // move to next cookie
        }

        return i;
    }

    // For VS Code testing
    public static void main(String[] args) {

        Solution sol = new Solution();

        int[] g1 = {1,2,3};
        int[] s1 = {1,1};

        int[] g2 = {1,2};
        int[] s2 = {1,2,3};

        System.out.println(sol.findContentChildren(g1, s1)); // 1
        System.out.println(sol.findContentChildren(g2, s2)); // 2
    }
}