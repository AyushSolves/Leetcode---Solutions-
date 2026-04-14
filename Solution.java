
public class Solution {

    public String licenseKeyFormatting(String s, int k) {
        StringBuilder cleaned = new StringBuilder();

        for (char c : s.toCharArray()) {
            if (c != '-') {
                cleaned.append(Character.toUpperCase(c));
            }
        }

        StringBuilder result = new StringBuilder();
        int count = 0;

        for (int i = cleaned.length() - 1; i >= 0; i--) {
            result.append(cleaned.charAt(i));
            count++;

            if (count == k && i != 0) {
                result.append('-');
                count = 0;
            }
        }

        return result.reverse().toString();
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        String s1 = "5F3Z-2e-9-w";
        int k1 = 4;
        System.out.println(sol.licenseKeyFormatting(s1, k1)); // Output: 5F3Z-2E9W

        String s2 = "2-5g-3-J";
        int k2 = 2;
        System.out.println(sol.licenseKeyFormatting(s2, k2)); // Output: 2-5G-3J
    }
}