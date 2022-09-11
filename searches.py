#!/usr/bin/env python
# coding: utf-8

# In[5]:


import structures
from collections import deque



def breadth_first_graph_search(problem):
    """[Figure 3.11]
    Note that this function can be implemented in a
    single line as below:
    return graph_search(problem, FIFOQueue())
    """
    structures.Node = structures.Node(problem.initial)
    if problem.goal_test(structures.Node.state):
        return structures.Node
    frontier = deque([structures.Node])
    explored = set()
    while frontier:
        structures.Node = frontier.popleft()
        explored.add(structures.Node.state)
        for child in structures.Node.expand(problem):
            if child.state not in explored and child not in frontier:
                if problem.goal_test(child.state):
                    return child
                frontier.append(child)
    #return none
    return None


def depth_first_graph_search(problem):
    """
    [Figure 3.7]
    Search the deepest structures.Nodes in the search tree first.
    Search through the successors of a problem to find a goal.
    The argument frontier should be an empty queue.
    Does not get trapped by loops.
    If two paths reach a state, only use the first one.
    """
    frontier = [(structures.Node(problem.initial))]  # Stack

    explored = set()
    while frontier:
        structures.Node = frontier.pop()
        if problem.goal_test(structures.Node.state):
            return structures.Node
        explored.add(structures.Node.state)
        frontier.extend(child for child in structures.Node.expand(problem)
                        if child.state not in explored and child not in frontier)
    return None

def depth_limited_search(problem, limit=50):
    """[Figure 3.17]"""

    def recursive_dls(Node, problem, limit):
        if problem.goal_test(structures.Node.state):
            return structures.Node
        elif limit == 0:
            return 'cutoff'
        else:
            cutoff_occurred = False
            for child in structures.Node.expand(problem):
                result = recursive_dls(child, problem, limit - 1)
                if result == 'cutoff':
                    cutoff_occurred = True
                elif result is not None:
                    return result
            return 'cutoff' if cutoff_occurred else None

    # Body of depth_limited_search:
    return recursive_dls(Node(problem.initial), problem, limit)


def iterative_deepening_search(problem):
    """[Figure 3.18]"""
    
    # sets a sensible maximum limit linked to graph size
    limit = int(len(romania_problem.graph.structures.Nodes())*.75)
    
    for depth in range(limit):
        result = depth_limited_search(problem, depth)
        if result != 'cutoff':
            return result


# In[ ]:




