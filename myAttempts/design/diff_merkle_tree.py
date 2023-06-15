from design.merkle_tree import MerkleTree, Node

def diff(tree0: MerkleTree, tree1: MerkleTree) -> None:
    def is_child(node: Node) -> bool:
        return not node.left and not node.right
    def diff_recursive(node0: Node, node1: Node) -> None:
        if node0.hash_val == node1.hash_val:
            # If hash match don't continue on this path
            return
        if node0.is_cloned and node0.is_cloned:
            # If cloned nodes don't continue on this path
            return
        if is_child(node0) and is_child(node1):
            # Diff is only possible for leaf nodes
            print(f"DIFF = {node0.content} <=> {node1.content}")
            return
        if node0.left and node1.left:
            diff_recursive(node0.left, node1.left)
        if node0.right and node1.right:
            diff_recursive(node0.right, node1.right)
        else:
            print(f"Error: Unequal trees")
    diff_recursive(tree0.root, tree1.root)
