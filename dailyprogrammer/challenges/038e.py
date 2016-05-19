#!/usr/bin/python3
"""
Information
-----------

.. _reddit: http://www.reddit.com/r/dailyprogrammer/comments/s2no2/4102012_challenge_38_easy/
.. _source: https://github.com/UltimateTimmeh/r-daily-programmer/blob/master/dailyprogrammer/challenges/038e.py

| **Challenge name:** Dijkstra's Algorithm (reddit_, source_)
| **Challenge number:** 38
| **Difficulty:** Easy
| **Submission date:** 2012-04-10
| **Status:** Complete

Description
-----------

Implement `Dijkstra's algorithm <http://en.wikipedia.org/wiki/Dijkstra's_algorithm>`_ in any way you
can :).

Example run
-----------

::

    $ python3 dailyprogrammer.py execute 038e
    This is the graph before doing anything:
    Graph with 9 vertices:
        Vertex 'H' - visited: False, parent: None, cost: None
            paths: {'G': 3, 'E': 1, 'I': 5}
        Vertex 'D' - visited: False, parent: None, cost: None
            paths: {'E': 2, 'B': 1, 'F': 3, 'G': 1, 'C': 3, 'A': 7}
        Vertex 'C' - visited: False, parent: None, cost: None
            paths: {'F': 2, 'D': 3, 'A': 5}
        Vertex 'I' - visited: False, parent: None, cost: None
            paths: {'F': 4, 'H': 5, 'G': 2}
        Vertex 'F' - visited: False, parent: None, cost: None
            paths: {'G': 3, 'D': 3, 'C': 2, 'I': 4}
        Vertex 'E' - visited: False, parent: None, cost: None
            paths: {'G': 2, 'D': 2, 'B': 7, 'H': 1}
        Vertex 'G' - visited: False, parent: None, cost: None
            paths: {'F': 3, 'E': 2, 'I': 2, 'D': 1, 'H': 3}
        Vertex 'B' - visited: False, parent: None, cost: None
            paths: {'E': 7, 'D': 1, 'A': 3}
        Vertex 'A' - visited: False, parent: None, cost: None
            paths: {'D': 7, 'C': 5, 'B': 3}
    Determine shortest route from vertex: A
    To vertex: I
    Graph after application of Dijkstra's algorithm with origin 'A':
    Graph with 9 vertices:
        Vertex 'H' - visited: True, parent: E, cost: 7
            paths: {'G': 3, 'E': 1, 'I': 5}
        Vertex 'D' - visited: True, parent: B, cost: 4
            paths: {'E': 2, 'B': 1, 'F': 3, 'G': 1, 'C': 3, 'A': 7}
        Vertex 'C' - visited: True, parent: A, cost: 5
            paths: {'F': 2, 'D': 3, 'A': 5}
        Vertex 'I' - visited: True, parent: G, cost: 7
            paths: {'F': 4, 'H': 5, 'G': 2}
        Vertex 'F' - visited: True, parent: D, cost: 7
            paths: {'G': 3, 'D': 3, 'C': 2, 'I': 4}
        Vertex 'E' - visited: True, parent: D, cost: 6
            paths: {'G': 2, 'D': 2, 'B': 7, 'H': 1}
        Vertex 'G' - visited: True, parent: D, cost: 5
            paths: {'F': 3, 'E': 2, 'I': 2, 'D': 1, 'H': 3}
        Vertex 'B' - visited: True, parent: A, cost: 3
            paths: {'E': 7, 'D': 1, 'A': 3}
        Vertex 'A' - visited: True, parent: None, cost: 0 (origin)
            paths: {'D': 7, 'C': 5, 'B': 3}
    Shortest route from vertex 'A' to vertex 'I': ['A', 'B', 'D', 'G', 'I']

Module contents
---------------
"""

import operator

from plugins import utils


class Vertex(object):
    """A graph vertex with a set of paths to other vertices.

    A vertex is characterized by a label (or name) and a dictionary of paths from the vertex to
    other vertices. For application of Dijkstra's algorithm for calculating the shortest path from
    any vertex to all other vertices, each vertex also has the 'visited', 'parent' and 'cost'
    attributes.

    :param str label: the vertex's label
    :param paths: dictionary specifying the connectivity of the vertex with other vertices, where
                  keys specify vertex labels and values indicate the associated cost of traveling to
                  the respective vertex (default {})
    :type paths: dict(str: int or float, ...)

    Example::

        >>> v1 = Vertex('v1', paths={'v2': 10})
        >>> v2 = Vertex('v2', paths={'v1': 5, 'v3': 2.5})
        >>> v3 = Vertex('v3')
        >>> for v in [v1, v2, v3]: print(v)
        ...
        Vertex 'v1' - visited: False, parent: None, cost: None
            paths: {'v2': 10}
        Vertex 'v2' - visited: False, parent: None, cost: None
            paths: {'v3': 2.5, 'v1': 5}
        Vertex 'v3' - visited: False, parent: None, cost: None
            paths: {}
    """


    def __init__(self, label, paths=None):
        """Create a new vertex."""
        self.label = label
        self.paths = paths
        if self.paths is None:
            self.paths = {}
        self.reset()


    def __str__(self):
        """Format the vertex as a string."""
        str_ = "Vertex '{label}' - visited: {visited}, parent: {parent}, cost: {cost}\n"
        str_ += "    paths: {paths}"
        return str_.format(**self.__dict__)


    def reset(self):
        """Reset the vertex to its default values.

        This includes:
            1) Setting the visited flag to False;
            2) Setting the parent to None;
            3) Setting the cost to None.

        Example::

            >>> v1 = Vertex('v1', paths={})
            >>> v1.visited = True; v1.parent = 'v2'; v1.cost = 10
            >>> v1.reset()
            >>> print(v1.visited, v1.parent, v1.cost)
            False None None
        """
        self.visited = False
        self.parent = None
        self.cost = None


