from __future__ import annotations
from board import Board
from collections.abc import Callable
import heapq
import copy

'''
Heuristics
'''
# The number of misplaced tiles are the numbers that are out of position in our current search.


def MT(board: Board) -> int:
    misplaced_tiles = 0

    # We iterate over the board to count the tiles. If any tiles are not the value they should be,
    # then we add one to misplaced_tiles.
    board_length = len(board.state)
    for i in range(board_length):
        for j in range(board_length):
            # If the current space on the board is not equal to the value it should be and it's not an empty
            # tile, then add one to misplaced tiles.
            if (i*board_length + j + 1 != board.state[i][j] and board.state[i][j] != 0):
                misplaced_tiles += 1
    return misplaced_tiles


def CB(board: Board) -> int:
    board_length = len(board.state)
    total = 0

    def findCB(num, current_x, current_y):
        #  Finds the distance to the number's correct position.
        subtotal = 0
        goal_state = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (
            1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1)}
        final_x = goal_state[num][0]
        final_y = goal_state[num][1]

        # Substract final x and y from current position of num
        if (current_x - final_x < 0):
            subtotal += -1*(current_x - final_x)
        else:
            subtotal += current_x - final_x

        if (current_y - final_y < 0):
            subtotal += -1*(current_y - final_y)
        else:
            subtotal += current_y - final_y
        return subtotal

    for i in range(board_length):
        for j in range(board_length):
            # Look at number that should be in current index.
            num = i*board_length + j + 1
            if (board.state[i][j] != 0 and board.state[i][j] != num):
                total += findCB(board.state[i][j], i, j)
            else:
                continue
    return total


def BF(board: Board):
    return 0


def NA(board: Board) -> int:
    # Add up the MT and CB heuristics to create an overestimating, non-admissible heuristic.
    total = MT(board) + CB(board)
    return total


'''
A* Search 
'''


def a_star_search(board: Board, heuristic: Callable[[Board], int]):

    # Declare initial values like the root node (the initial board) and the solution set used to create that board or state.
    pq = []
    max_nodes_explored = 60000
    visited_states = {}
    id = 1
    heapq.heappush(pq, [heuristic(board), id, (board, [])])

    # While there are still children to explore in the queue, continue popping them off and exploring them.
    while (len(pq) > 0 and max_nodes_explored >= id):
        *_, (current_state, solution) = heapq.heappop(pq)
        solution = copy.copy(solution)
        visited_states[str(current_state.state)] = True

        # If goal state has been found, we break the loop.
        if (board.check_solution(solution)):
            break

        # From the currently selected node, add its children to the priority queue.
        for child_node, direction in current_state.next_action_states():

            # If node hasn't been visited already, we should add it to the queue.
            # Otherwise, we should move on to the next child node.
            if str(child_node.state) in visited_states.keys():
                continue

            solution.append(direction)

            # The child node's value in the pq should be the child node's heuristic
            # (estimate of the cost to get to the goal state from the child node)
            # and the cost taken to get to the child node. The next node we explore
            # should have the lowest cost function
            # (smallest value of heuristic + smallest solution length) to find
            # the optimal solution.
            cost_function = heuristic(child_node) + len(solution)
            id += 1
            heapq.heappush(
                pq, [cost_function, id, (child_node, copy.copy(solution))])

            # Pop off last direction from the solution so we can check another transition model
            # (child node).
            solution.pop()

    # id represents all the states (nodes) that have been generated (id starts at 1 when the first state
    # is put in the priority queue).
    print(f'Number of Search Nodes Generated: {id}')
    return solution
