import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter column number: ");
        int n = sc.nextInt();

        String result = convertToTitle(n);

        System.out.println("Column Title: " + result);
    }

    static String convertToTitle(int n) {

        String result = "";

        while (n > 0) {
            n--;  // important

            char ch = (char) ('A' + (n % 26));
            result = ch + result;

            n /= 26;
        }

        return result;
    }
}