class Graph(object):
    """Class representing a graph.

    A graph is characterized by a list of vertices (which may have paths defined between
    one another). For application of Dijkstra's algorithm for calculating the shortest path from
    any vertex to all other vertices, a graph also has the 'origin' attribute (i.e. the label of
    the algorithm's starting vertex).

    :param vertices: list of vertices contained within the graph
    :type vertices: list(Vertex, ...)

    Example::

        >>> vertices = {
        ...     'A': {'B': 3, 'C': 5, 'D': 7},
        ...     'B': {'A': 3, 'D': 1, 'E': 7},
        ...     'C': {'A': 5, 'D': 3, 'F': 2},
        ...     'D': {'A': 7, 'B': 1, 'C': 3, 'E': 2, 'F': 3, 'G': 1},
        ...     'E': {'B': 7, 'D': 2, 'G': 2, 'H': 1},
        ...     'F': {'C': 2, 'D': 3, 'G': 3, 'I': 4},
        ...     'G': {'D': 1, 'E': 2, 'F': 3, 'H': 3, 'I': 2},
        ...     'H': {'E': 1, 'G': 3, 'I': 5},
        ...     'I': {'F': 4, 'G': 2, 'H': 5},
        ... }
        >>> graph = Graph.from_dict(vertices)
        >>> print(graph['I'])
        Vertex 'I' - visited: False, parent: None, cost: None
            paths: {'H': 5, 'F': 4, 'G': 2}
        >>> graph.dijkstra('A')
        >>> print(graph['I'])
        Vertex 'I' - visited: True, parent: G, cost: 7
            paths: {'H': 5, 'F': 4, 'G': 2}
        >>> graph.route('A', 'I')
        ['A', 'B', 'D', 'G', 'I']
    """


    def __init__(self, vertices):
        """Create a new graph."""
        self.vertices = {vertex.label: vertex for vertex in vertices}
        self.reset()


    def __str__(self):
        """Format the graph as a string."""
        str_ = "Graph with {} vertices:".format(self.nvertices())
        for vertex in self.vertices.values():
            info, paths = str(vertex).split('\n')
            str_ += '\n    ' + info
            if vertex.label == self.origin:
                str_ += " (origin)"
            str_ += '\n    ' + paths
        return str_


    def __getitem__(self, label):
        """Get the vertex with the specified label.

        This allows you to get a Vertex from a graph like you would an item from a dictionary:
        ``vertex = graph[label]``.

        :param str label: label of the desired vertex
        :return: the first vertex from the list of vertices with the specified label
        :rtype: Vertex
        :raise: KeyError if the provided label is not present in the graph's dictionary of vertices

        For an example that uses this method, see :func:`challenges.038e.Graph`.
        """
        if label not in self.vertices:
            raise KeyError("Vertex with label '{}' not found in graph.".format(label))
        return self.vertices[label]


    def reset(self):
        """Reset the graph to its default values.

        This includes:
            1) Setting the graph's origin to None;
            2) Resetting all vertices.

        Example::

            >>> v1 = Vertex('v1', paths={})
            >>> g = Graph([v1])
            >>> g.origin = 'v1'
            >>> g.reset()
            >>> print(g.origin)
            None
        """
        self.origin = None
        for vertex in self.vertices.values():
            vertex.reset()


    def nvertices(self):
        """Return the amount of vertices in the graph.

        :return: the amount of vertices in the graph
        :rtype: int

        Example::

            >>> v1 = Vertex('v1', paths={})
            >>> v2 = Vertex('v2', paths={})
            >>> g = Graph([v1, v2])
            >>> g.nvertices()
            2
        """
        return len(self.vertices)


    def unvisited(self):
        """Return the list of unvisited vertices.

        This is used in the Dijkstra algorithm to find the next vertex that should be considered.
        Outside of the algorithm, this method can be used to see which vertices cannot be reached
        from the graph's current origin.

        :return: dictionary containing only unvisited vertices
        :rtype: dict(str: Vertex, ...)

        Example::

            >>> v1 = Vertex('v1', paths={})
            >>> v2 = Vertex('v2', paths={})
            >>> v3 = Vertex('v3', paths={})
            >>> g = Graph([v1, v2, v3])
            >>> g['v1'].visited = True; g['v3'].cost = 10
            >>> for v in g.unvisited(): print(v)
            ...
            v2
            v3
        """
        return {l: v for l, v in self.vertices.items() if not v.visited}


    def unvisited_with_cost(self):
        """Return the list of unvisited vertices that have a cost.

        :return: dictionary containing only unvisited vertices with a cost
        :rtype: dict(str: Vertex, ...)

        Example::

            >>> v1 = Vertex('v1', paths={})
            >>> v2 = Vertex('v2', paths={})
            >>> v3 = Vertex('v3', paths={})
            >>> g = Graph([v1, v2, v3])
            >>> g['v1'].visited = True; g['v3'].cost = 10
            >>> for v in g.unvisited_with_cost(): print(v)
            ...
            v3
        """
        return {l: v for l, v in self.unvisited().items() if v.cost is not None}


    def dijkstra(self, origin):
        """Perform Dijkstra's algorithm on the graph starting from the given origin.

        After execution of the algorithm, each vertex will point to a parent such that the cost
        of traveling from the origin to the respective vertex is minimal. Vertices that are not
        connected to the origin will remain unvisited and will have no parent and no cost. The
        origin itself is of course visited with a cost of zero, but it has no parent.

        :param str origin: label of the vertex from which the algorithm is started

        For an example that uses this method, see :func:`challenges.038e.Graph`.
        """
        # Reset the graph, set the graph's origin label to the passed origin label
        # and set the cost of the origin to zero.
        self.reset()
        self.origin = origin
        originv = self[origin]
        originv.cost = 0

        # Go through all vertices until there are no more unvisited vertices with
        # a cost.
        availablevs = self.unvisited_with_cost()
        while len(availablevs) > 0:
            # Consider the unvisited vertex with the lowest cost.
            currentv = min(availablevs.values(), key=operator.attrgetter('cost'))
            # Go through all paths of the considered vertex.
            for destination, pathcost in currentv.paths.items():
                destinationv = self[destination]
                # If the destination vertex was already visited, pass.
                if destinationv.visited:
                    pass
                # If the destination vertex has no cost or its cost is higher
                # than the sum of the considered vertex' cost and the path cost,
                # then set the destination vertex' cost to this sum and make
                # its parent the current vertex.
                if destinationv.cost is None or destinationv.cost > currentv.cost+pathcost:
                    destinationv.cost = currentv.cost + pathcost
                    destinationv.parent = currentv.label
            # Set the considered vertex to visited and refresh the available vertices.
            currentv.visited = True
            availablevs = self.unvisited_with_cost()


    def route(self, origin, destination):
        """Return the shortest route on the graph from the start vertex to the end vertex.

        If the end vertex is not connected to the start vertex, then no route exists
        and an empty list is returned.

        :param str origin: label of the origin vertex (will become the new graph origin)
        :param str destination: label of the destination vertex
        :return: a list of vertex labels that represents the shortest route from the origin
                 vertex to the destination vertex
        :rtype: list(str, ...)

        For an example that uses this method, see :func:`challenges.038e.Graph`.
        """
        # Execute the Dijkstra algirithm with the provided origin vertex.
        self.dijkstra(origin)
        # Make sure the destination vertex is connected to the origin vertex. Return an empty list
        # if this is not the case.
        vdest = self[destination]
        if not vdest.visited:
            return []
        # Extract the route.
        route = [destination]
        while vdest.parent is not None:
            route.append(vdest.parent)
            vdest = self[vdest.parent]
        return route[::-1]


    @classmethod
    def from_dict(cls, dict_):
        """Create a graph from a dictionary representation.

        :param dict dict_: dictionary representation of the graph
        :return: the graph
        :rtype: Graph

        For an example that uses this method, see :func:`challenges.038e.Graph`.
        """
        vertices = [Vertex(key, paths=value) for key, value in dict_.items()]
        return cls(vertices)


