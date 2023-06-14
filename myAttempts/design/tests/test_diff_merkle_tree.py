import pytest

from design.merkle_tree import MerkleTree
from design.diff_merkle_tree import diff


class TestDiffMerkleTree:
    def test_example1(self):
        data0 = ["a", "b", "c", "d"]
        tree0 = MerkleTree(data0)
        data1 = ["a", "b", "e", "d"]
        tree1 = MerkleTree(data1)
        diff(tree0, tree1)

        data0 = ["a", "b", "c", "d"]
        tree0 = MerkleTree(data0)
        data1 = ["a", "b", "c", "e"]
        tree1 = MerkleTree(data1)
        diff(tree0, tree1)
        
    def test_example2(self):
        data0 = ["a", "b", "c"]
        tree0 = MerkleTree(data0)
        data1 = ["a", "b", "d"]
        tree1 = MerkleTree(data1)
        diff(tree0, tree1)

        data0 = ["a", "b", "c"]
        tree0 = MerkleTree(data0)
        data1 = ["a", "c", "c"]
        tree1 = MerkleTree(data1)
        diff(tree0, tree1)
    