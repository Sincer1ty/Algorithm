# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        n = 0
        while head:
            n = (n<<1) | head.val # 왼쪽으로 밀고 or(+)로 현재 노드 값 추가
            head = head.next
        return n