import heapq
import numpy as np
import pygame

from settings import WHITE, BLACK, BGCOLOUR
from sprite import UIElement, Button


class PuzzleNode:
    def __init__(self, state, parent, move, cost, heuristic):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = cost
        self.heuristic = heuristic

    def total_cost(self):
        return self.cost + self.heuristic

    def __lt__(self, other):
        return self.total_cost() < other.total_cost()

class Astar:
    def __init__(self, puzzle_size=3):
        self.PUZZLE_SIZE = puzzle_size
        self.GOAL_STATE = np.arange(0, puzzle_size * puzzle_size).reshape(puzzle_size, puzzle_size)
        self.MOVES = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        self.MOVE_NAMES = ['Left', 'Right', 'Up', 'Down']

    def get_blank_position(self, state):
        empty_pos = np.where(np.array(state) == 0)
        return empty_pos[0][0], empty_pos[1][0]

    def is_valid_move(self, x, y):
        return 0 <= x < self.PUZZLE_SIZE and 0 <= y < self.PUZZLE_SIZE

    def heuristic(self, state, target):
        h = 0
        for i in range(self.PUZZLE_SIZE):
            for j in range(self.PUZZLE_SIZE):
                if state[i][j] != 0:
                    target_i, target_j = divmod(state[i][j], self.PUZZLE_SIZE)
                    h += abs(i - target_i) + abs(j - target_j)
        return h

    def solve_puzzle(self, initial_state, sc):
        open_list = [PuzzleNode(initial_state, None, None, 0, self.heuristic(initial_state, self.GOAL_STATE))]
        closed_set = set()
        move_steps = []

        deep = 0

        while open_list:
            deep += 1
            # Button(430, 350, 300, 50, "Deep - %.f" % deep, WHITE, BLACK).draw(sc)
            #
            # pygame.display.flip()
            # # pygame.time.Clock().tick(60)
            current_node = heapq.heappop(open_list)

            if np.array_equal(current_node.state, self.GOAL_STATE):
                solution_path = []
                while current_node.parent is not None:
                    solution_path.append(current_node.move)
                    current_node = current_node.parent
                solution_path.reverse()
                return solution_path, deep

            closed_set.add(tuple(map(tuple, current_node.state)))

            blank_i, blank_j = self.get_blank_position(current_node.state)

            for move_i, move_j in self.MOVES:
                new_i, new_j = blank_i + move_i, blank_j + move_j

                if self.is_valid_move(new_i, new_j):
                    new_state = current_node.state.copy()
                    new_state[blank_i][blank_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[blank_i][blank_j]
                    new_move = self.MOVE_NAMES[self.MOVES.index((move_i, move_j))]
                    new_cost = current_node.cost + 1
                    new_heuristic = self.heuristic(new_state, self.GOAL_STATE)
                    new_node = PuzzleNode(new_state, current_node, new_move, new_cost, new_heuristic)

                    if tuple(map(tuple, new_state)) not in closed_set:
                        heapq.heappush(open_list, new_node)

        return None

if __name__ == "__main__":
    solver = Astar()

    initial_state = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [0, 7, 8]
    ])


    solution = solver.solve_puzzle(initial_state)

    if solution:
        print("Solution found! Moves:")
        for move in solution:
            print(move)
    else:
        print("No solution found.")