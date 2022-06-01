
import sys
class Node():
    def __init__(self, data):
        self.data = data  # holds the key
        self.parent = None #pointer to the parent
        self.left = None  #pointer to left child
        self.right = None #pointer to right child
        self.color = 1 # 1 for Red, 2 for black

class RedBlackTree():
            def __init__(self):
                self.nill = Node(0)
                self.nill.color = 0
                self.nill.left = None
                self.nill.right = None
                self.root = self.nill

            def insertion(self, key):
                node = Node(key)
                node.parent = None
                node.val = key
                node.left = self.nill
                node.right = self.nill
                node.color = 1
                parent = None
                root = self.root
                while root != self.nill:
                    parent = root
                    if node.val < root.val:
                        root = root.left
                    else:
                        root = root.right
                node.parent = parent
                if parent == None:
                    self.root = node
                elif node.val < parent.val:
                    parent.left = node
                else:
                    parent.right = node
                if node.parent == None:
                    node.color = 2
                    return
                if node.parent.parent == None:
                    return
                self.fix_insertion(node)

            def fix_insertion(self, node):
                while node.parent.color == 1:
                    if node.parent == node.parent.parent.right:
                        uncle = node.parent.parent.left
                        if uncle.color == 1:
                            uncle.color = 2
                            node.parent.color = 2
                            node.parent.parent.color = 1
                            node = node.parent.parent
                        else:
                            if node == node.parent.left:
                                node = node.parent
                                self.rightRotate(node)
                            node.parent.color = 2
                            node.parent.parent.color = 1
                            self.leftRotate(node.parent.parent)
                    else:
                        uncle = node.parent.parent.right
                        if uncle.color == 1:
                            uncle.color = 2
                            node.parent.color = 2
                            node.parent.parent.color = 1
                            node = node.parent.parent
                        else:
                            if node == node.parent.right:
                                node = node.parent
                                self.leftRotate(node)
                            node.parent.color = 2
                            node.parent.parent.color = 1
                            self.rightRotate(node.parent.parent)
                    if node == self.root:
                        break
                self.root.color = 2

            def leftRotate(self, x):
                y = x.right
                x.right = y.left
                if y.left != self.nill:
                    y.left.parent = x
                y.parent = x.parent
                if x.parent == None:
                    self.root = y
                elif x == x.parent.left:
                    x.parent.left = y
                else:
                    x.parent.right = y
                y.left = x
                x.parent = y

            def rightRotate(self, x):
                y = x.left
                x.left = y.right
                if y.right != self.nill:
                    y.right.parent = x

                y.parent = x.parent
                if x.parent == None:
                    self.root = y
                elif x == x.parent.right:
                    x.parent.right = y
                else:
                    x.parent.left = y
                y.right = x
                x.parent = y

            def searchTree(self, node, key):
                if node == self.nill or key == node.data:
                    return node.data
                if key < node.data:
                    return self.searchTree(node.left, key)
                return self.searchTree(node.right, key)

            def size(self,node):
                if node == self.nill:
                    return 0
                else:
                    return (self.size(node.left) + 1 + self.size(node.right))

            def maxDepth(self,node):
                if node == self.nill:
                    return -1

                else:
                    lDepth = self.maxDepth(node.left)
                    rDepth = self.maxDepth(node.right)

                    if (lDepth > rDepth):
                        return lDepth + 1
                    else:
                        return rDepth + 1
            def getroot(self):
               return self.root

if __name__ == '__main__':
    rbt = RedBlackTree()
    dictf = open('EN-US-Dictionary.txt', 'r')
    dictionary = dictf.read().splitlines()
    for key in dictionary:
        key=key.lower()
        rbt.insertion(key)
    x = 1
    while x != 0:
        x = input("1-Insert\n 2-Search\n 3-Print height\n 4-Print size\n 0-Exit\n")
        x = int(x)
        if x == 1:
            word = input("Insert Word: ")
            word = word.lower()
            if rbt.searchTree(rbt.getroot(),word) == 0:
                rbt.insertion(word)
                print("Insertion done")
                h = rbt.maxDepth(rbt.getroot())
                print("Height = ", h)
                s = rbt.size(rbt.getroot())
                print("Size = ", s)
            else:
                print("Word already exist")
        elif x == 2:
            word = input("Insert Word you want to lookup: ")
            word = word.lower()
            if rbt.searchTree(rbt.getroot(),word) == 0:
                print("Word you looking up is not existed")
            else:
                print("Word you looking up exists")
        elif x == 3:
            h = rbt.maxDepth(rbt.getroot())
            print("Height = ", h)
        elif x == 4:
            s = rbt.size(rbt.getroot())
            print("Size = ", s)
        elif x == 0:
            break