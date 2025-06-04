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
    def addLinkedLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        stack2 = []

        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        carry = 0
        head = None
        while stack1 or stack2 or carry:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            new_node = ListNode(digit)
            new_node.next = head
            head = new_node

        return head
    
if __name__ == "__main__":
    l1_values = list(map(int, input("Enter the values for first linked list: ").split()))
    l2_values = list(map(int, input("Enter the values for second linked list: ").split()))

    l1 = create_linked_list(l1_values)
    l2 = create_linked_list(l2_values)

    sol = Solution()
    result = sol.addLinkedLists(l1, l2)
    
    print("\nSum of linked lists: ")
    print_linked_list(result)



