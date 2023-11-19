import numpy as np
import random

class PuzzleNode:
    def __init__(self, state, parent, move):
        self.state = state
        self.parent = parent
        self.move = move

class HillClimbing:
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

    def solve_puzzle(self, initial_state, sc):
        current_node = PuzzleNode(initial_state, None, None)
        move_steps = []
        last_move = None  # Store the last move
        deep = 0

        while True:
            deep += 1
            if np.array_equal(current_node.state, self.GOAL_STATE):
                solution_path = []
                while current_node.parent is not None:
                    solution_path.append(current_node.move)
                    current_node = current_node.parent
                solution_path.reverse()
                return solution_path, deep

            blank_i, blank_j = self.get_blank_position(current_node.state)
            possible_moves = []

            for move_i, move_j in self.MOVES:
                new_i, new_j = blank_i + move_i, blank_j + move_j

                if self.is_valid_move(new_i, new_j) and (move_i, move_j) != last_move:
                    possible_moves.append(self.MOVE_NAMES[self.MOVES.index((move_i, move_j))])

            if not possible_moves:
                return None

            random.shuffle(possible_moves)
            move = possible_moves[0]
            if self.MOVES[self.MOVE_NAMES.index(move)] == (0, -1):
                last_move = (0, 1)
            if self.MOVES[self.MOVE_NAMES.index(move)] == (0, 1):
                last_move = (0, -1)
            if self.MOVES[self.MOVE_NAMES.index(move)] == (-1, 0):
                last_move = (1, 0)
            if self.MOVES[self.MOVE_NAMES.index(move)] == (1, 0):
                last_move = (-1,0)



            new_i, new_j = blank_i, blank_j
            if move == 'Left':
                new_j -= 1
            elif move == 'Right':
                new_j += 1
            elif move == 'Up':
                new_i -= 1
            elif move == 'Down':
                new_i += 1

            new_state = current_node.state.copy()
            new_state[blank_i][blank_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[blank_i][blank_j]

            new_node = PuzzleNode(new_state, current_node, move)
            current_node = new_node
if __name__ == "__main__":
    solver = HillClimbing()

    initial_state = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [0, 7, 8]
    ])


    solution = solver.solve_puzzle(initial_state)

    if solution:
        print("solution:")
        for move in solution:
            print(move)
    else:
        print("No solution found.")