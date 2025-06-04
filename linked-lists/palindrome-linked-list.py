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

    print(None)

class Solution:
    def palindromeLinkedList(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        first = head
        second = prev
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next

        return True

if __name__ == "__main__":
    values = list(map(int, input("Enter the values for the linked list: ").split()))
    head = create_linked_list(values)

    print("\nOriginal Linked List: ")
    print_linked_list(head)

    sol = Solution()
    result = sol.palindromeLinkedList(head)
    print("Palindrome: ", result)