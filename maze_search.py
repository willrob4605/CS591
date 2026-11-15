from collections import deque
#Todo List
#Counters: nodes expanded, max depth, and max fringe size.

#file path
files=["Maze/bigMaze.lay","Maze/mediumMaze.lay","Maze/openMaze.lay","Maze/smallMaze.lay"]



#Parse the maze
#returns the maze, start point, and goal positions

def maze_parser(path):
    maze=[]
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            clean_line = line.rstrip("\n")
            maze.append(clean_line)
    start=None
    goal=set()
    for row, row_string in enumerate(maze):
        for col, character in enumerate(row_string):
            if character=="P":
                start=(row,col)
            elif character==".":
                goal.add((row,col))
    if start is None:
        raise ValueError("No p found")
    return maze,start,goal

#Node class to store the position, parent node, and cost
class Node:
    def __init__(self,state, parent):
        self.state = state
        self.parent=parent
        if parent is None:
            self.cost=0
        else:
            self.cost=parent.cost+1

def path_list(goal_node):
    states=[]

    while goal_node is not None:
        states.append(goal_node.state)
        goal_node=goal_node.parent
    states.reverse()
    return states


#returns walkable neighbor positions as a tuple
def get_neighbors(row,col,maze):
    results=[]
    for i in range(-1,2,2):
        new_row=row+i
        new_col=col+i
        if maze[row][new_col] != "%":
            results.append((row,new_col))
                           
        if maze[new_row][col] != "%":
            results.append((new_row,col))
    return results

#takes a file path and returns the shorest path as a list of row,col positions
def bfs(path):
    maze, start_pos, goal = maze_parser(path)
    start=Node(start_pos,None)
    fringe=deque([start])
    explored=set([(start.state)])
 
    while fringe:
        current=fringe.popleft()
        if current.state in goal:
            return (path_list(current))

        row,col=current.state
        neighbors=get_neighbors(row,col,maze)
        for neighbor in neighbors:
            if neighbor not in explored:
                explored.add(neighbor)
                fringe.append(Node(neighbor,current))
for f in files:
    print(f)
    print(bfs(f))

