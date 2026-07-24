# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        def traverseAndStore(head):
            number = ""
            currentNode = head
            while currentNode:
                number = str(currentNode.val) + number
                currentNode = currentNode.next
            return int(number)
    
        addedList = traverseAndStore(l1) + traverseAndStore(l2)

        def createList(convert):
            digits = str(convert)
            digits = digits[::-1]
            head = None
            current = None

            for x in range(len(digits)):
                digit = digits[x]
                
                new_node = ListNode(int(digit))

                if head == None:
                    head = new_node
                    current = new_node
                else:
                    current.next = new_node
                    current = current.next

            return head
        
        result = createList(addedList)
        return result