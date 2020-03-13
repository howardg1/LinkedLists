from LinkedLists import LinkedList

class Stack:
    def __init__(self):
        self.myList = LinkedList()

    def push(self, data):
        self.myList.add_head(data)

    def pop(self, data):
        return self.myList.remove_head()

    def peek(self):
        return self.myList.peek()
