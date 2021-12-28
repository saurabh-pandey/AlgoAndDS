from bst.node import Node

def create(in_list):
    """
    Create a Binary Tree from input list and return root.
    Here the list is of the form [Node, Node.Left, Node.Right] and all null branches are ignored. Thus
    the array is not a complete tree representation
    """
    if len(in_list) == 0:
        return None
    if in_list[0] == None:
        return None
    
    val_queue = in_list[1:]
    root = Node(in_list[0])
    nodes_queue = [root]
    while len(val_queue) > 0:
        leftVal = None if len(val_queue) == 0 else val_queue.pop(0)
        rightVal = None if len(val_queue) == 0 else val_queue.pop(0)

        currNode = nodes_queue.pop(0)
        if leftVal is not None:
            leftNode = Node(leftVal)
            currNode.left = leftNode
            nodes_queue.append(leftNode)
        if rightVal is not None:
            rightNode = Node(rightVal)
            currNode.right = rightNode
            nodes_queue.append(rightNode)
    return root


def toList(root):
    """
    Create a BFS list and from binary tree.
    Here the list is of the form [Node, Node.Left, Node.Right] and all null branches are ignored. Thus
    the array is not a complete tree representation
    """
    if root is None:
        return []
    
    treeList = [root.val]
    nodes_queue = [root]
    while nodes_queue:
        curr_layer_nodes = nodes_queue[:]
        nodes_queue.clear()
        for node in curr_layer_nodes:
            if node.left is not None:
                nodes_queue.append(node.left)
            if node.right is not None:
                nodes_queue.append(node.right)
        if nodes_queue:
            for node in curr_layer_nodes:
                treeList.append(None if node.left is None else node.left.val)
                treeList.append(None if node.right is None else node.right.val)
    while treeList[-1] == None:
        treeList.pop()
    return treeList