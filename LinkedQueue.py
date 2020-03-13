from LinkedListTail import LinkedListTail

class Queue:
    def __init__(self):
        self.myQueue = LinkedListTail()

    def push(self, data):
        self.myQueue.add_end(data)

    def pop(self):
        return self.myQueue.remove_head().data


myList = Queue()
myList.push(7)
print(myList.pop())
