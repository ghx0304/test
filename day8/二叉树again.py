# -*- coding = utf-8 -*-
# @Time : 2025/1/2 19:37
# @Author : guohexing
# @Fire : 二叉树again.py
# @Software : PyCharm
class TreeNode():
    '''
    定义二叉树节点
    '''

    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class BinaryTree():
    '''
    定义二叉树类
    '''

    def __init__(self):
        self.root = None
        self.queue = []  # 定义一个辅助队列，用于一个一个的加入节点

    def add(self, elem):
        '''
        添加节点
        :param elem: 需要添加的节点元素
        :return:
        '''
        new_node = TreeNode(elem)
        if self.root is None:  # 如果树为空，则直接将新节点作为根节点
            self.root = new_node
            self.queue.append(new_node)
            print("根节点添加成功")
        else:  # 如果树不为空，则将新节点加入队列，等待父节点确定位置
            father = self.queue[0]
            if father.lchild is None:  # 如果父节点的左子树为空，则将新节点作为左子树
                father.lchild = new_node
                self.queue.append(new_node)
                print(f'{father.elem}的左子树添加{new_node.elem}成功')
            else:  # 如果父节点的左子树不为空，则将新节点作为右子树
                father.rchild = new_node
                print(f'{father.elem}的右子树添加{new_node.elem}成功')
                self.queue.append(new_node)
                self.queue.pop(0)  # 父节点确定位置后，将父节点出队，等待下一个节点确定位置

    def pre_order(self, node):
        '''
        从node节点开始，先访问node节点，再访问node的左子树，最后访问node的右子树
        :param node:
        :return:
        '''
        if node is not None:
            print(node.elem, end=' ')
            self.pre_order(node.lchild)
            self.pre_order(node.rchild)
    def in_order(self, node):
        '''
        从node节点开始，先访问node的左子树，再访问node节点，最后访问node的右子树
        :param node:
        :return:
        '''
        if node is not None:
            self.in_order(node.lchild)
            print(node.elem, end=' ')
            self.in_order(node.rchild)

    def post_order(self, node):
        '''
        从node节点开始，先访问node的左子树，再访问node的右子树，最后访问node节点
        :param node:
        :return:
        '''
        if node is not None:
            self.post_order(node.lchild)
            self.post_order(node.rchild)
            print(node.elem, end=' ')
    def level_order(self):
        '''
        层次遍历二叉树
        :return:
        '''
        if self.root is None:
            print("树为空")
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.elem, end=' ')
            if node.lchild is not None:
                queue.append(node.lchild)
            if node.rchild is not None:
                queue.append(node.rchild)


if __name__ == '__main__':
    tree = BinaryTree()
    for i in range(1, 11):
        tree.add(i)
    tree.level_order()
    print()
    tree.pre_order(tree.root)
    print()  # 先序遍历
    tree.in_order(tree.root)
    print()  # 中序遍历
    tree.post_order(tree.root)
    print()  # 后序遍历
