
import heapq
import itertools

class Graph:
    def __init__(self, graph_data, h_data):
        self.graph_data = graph_data
        self.h_data = h_data

    def get_neighbors(self, node):
        return self.graph_data.get(node, [])

    def h(self, node):
        return self.h_data.get(node, 0)

class seach:
    def __init__(self, graph):
        self.graph = graph
        self.counter = itertools.count()

    def Astar_search(self, start, goal):
        frontier = []
        heapq.heappush(
            frontier,
            (self.graph.h(start), 0, next(self.counter), start)
        )

        g_cost = {start: 0}
        parents = {start: None}
        visited = set()

        while frontier:
            f_current, g_current, _, current_node = heapq.heappop(frontier)

            if current_node == goal:
                return self._reconstruc(parents, current_node), g_current

            if current_node in visited:
                continue

            visited.add(current_node)

            for neighbor, weight in self.graph.get_neighbors(current_node):
                if neighbor in visited:
                    continue

                tentative_g = g_current + weight

                if tentative_g < g_cost.get(neighbor, float('inf')):
                    g_cost[neighbor] = tentative_g
                    parents[neighbor] = current_node
                    f_cost = tentative_g + self.graph.h(neighbor)

                    heapq.heappush(
                        frontier,
                        (f_cost, tentative_g, next(self.counter), neighbor)
                    )

        return None, float('inf')
    def beam_search(self, start, goal, beam_width=3):
        frontier = [(self.graph.h(start), start)]
        parents = {start: None}

        step = 0
        while frontier:
            step += 1

            # check goal
            for _, node in frontier:
                if node == goal:
                    return self._reconstruc(parents, node), step

            next_candidates = []

            for _, current_node in frontier:
                for neighbor, _ in self.graph.get_neighbors(current_node):
                    if neighbor not in parents:   # กันวนแบบเบา ๆ
                        parents[neighbor] = current_node
                        h_val = self.graph.h(neighbor)
                        next_candidates.append((h_val, neighbor))

            if not next_candidates:
                break

            next_candidates.sort(key=lambda x: x[0])
            frontier = next_candidates[:beam_width]

        return None, float('inf')
    def _reconstruc(self, parents, current_node):
        path = []
        while current_node is not None:
            path.append(current_node)
            current_node = parents[current_node]
        return path[::-1]


class PuzzleGraph(Graph):
    """Inheritance from Graph and override methods"""

    def __init__(self, goal_state):
        self.goal_state = goal_state

    def h(self, node):
        """Manhattan Distance (Polymorphism)"""
        distance = 0
        for i, val in enumerate(node):
            if val != 0:
                curr_r, curr_c = divmod(i, 3)
                goal_idx = self.goal_state.index(val)
                goal_r, goal_c = divmod(goal_idx, 3)
                distance += abs(curr_r - goal_r) + abs(curr_c - goal_c)
        return distance

    def get_neighbors(self, node):
        """Generate possible moves"""
        neighbors = []
        state = list(node)

        zero_idx = state.index(0)
        r, c = divmod(zero_idx, 3)

        moves = [(-1,0), (1,0), (0,-1), (0,1)]

        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                new_state = state[:]
                swap_idx = nr * 3 + nc
                new_state[zero_idx], new_state[swap_idx] = \
                    new_state[swap_idx], new_state[zero_idx]

                neighbors.append((tuple(new_state), 1))

        return neighbors
def print_path(path, total_cost):
    if not path:
        print("Not found")
        return

    print(f"Finish! process {total_cost} levels\n")
    for step_idx, step in enumerate(path):
        print(f"Level {step_idx}")
        for i in range(0, 9, 3):
            print(step[i:i+3])
        print("-" * 12)
if __name__ == "__main__":
    start_node = (
        2, 4, 1,
        8, 5, 6,
        3, 7, 0
    )
    goal_node = (
        1, 2, 3,
        8, 0, 4,
        7, 6, 5
    )

    graph = PuzzleGraph(goal_node)
    search = seach(graph)
    path, cost = search.Astar_search(start_node, goal_node)
    path_b,cost_b = search.beam_search(start_node, goal_node, beam_width=3)
    
print_path(path, cost)
print_path(path_b, cost_b)