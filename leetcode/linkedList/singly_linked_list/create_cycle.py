from singly_linked_list.node import Node
import singly_linked_list.operations as sll

def createCycle(head, index):
  tailNode = sll.getTailNode(head)
  toNode = sll.getNode(head, index)
  if tailNode is not None and toNode is not None:
    assert tailNode._next is None
    # Avoid self-loops ??
    assert tailNode is not toNode
    print(f'Creating cycle between {tailNode._val} and {toNode._val}')
    tailNode._next = toNode