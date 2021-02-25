# -*- coding: utf-8 -*-
"""
 iteration reverse the whole link list
"""


class Node(object):
    """
    define a link list node
    """
    def __init__(self, val=0):
        self.val = val
        self.next = None

    # def __str__(self):
    #     return '%s' % self.val


class LinkList(object):

    def __init__(self):

        self.head = None

    def is_empty(self):

        return self.head is None

    def add(self, val):
        _node = Node(val)

        _node.next = self.head

        self.head = _node

    def append(self, val):

        _node = Node(val)

        if self.is_empty():
            self.head = _node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = _node

    def items(self):

        cur = self.head
        while cur is not None:
            yield cur.val
            cur = cur.next

    def traversal(self, head):

        if head is None:
            return []
        res = self.traversal(head.next)
        res.append(head.val)
        return res

    def find(self, val):

        return val in self.traversal(self.head)

    def remove(self, val):

        if not self.find(val):
            return False

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

    def length(self):
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def insert(self, val, index):

        if index <= 0:
            self.add(val)
        elif index >= self.length():
            self.append(val)
        else:
            cur = self.head
            _node = Node(val)

            for i in range(index-1):
                cur = cur.next
            _node.next = cur.next
            cur.next = _node


if __name__ == '__main__':

    link_list = LinkList()
    for i in range(1, 6):
        link_list.append(i)

    link_list.add(0)

    # print link_list.remove(0)
    print link_list.insert('a', 1)

    print link_list.traversal(link_list.head)
