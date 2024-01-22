"""
File: new_head.py
Name: Yvonne Chan
------------------------
Rearranges the ListNode by the order that
the nodes which is smaller than x will be linked first without changing the original order
and the nodes which is bigger than or equals to x will be linked then.
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def new_head(head: ListNode, x: int) -> ListNode:
    cur = head
    small = []
    big = []

    while cur:
        if cur.val < x:
            small.append(cur.val)
        else:
            big.append(cur.val)
        cur = cur.next
    s_b = small + big

    head, cur = None, None
    for i in range(len(s_b)):
        new_node = ListNode(s_b[i], None)
        if not head:
            head = new_node
            cur = head
        else:
            cur.next = new_node
            cur = cur.next
    return head

    # smaller, bigger = ListNode(), ListNode()
    # cur, small_cur, big_cur = head, smaller, bigger
    #
    # while cur:  # is not None
    #     if cur.val < x:
    #         small_cur.next = cur  # 因為小於X, 所以存到小的ListNode
    #         cur = cur.next  # cur往前
    #         small_cur = small_cur.next  # 小cur往前
    #
    #     else:
    #         big_cur.next = cur
    #         cur = cur.next
    #         big_cur = big_cur.next
    #
    # # 小串跟大串連起來
    # small_cur.next = bigger.next
    # big_cur.next = None
    #
    # return smaller.next


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 new_head.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(9, None)
            l1.next = ListNode(6, None)
            l1.next.next = ListNode(3, None)
            l1.next.next.next = ListNode(8, None)
            ans = new_head(l1, 8)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(1, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l1.next.next.next = ListNode(2, None)
            l1.next.next.next.next = ListNode(5, None)
            l1.next.next.next.next.next = ListNode(1, None)
            ans = new_head(l1, 3)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 new_head.py test1"')


if __name__ == '__main__':
    main()
