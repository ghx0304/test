# -*- coding = utf-8 -*-
# @Time : 2025/1/2 14:57
# @Author : guohexing
# @Fire : 1二叉树.py
# @Software : PyCharm
class Node():
    '''
    Node类，用于构建二叉树
    '''

    def __init__(self, elem=-1, lchid=None, rchid=None):
        self.elem = elem
        self.lchid = lchid
        self.rchid = rchid


class BinaryTree():
    '''
    BinaryTree类，用于构建二叉树
    '''

    def __init__(self):
        self.root = Node()
        self.myQueue = []

    def add(self, elem):
        '''
        向二叉树中添加元素
        :param elem: 待添加的元素
        :return: None
        '''
        node = Node(elem)
        if self.root.elem == -1:
            self.root = node
            self.myQueue.append(self.root)
        else:
            treeNode = self.myQueue[0]
            if treeNode.lchid == None:
                treeNode.lchid = node
                self.myQueue.append(treeNode.lchid)
            else:
                treeNode.rchid = node
                self.myQueue.append(treeNode.rchid)
                self.myQueue.pop(0)
    def preorder(self, node):
        '''
        先序遍历二叉树
        :param node:
        :return:
        '''
        if node == None:
            return
        print(node.elem, end=' ')
        self.preorder(node.lchid)
        self.preorder(node.rchid)
    def inorder(self, node):
        '''
        中序遍历二叉树
        :param node:
        :return:
        '''
        if node == None:
            return
        self.inorder(node.lchid)
        print(node.elem, end=' ')
        self.inorder(node.rchid)

    def postorder(self, node):
        '''
        后序遍历二叉树
        :param node:
        :return:
        '''
        if node == None:
            return
        self.postorder(node.lchid)
        self.postorder(node.rchid)
        print(node.elem, end=' ')

    def levelorder(self, node):
        '''
        层序遍历二叉树
        :param node:
        :return:
        '''
        if node == None:
            return
        myQueue = [node]
        while myQueue:
            treeNode = myQueue[0]
            print(treeNode.elem, end=' ')
            if treeNode.lchid:
                myQueue.append(treeNode.lchid)
            if treeNode.rchid:
                myQueue.append(treeNode.rchid)
            myQueue.pop(0)


if __name__ == '__main__':
    tree = BinaryTree()

    for i in range(1, 10):
        tree.add(i)
    print(tree.root.elem)
    print(type(tree))
    tree.preorder(tree.root)
    print()
    tree.inorder(tree.root)
    print()
    tree.postorder(tree.root)
    print()
    tree.levelorder(tree.root)
    print()
