import numpy as np
import pygame

from settings import WHITE, BLACK
from sprite import Button


class DFS:
    def __init__(self, puzzle_size=3):
        self.PUZZLE_SIZE = puzzle_size
        self.GOAL_STATE = np.arange(0, puzzle_size * puzzle_size).reshape(puzzle_size, puzzle_size)
        self.MOVES = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        self.MOVE_NAMES = ['Left', 'Right', 'Up', 'Down']

    def get_neighbors(self, state):
        neighbors = []
        empty_pos = np.where(np.array(state) == 0)
        empty_row, empty_col = empty_pos[0][0], empty_pos[1][0]

        for move, move_name in zip(self.MOVES, self.MOVE_NAMES):
            new_row, new_col = empty_row + move[0], empty_col + move[1]
            if 0 <= new_row < self.PUZZLE_SIZE and 0 <= new_col < self.PUZZLE_SIZE:
                new_state = state.copy()
                new_state[empty_row, empty_col], new_state[new_row, new_col] = new_state[new_row, new_col], new_state[empty_row, empty_col]
                neighbors.append((new_state, move_name))

        return neighbors

    def solve_puzzle(self, initial_state, sc):
        visited = set()
        stack = [(initial_state, [])]

        deep = 0
        while stack:
            deep += 1
            # Button(430, 350, 300, 50, "Deep - %.f" % deep, WHITE, BLACK).draw(sc)
            #
            # pygame.display.flip()
            # # pygame.time.Clock().tick(60)
            current_state, moves = stack.pop()

            if np.array_equal(current_state, self.GOAL_STATE):
                return moves, deep

            if tuple(map(tuple, current_state)) in visited:
                continue

            visited.add(tuple(map(tuple, current_state)))

            for neighbor_state, move_name in self.get_neighbors(current_state):
                if tuple(map(tuple, neighbor_state)) not in visited:
                    stack.append((neighbor_state, moves + [move_name]))

        return None  # If no solution is found

    def solve_and_print_solution(self, initial_state):
        solution = self.solve_puzzle(initial_state)
        if solution:
            print("Solution:", solution)
        else:
            print("No solution found.")
