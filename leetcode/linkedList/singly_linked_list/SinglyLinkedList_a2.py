from typing import List

from singly_linked_list.node_a2 import Node

class SinglyLinkedList:
    def __init__(self, lst : List = []) -> None:
        self._head = None
        if lst:
            self._head = Node(lst[0])
            curr = self._head
            for n in lst[1:]:
                curr.next = Node(n)
                curr = curr.next

    def get(self, index: int) -> Node:
        curr = self._head
        depth = 0
        while depth < index:
            if curr.next is None:
                return -1
            curr = curr.next
        return curr.val

    def add(self, index: int, val: int) -> Node:
        if index == 0:
            self._head = Node(val, self._head)
            return self._head
        else:
            curr = self._head
            depth = 0
            while depth < (index - 1):
                if curr.next is None:
                    return None
                else:
                    curr = curr.next
            curr.next = Node(val, curr.next)
            return curr.next


    def delete(self, index: int) -> Node:
        if index == 0:
            deleted_node = self._head
            self._head = self._head.next
            return deleted_node
        else:
            curr = self._head
            depth = 0
            while depth < (index - 1):
                if curr.next is None:
                    return None
                else:
                    curr = curr.next
            deleted_node = curr.next
            curr.next = curr.next.next
            return deleted_node

    def addAtTail(self, val: int) -> Node:
        curr = self._head
        while curr.next is not None:
            curr = curr.next
        curr.next = Node(val)
        return curr.next
    
    def getHeadNode(self):
        # return self._head
        pass
        
    def getTailNode(self):
        # return sll.getTailNode(self._head)
        pass
  
    def addAtHead(self, val):
        # self._head = sll.addAtHead(self._head, val)
        pass
    
    def addAtTail(self, val):
        # self._head = sll.addAtTail(self._head, val)
        pass
    
    def addAtIndex(self, index, val):
        # self._head = sll.addAtIndex(self._head, index, val)
        pass
    def deleteAtIndex(self, index):
        # self._head = sll.deleteAtIndex(self._head, index)
        pass
    
    def toString(self):
        # return sll.toString(self._head)
        pass

