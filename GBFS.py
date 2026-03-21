#66011212124 Phanuwat Khamtha
import heapq
def greedy_best_first_search_trace(graph, start, goal, heuristic):
    frontier = []
    heapq.heappush(frontier, (heuristic[start], start))

    visited = []
    visited_set = set()

    step = 0

    def print_frontier(frontier):
        return "[" + ", ".join(f"{n}{h}" for h, n in sorted(frontier)) + "]"

    while frontier:
        print(f"• Frontier:{print_frontier(frontier)};")
        print(f"Visited={visited}")

        h, current = heapq.heappop(frontier)

        if current == goal:
            print(f"• Success, {current}= goal!")
            return

        visited.append(f"{current}{h}")
        visited_set.add(current)

        for neighbor in graph.get(current, []):
            if neighbor not in visited_set:
                heapq.heappush(
                    frontier,
                    (heuristic[neighbor], neighbor)
                )

        step += 1


graph = {
    'S': ['A', 'B', 'C'],
    'A': ['D', 'E'],
    'B': ['F', 'G'],
    'C': ['H'],
    'H': ['I', 'J'],
    'I': ['K', 'L', 'M'],
    'G': []
}

heuristic = {
    'S': 0,
    'A': 3,
    'B': 6,
    'C': 5,
    'D': 9,
    'E': 8,
    'F': 12,
    'G': 14,
    'H': 7,
    'I': 5,
    'J': 6,
    'K': 1,
    'L': 10,
    'M': 2
}

greedy_best_first_search_trace(graph, 'S', 'I', heuristic)

