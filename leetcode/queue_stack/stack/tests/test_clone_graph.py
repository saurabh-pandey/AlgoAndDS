import pytest

import queue_stack.stack.clone_graph as prob

def getNode(nodeList, id):
  if id in nodeList:
    return nodeList[id]
  else:
    node = prob.Node(id)
    nodeList[id] = node
    return node


def createGraph(adjList):
  if len(adjList) == 0:
    return None
  # Create graph from adjacency list
  nodeList = {}
  for i in range(len(adjList)):
    id = i + 1
    node = getNode(nodeList, id)
    for neighbourId in adjList[i]:
      neighbourNode = getNode(nodeList, neighbourId)
      node.neighbors.append(neighbourNode)
  return nodeList[1]


def getAdjList(node):
  if node is None:
    return []
  
  nodeList = {}
  nodes = [node]
  while len(nodes) > 0:
    node = nodes.pop(0)
    nodeList[node.val] = []
    for neighbour in node.neighbors:
      nodeList[node.val].append(neighbour.val)
      if neighbour.val not in nodeList:
        nodes.append(neighbour)
  
  adjList = []
  for id, neighbours in sorted(nodeList.items()):
    adjList.append([])
    for n in neighbours:
      adjList[id - 1].append(n)
  return adjList


class TestCloneGraph:
  def test_example1(self):
    adjList = [[2,4],[1,3],[2,4],[1,3]]
    node = createGraph(adjList)
    clonedNode = prob.cloneGraph(node)
    assert getAdjList(clonedNode) == adjList
  

  def test_example2(self):
    adjList = [[]]
    node = createGraph(adjList)
    clonedNode = prob.cloneGraph(node)
    assert getAdjList(clonedNode) == adjList
  

  def test_example3(self):
    adjList = []
    node = createGraph(adjList)
    clonedNode = prob.cloneGraph(node)
    assert getAdjList(clonedNode) == adjList
  

  def test_example5(self):
    adjList = [[2],[1]]
    node = createGraph(adjList)
    clonedNode = prob.cloneGraph(node)
    assert getAdjList(clonedNode) == adjList