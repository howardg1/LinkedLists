# Gavin Howard 
# 2/19/2020
# Linked Lists

class Node:
    def __init__(self, data):
        self.data = data
        self.next = next


    def __repr__(self):
        return repr(self)


class LinkedList:
    def __init__(self):
        self.head = None


    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ', '.join(nodes) + ']'


    def add_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def add_end(self, data):
        new_node = Node(data)
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node


    def remove_head(self):
        new_node = self.head
        self.head = self.head.next
        return new_node.data


    def remove_end(self):
        curr_node = self.head
        prev_node = self.head
        while curr_node.next:
            prev_node = curr_node
            curr_node = curr_node.next
        prev_node.next = None
        return curr_node.data


    def clear(self):
        self.head = None


    def search_list(self, key):
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        return curr


    def remove_node(self, key):
        curr = self.head
        prev = None
        while curr and curr.data != kay:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None



