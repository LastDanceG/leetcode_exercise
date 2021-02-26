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


def iteration_reverse(head):

    # 申请两个节点，并初始化，cur为当前节点，即头节点，pre指向None
    cur = head
    pre = None

    # 遍历链表
    while cur is not None:

        # 将当前节点的下一个节点指向tmp
        tmp = cur.next
        # 然后将当前节点的next指向pre
        cur.next = pre
        # 当前节点赋值给pre，当前节点后移一位，即pre和cur都前进一位
        pre = cur
        cur = tmp
    return pre


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

    @staticmethod
    def items(head):

        cur = head
        while cur is not None:
            yield cur.val
            cur = cur.next

    def traversal(self, head):

        if head is None:
            return []
        res = self.traversal(head.next)
        res.append(head.val)
        return res

    def reverse(self, head):
        # base case，递归的终止条件：当前节点为空或者下一个节点为空
        if head is None or head.next is None:
            return head

        # 如果链表是1->2->3->4->5，则此时的last为5，head=4，
        # 因此head.next.next=head。就相当于5.next=4，即5->4
        last = self.reverse(head.next)
        head.next.next = head
        # 防止链表循环，需要将head.next设置成空
        head.next = None

        # 每层递归函数返回的都是last，也就是最后一个节点5
        return last

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
    for i in range(0):
        link_list.append(i)

    # link_list.add(0)

    # print link_list.remove(0)
    # print link_list.insert('a', 1)

    for i in link_list.items(link_list.head):
        print i
    print "=" * 20
    for i in link_list.items(iteration_reverse(link_list.head)):
        print i

