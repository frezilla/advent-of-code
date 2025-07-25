from math import inf

from arc_class import Arc
from node_class import Node


class Graph:
    def __init__(self):
        self.arcs = set()
        self.nodes = set()
        self.set_p = set()
        self.set_q = set()

    def add(self, node_name_1, node_name_2, distance):
        node1 = Node(node_name_1)
        node2 = Node(node_name_2)
        arc = Arc(node1, node2, distance)
        self.nodes.add(Node(node_name_1))
        self.nodes.add(Node(node_name_2))
        self.arcs.add(arc)

    def dijkstra(self, node_name_1):
        self.init_graph(node_name_1)
        while len(self.set_q) > 0:
            min_node = self.find_min()
            self.set_q.remove(min_node)
            arcs_neighbours = self.find_neighbours(min_node)
            for arc in arcs_neighbours:
                if min_node == arc.node1:
                    node_to = arc.node2
                else:
                    node_to = arc.node1
                if node_to.weight > (min_node.weight + arc.distance):
                    node_to.weight = (min_node.weight + arc.distance)

    def find_min(self):
        min_value = inf
        result_node = None
        for node in self.set_q:
            if node.weight < min_value:
                min_value = node.weight
                result_node = node
        return result_node

    def find_neighbours(self, node):
        result_set = set()
        for arc in self.arcs:
            if node in [arc.node1, arc.node2]:
                result_set.add(arc)
        return result_set

    def init_graph(self, node_name):
        self.set_p.clear()
        self.set_q.clear()
        for node in self.nodes:
            if node.name == node_name:
                node.weight = 0
            else:
                node.weight = inf
            self.set_q.add(node)
