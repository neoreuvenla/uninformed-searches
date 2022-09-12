#!/usr/bin/env python
# coding: utf-8

# In[4]:


#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Module documentation goes here
   and here
   and ...
"""

class Node:

    # data structure for each node in a search tree 
    
    def __init__(self, state, parent=None, action=None):
        
        # constructor
        
        self.state = state # the name of this node in the graph
        self.parent = parent  # the node that generated this node
        self.action = action # the action that generated this node

    def expand(self, problem):
        
        # lists all the nodes neighbouring the current node
        
        return [self.child_node(problem, action) for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        
        # creates a child node from an action on a parent node
        
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, self, action)
        
        return next_node

    def solution(self):
        
        # returns the sequence 
        
        return [node.action for node in self.path()[1:]]
        
        return 

    def path(self):
        
        # lists the nodes in the path from the initial node to this node
        
        node, path = self, []
        
        while node: # loops through successive parent nodes and adds to list
            path.append(node)
            node = node.parent
            
        return list(reversed(path)) # reverses path to progress from start to finish
    
    def __repr__(self):
        # mainly used for clairty when testing
        return "<Node {}>".format(self.state)
    
class Problem():
    
    # defines the problem to be solved

    def __init__(self, initial, goal, graph):
        
        # constructor
        
        self.initial = initial # the starting node
        self.goal = goal # the target node
        self.graph = graph # the graph which to search

    def actions(self, node):
              
        # determines available movements from a given graph node
        
        return self.graph.get(node).keys()

    def result(self, state, action):
        
        # resulting state from the action taken
        
        return action
    
    def goal_test(self, state):

        # determines if a node state is the goal state
        
            return state == self.goal

class Graph:
    
    # converts a dictionary into a graph for searching
    
    def __init__(self, data, directed):
        
        # constructor
        
        self.data = data # the dict with the node connections
        self.directed = directed # whether graph is directed or undirected        

        if not directed:
            # adds symmetric edges if missing from an undirected graph
            self.make_undirected()

    def make_undirected(self):
        
        # adds edges to make an undirected graph from a

        for a in list(self.data.keys()):
            for (b, dist) in self.data[a].items():
                self.connect(b, a, dist)

    def connect(self, A, B, distance):
        """Add a link from A to B of given distance, in one direction only."""
        self.data.setdefault(A, {})[B] = distance

    def get(self, a, b=None):
        """Return a link distance or a dict of {node: distance} entries.
        .get(a,b) returns the distance or None;
        .get(a) returns a dict of {node: distance} entries, possibly {}."""
        links = self.data.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)

    def nodes(self):
        """Return a list of nodes in the graph."""
       # s1 = set([k for k in self.data.keys()])
       # s2 = set([k2 for v in self.data.values() for k2, v2 in v.items()])
       # nodes = s1.union(s2)
        return self.data.keys()


# In[ ]:




