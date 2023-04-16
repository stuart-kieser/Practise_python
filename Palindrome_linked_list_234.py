# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome(self, head):
        ispalindrome = []
        while head:
            ispalindrome.append(head.val)
            head = head.next
        ispalindrome2 = ispalindrome[::-1]
        if ispalindrome == ispalindrome2:
            return True
        else:
            return False
