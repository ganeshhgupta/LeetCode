class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val

        # CHANGED: track frequency
        self.freq = 1

        self.prev, self.next = None, None


class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity

        self.map = {}

        # NEW: frequency -> DLL
        self.freqMap = {}
        
        # NEW: minimum frequency currently in cache
        self.minFreq = 0


    def get(self, key: int) -> int:

        if key not in self.map:
            return -1

        node = self.map[key]

        # CHANGED: update frequency instead of just moving to MRU
        self.updateFreq(node)

        return node.val


    def put(self, key: int, value: int) -> None:

        if self.cap == 0:
            return

        if key in self.map:

            node = self.map[key]
            node.val = value

            # CHANGED: update frequency
            self.updateFreq(node)

            return

        # NEW: evict from minimum-frequency list
        if len(self.map) >= self.cap:

            lfu = self.freqMap[self.minFreq].least.next

            self.remove(lfu)
            del self.map[lfu.key]

        # NEW: new node starts at frequency 1
        node = Node(key, value)

        self.map[key] = node

        # NEW: add to frequency-1 list
        if 1 not in self.freqMap:
            self.freqMap[1] = DLL()

        self.freqMap[1].insert(node)

        # NEW
        self.minFreq = 1


    # NEW
    def updateFreq(self, node):

        oldFreq = node.freq

        # Remove from old frequency list
        self.freqMap[oldFreq].remove(node)

        # If this was the last node at minFreq,
        # minFreq moves up
        if oldFreq == self.minFreq:
            if self.freqMap[oldFreq].isEmpty():
                self.minFreq += 1

        # Increase frequency
        node.freq += 1
        newFreq = node.freq

        # Create new frequency list if needed
        if newFreq not in self.freqMap:
            self.freqMap[newFreq] = DLL()

        # Add node as most recently used within this frequency
        self.freqMap[newFreq].insert(node)


    # SAME logic as your LRU remove
    def remove(self, node):

        p, n = node.prev, node.next
        p.next, n.prev = n, p


    # SAME logic as your LRU insert
    # BUT now insert into a specific frequency DLL
    def insert(self, node):

        freq = node.freq

        p, n = self.freqMap[freq].most.prev, self.freqMap[freq].most

        p.next = n.prev = node
        node.next, node.prev = n, p


class DLL:

    def __init__(self):

        # NEW: every frequency gets its own DLL
        self.least, self.most = Node(0, 0), Node(0, 0)

        self.least.next = self.most
        self.most.prev = self.least


    # NEW
    def insert(self, node):

        p, n = self.most.prev, self.most

        p.next = n.prev = node
        node.next, node.prev = n, p


    # NEW
    def remove(self, node):

        p, n = node.prev, node.next
        p.next, n.prev = n, p


    # NEW
    def isEmpty(self):

        return self.least.next == self.most