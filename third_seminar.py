class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack():
    def __init__(self):
        self.head = Node("head")

    def __str__(self):
        # первый элемент
        cur = self.head.next
        out = ''
        sep = '->'
        while cur:
            out += f"{cur.value}{sep}"
            cur = cur.next
        out = out[:-2]
        return out

    def push(self, value):
        new_element = Node(value)
        new_element.next = self.head.next
        self.head.next = new_element

    def pop(self):
        tmp = self.head.next.value
        # del self.next в C++
        self.head.next = self.head.next.next
        return tmp


class PersistentStack(Stack):
    def __init__(self):
        self.backups = []
        super().__init__()

    def backup(self):
        tmp = PersistentStack()
        tmp.head.next = self.head.next
        self.backups.append(tmp)

    def get_backup(self, i):
        return self.backups[i]

    def push(self, value):
        self.backup()
        super().push(value)

    def pop(self):
        self.backup()
        return super().pop()

s = PersistentStack()
for i in range(5):
    s.push(i)
print(f'Stack: {s}')
print(f'Pop {s.pop()}')
print(f"Stack: {s}")
print(f"Backups:")
for i in range(5):
    print(s.get_backup(i))