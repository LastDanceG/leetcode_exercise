# -*- coding: utf-8 -*-


class Node(object):

    def __init__(self, val=0):

        self.val = val
        self.next = None


class LinkListOpt(object):

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

    def items(self):

        cur = self.head
        while cur is not None:
            yield cur.val
            cur = cur.next

    def traverse(self, head):
        if head is None:
            return []
        aes = self.traverse(head.next)
        aes.append(head.val)
        return aes

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

    def find(self, val):

        return val in self.items()

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
            node = Node(val)
            cur = self.head
            for i in range(index-1):
                cur = cur.next
            node.next = cur.next
            cur.next = node


class TreeNode(object):

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def pre_order_traversal(self, root):

        res = []
        self.pre_order(root, res)
        return res

    def pre_order(self, root, res):

        if not root:
            return
        res.append(root.val)
        self.pre_order(root.left, res)
        self.pre_order(root.right, res)


if __name__ == '__main__':

    # 从尾部为链表增加元素
    link_list = LinkListOpt()
    for i in range(1, 11):
        link_list.append(i)

    # 从头遍历链表并打印
    # for i in link_list.items():
    #     print i
    print link_list.insert(100, 1)
    print link_list.traverse(link_list.head)

