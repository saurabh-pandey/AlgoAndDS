
def createCycleSLL(sll, index):
    tailNode = sll.getTailNode()
    toNode = sll.getNode(index)
    if tailNode is not None and toNode is not None:
      assert tailNode is not toNode
      assert tailNode._next is None
      print(f'Creating cycle between {tailNode._val} and {toNode._val}')
      tailNode._next = toNode