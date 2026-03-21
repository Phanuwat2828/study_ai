#66011212124 Phanuwat Khamtha
from collections import deque
import time 
graph = {
'A': ['B', 'C', 'D'],
'B': ['E', 'F'],
'C': ['G','H'],
'D': [],
'E': ['I','J'],
'F': ['K'],
'G': ['L','M'],
'H': [],
'I': [],
'J': [],
'K': [],
'L': [],
'M': []
}

def dfs_graph_search(graph, start, goal):
    if start not in graph:
        print("Start node not in graph")
        return False
    stack = [start]
    visited = {start}
    order = []
    print(f"Starting DFS from {start} to find {goal}")
    while stack:
        print("stack : ",stack);
        current = stack.pop()
        order.append(current)
        print("visiting: ", current)
        if current == goal: 
            print(f"ผลลัพธ์ : พบเป้าหมาย ",goal)
            print(order)
            print("\n" + "="*50 + "\n")
            return True
        for neighbor in reversed(graph.get(current, [])):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
        time.sleep(0.5)  # Pause for visualization
    print(f"ผลลัพธ์ : ไม่พบเป้าหมาย ",goal)
    return False

#66011212124 Phanuwat Khamtha
goal = 'I'
print(f"[ตัวอย่างที่ 1: ค้นหาโหนด {goal} (อยู่ลึก) ]")
found = dfs_graph_search(graph, 'A', goal)

# ตัวอย่างที่2: ค้นหาโหนด 'Z' (ไม่พบ)
goal='Z'
print(f"[ตัวอย่างที่ 2: ค้นหาโหนด {goal} (ไม่พบ)]")
found = dfs_graph_search(graph, 'A', goal)