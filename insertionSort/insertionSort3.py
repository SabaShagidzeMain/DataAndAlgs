# Given a singly linked list (Node: val, next), implement insertion_sort_II(head).
# No arrays - pointer manipulation only! Maintain a sorted sub-list and find the correct position using prev/curr pointers
# input: 4->2->1->3->None Output: 1->2->3->4->None

# Definition for singly-linked list
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Insertion Sort on Linked List
def insertion_sort_ll(head):

    # dummy node helps simplify insertion at head
    dummy = Node(0)

    curr = head

    while curr:

        # save next node before changing pointers
        next_node = curr.next

        # find correct insertion position
        prev = dummy

        while prev.next and prev.next.val < curr.val:
            prev = prev.next

        # insert current node into sorted part
        curr.next = prev.next
        prev.next = curr

        # move to next node
        curr = next_node

    return dummy.next


# Helper: build linked list from Python list
def build_linked_list(values):

    if not values:
        return None

    head = Node(values[0])
    curr = head

    for v in values[1:]:
        curr.next = Node(v)
        curr = curr.next

    return head


# Helper: print linked list
def print_linked_list(head):

    curr = head

    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next

    print("None")


# TEST
head = build_linked_list([4, 2, 1, 3])

print("Original:")
print_linked_list(head)

sorted_head = insertion_sort_ll(head)

print("Sorted:")
print_linked_list(sorted_head)