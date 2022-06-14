from Abstract import CSVPrice


class TreeNode:
    def __init__(self, key, leftPtr=None, rightPtr=None):
        self.key = key
        self.leftPtr = leftPtr
        self.rightPtr = rightPtr
        

class UpdateCSV(CSVPrice):
    def __init__(self):
        self.root = None
        

    def buildTree(self, data, price):
        mid = len(data)//2
        if not data: return
        root = TreeNode(data[mid][price])
        

        leftTree =  data[:mid]
        rightTree = data[mid+1:]

        root.leftPtr = self.buildTree(leftTree,price)
        root.rightPtr = self.buildTree(rightTree,price)

        return root
    
    def minPrice(self, root):
        current = root

        while current.leftPtr != None:
            current = current.leftPtr

            return current.key



    
    def csvPrice(self,root):
        # using inorder traversal
        if not root: return
        self.csvPrice(root.leftPtr)
        print(root.key)
        self.csvPrice(root.rightPtr)

    