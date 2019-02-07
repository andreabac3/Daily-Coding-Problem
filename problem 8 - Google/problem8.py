#!/bin/python3

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def solve(self):

        if self.left == None and self.right == None:  # if leaf return 1
            return 1
        sum = 0
        if self.left != None and self.right != None:
            if self.right.val == self.left.val == self.val:
                if self.checkSubTree(self.val, self):
                    sum += 1
        if self.left != None:
            sum += self.left.solve()
            if self.left.val == self.val and self.right == None:
                sum += 1
        if self.right != None:
            sum += self.right.solve()
            if self.right.val == self.val and self.left == None:
                sum += 1
        return sum

        # check if root or subtree root as both child with the same self value or if one of child is None and other one has the same value of it self.

    def checkSubTree(self, value, root):
        if root.left == None and root.right == None:  # base case
            return True
        if root.left != None and root.right != None:
            if root.left.val == root.right.val == value:
                return self.checkSubTree(value, root.left) and self.checkSubTree(value, root.right)
            else:
                return False
        if root.left != None:
            if root.left.val == value:
                return self.checkSubTree(value, root.left)
            else:
                return False
        elif root.right != None:
            if root.right.val == value:
                return self.checkSubTree(value, root.right)
            else:
                return False


tree = Node(0, Node(1), Node(0,
                             Node(1, Node(1), Node(1)), Node(0)))

print(tree.solve())

tree = Node(1, Node(1),
            Node(1, Node(1, Node(1), Node(1)), Node(1)))
print(tree.solve())

tree = Node(1,
            Node(1, Node(1, Node(1), Node(1)), Node(1)))
print(tree.solve())
