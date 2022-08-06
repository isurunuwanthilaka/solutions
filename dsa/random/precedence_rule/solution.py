class Node:
    def __init__(self, v=None):
        self.p = None
        self.v = v
        self.n = None


class NodeList:
    def __init__(self):
        self.v = []

    def getNode(self, i):
        for n in self.v:
            if n.v == i:
                return n
        r = Node(i)
        self.v.append(r)
        return r

    def listPrint(self):
        current = None
        for i in self.v:
            if i.p is None:
                current = i
                break
        result = ''
        while current is not None:
            result += current.v
            current = current.n

        return result


def findWord(list):
    nodes = NodeList()

    for item in list:
        l, r = item.split('>')
        lNode = nodes.getNode(l)
        rNode = nodes.getNode(r)
        lNode.n = rNode
        rNode.p = lNode

    return nodes.listPrint()


print(findWord(["P>E", "E>R", "R>U"]))
print(findWord(["I>N", "A>I", "P>A", "S>P"]))
print(findWord(["U>N", "G>A", "R>Y", "H>U", "N>G", "A>R"]))
print(findWord(["I>F", "W>I", "S>W", "F>T"]))
print(findWord(["R>T", "A>L", "P>O", "O>R", "G>A", "T>U", "U>G"]))
print(findWord(["W>I", "R>L", "T>Z", "Z>E",
      "S>W", "E>R", "L>A", "A>N", "N>D", "I>T"]))

# concept: singly linked lists
