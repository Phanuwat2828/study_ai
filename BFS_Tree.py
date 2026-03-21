#66011212124 Phanuwat Khamtha
from collections import deque
class Node:
    def __init__(self,data):
        self.data = data # ข้อมูลที่เก็บใน Node
        self.children = [] # Node ลูก

    def add_child(self,child_node):
        self.children.append(child_node) # เพิ่ม Node ลูก
    
    def __repr__(self): # แสดงข้อมูล Node
        return f"Node({self.data})"
    
def bsf_tree_search(root_node,target_data):
    if root_node is None:
        return None # กรณีที่ Node รากเป็น None
    
    queue = deque([root_node]) # สร้างคิวเริ่มต้นด้วย Node ราก
    print(f"เริ่มการค้นหาแบบ BFS  Target: {target_data}...")
    
    while queue:
        
        current_node = queue.popleft() # นำ Node แรกออกจากคิว
        print(f"สำรวจ Node: {current_node.data}")
        if current_node.data == target_data: # ตรวจสอบข้อมูล
            return current_node # พบ Node ที่ต้องการ
        for child in current_node.children:
            queue.append(child) # เพิ่ม Node ลูกลงในคิว
    return None # ไม่พบ Node ที่ต้องการ

#66011212124 Phanuwat Khamtha
# สร้างต้นไม้ตัวอย่าง
root = Node("A")
node_b = Node("B")
node_c = Node("C")
node_d = Node("D")
node_e = Node("E")
node_f = Node("F")
node_g = Node("G")
node_h = Node("H")


# สร้างความสัมพันธ์ระหว่าง Node
root.add_child(node_b)
root.add_child(node_c)  
node_b.add_child(node_d)
node_b.add_child(node_e)
node_c.add_child(node_f)
node_c.add_child(node_g)
node_e.add_child(node_h)


# เรียกใช้ฟังก์ชันค้นหา
while True:
    goal = input("ป้อนข้อมูล Node ที่ต้องการค้นหา (หรือ 'exit' เพื่อออก): ")
    if goal=="":
        break
    result_node = bsf_tree_search(root,goal)
    print("ผลลัพธ์การค้นหา:")
    if result_node:
        print("พบ Node:", result_node.data)
    else:
        print("ไม่พบ Node ที่ต้องการค้นหา")
