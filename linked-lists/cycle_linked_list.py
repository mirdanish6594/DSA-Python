class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(values):
    head = ListNode(values[0])
    curr = head
    nodes = [head]
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
        nodes.append(curr)
    return head, nodes

def create_cycle(head, nodes, pos):
    if pos == -1:
        return
    tail = nodes[-1]
    tail.next = nodes[pos]

def print_linked_list(head, limit=20):
    count = 0
    while head and count < limit:
        print(head.val , end='->')
        head = head.next
        count += 1
    if head:
        print('...')
    else:
        print(None)

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
if __name__ == "__main__":
    values = list(map(int, input("Enter values in spaced way: ").split()))
    pos = int(input("Enter cycle position(-1 if no cycle): "))

    head, nodes = create_linked_list(values)
    create_cycle(head, nodes, pos)

    print("Printing linked list upto 20 nodes to avoid infinite loop: ")
    print_linked_list(head)

    sol = Solution()
    result = sol.hasCycle(head)
    print("\nDoes the linked list have a cycle: ", result)