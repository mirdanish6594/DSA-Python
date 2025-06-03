class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(values):
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def print_linked_list(head):
    while head:
        print(head.val, end=' -> ')
        head = head.next
    print('None')

class Solution:
    def RemoveNode(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        fast = slow = dummy

        for _ in range(n+1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next
    
if __name__ == "__main__":
    values = list(map(int, input("Enter the values of linked list: ").split()))
    n = int(input("Enter the value of n: "))

    head = create_linked_list(values)
    print("\nOriginal Linked List: ")
    print_linked_list(head)

    sol = Solution()
    new_head = sol.RemoveNode(head, n)

    print("\nNew linked list: ")
    print_linked_list(new_head)
