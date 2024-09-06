from typing import Optional, Self


class Node:
    prev: Optional[Self]
    next: Optional[Self]

    def __init__(self, key: int, val: int) -> None:
        self.key, self.val = key, val
        self.prev, self.next = None, None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # insert into LINKED LIST (important -- operatins performed with linked list only)
    def _insert(self, node: Node):
        prev, next = self.right.prev, self.right
        prev.next, next.prev = node, node
        node.next, node.prev = next, prev

    # remove from LINKED LIST (important -- operatins performed with linked list only)
    def _remove(self, node: Node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self._remove(self.cache[key])
        self._insert(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, val: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])

        self.cache[key] = Node(key, val)
        self._insert(self.cache[key])
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self._remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
