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
            print(head.val, end='->')
            head = head.next
        print('None')

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
    
if __name__ == "__main__":
    values = list(map(int, input("Enter the values seperated by spaces: ").split()))
    head = create_linked_list(values)

    print("Original Linked List: ")
    print_linked_list(head)

    sol = Solution()
    result = sol.reverseList(head)

    print("Reversed linked List: ")
    print_linked_list(result)