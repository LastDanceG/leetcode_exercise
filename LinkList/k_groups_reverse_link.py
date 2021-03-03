# -*- coding: utf-8 -*-

from LinkList import Node


class LinkList(object):

    def __init__(self):

        self.head = None

    def length(self):
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def is_empty(self):
        return self.head is None

    def add(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node

    def append(self, val):
        node = Node(val)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def item(self, head):
        cur = head
        while cur is not None:
            yield cur.val
            cur = cur.next

    def insert(self, val, index):
        if index <= 0:
            self.add(val)
        elif index >= self.length():
            self.append(val)
        else:
            cur = self.head
            node = Node(val)
            for i in range(index - 1):
                cur = cur.next
            node.next = cur.next
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

    def find(self, val):
        return val in self.item(self.head)


class ReverseLinkList(object):

    def __init__(self):
        self.successor = None

    def reverse_link_top_n(self, head, n):
        """
        反转链表的前n个
        """
        if n == 1:
            self.successor = head.next
            return head
        last = self.reverse_link_top_n(head.next, n-1)
        head.next.next = head
        head.next = self.successor
        return last

    def reverse_link_list_all(self, head):
        """
        反转整个链表
        """
        if head is None or head.next is None:
            return head
        last = self.reverse_link_list_all(head.next)
        head.next.next = head
        head.next = None
        return last

    def reverse_link_list_between(self, head, m, n):
        """
        反转给定区间内的链表
        """
        if m == 1:
            return self.reverse_link_top_n(head, n)
        else:
            head.next = self.reverse_link_list_between(head.next, m - 1, n - 1)
            return head


if __name__ == '__main__':

    link_list = LinkList()

    for i in range(1, 11):

        link_list.append(i)

    # link_list.insert(100, 2)

    # print link_list.find(5)

    for i in link_list.item(link_list.head):
        print i,
    print '\n'
    for j in link_list.item(ReverseLinkList().reverse_link_list_between(link_list.head, 1, 3)):
        print j,
