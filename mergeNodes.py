from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        tail = dummy = ListNode()

        while curr.next:
            node = ListNode(0)
            while curr.next and curr.next.val != 0:
                node.val += curr.next.val
                curr = curr.next
            tail.next = node 
            tail = tail.next
            curr = curr.next
        
        return dummy.next

def create_linked_list(values):
    dummy = ListNode()
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

def print_linked_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(" -> ".join(map(str, values)))

def main():
    solution = Solution()
    
    # Test case 1
    head1 = create_linked_list([0, 3, 1, 0, 4, 5, 2, 0])
    print("Original List 1:")
    print_linked_list(head1)
    merged_head1 = solution.mergeNodes(head1)
    print("Merged List 1:")
    print_linked_list(merged_head1)

    # Test case 2
    head2 = create_linked_list([0, 1, 0, 3, 2, 0])
    print("Original List 2:")
    print_linked_list(head2)
    merged_head2 = solution.mergeNodes(head2)
    print("Merged List 2:")
    print_linked_list(merged_head2)

if __name__ == "__main__":
    main()
