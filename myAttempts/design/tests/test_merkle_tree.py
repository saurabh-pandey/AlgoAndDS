import pytest

from design.merkle_tree import MerkleTree


class TestMerkleTree:
    def test_example1(self):
        data = ["a", "b", "c", "d"]
        merkle_tree = MerkleTree(data)
        print()
        print(merkle_tree.root.hash_val)
        print(merkle_tree.root.content)
        print(merkle_tree.root.left.hash_val)
        print(merkle_tree.root.left.content)
        print(merkle_tree.root.right.hash_val)
        print(merkle_tree.root.right.content)
        print(merkle_tree.root.left.left.hash_val)
        print(merkle_tree.root.left.left.content)
        print(merkle_tree.root.left.right.hash_val)
        print(merkle_tree.root.left.right.content)
        print(merkle_tree.root.right.left.hash_val)
        print(merkle_tree.root.right.left.content)
        print(merkle_tree.root.right.right.hash_val)
        print(merkle_tree.root.right.right.content)
    
    def test_example2(self):
        data = ["a", "b", "e", "d"]
        merkle_tree = MerkleTree(data)
        print()
        print(merkle_tree.root.hash_val)
        print(merkle_tree.root.content)
        print(merkle_tree.root.left.hash_val)
        print(merkle_tree.root.left.content)
        print(merkle_tree.root.right.hash_val)
        print(merkle_tree.root.right.content)
        print(merkle_tree.root.left.left.hash_val)
        print(merkle_tree.root.left.left.content)
        print(merkle_tree.root.left.right.hash_val)
        print(merkle_tree.root.left.right.content)
        print(merkle_tree.root.right.left.hash_val)
        print(merkle_tree.root.right.left.content)
        print(merkle_tree.root.right.right.hash_val)
        print(merkle_tree.root.right.right.content)
    
    def test_example3(self):
        data = ["a", "b", "c"]
        merkle_tree = MerkleTree(data)
        print()
        print(merkle_tree.root.hash_val)
        print(merkle_tree.root.content)
        print(merkle_tree.root.left.hash_val)
        print(merkle_tree.root.left.content)
        print(merkle_tree.root.right.hash_val)
        print(merkle_tree.root.right.content)
        print(merkle_tree.root.left.left.hash_val)
        print(merkle_tree.root.left.left.content)
        print(merkle_tree.root.left.right.hash_val)
        print(merkle_tree.root.left.right.content)
        print(merkle_tree.root.right.left.hash_val)
        print(merkle_tree.root.right.left.content)
        print(merkle_tree.root.right.right.hash_val)
        print(merkle_tree.root.right.right.content)
    
    def test_example4(self):
        data = ["a", "b", "e"]
        merkle_tree = MerkleTree(data)
        print()
        print(merkle_tree.root.hash_val)
        print(merkle_tree.root.content)
        print(merkle_tree.root.left.hash_val)
        print(merkle_tree.root.left.content)
        print(merkle_tree.root.right.hash_val)
        print(merkle_tree.root.right.content)
        print(merkle_tree.root.left.left.hash_val)
        print(merkle_tree.root.left.left.content)
        print(merkle_tree.root.left.right.hash_val)
        print(merkle_tree.root.left.right.content)
        print(merkle_tree.root.right.left.hash_val)
        print(merkle_tree.root.right.left.content)
        print(merkle_tree.root.right.right.hash_val)
        print(merkle_tree.root.right.right.content)

