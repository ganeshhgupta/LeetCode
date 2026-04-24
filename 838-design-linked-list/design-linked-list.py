class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.left = Node(0)
        self.right = Node(0)
        self.left.next = self.right
        self.right.prev = self.left
        self.size = 0

    def get(self, index: int) -> int:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and curr != self.right and index == 0:
            return curr.val
        return -1

    def addAtHead(self, val: int) -> None:
        node, next, prev = Node(val), self.left.next, self.left
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev
        self.size += 1

    def addAtTail(self, val: int) -> None:
        node, next, prev = Node(val), self.right, self.right.prev
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and index == 0:
            node, next, prev = Node(val), curr, curr.prev
            prev.next = node
            next.prev = node
            node.next = next
            node.prev = prev
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and curr != self.right and index == 0:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            self.size -= 1