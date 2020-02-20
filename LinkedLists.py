# Gavin Howard 
# 2/19/2020
# Linked Lists

class ListNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


    def __repr__(self):
        return repr(self)


class LinkedList:
    def __init__(self):
        self.head = head


    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ', '.join(nodes) + ']'

