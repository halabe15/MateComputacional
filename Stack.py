class Stack:
    def __init__(self):
        self.items = []

    def __str__(self):
        str = "\n----------------------Start----------------------\n"
        for element in self.items:
            str = str + "->" + element
        str = str + "\n----------------------End----------------------\n"
        return str

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
