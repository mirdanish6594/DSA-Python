class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUcache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.next = self.head

    def _remove(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_front(self, node: Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_front(node)
            return node.value
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_front(node)

        else:
            if len(self.cache) == self.capacity:
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]

            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)

if __name__ == "__main__":
    capacity = int(input("Enter the capacity of LRU cache: "))
    lru = LRUcache(capacity)

    while True:
        command = input("Enter command (put a key value / get key / exit): ").split()
        if command[0] == "put":
            key, value = int(command[1]), int(command[2])
            lru.put(key, value)
            print(f"Put ({key} , {value}) in cache")

        elif command[0] == "get":
            key = int(command[1])
            value = lru.get(key)
            print(f"Value for key {key}: {value}")

        elif command[0] == "exit":
            break

