class Node:
    def __init__(self, data):
        self.left=None
        self.right=None
        self.data=None
    def insert(self, data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                   self.right=Node(data)
                else:
                   self.right.insert(data)

        else:
            self.data=data
    def printtree(self):
        if self.left:
            self.left.printtree()
        print(self.data)
        if self.right:
            self.right.printtree()
root=Node(12)
root.insert(6)
root.insert(3)
root.insert(13)
root.insert(2)
root.insert(14)
root.printtree()
