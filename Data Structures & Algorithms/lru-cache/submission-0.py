class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
    
    def remove(self, node): # remove from left
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        node.prev, node.next = None, None

    def insert(self, node): # add to the right
        prev = self.right.prev
        prev.next, self.right.prev = node, node
        node.prev, node.next = prev, self.right

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            del self.cache[key]
        node = Node(key, value)
        self.insert(node)
        self.cache[key] = node

        if len(self.cache) > self.cap:
            node = self.left.next
            del self.cache[node.key]
            self.remove(node)
