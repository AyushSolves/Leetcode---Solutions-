class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


if __name__ == "__main__":
    sol = Solution()

    head = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)

    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  

    print("Has cycle:", sol.hasCycle(head)) 

    a = ListNode(1)
    b = ListNode(2)
    a.next = b

    print("Has cycle:", sol.hasCycle(a))
