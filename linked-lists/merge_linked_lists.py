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
    def mergeList(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 =list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next


        if list1:
            curr.next = list1
        else:
            curr.next = list2
    
        return dummy.next
    
if __name__ == "__main__":
    values1 = list(map(int, input("Enter the values for 1st linked list: ").split()))
    values2 = list(map(int, input("Enter the values for 2st linked list: ").split()))

    head1 = create_linked_list(values1)
    head2 = create_linked_list(values2)

    print("\nFirst Linked List: ")
    print_linked_list(head1)

    print("\nSecond Linked List: ")
    print_linked_list(head2)

    sol = Solution()
    merged_list = sol.mergeList(head1, head2)
    print("\nMerged Linked List:")
    print_linked_list(merged_list)
