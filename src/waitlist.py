class _Node:
    __slots__ = ("name", "next")
    def __init__(self, name, next=None):
        self.name = name
        self.next = next


class Waitlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __len__(self):
        """Return number of people on the waitlist."""
        return self._size

    def to_list(self):
        """Return names from head to tail as a Python list."""
        names = []
        curr = self.head
        while curr:
            names.append(curr.name)
            curr = curr.next
        return names

    def join(self, name):
        """Append name at the tail (O(1))."""
        node = _Node(name)
        if self.tail is None:   # empty list
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self._size += 1

    def find(self, name):
        """Return True if name exists, else False."""
        curr = self.head
        while curr:
            if curr.name == name:
                return True
            curr = curr.next
        return False

    def cancel(self, name):
        """Remove first occurrence; return True if removed."""
        prev, curr = None, self.head
        while curr:
            if curr.name == name:
                # unlink
                if prev is None:   # removing head
                    self.head = curr.next
                else:
                    prev.next = curr.next

                if curr is self.tail:  # removed tail
                    self.tail = prev

                self._size -= 1
                return True
            prev, curr = curr, curr.next
        return False

    def bump(self, name):
        """Move first occurrence to the head; return True if moved."""
        if self.head is None or self.head.name == name:
            return bool(self.head and self.head.name == name)

        prev, curr = None, self.head
        while curr:
            if curr.name == name:
                # unlink from current spot
                if prev:
                    prev.next = curr.next
                if curr is self.tail:
                    self.tail = prev
                # move to head
                curr.next = self.head
                self.head = curr
                return True
            prev, curr = curr, curr.next
        return False
