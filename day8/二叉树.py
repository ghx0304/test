# -*- coding = utf-8 -*-
# @Time : 2025/1/2 18:51
# @Author : guohexing
# @Fire : 二叉树.py
# @Software : PyCharm
class TreeNode():
    def __init__(self, element=-1, lchild=None, rchild=None):
        self.element = element
        self.lchild = lchild
        self.rchild = rchild

class BinaryTree():
    def __init__(self):
        self.root = TreeNode()
        self.Queue = []

    def add_node(self, node:TreeNode):
        '''
        添加节点
        :param node:需要添加的一个节点
        :return:
        '''
        if self.root.element == -1:
            self.root = node
            self.Queue.append(self.root)
        else:
            tree_node = self.Queue[0]
            if tree_node.lchild is None:
                tree_node.lchild = node
                self.Queue.append(node)
                print(f'{tree_node.element}的左孩子是{node.element}')
            else:
                tree_node.rchild = node
                self.Queue.append(node)
                print(f'{tree_node.element}的右孩子是{node.element}')
                self.Queue.pop(0)




if __name__ == '__main__':
    BT = BinaryTree()
    for i in range(1, 10):
        Tnode = TreeNode(i)
        # print(Tnode.element)
        BT.add_node(Tnode)
    # for i in BT.Queue:
    #     print(i.element)