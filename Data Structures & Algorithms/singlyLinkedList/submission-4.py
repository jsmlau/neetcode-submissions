class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        lst = self.getValues()
        if not lst or index < 0 or index >= len(lst):
            return -1
        current_index = 0
        current = self.head.next
        previous = self.head
        while current_index <= index:
            if current_index == index:
                return current.val
            prev = current
            current = current.next
            current_index += 1
        

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node


    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = new_node


    def remove(self, index: int) -> bool:
        lst = self.getValues()
        if not lst or index < 0 or index >= len(lst):
            return False
        curr_index = 0
        curr = self.head.next
        prev = self.head
        while curr_index <= index:
            if curr_index == index:
                if curr == self.tail:
                    self.tail = prev
                prev.next = curr.next
                
            prev = curr
            curr = curr.next
            curr_index += 1
        return True
        

    def getValues(self) -> List[int]:
        lst = []
        if not self.head.next:
            return []
        current = self.head.next
        while current and current.next:
            lst.append(current.val)
            current = current.next
        if current and current.val:
            lst.append(current.val)
            current = current.next
        return lst
        
