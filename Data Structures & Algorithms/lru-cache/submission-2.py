class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()

        self.head = Node()
        self.tail = Node()
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert_at_tail(self, node):
        previous = self.tail.prev
        
        previous.next = node
        node.prev = previous

        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key] # new {key, value} pair

        # remove existing node from leftmost and add to rightmost in the list
        self.remove(node)
        self.insert_at_tail(node)

        return node.value


    def put(self, key: int, value: int) -> None:
        # If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key
        # A key is considered used if get or a put is called on it
        if key in self.cache:
            node = self.cache[key]
            node.value = value

            # remove existing node from leftmost and add to rightmost in the list
            self.remove(node)
            self.insert_at_tail(node)

            return
        else:
            node = Node(key, value)
            self.cache[key] = node

            self.insert_at_tail(node)

            if len(self.cache) > self.capacity:
                least_recent = self.head.next
                self.remove(least_recent)
                del self.cache[least_recent.key]
