class Node(object):
    id = 1
    def __init__(self):
        self.metadata = []
        self.children = []
        self.id = Node.id
        Node.id += 1

    def read (self, buf):
        n_children = buf.pop()
        n_metadata = buf.pop()
        print ("reading id {}, {} children, {} metadata".format(self.id, n_children, n_metadata))
        for i in range(n_children):
            child = Node()
            child.read(buf)
            self.children.append(child)
        self.metadata = [buf.pop() for i in range(n_metadata)]

    def print (self, level):
        print ('\t'*level, self.id, self.metadata)
        for n in self.children:
            n.print(level+1)

    def checksum(self):
        return sum(self.metadata) + sum([n.checksum() for n in self.children])

    def value(self):
        if not self.children:
            return sum(self.metadata)
        else:
            return sum([self.children[i-1].value() for i in self.metadata if 0 < i <= len(self.children)])

data = list(map(int, """2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2""".split(" ")))[::-1]
with open("day08.txt", "r") as f:
    data = list(map(int, f.read().split(" ")))[::-1]

n = Node()
n.read(data)

n.print(0)
print (n.checksum())
print (n.value())