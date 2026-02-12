import java.util.Scanner;

public class Solution 
{

    public static int titleToNumber(String s) 
    {

        int result = 0;

        for (char ch : s.toCharArray()) 
        {
            result = result * 26 + (ch - 'A' + 1);
        }

        return result;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter column title: ");
        String title = sc.next();

        System.out.println("Column Number: " + titleToNumber(title));

        sc.close();
    }
}
