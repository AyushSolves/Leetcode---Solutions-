class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):

        pA, pB = headA, headB

        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA

        return pA

if __name__ == "__main__":

    c1 = ListNode(8)
    c2 = ListNode(10)
    c1.next = c2

    a1 = ListNode(3)
    a2 = ListNode(7)
    a1.next = a2
    a2.next = c1

    b1 = ListNode(99)
    b2 = ListNode(1)
    b1.next = b2
    b2.next = c1

    sol = Solution()
    result = sol.getIntersectionNode(a1, b1)

    if result:
        print("Intersection at node value:", result.val)
    else:
        print("No intersection")
