class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}

        self.least, self.most = Node(0,0), Node(0,0)
        self.least.next, self.most.prev = self.most, self.least

    def get(self, key: int) -> int:
        if key in self.map:
            self.remove(self.map[key])
            self.insert(self.map[key])
            return self.map[key].val
        return -1

    def remove(self, node):
        p, n = node.prev, node.next
        p.next, n.prev = n, p
    
    def insert(self, node):
        p, n = self.most.prev, self.most
        p.next = n.prev = node
        node.next, node.prev = n, p
        
    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])
        self.map[key] = Node(key, value) 
        self.insert(self.map[key])

        if len(self.map) > self.cap:
            lru = self.least.next
            self.remove(lru)
            del self.map[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)