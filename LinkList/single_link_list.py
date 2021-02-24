# -*- coding: utf-8 -*-


class Node(object):
    """
    单链表节点类定义
    """

    def __init__(self, val=0):

        self.val = val
        self.next = None


class LinkListOpt(object):
    """
    链表操作
    """
    def __init__(self):

        self.head = None

    def is_empty(self):
        """
        判断链表是否为空
        :return: bool True or False
        """
        return self.head is None

    def length(self):
        """
        计算链表的长度
        :return: int
        """
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def items(self):
        """
        迭代遍历链表
        """
        cur = self.head
        while cur is not None:
            yield cur.val
            cur = cur.next

    def traverse(self, head):
        """
        递归遍历链表
        """
        if head is None:
            return []
        aes = self.traverse(head.next)
        aes.append(head.val)
        return aes

    def add(self, val):
        """
        在链表的头部添加节点
        """
        node = Node(val)

        # 新节点的next指向原链表头部
        node.next = self.head

        # 头部节点修改为新节点
        self.head = node

    def append(self, val):

        node = Node(val)
        # 如果链表为空，直接将链表头部修改为新节点
        if self.is_empty():
            self.head = node
        else:
            # 不是空链表的话，则循环找到链表尾部，将尾部的next指向新的节点
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def find(self, val):
        """
        查找链表中是否含有该元素
        """
        return val in self.items()

    def remove(self, val):
        """
        删除链表中的节点
        """
        cur = self.head
        pre = None
        while cur is not None:
            if cur.val == val:
                # 如果是头部节点，直接将下一个节点指向链表头部
                if not pre:
                    self.head = cur.next
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                return True
            else:
                # 链表后移
                pre = cur
                cur = cur.next

    def insert(self, val, index):
        # 插入位置在头部元素之前，调用add方法
        if index <= 0:
            self.add(val)
        # 插入位置大于等于链表长度，调用append方法
        elif index >= self.length():
            self.append(val)
        else:
            node = Node(val)
            cur = self.head
            # 迭代遍历到要插入的位置
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

