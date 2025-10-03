# Search Algorithms Implementation and Analysis

This project contains the implementation and analysis of several fundamental search algorithms applied to graph and maze problems. The goal is to evaluate the efficiency, optimality, and completeness of each algorithm under different scenarios.

---

## 📖 Algorithms Covered
- **Breadth-First Search (BFS)** – Explores level by level, guarantees the shortest path in unweighted graphs.  
- **Depth-First Search (DFS)** – Explores as deep as possible along each branch, memory-efficient but not always optimal.  
- **Uniform Cost Search (UCS)** – Finds the least-cost path considering variable step costs.  
- **Greedy Best-First Search** – Uses heuristic functions to prioritize nodes closer to the goal.  
- **A*** – Combines path cost and heuristic to guarantee an optimal solution (if admissible and consistent).  

---

## 📂 Project Structure
- **`bfs.py`** – Implementation of BFS with queue data structure.  
- **`dfs.py`** – Implementation of DFS with recursion and stack.  
- **`ucs.py`** – Implementation of UCS using priority queues.  
- **`greedy.py`** – Greedy search with heuristic evaluation.  
- **`astar.py`** – A* algorithm combining cost and heuristic.  
- **`utils.py`** – Helper functions for graph representation and visualization.  
- **`report.pdf`** – Full written analysis and comparison of algorithms (Persian report provided).  

---

## ⚙️ How to Run
1. Install dependencies (if any):  
   ```bash
   pip install -r requirements.txt
   ```  

2. Run a specific algorithm:  
   ```bash
   python bfs.py
   python dfs.py
   python ucs.py
   python greedy.py
   python astar.py
   ```  

---

## 📊 Evaluation Criteria
Each algorithm was analyzed based on:  
- **Completeness** (Does it always find a solution?)  
- **Optimality** (Does it guarantee the best/shortest solution?)  
- **Time Complexity**  
- **Space Complexity**  
- **Number of Expanded Nodes**  

---

## 🔍 Results & Insights
- **BFS** is complete and optimal for unweighted graphs but has high memory usage.  
- **DFS** is memory-efficient but not optimal; may get stuck in deep paths.  
- **UCS** guarantees optimal solutions with varying step costs but can be slow.  
- **Greedy** is fast but not always optimal (depends on heuristic quality).  
- **A*** is the most powerful, combining path cost and heuristic, and guarantees optimality if heuristics are admissible and consistent.  

---
