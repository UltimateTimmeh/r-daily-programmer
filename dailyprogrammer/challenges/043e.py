#!/usr/bin/python3
"""
Information
-----------

.. _reddit: https://www.reddit.com/r/dailyprogrammer/comments/sq3p9/4242012_challenge_43_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/043e.py

| **Challenge name:** Lowest Common Ancestor (reddit_, source_)
| **Challenge number:** 43
| **Difficulty:** Easy
| **Submission date:** 2012-04-25
| **Status:** Complete

Description
-----------

Today is a common interview question.

Given a binary tree t and two elements of the tree, m and n, with m < n, find the lowest element of
the tree (farthest from the root) that is an ancestor of both m and n.

Example run
-----------

::

    This is the tree I've constructed for you:
    a
    └─── b
         └─── d
         └─── e
              └─── g
              └─── h
    └─── c
         └─── f
              └─── i
    Give me two nodes, and I will find you the lowest common ancestor:
    Node 1 > d
    Node 2 > h
    The lowest common ancestor of 'd' and 'h' is 'b'

Module contents
---------------
"""

from plugins import utils


class Node(object):
    """A node in a binary tree.

    :param str name: name of the node
    :param left: left child of the node
    :type left: None or Node
    :param right: right child of the node
    :type right: None or Node
    """


    def __init__(self, name, left=None, right=None):
        """Initialize a new node object."""
        self.name = name
        self.left = left
        self.right = right


    def __str__(self):
        """Format a string representation of the node."""
        return self.name


    def draw(self, level=0):
        """Draw the binary tree.

        :param int level: indentation level of the tree drawing (default 0)
        """
        if level == 0:
            str_ = self.name
        else:
            str_ = "     "*(level-1) + "└─── " + self.name
        print(str_)
        if self.left is not None:
            self.left.draw(level=level+1)
        if self.right is not None:
            self.right.draw(level=level+1)


    def path(self, target):
        """Return the path of nodes that is followed to reach the target node.

        :param str target: name of the target node
        :return: a list of nodes representing the path followed to reach the target node
        :rtype: list(Node, ...)
        """
        if self.name == target:
            return [self]
        if self.left is not None:
            left_path = self.left.path(target)
            if len(left_path) > 0:
                return [self] + left_path
        if self.right is not None:
            right_path = self.right.path(target)
            if len(right_path) > 0:
                return [self] + right_path
        return []


    def common_ancestors(self, node1, node2):
        """Return the common ancestors of two nodes, ordered from highest to lowest.

        :param str node1: name of the first node of which to find common ancestors
        :param str node2: name of the second node of which to find common ancestors
        :return: list of common ancestors, ordered from highest to lowest
        :rtype: list(Node, ...)
        """
        node1_path = self.path(node1)
        node2_path = self.path(node2)
        node2_path_names = [node.name for node in node2_path]
        ca = [node for node in node1_path if node.name in node2_path_names]
        return ca


    def lowest_common_ancestor(self, node1, node2):
        """Find the lowest common ancestor of two nodes.

        :param str node1: name of the first node of which to find the lowest common ancestor
        :param str node2: name of the second node of which to find the lowest common ancestor
        :return: the lowest common ancestor or None if no such ancestor exists
        :rtype: Node or None
        """
        ca = self.common_ancestors(node1, node2)
        if len(ca) > 0:
            return ca[-1]
        return


def run():
    """Execute the challenges.043e module."""
    # Construct the binary tree.
    ni = Node('i')
    nh = Node('h')
    ng = Node('g')
    nf = Node('f', left=ni)
    ne = Node('e', left=ng, right=nh)
    nd = Node('d')
    nc = Node('c', left=nf)
    nb = Node('b', left=nd, right=ne)
    na = Node('a', left=nb, right=nc)
    # Execute challenge.
    print("This is the tree I've constructed for you:")
    na.draw()
    print("Give me two nodes, and I will find you the lowest common ancestor:")
    n1 = utils.get_input("Node 1 > ")
    n2 = utils.get_input("Node 2 > ")
    lca = na.lowest_common_ancestor(n1, n2)
    print("The lowest common ancestor of '{}' and '{}' is '{}'".format(n1, n2, lca))

