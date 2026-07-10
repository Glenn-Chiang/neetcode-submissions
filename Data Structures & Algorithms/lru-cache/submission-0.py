class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # Maps keys to nodes
        self.head = Node(0, 0) # Maintain pointer to head of linked list
        self.tail = Node(0, 0) # Maintain pointer to tail of linked list
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    # Insert node at tail
    def insert(self, node: Node) -> None:
        self.tail.prev.next = node
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        # If key in cache, retrieve node from map and update val of node
        if key in self.cache:
            self.remove(self.cache[key])
        
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.insert(new_node)

        # If we add a new node when already at capacity, remove LRU key
        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.remove(lru) # Remove from linked list
            del self.cache[lru.key] # Remove from hash map

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
