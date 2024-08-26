'''your bst here'''
#from TreePrint import pretty_tree






def _pretty_tree_helper(root, curr_index=0):
    if root is None:
        return [], 0, 0, 0

    line1 = []
    line2 = []
    node_repr = str(root.key)

    new_root_width = gap_size = len(node_repr)
    
    # Get the left and right sub-boxes, their widths, and root repr positions
    l_box, l_box_width, l_root_start, l_root_end = _pretty_tree_helper(root.left, 2 * curr_index + 1)
    r_box, r_box_width, r_root_start, r_root_end = _pretty_tree_helper(root.right, 2 * curr_index + 2)

    # Draw the branch connecting the current root to the left sub-box
    # Pad with whitespaces where necessary
    if l_box_width > 0:
        l_root = (l_root_start + l_root_end) // 2 + 1
        line1.append(' ' * (l_root + 1))
        line1.append('_' * (l_box_width - l_root))
        line2.append(' ' * l_root + '/')
        line2.append(' ' * (l_box_width - l_root))
        new_root_start = l_box_width + 1
        gap_size += 1
    else:
        new_root_start = 0

    # Draw the representation of the current root
    line1.append(node_repr)
    line2.append(' ' * new_root_width)

    # Draw the branch connecting the current root to the right sub-box
    # Pad with whitespaces where necessary
    if r_box_width > 0:
        r_root = (r_root_start + r_root_end) // 2
        line1.append('_' * r_root)
        line1.append(' ' * (r_box_width - r_root + 1))
        line2.append(' ' * r_root + '\\')
        line2.append(' ' * (r_box_width - r_root))
        gap_size += 1
    new_root_end = new_root_start + new_root_width - 1

    # Combine the left and right sub-boxes with the branches drawn above
    gap = ' ' * gap_size
    new_box = [''.join(line1), ''.join(line2)]
    for i in range(max(len(l_box), len(r_box))):
        l_line = l_box[i] if i < len(l_box) else ' ' * l_box_width
        r_line = r_box[i] if i < len(r_box) else ' ' * r_box_width
        new_box.append(l_line + gap + r_line)

    # Return the new box, its width and its root positions
    return new_box, len(new_box[0]), new_root_start, new_root_end
    
def pretty_tree(tree):
    lines = _pretty_tree_helper(tree.root, 0)[0]
    return '\n' + '\n'.join((line.rstrip() for line in lines))










class Node:
    def __init__(self, key):
        self.key = key #can also be a string
        self.right = None
        self.left = None

class BST:

    def __init__(self):
        self.root = None
        #self.size = 0

    def size(self):
        return self._size(self.root)
    
    def _size(self, node):
        if node == None:
            return 0
        else:
            return 1 + self._size(node.left) + self._size(node.right)

    def is_empty(self):
        if self.root == None:
            return True

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return -1
        else:
            return 1+ max(self._height(node.left), self._height(node.right))

    def add(self, item):
        if self.root == None:
            self.root = Node(item)
            return self
        else:
            curr_node = self.root
            while curr_node != None:
                if item < curr_node.key:
                    if curr_node.left == None:
                        curr_node.left = Node(item)
                        curr_node = None
                    else:
                        curr_node = curr_node.left
                        

                else: #itme > curr_node.key 
                    if curr_node.right == None:
                        curr_node.right = Node(item)
                        curr_node = None
                    else:
                        curr_node = curr_node.right
        return self

    def __str__(self):
        return pretty_tree(self)


    def remove(self, key):
        prev_node = None
        curr_node = self.root
        while curr_node != None: 
            if curr_node.key == key:

                if curr_node.left == None and curr_node.right == None: #case 1, node is leaf
                    if prev_node == None: #Node is root
                        self.root = None
                    elif prev_node.left is curr_node: #Figuring out which direction to sever
                        prev_node.left = None
                    else: #if prev_node.right is curr_node:
                        prev_node.right = None
                    return #self?
                
                elif curr_node.left != None and curr_node.right == None: #case 2, only one child, left
                    if prev_node == None: #Node is root
                        self.root = curr_node.left #keep going where possisble
                    elif prev_node.left == curr_node:
                        prev_node.left = curr_node.left
                    else:
                        prev_node.left = curr_node.left
                    return
                        
                elif curr_node.left == None and curr_node.right != None: #case 2
                    if prev_node == None:
                        self.root = curr_node.right
                    elif prev_node.left == curr_node:
                        prev_node.left = curr_node.right
                    else:
                        prev_node.right = curr_node.right
                    return

                else: #case 3 I think where the node has 2 kids, find successor, leftmost child of right subtree
                    #left most child of right subtree
                    successor = curr_node.right
                    while successor.left != None:
                        successor = successor.left #keep going left
                    curr_node.key = successor.key
                    prev_node = curr_node
                    curr_node = curr_node.right
                    key = prev_node.key

            elif curr_node.key < key: #search right
                prev_node = curr_node
                curr_node = curr_node.right
            else: #search left
                prev_node = curr_node
                curr_node = curr_node.left
        return #node not found


    def find(self, key): #return the mathced item from the tree (not the node that contains it, and not the item use d as the parameter), if not in tree, Value Error
        curr_node = self.root
        while curr_node != None:
            if key == curr_node.key:
                return curr_node.key
            elif key < curr_node.key:
                curr_node = curr_node.left
            else: #key > curr_node.key
                curr_node = curr_node.right
        raise ValueError("Item not found")
    
    def inorder(self):
       return self._inorder(self.root)

    def _inorder(self, node):
        result = []
        if node == None:
            return result
        result.extend(self._inorder(node.left))
        result.append(node.key)
        result.extend(self._inorder(node.right))
        return result


    def preorder(self):
        return self._preorder(self.root)

    def _preorder(self, node):
        result = []
        if node == None:
            return result
        result.append(node.key)
        result.extend(self._preorder(node.left))
        result.extend(self._preorder(node.right))
        return result
    
    def postorder(self):
        return self._postorder(self.root)

    def _postorder(self, node):
        result = []
        if node == None:
            return result
        result.extend(self._postorder(node.left))
        result.extend(self._postorder(node.right))
        result.append(node.key)
        return result

