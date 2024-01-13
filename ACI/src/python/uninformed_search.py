from collections import deque
import queue
from utils.general_utils import Point, Node, get_n4_neighbourhood, get_n8_neighbourhood



#----------------------------------------------------------------------------------------

def shortest_path_in_maze(maze, src, dest, is_n4_neighbourhood = True):
    return BFS(maze, len(maze), len(maze[0]), src, dest)
    # return DFS(maze, len(maze), len(maze[0]), src, dest)



def is_within_maze_boundry(maze, nrows, ncols, next_row, next_col):
    return True if (
        next_row >= 0 and next_row < nrows and next_col >= 0 and next_col < ncols
    ) else False



def BFS(maze, nrows, ncols, src, dest, is_n4_neighbourhood = True) -> int:
    '''
    Considering N-4 Neighbourhood, i.e. allowed moves are up, down, left and right.
    Also, maze[i][j] = 1 --> Traversable cell
    but maze[i][j] = 0 ---> Blocked cells/obstacles
    '''
    # defining visited node, and filling all values as false
    visited = []
    for i in range(len(maze)): visited.append([False] * len(maze[i]))

    #check if source and destination cells are not blocked
    if maze[src.x][src.y] != 1 or maze[dest.x][dest.y] != 1: return -1
    
    # Mark source as visited
    visited[src.x][src.y] = True

    # Creating a queue to visit the nodes in order
    q = queue.Queue(maxsize=(nrows * ncols))

    # Add source node to the queue
    q.put(Node(src, 0))

    dx, dy =  get_n4_neighbourhood() if is_n4_neighbourhood else get_n8_neighbourhood()

    while not q.empty():
        current_node = q.get()
        current_coordinate = current_node.coordinate

        # If current node's coordinate matches the destination, goal has been reached.
        # simply return the distance to reach the current node from the source node.
        if current_coordinate.x == dest.x and current_coordinate.y == dest.y: return current_node.distance

        # Get the next node (n4 or n8 neighbour), mark it as visited, and add it to the queue.
        for idx in range(0, 4 if is_n4_neighbourhood else 8):
            next_row = current_coordinate.x + dx[idx]
            next_col = current_coordinate.y + dy[idx]

            if is_within_maze_boundry(maze, nrows, ncols, next_row, next_col) \
            and maze[next_row][next_col] != 0 \
            and not visited[next_row][next_col]:
                visited[next_row][next_col] = True
                q.put(Node(Point(next_row, next_col), current_node.distance + 1))

    return -1


def DFS(maze, nrows, ncols, src, dest, is_n4_neighbourhood=True) -> int:
    '''
    Considering N-4 Neighbourhood, i.e. allowed moves are up, down, left and right.
    Also, maze[i][j] = 1 --> Traversable cell
    but maze[i][j] = 0 ---> Blocked cells/obstacles
    '''
    visited = []
    for idx in range(len(maze)): visited.append([False] * len(maze[idx]))

    # Check if the source and destination cells are not blocked
    if maze[src.x][src.y] != 1 or maze[dest.x][dest.y] != 1: return -1

    # Mark source as visited
    visited[src.x][src.y] = True

    # Creating a stack to visit the nodes in order
    stack = [] * (nrows * ncols) # deque(maxlen=(nrows * ncols)) #
    # If thead are involved, use queue.LifoQueue, else use deque or list

    # Add source node to the stack
    stack.append(Node(src, 0))

    dx, dy = get_n4_neighbourhood() if is_n4_neighbourhood else get_n8_neighbourhood()

    # while len(stack) != 0 :
    while len(stack) != 0:
        current_node = stack.pop()
        current_coordinate = current_node.coordinate

        # If current node's coordinate the destination, goal has been reached.
        # Simply return the distance to reach the current node from the source node.
        if current_coordinate.x == dest.x and current_coordinate.y == dest.y: return current_node.distance

        # Get the next node (n4 or n8), mark it visited and add it to the stack
        for idx in range(0, 4 if is_n4_neighbourhood else 8):
            next_row = current_coordinate.x + dx[idx]
            next_col = current_coordinate.y + dy[idx]

            if is_within_maze_boundry(maze, nrows, ncols, next_row, next_col) \
            and not visited[next_row][next_col] \
            and maze[next_row][next_col] != 0:
                visited[next_row][next_col] = True
                stack.append(Node(Point(next_row, next_col), current_node.distance + 1))


    return -1




if __name__ == "__main__":
    input_maze = [[1,0, 0, 0],
                  [1, 1, 0, 1],
                  [0, 1, 0, 0],
                  [1, 1, 1, 1]]
    
    maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
            [0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1],
            [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    src = [4, 11]
    dest = [10, 0]
    input_maze = maze

    shortest_distance = shortest_path_in_maze(input_maze, Point(src[0], src[1]), Point(dest[0], dest[1]), is_n4_neighbourhood=True)

    print("Input maze : \n{}".format(input_maze))

    if shortest_distance == -1: print(f"Path from ({src}) to ({dest}) does not exist.")
    else : print(f"Length of shortest path from ({src}) to ({dest}) is : {shortest_distance}.")
