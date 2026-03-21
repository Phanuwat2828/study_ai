graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J'],
    'F': ['K'],
    'G': [],
    'H': ['C'],
    'I': [ ],
    'J': [ 'L'],
    'K': [ ]
}

def recursive_dls(graph, current_node, goal_state, limit, current_depth, visited_nodes, parents, path_current):
    
    if current_node == goal_state:
        print(f"  ✓ Found goal '{goal_state}' at depth {current_depth}")
        return current_node
    
    if current_depth == limit:
        print(f"  ✗ Reached depth limit {limit} at node '{current_node}'")
        return "Cutoff"
    
    cutoff_occurred = False
    
    visited_nodes.add(current_node)
    path_current.append(current_node)
    
    # Show current path
    print(f"  Path: {' -> '.join(path_current)}")
    
    for neighbor in graph.get(current_node, []):
        if neighbor not in visited_nodes:
            print(f"    → Exploring '{neighbor}' (depth {current_depth + 1})")
            result = recursive_dls(graph, neighbor, goal_state, limit, 
                                  current_depth + 1, visited_nodes, parents, path_current)
            
            if result == "Cutoff":
                cutoff_occurred = True
                print(f"    ↳ Backtracking from '{neighbor}' due to cutoff")
            elif result is not None:
                # Found goal, propagate back up
                return result
    
    # Backtrack
    path_current.pop()
    visited_nodes.remove(current_node)
    
    if cutoff_occurred:
        print(f"  ↺ Backtracking from '{current_node}' (cutoff occurred)")
        return "Cutoff"
    
    print(f"  ↺ Backtracking from '{current_node}' (no solution)")
    return None

def reconstruct_path(parents, current_node):
    path = []
    while current_node is not None:
        path.append(current_node)
        current_node = parents.get(current_node)
    return path[::-1]

def ids_search(graph, start_node, goal_state, max_depth):
    print("=" * 60)
    print(f"IDS SEARCH")
    print(f"Start: {start_node}, Goal: {goal_state}, Max Depth: {max_depth}")
    print("=" * 60)
    
    for depth in range(max_depth + 1):
        print(f"\n{'─' * 50}")
        print(f"Depth Limit: {depth}")
        print(f"{'─' * 50}")
        
        visited_nodes = set()
        parents = {start_node: None}
        path_current = []  # Track current path for printing
        
        result = recursive_dls(graph, start_node, goal_state, depth, 0, 
                               visited_nodes, parents, path_current)
        
        if result is not None and result != "Cutoff":
            print(f"\n{'=' * 60}")
            print(f"✓ SUCCESS: Goal '{goal_state}' found at depth {depth}!")
            print(f"{'=' * 60}")
            return reconstruct_path(parents, result)
        
        print(f"\n✗ Goal not found at depth limit {depth}")
    
    print(f"\n{'=' * 60}")
    print(f"✗ FAILED: Goal '{goal_state}' not found up to max depth {max_depth}")
    print(f"{'=' * 60}")
    return None

# Run the search
solution_path = ids_search(graph, 'A', 'J', max_depth=5)

if solution_path:
    print(f"\n🎯 Complete Search Path to Goal:")
    print(f"   {' → '.join(solution_path)}")
    print(f"\n📊 Path Length: {len(solution_path) - 1} steps")
else:
    print(f"\n❌ Goal not found")