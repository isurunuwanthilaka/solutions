class BSTNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
        if self.data == data:
            return
        elif data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BSTNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BSTNode(data)

    def in_order_traverse(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traverse()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traverse()

        return elements

    def pre_order_traverse(self):
        elements = []

        elements.append(self.data)
        
        if self.left:
            elements += self.left.in_order_traverse()

        if self.right:
            elements += self.right.in_order_traverse()

        return elements

    def post_order_traverse(self):
        elements = []
        
        if self.left:
            elements += self.left.in_order_traverse()

        if self.right:
            elements += self.right.in_order_traverse()

        elements.append(self.data)

        return elements
    
    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data
        
    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data
        
    def search(self,val):
        if self.data == val:
            return True
        elif val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        else:
            if self.right:
                return self.right.search(val)
            else:
                return False

def build_bst(elements):
    root = BSTNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    elements = [7,9,1,90,2,87,23,12]

    root = build_bst(elements)

    print(root.in_order_traverse())
    print(root.pre_order_traverse())
    print(root.post_order_traverse())
    print(root.find_min())
    print(root.find_max())
    print(root.search(87))
    print(root.search(50))