def run():
    """Execute the challenges.038e module."""
    graph_dict = {
        'A': {'B': 3, 'C': 5, 'D': 7},
        'B': {'A': 3, 'D': 1, 'E': 7},
        'C': {'A': 5, 'D': 3, 'F': 2},
        'D': {'A': 7, 'B': 1, 'C': 3, 'E': 2, 'F': 3, 'G': 1},
        'E': {'B': 7, 'D': 2, 'G': 2, 'H': 1},
        'F': {'C': 2, 'D': 3, 'G': 3, 'I': 4},
        'G': {'D': 1, 'E': 2, 'F': 3, 'H': 3, 'I': 2},
        'H': {'E': 1, 'G': 3, 'I': 5},
        'I': {'F': 4, 'G': 2, 'H': 5},
    }
    graph = Graph.from_dict(graph_dict)
    print("This is the graph before doing anything:\n{}".format(graph))
    start = utils.get_input("Determine shortest route from vertex: ")
    end = utils.get_input("To vertex: ")
    route = graph.route(start, end)
    msg_graph = "Graph after application of Dijkstra's algorithm with origin '{}':\n{}"
    msg_route = "Shortest route from vertex '{}' to vertex '{}': {}"
    print(msg_graph.format(start, graph))
    print(msg_route.format(start, end, route))

