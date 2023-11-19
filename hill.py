import numpy as np
import pygame

from settings import WHITE, BLACK
from sprite import Button


class PuzzleNode:
    def __init__(self, state, parent, move, cost, heuristic):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = cost
        self.heuristic = heuristic

    def total_cost(self):
        return self.cost + self.heuristic

class HillClimbingPuzzleSolver:
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

    def heuristic(self, state):
        h = 0
        for i in range(self.PUZZLE_SIZE):
            for j in range(self.PUZZLE_SIZE):
                if state[i][j] != 0:
                    target_i, target_j = divmod(state[i][j], self.PUZZLE_SIZE)
                    h += abs(i - target_i) + abs(j - target_j)
        return h

    def hill_climbing(self, initial_state, sc, max_iterations=1000):
        current_state = initial_state
        current_value = self.heuristic(current_state)

        path_to_solution = []  # Store the path to the solution
        deep = 0
        for iteration in range(max_iterations):
            deep += 1
            # Button(430, 350, 300, 50, "Deep - %.f" % deep, WHITE, BLACK).draw(sc)
            #
            # pygame.display.flip()
            # # pygame.time.Clock().tick(60)
            neighbors = []
            blank_i, blank_j = self.get_blank_position(current_state)

            for move_i, move_j in self.MOVES:
                new_i, new_j = blank_i + move_i, blank_j + move_j

                if self.is_valid_move(new_i, new_j):
                    new_state = current_state.copy()
                    new_state[blank_i][blank_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[blank_i][blank_j]
                    new_value = self.heuristic(new_state)
                    neighbors.append((new_state, new_value, self.MOVE_NAMES[self.MOVES.index((move_i, move_j))]))

            best_neighbor = min(neighbors, key=lambda x: x[1])

            if best_neighbor[1] >= current_value:
                break

            path_to_solution.append(best_neighbor[2])  # Append the move name to the path
            current_state = best_neighbor[0]
            current_value = best_neighbor[1]
            print(path_to_solution)

        return path_to_solution, deep

if __name__ == "__main__":
    solver = HillClimbingPuzzleSolver()

    initial_state = np.array([
        [1, 0, 2],
        [3, 4, 6],
        [7, 5, 8]
    ])

    result, solution_path = solver.hill_climbing(initial_state, max_iterations=1000)
    print(solution_path)
    for move in solution_path:
        print(move)
    if np.array_equal(result, solver.GOAL_STATE):
        print("Solution found! Path to the solution:")
    else:
        print("No solution found.")

