import heapq
import numpy as np

class UCS:
    def __init__(self):
        self.MOVES = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        self.MOVE_NAMES = ['Left', 'Right', 'Up', 'Down']
        self.GOAL_STATE = np.arange(0, 9).reshape(3, 3)

    def solve_puzzle(self, initial_state):
        initial_state = np.array(initial_state).reshape((9,1)).flatten().tolist()
        def is_goal(puzzle):
            return puzzle == self.GOAL_STATE.reshape((9,1)).flatten().tolist()

        def generate_successors(puzzle, cost):
            successors = []
            empty_cell = puzzle.index(0)

            for move, move_name in zip(self.MOVES, self.MOVE_NAMES):
                new_row = empty_cell // 3 + move[0]
                new_col = empty_cell % 3 + move[1]

                if 0 <= new_row < 3 and 0 <= new_col < 3:
                    new_puzzle = puzzle[:]
                    new_index = new_row * 3 + new_col
                    new_puzzle[empty_cell], new_puzzle[new_index] = new_puzzle[new_index], new_puzzle[empty_cell]
                    successors.append((new_puzzle, move_name, cost + 1))

            return successors

        visited = set()
        frontier = []
        start = (initial_state, None, None, 0)
        heapq.heappush(frontier, start)

        while frontier:
            current_puzzle, parent, action, cost = heapq.heappop(frontier)

            if is_goal(current_puzzle):
                path = []
                while action:
                    path.append(action)
                    current_puzzle, action, parent, cost = parent
                return path[::-1]

            visited.add(tuple(current_puzzle))

            for successor_puzzle, successor_action, successor_cost in generate_successors(current_puzzle, cost):
                if tuple(successor_puzzle) not in visited:
                    heapq.heappush(frontier, (successor_puzzle, (current_puzzle, action, parent, cost), successor_action, successor_cost))

        return None

# Example usage:
# initial_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]
# goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
#
# solver = UCS()
# path = solver.solve_puzzle(initial_state)
#
# if path:
#     print("Solution Path:", path)
# else:
#     print("No solution found.")
