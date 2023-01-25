'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Solution explained:

This code takes in two linked lists, l1 and l2, representing two non-negative integers. 
The digits in each linked list are stored in reverse order, and each node contains a single digit. 
The function addTwoNumbers() iterates through the linked lists.
For each corresponding pair of digits it adds them together and the carry from the previous addition. 
It then updates the carry for the next iteration. 
If one of the linked lists is longer than the other, the function continues to add the remaining digits from the longer list with 0. 
Finally, if there is a carry left over, it creates a new node to store it. The function returns the resulting linked list.

The above example of l1=[2,4,3] and l2=[5,6,4] will return [7,0,8], which is the sum of 342 and 465.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()
    current = dummy
    carry = 0
    while l1 or l2:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        s = x + y + carry
        carry = s // 10
        current.next = ListNode(s % 10)
        current = current.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    if carry > 0:
        current.next = ListNode(carry)
    return dummy.next

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
result = addTwoNumbers(l1, l2)
while result:
    print(result.val, end=' ')
    result = result.next
