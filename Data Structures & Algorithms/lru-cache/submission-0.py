class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}

        # Dummy nodes
        self.head = Node(None, None)
        self.tail = Node(None, None)

        self.head.next = self.tail
        self.tail.prev = self.head


    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node


    def insert(self, node):
        first = self.head.next

        self.head.next = node
        node.prev = self.head

        node.next = first
        first.prev = node


    def get(self, key: int) -> int:
        if key in self.hashmap:

            node = self.hashmap[key]

            # Move to front (most recently used)
            self.remove(node)
            self.insert(node)

            return node.val

        return -1


    def put(self, key: int, value: int) -> None:

        # Key already exists
        if key in self.hashmap:

            node = self.hashmap[key]

            self.remove(node)

            node.val = value

            self.insert(node)

        # New key
        else:

            node = Node(key, value)

            self.hashmap[key] = node

            self.insert(node)


        # Remove least recently used if capacity exceeded
        if len(self.hashmap) > self.capacity:

            lru_node = self.tail.prev

            self.remove(lru_node)

            del self.hashmap[lru_node.key]