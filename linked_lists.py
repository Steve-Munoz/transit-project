class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self._size += 1
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        self._size += 1

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def delete(self, data):
        if self.head is None:
            raise ValueError("Cannot delete from empty list")
        if self.head.data == data:
            self.head = self.head.next
            self._size -= 1
            return
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                self._size -= 1
                return
            current = current.next
        raise ValueError(f"{data} not found in list")

    def search(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def size(self):
        return self._size

    def display(self):
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next
        print(" → ".join(nodes) + " → None")


# --- Transit Scenario ---
ll = LinkedList()
ll.append("Route 101")
ll.append("Route 202")
ll.append("Route 302")
ll.prepend("Route 000")
ll.display()
ll.delete("Route 202")
ll.display()
print(ll.search("Route 101"))
print(ll.search("Route 999"))
print(ll.size())