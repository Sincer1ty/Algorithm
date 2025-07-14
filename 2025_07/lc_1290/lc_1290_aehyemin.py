# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        ans = []
        #연결리스트의 10진수를 반환
        while head:
            ans.append(head.val)
            head = head.next
        new_ans = "".join(str(i) for i in ans)

        return int(new_ans, 2)
            

        