# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    def createNode(self, oldNode):
        newNode = UndirectedGraphNode(oldNode.label)
        self.newNodeDict[newNode.label] = newNode
        for i in oldNode.neighbors:
            if i.label not in self.newNodeDict:
                self.createNode(i)
            newNode.neighbors.append(self.newNodeDict[i.label])
        return newNode

    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node:
            return None
        self.newNodeDict = {}
        return self.createNode(node)


class Solution_self(object):
    def __init__(self):
        self.new_node_dict = {}

    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node:
            return None
        return self.create_node(node)

    def create_node(self, node):
        new_node = UndirectedGraphNode(node.label)
        self.new_node_dict[new_node.label] = new_node
        for n in node.neighbors:
            if n.label not in self.new_node_dict:
                self.create_node(n)
            new_node.neighbors.append(self.new_node_dict[n.label])
        return new_node
