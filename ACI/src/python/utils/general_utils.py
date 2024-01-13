class Point():
    '''
    Storing maze coordinate points as (row, column) points
    '''
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class Node():
    '''
    store the maze information as coordinate point and distance from source node.
    '''
    def __init__(self, coordinate, distance) -> None:
        self.coordinate = coordinate
        self.distance = distance


def get_n4_neighbourhood():
    return [0, -1, 0, 1], [1, 0, -1, 0]

def get_n8_neighbourhood():
    return [0, -1, -1, -1, 0, 1, 1, 1], [1, 1, 0, -1, -1, -1, 0, 1]