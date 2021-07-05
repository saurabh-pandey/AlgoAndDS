from leetcode.queue_stack.stack.clone_graph import cloneGraph
import pytest

import queue_stack.stack.clone_graph as prob

def createGraph(adjList):
  # Create graph from adjacency list
  rootNode = prob.Node(1)
  for i in range(len(adjList)):
    pass
  return rootNode


def getAdjList(node):
  adjList = []
  return adjList


class TestCloneGraph:
  def test_example1(self):
    adjList = [[2,4],[1,3],[2,4],[1,3]]
    node = createGraph(adjList)
    clonedNode = prob.cloneGraph(node)
    assert getAdjList(clonedNode) == adjList