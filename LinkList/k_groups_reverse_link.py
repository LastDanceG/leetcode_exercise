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
    pass


def reverse_link_list_all(head):
    """
    反转整个链表
    """
    if head is None or head.next is None:
        return head
    last = reverse_link_list_all(head.next)
    head.next.next = head
    head.next = None
    return last


if __name__ == '__main__':

    link_list = LinkList()

    for i in range(1, 6):

        link_list.append(i)

    # link_list.insert(100, 2)

    print link_list.find(5)

    for i in link_list.item(link_list.head):
        print i,
    print '\n'
    for j in link_list.item(reverse_link_list_all(link_list.head)):
        print j,
