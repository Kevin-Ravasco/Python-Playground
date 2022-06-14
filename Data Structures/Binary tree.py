"""
Python implementation for a binary tree
"""


# create a node class for every node in our tree
from platform import node


class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# create our binary tree data structure
class BinaryTree():
    def __init__(self, root):  # assuming root will be a string or integer
        self.root = Node(root)

    def print_tree(self, traversal_type):
        """
        Helper function to print the traversal types
        """
        if traversal_type == 'preorder':
            return self.preorder_print(self.root, '')
        elif traversal_type == 'inorder':
            return self.inorder_print(self.root, '')
        elif traversal_type == 'postorder':
            return self.postorder_print(self.root, '')
        elif traversal_type == 'level_order_traversal':
            return self.level_order_traversal(self.root)
        elif traversal_type == 'reverse_level_order_traversal':
            return self.reverse_level_order_traversal(self.root)
        elif traversal_type == 'height':
            return self.tree_height(self.root)
        else:
            return print('invalid traversal type entered')

    def preorder_print(self, start, output):
        """
        The print sequence is Root > Left > Right
        """
        if start:
            output += (str(start.value) + '-')
            output = self.preorder_print(start.left, output)
            output = self.preorder_print(start.right, output)
        return output

    def inorder_print(self, start, output):
        """
        Traversal sequence: Left > Root > Right
        """
        if start:
            output = self.inorder_print(start.left, output)
            output += (str(start.value) + '-')
            output = self.inorder_print(start.right, output)
        return output

    def postorder_print(self, start, output):
        """
        Traversal sequence: Left > Right > Root
        """
        if start:
            output = self.postorder_print(start.left, output)
            output = self.postorder_print(start.right, output)
            output += (str(start.value) + '-')
        return output

    def level_order_traversal(self, start):
        items = []
        traversal = ''
        if start:
            items.insert(0, start)
            while len(items) > 0:
                traversal += str(items[-1].value)
                node = items.pop()

                if node.left:
                    items.insert(0, node.left)
                if node.right:
                    items.insert(0, node.right)
        return traversal

    def reverse_level_order_traversal(self, start):
        items = []
        final_items = []
        traversal = ''

        items.append(start)
        if start:
            while len(items) > 0:
                node = items.pop()
                final_items.append(node.value)

                if node.left:
                    items.insert(0, node.left)
                if node.right:
                    items.insert(0, node.right)

        final_items.reverse()
        for item in final_items:
            traversal += str(item)
        return traversal

    def tree_height(self, node):
        if node is None:
            return -1
        left_height = self.tree_height(node.left)
        right_height = self.tree_height(node.right)
        return 1 + max(left_height, right_height)

    def size(self):
        if self.root is None:
            return 0

        nodes = []
        nodes.push(self.root)
        size = 1
        while nodes:
            node = nodes.pop()
            if node.left:
                size += 1
                nodes.push(node.right)
            if node.right:
                size += 1
                nodes.append(node.right)

        return


# creating our binary tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)


# Our created Tree visualization

#                       1
#                 /           \
#                2             3
#              /    \        /    \
#             4      5      6      7


# print(tree.print_tree('preorder'))
# print(tree.print_tree('inorder'))
# print(tree.print_tree('postorder'))

# print(tree.print_tree('level_order_traversal'))
# print(tree.print_tree('reverse_level_order_traversal'))
print(tree.print_tree('height'))
