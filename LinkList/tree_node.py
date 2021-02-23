# -*- coding: utf-8 -*-
"""
使用递归的方式前序遍历二叉树
输入:[1, null, 2, 3]
输出：[1, 2, 3]
"""


class TreeNode(object):
    """
    定义一个二叉树节点
    """
    def __init__(self, val=0, left=None, right=None):

        self.val = val
        self.left = left
        self.right = right


def pre_order_traversal(root):
    def pre_order(root):
        if root is None:
            return None
        res.append(root.val)
        pre_order(root.left)
        pre_order(root.right)
    res = []
    pre_order(root)
    return res


if __name__ == '__main__':

    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)

    node1.left = None
    node1.right = node2
    node2.left = node3

    print pre_order_traversal(node1)
