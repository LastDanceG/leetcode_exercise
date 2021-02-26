# -*- coding: utf-8 -*-
"""
反转链表的前n个节点
给定一个区间[m, n],只反转区间内的链表元素
"""


class Node(object):

    def __init__(self, val=0):
        self.val = val
        self.next = None


class LinkList(object):

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def length(self):
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def add(self, val):
        _node = Node(val)
        _node.next = self.head
        self.head = _node

    def append(self, val):
        node = Node(val)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def remove(self, val):
        cur = self.head
        pre = None

        while cur is not None:
            if cur.val == val:
                if not pre:
                    self.head = cur.next
                else:
                    pre.next = cur.next
                return True
            else:
                pre = cur
                cur = cur.next

    def insert(self, val, index):

        if index <= 0:
            self.add(val)
        elif index >= self.length():
            self.append(val)
        else:
            _node = Node(val)
            cur = self.head
            for i in range(index-1):
                cur = cur.next
            _node.next = cur.next
            cur.next = _node


def recursion_reverse_all_link_list(head):
    if head is None or head.next is None:
        return head
    last = recursion_reverse_all_link_list(head.next)
    head.next.next = head
    head.next = None
    return last


def iteration_reverse_all_link_list(head):
    cur = head
    pre = None
    while cur is not None:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return pre


def item(head):
    res = []
    cur = head
    while cur is not None:
        res.append(cur.val)
        cur = cur.next
    return res


class ReverseLinkList(object):

    def __init__(self):
        self.successor = None

    def reverse_link_list_top_n(self, head, n):
        """
        反转列表的前n个节点
        """
        if n == 1:
            self.successor = head.next
            return head
        last = self.reverse_link_list_top_n(head.next, n - 1)
        head.next.next = head
        head.next = self.successor
        return last

    def reverse_link_list_between(self, head, m, n):
        """
        给定一个区间[m, n],只反转区间内的链表元素
        """
        if m == 1:
            return self.reverse_link_list_top_n(head, n)
        else:
            head.next = self.reverse_link_list_between(head.next, m - 1, n - 1)
            return head


if __name__ == '__main__':

    link_list = LinkList()

    for i in range(1, 6):
        link_list.append(i)

    # link_list.insert('a', 3)

    print item(link_list.head)

    # print item(recursion_reverse_all_link_list(link_list.head))

    print item(ReverseLinkList().reverse_link_list_between(link_list.head, 2, 4))




