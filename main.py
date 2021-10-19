class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        l_1 = []
        l_2 = []
        while l1:
            l_1.append(l1)
            l1 = l1.next

        while l2:
            l_2.append(l2)
            l2 = l2.next
        num1 = ''
        num2 = ''
        for num in l_1:
            num1 += str(num.val)
        for num in l_2:
            num2 += str(num.val)
        sum_res = str(int(num1[::-1]) + int(num2[::-1]))
        count = len(sum_res) - 1
        a = ListNode(int(sum_res[count]))
        count -= 1
        while count != 0:
            for num in sum_res:
                num = int(num)
                node = ListNode(num, a)
                count -= 1

        return a


if __name__ == '__main__':
    solution = Solution()
    n3 = ListNode(2)
    n2 = ListNode(4, n3)
    n1 = ListNode(3, n2)
    n3_2 = ListNode(5)
    n2_2 = ListNode(6, n3_2)
    n1_2 = ListNode(4, n2_2)
    print(solution.addTwoNumbers(n1, n1_2))
