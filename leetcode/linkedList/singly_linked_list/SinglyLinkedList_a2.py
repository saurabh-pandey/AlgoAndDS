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
        if index < 0 or self._head is None:
            return -1
        curr = self._head
        depth = 0
        while depth < index:
            if curr.next is None:
                return -1
            curr = curr.next
            depth += 1
        return curr.val

    def add(self, index: int, val: int) -> Node:
        if index == 0:
            self._head = Node(val, self._head)
            return self._head
        else:
            if self._head is None:
                return None
            else:
                curr = self._head
                depth = 0
                while depth < (index - 1):
                    if curr.next is None:
                        return None
                    else:
                        curr = curr.next
                    depth += 1
                curr.next = Node(val, curr.next)
                return curr.next


    def delete(self, index: int) -> Node:
        if index < 0 or self._head is None:
            return None
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
                depth += 1
            deleted_node = curr.next
            if deleted_node is not None:
                curr.next = curr.next.next
            return deleted_node

    def addAtTail(self, val: int) -> Node:
        if self._head is None:
            self._head = Node(val)
            return self._head
        else:
            curr = self._head
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(val)
            return curr.next
    
    def getHeadNode(self) -> Node:
        # return self._head
        pass
        
    def getTailNode(self) -> Node:
        # return sll.getTailNode(self._head)
        pass
  
    def addAtHead(self, val) -> Node:
        return self.add(0, val)
    
    def addAtIndex(self, index, val) -> Node:
        return self.add(index, val)
    
    def deleteAtIndex(self, index) -> Node:
        return self.delete(index)
    
    def toString(self):
        # return sll.toString(self._head)
        s = ""
        curr = self._head
        while curr is not None:
            s += str(curr.val)
            if curr.next is not None:
                s += "->"
            curr = curr.next
        return s

