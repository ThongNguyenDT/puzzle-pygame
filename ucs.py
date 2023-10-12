import heapq

from solver import Solver


class UCS(Solver):
    def __init__(self, initial_stata):
        super(UCS, self).__init__(initial_stata)
        self.frontier = []

    def solve(self):
        heapq.heappush(self.frontier, self.initial_state)
        while self.frontier:
            board = heapq.heappop(self.frontier)
            self.explored_nodes.add(tuple(board.state))
            # if tuple(board.state) in self.explored_nodes:
            #     continue
            if board.goal_test():
                self.set_solution(board)
                break
            for neighbor in board.neighbors():
                if tuple(neighbor.state) not in self.explored_nodes:
                    heapq.heappush(self.frontier, neighbor)
                    self.explored_nodes.add(tuple(neighbor.state))
                    self.max_depth = max(self.max_depth, neighbor.depth)
        return


# def ucs(graph, start, goal):
#     # Priority queue to store nodes to be explored
#     frontier = [(0, start, [])]  # (cost, node, path)
#     explored = set()  # Set to keep track of explored nodes
#
#     while frontier:
#         cost, current_node, path = heapq.heappop(frontier)  # Get the node with the lowest cost
#         if current_node in explored:
#             continue  # Skip this node if it has already been explored
#
#         explored.add(current_node)  # Mark the current node as explored
#         path = path + [current_node]
#
#         if current_node == goal:
#             return path  # If the goal is reached, return the path
#
#         # Explore the neighbors of the current node
#         for neighbor, neighbor_cost in graph[current_node].items():
#             if neighbor not in explored:
#                 total_cost = cost + neighbor_cost
#                 heapq.heappush(frontier, (total_cost, neighbor, path))  # Add neighbors to the frontier
#
#     return None  # If the goal is not reached, return None
#
# # Example usage:
# graph = {
#     'S': {'B': 2, 'A': 3},
#     'A': {'B': 2, 'C': 1, 'D': 3},
#     'B': {'C': 4},
#     'C': {'D': 1, 'G': 3},
#     'D': {'G': 2},
#     'G': {}
# }
#
# start_node = 'S'
# goal_node = 'G'
#
# result = ucs(graph, start_node, goal_node)
# if result is not None:
#     print(f"Shortest path from {start_node} to {goal_node}: {result}")
# else:
#     print(f"No path found from {start_node} to {goal_node}.")
