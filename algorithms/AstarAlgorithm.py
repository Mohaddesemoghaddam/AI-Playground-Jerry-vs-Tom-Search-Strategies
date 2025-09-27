from node import Node
from time import process_time

class StarAlgorithm:
    def __init__(self, world):
        self.emptyNode = Node(None, None, "first father", -1, 0, 0, 0)
        self.firstNode = Node(world, self.emptyNode, " ", 0, 0, 0, 0)
        self.tomPos = self.firstNode.searchForTom()
        self.jerryPos = self.searchForJerry(world)
        self.stack = [self.firstNode]
        self.computingTime = ""
        self.length_world = world.shape[0]
        self.height_world = world.shape[1]

    def getNodeMinSumCostHeuristic(self, stack):
        return min(stack, key=lambda node: node.getSumCostHeuristic())

    def getComputingTime(self):
        return self.computingTime

    def setComputingTime(self, computingTime):
        self.computingTime = computingTime

    def searchForJerry(self, world):
        jerryPos = []
        for i in range(world.shape[0]):
            for j in range(world.shape[1]):
                if world[i, j] == self.firstNode.PRINCESS:
                    jerryPos = [i, j]
        return jerryPos

    def start(self):
        startTime = process_time()
        stack = self.stack
        tomPos = self.tomPos
        expandedNodes = 0
        depth = 0
        vis = [[False for _ in range(self.height_world)] for _ in range(self.length_world)]
        currentNode = stack[0]  
         
        while not currentNode.isGoal():
            vis[tomPos[0]][tomPos[1]] = True

            # حرکت به راست
            if (tomPos[1] + 1 < self.length_world and 
                currentNode.getState()[tomPos[0], tomPos[1] + 1] != 1 and 
                not vis[tomPos[0]][tomPos[1] + 1]):
                son = Node(currentNode.getState(), currentNode, "right", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())
                right = son.rightMovement(tomPos)
                son.setNewCost(right)
                son.setTomPos(right)
                son.setHeuristic(son.calculateManhattanDistance(self.jerryPos))
                son.setSumCostHeuristic(son.getCost() + son.getHeuristic())
                son.moveRight(tomPos)
                if son.avoidGoBack2(right):
                    stack.append(son)
                    depth = max(depth, son.getDepth())
                vis[tomPos[0]][tomPos[1] + 1] = True

            # حرکت به چپ
            if (tomPos[1] - 1 >= 0 and 
                currentNode.getState()[tomPos[0], tomPos[1] - 1] != 1 and 
                not vis[tomPos[0]][tomPos[1] - 1]):
                son = Node(currentNode.getState(), currentNode, "left", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())
                left = son.leftMovement(tomPos)
                son.setNewCost(left)
                son.setTomPos(left)
                son.setHeuristic(son.calculateManhattanDistance(self.jerryPos))
                son.setSumCostHeuristic(son.getCost() + son.getHeuristic())
                son.moveLeft(tomPos)
                if son.avoidGoBack2(left):
                    stack.append(son)
                    depth = max(depth, son.getDepth())
                vis[tomPos[0]][tomPos[1] - 1] = True

            # حرکت به پایین
            if (tomPos[0] + 1 < self.height_world and 
                currentNode.getState()[tomPos[0] + 1, tomPos[1]] != 1 and 
                not vis[tomPos[0] + 1][tomPos[1]]):
                son = Node(currentNode.getState(), currentNode, "down", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())
                down = son.downMovement(tomPos)
                son.setNewCost(down)
                son.setTomPos(down)
                son.setHeuristic(son.calculateManhattanDistance(self.jerryPos))
                son.setSumCostHeuristic(son.getCost() + son.getHeuristic())
                son.moveDown(tomPos)
                if son.avoidGoBack2(down):
                    stack.append(son)
                    depth = max(depth, son.getDepth())
                vis[tomPos[0] + 1][tomPos[1]] = True

            # حرکت به بالا
            if (tomPos[0] - 1 >= 0 and 
                currentNode.getState()[tomPos[0] - 1, tomPos[1]] != 1 and 
                not vis[tomPos[0] - 1][tomPos[1]]):
                son = Node(currentNode.getState(), currentNode, "up", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())
                up = son.upMovement(tomPos)
                son.setNewCost(up)
                son.setTomPos(up)
                son.setHeuristic(son.calculateManhattanDistance(self.jerryPos))
                son.setSumCostHeuristic(son.getCost() + son.getHeuristic())
                son.moveUp(tomPos)
                if son.avoidGoBack2(up):
                    stack.append(son)
                    depth = max(depth, son.getDepth())
                vis[tomPos[0] - 1][tomPos[1]] = True

            currentNode = self.getNodeMinSumCostHeuristic(stack)
            stack.remove(currentNode)  

            expandedNodes += 1
            tomPos = currentNode.getTomPos()

        elapsedTime = process_time() - startTime
        self.setComputingTime(f"{elapsedTime:.10f} s.")
        
        solution = currentNode.recreateSolutionWorld()
        solutionWorld = solution[::-1]
        print("Expanded nodes: ", expandedNodes + 1)
        print("Depth: ", depth)
        print("The final cost of the solution is: " + str(currentNode.getCost()))
        print(currentNode.recreateSolution())
        return [solutionWorld, expandedNodes + 1, depth]