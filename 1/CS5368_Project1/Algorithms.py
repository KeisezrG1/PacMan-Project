import util

class DFS(object):
    def depthFirstSearch(self, problem):
        """
        Search the deepest nodes in the search tree first
        [2nd Edition: p 75, 3rd Edition: p 87]

        Your search algorithm needs to return a list of actions that reaches
        the goal.  Make sure to implement a graph search algorithm
        [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].

        To get started, you might want to try some of these simple commands to
        understand the search problem that is being passed in:

        print "Start:", problem.getStartState()
        print "Is the start a goal?", problem.isGoalState(problem.getStartState())
        print "Start's successors:", problem.getSuccessors(problem.getStartState())
        """
        "*** TTU CS 5368 Fall 2023 YOUR CODE HERE ***"
        intial_state=problem.getStartState()
        successors=list(reversed(problem.getSuccessors(intial_state)))
        l=[]
        visted={}
        def dfs_helper(problem,intial_state,successors):
            if(visted.get(intial_state)==None):
                visted[intial_state]=1
                returned_ans=False
                for successor in successors:
                    next_state=successor[0]
                    if(problem.isGoalState(next_state)):
                        l.append(successor[1])
                        return True
                    else:
                        l.append(successor[1])
                        next_state_successors=list(reversed(problem.getSuccessors(next_state)))
                        if(visted.get(next_state)==None):
                            returned_ans=dfs_helper(problem,next_state,next_state_successors)
                            if(returned_ans):
                                break
                        l.pop()
                
            return returned_ans
        dfs_helper(problem,intial_state,successors)
        vistedited_states=visted.keys()
        problem.expanded_states=list(vistedited_states)
        return l
class BFS(object):
    
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    def breadthFirstSearch(self, problem):
        "*** TTU CS 5368 Fall 2023 YOUR CODE HERE ***"
        intial_state=problem.getStartState()
        vis={}
        queue=[]
        queue.append((intial_state,[]))
        vis[intial_state]=1
        while(len(queue)>0):
            current_state,transition=queue.pop(0)
            for successor in problem.getSuccessors(current_state):
                next_state=successor[0]
                if(problem.isGoalState(next_state)):
                    problem.expanded_states=list(vis.keys())
                    return transition+[successor[1]]
                if(vis.get(next_state)==None):
                    vis[next_state]=1
                    new_transition=transition+[successor[1]]
                    queue.append((next_state,new_transition))
        return []
    


        

class UCS(object):
    def uniformCostSearch(self, problem):
        "*** TTU CS 5368 Fall 2023 YOUR CODE HERE ***"
        intial_state=problem.getStartState()
        vis={}
        queue=util.PriorityQueue()
        queue.push((intial_state,0,[]),0)
        while(queue.count>0):
            current_state,cost,transition=queue.pop()
            if(vis.get(current_state)==None or cost<vis[current_state]):
                 if(problem.isGoalState(current_state)):
                    problem.expanded_states=list(vis.keys()) 
                    return transition
                 else:
                    vis[current_state]=cost
                    for successor in problem.getSuccessors(current_state):
                        next_state=successor[0]
                        priority=cost+successor[2]
                        new_transition=transition+[successor[1]]
                        new_cost=successor[2]+cost
                        queue.push((next_state,new_cost,new_transition),priority)
        return ans
        
class aSearch (object):
    def nullHeuristic( state, problem=None):
        """
        A heuristic function estimates the cost from the current state to the nearest goal in the provided SearchProblem.  This heuristic is trivial.
        """
        return 0
    def aStarSearch(self,problem, heuristic=nullHeuristic):
        "Search the node that has the lowest combined cost and heuristic first."
        "*** TTU CS 5368 Fall 2023 YOUR CODE HERE ***"
        intial_state=problem.getStartState()
        vis={}
        queue=util.PriorityQueue()
        queue.push((intial_state,0,[]),0)
        while(queue.count>0):
            current_state,cost,transition=queue.pop()
            if(vis.get(current_state)==None or cost<vis[current_state]):
                 if(problem.isGoalState(current_state)):
                    problem.expanded_states=list(vis.keys()) 
                    return transition
                 else:
                    vis[current_state]=cost
                    for successor in problem.getSuccessors(current_state):
                        next_state=successor[0]
                        priority=cost+successor[2]
                        new_transition=transition+[successor[1]]
                        new_cost=successor[2]+cost
                        queue.push((next_state,new_cost,new_transition),heuristic(next_state,problem)+new_cost)
        return ans
       