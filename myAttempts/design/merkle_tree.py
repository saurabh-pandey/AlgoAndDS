import hashlib

from typing import List, Optional

class Node:
    def __init__(self,
                 left: Optional['Node'],
                 right: Optional['Node'],
                 hash_val: str,
                 content: str) -> None:
        self.left: 'Node' = left
        self.right: 'Node' = right
        self.hash_val: str = hash_val
        self.content: str = content
    
    @staticmethod
    def hash(data: str) -> str:
        return hashlib.sha256(data.encode()).hexdigest()
    
    def clone(self) -> 'Node':
        return Node(self.left,
                    self.right,
                    Node.hash(self.content),
                    self.content)
    
class MerkleTree:
    def __init__(self, values: List[str]) -> None:
        leaves: List[Node] = [Node(None, None, Node.hash(v), v) for v in values]
        self.root: Node = self._build_tree(leaves)
    
    def _build_tree(self, nodes: List[Node]) -> Node:
        if len(nodes) % 2 == 1:
            nodes.append(nodes[-1].clone())
        if len(nodes) == 2:
            return Node(nodes[0],
                        nodes[1],
                        Node.hash(nodes[0].hash_val + nodes[1].hash_val),
                        nodes[0].content + ":" + nodes[1].content)
        half = len(nodes) // 2
        left_node = self._build_tree(nodes[:half])
        right_node = self._build_tree(nodes[half:])
        return Node(left_node,
                    right_node,
                    Node.hash(left_node.hash_val + right_node.hash_val),
                    left_node.content + ":" + right_node.content)
