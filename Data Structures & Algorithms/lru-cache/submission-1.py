

class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def insert_at_head(self, node: Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self.insert_at_head(node)
            return node.val
        return -1

    def put(self, key: int, val: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            node.val = val
            self.insert_at_head(node)
        else:
            node = Node(key, val)
            self.insert_at_head(node)
            self.cache[key] = node

        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
