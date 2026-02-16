class ListNode 
{
    int val;
    ListNode next;

    ListNode() {}

    ListNode(int val) 
    {
        this.val = val;
    }

    ListNode(int val, ListNode next) 
    {
        this.val = val;
        this.next = next;
    }
}

public class Solution 
{

    public ListNode reverseList(ListNode head) 
    {

        ListNode prev = null;
        ListNode curr = head;

        while (curr != null) 
        {

            ListNode nextTemp = curr.next;

            curr.next = prev; 

            prev = curr; 
            curr = nextTemp; 
        }

        return prev;
    }

    public static void main(String[] args) 
    {

        ListNode head = new ListNode(1,
                new ListNode(2,
                new ListNode(3,
                new ListNode(4,
                new ListNode(5)))));

        Solution sol = new Solution();

        head = sol.reverseList(head);

        while (head != null) {
            System.out.print(head.val + " ");
            head = head.next;
        }
    }
}
