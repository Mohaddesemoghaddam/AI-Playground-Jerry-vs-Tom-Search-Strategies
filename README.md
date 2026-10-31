# Tom vs. Jerry: Search Strategies in an Interactive Maze

An interactive **Pygame** application in which Tom searches a maze for Jerry using five classical **uninformed and informed search algorithms**. Each run animates the path found and reports the **computing time** and **number of expanded nodes**, so the algorithms can be compared side by side.

## Algorithms

| Algorithm | Type | Key property |
|---|---|---|
| **Breadth-First Search (BFS)** | Uninformed | Finds the shortest path in unweighted mazes |
| **Depth-First Search (DFS)** | Uninformed | Low memory use; explores deep branches first |
| **Uniform Cost Search (UCS)** | Uninformed | Finds the lowest-cost path with variable step costs |
| **Greedy Best-First Search** | Informed | Fast, guided by a Manhattan-distance heuristic |
| **A\*** | Informed | Combines path cost and heuristic for optimal paths with an admissible heuristic |

## Features

- Interactive maze rendered with Pygame, with buttons for each algorithm
- Step-by-step animation of the path from Tom to Jerry
- Live display of **computing time** and **number of expanded nodes**
- Maze loaded from a simple text file, so new maps are easy to create
- Manhattan-distance heuristic for Greedy and A\*
- Background music and character sprites

## Project structure

```text
├── main.py                 # entry point: loads the maze and starts the interface
├── interface.py            # Pygame interface, animation, and statistics
├── node.py                 # search-tree node: state, cost, depth, heuristic
├── matrix.txt              # maze definition
├── algorithms/
│   ├── bfsAlgorithm.py
│   ├── dfsAlgorithm.py
│   ├── costAlgorithm.py    # Uniform Cost Search
│   ├── greedyAlgorithm.py
│   └── AstarAlgorithm.py
├── images/                 # Tom and Jerry sprites
└── music/                  # background music
```

## Maze format

The maze in `matrix.txt` is a grid of space-separated numbers:

| Value | Meaning |
|---:|---|
| `0` | Free cell |
| `1` | Wall |
| `2` | Tom (start) |
| `6` | Jerry (goal) |

Edit this file to try the algorithms on different mazes.

## How to run

```bash
git clone https://github.com/Mohaddesemoghaddam/AI-Playground-Jerry-vs-Tom-Search-Strategies.git
cd AI-Playground-Jerry-vs-Tom-Search-Strategies
pip install pygame numpy
python main.py
```

Click an algorithm name on the right side of the window to run it and watch Tom find Jerry.

## Comparison criteria

Each algorithm is compared on:

- **Completeness:** does it always find a solution?
- **Optimality:** does it find the shortest or cheapest path?
- **Time complexity:** measured as computing time
- **Space complexity:** reflected in the number of expanded nodes

## Insights

- **BFS** is complete and optimal on unweighted mazes but expands many nodes.
- **DFS** uses little memory but may return long, non-optimal paths.
- **UCS** guarantees the lowest-cost path when step costs vary.
- **Greedy** search is fast but its paths depend on heuristic quality.
- **A\*** balances path cost and heuristic guidance, finding optimal paths while typically expanding fewer nodes than uninformed methods.

## Tech stack

Python · Pygame · NumPy
