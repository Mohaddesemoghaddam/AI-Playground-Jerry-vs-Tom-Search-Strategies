from node import Node
from time import process_time
from collections import deque  


class AmplitudeAlgorithm:
    def __init__(self, world):
        self.emptyNode = Node(None, None, "first father", -1, 0, 0, 0)
        self.firstNode = Node(world, self.emptyNode, " ", 0, 0, 0, 0)
        self.tomPos = self.firstNode.searchForTom()
        self.queue = deque([self.firstNode])  
        self.computingTime = ""
        self.length_world = world.shape[0]
        self.height_world = world.shape[1]

    def getComputingTime(self):
        return self.computingTime

    def setComputingTime(self, computingTime):
        self.computingTime = computingTime

    def start(self):
        startTime = process_time()

        queue = self.queue
        expandedNodes = 0
        depth = 0
        vis = [[False for _ in range(self.height_world)] for _ in range(self.length_world)]

        while queue:
            currentNode = queue.popleft()  
            tomPos = currentNode.getTomPos()
            expandedNodes += 1  
            vis[tomPos[0]][tomPos[1]] = True

            
            if currentNode.isGoal():
                break

            if (tomPos[1] + 1 < self.height_world and 
                    currentNode.getState()[tomPos[0], tomPos[1] + 1] != 1 and 
                    not vis[tomPos[0]][tomPos[1] + 1]):
                son = Node(currentNode.getState(), currentNode, "right", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())
                right = son.rightMovement(tomPos)
                son.setNewCost(right)
                son.setTomPos(right)
                son.moveRight(tomPos)
                if son.compareCicles2(right):
                    queue.append(son)  
                    if son.getDepth() > depth:
                        depth = son.getDepth()
                vis[tomPos[0]][tomPos[1] + 1] = True

            
            if (tomPos[1] - 1 >= 0 and 
                    currentNode.getState()[tomPos[0], tomPos[1] - 1] != 1 and 
                    not vis[tomPos[0]][tomPos[1] - 1]):
                son = Node(currentNode.getState(), currentNode, "left", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())
                left = son.leftMovement(tomPos)
                son.setNewCost(left)
                son.setTomPos(left)
                son.moveLeft(tomPos)
                if son.compareCicles2(left):
                    queue.append(son)
                    if son.getDepth() > depth:
                        depth = son.getDepth()
                vis[tomPos[0]][tomPos[1] - 1] = True

            
            if (tomPos[0] + 1 < self.length_world and 
                    currentNode.getState()[tomPos[0] + 1, tomPos[1]] != 1 and 
                    not vis[tomPos[0] + 1][tomPos[1]]):
                son = Node(currentNode.getState(), currentNode, "down", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())
                down = son.downMovement(tomPos)
                son.setNewCost(down)
                son.setTomPos(down)
                son.moveDown(tomPos)
                if son.compareCicles2(down):
                    queue.append(son)
                    if son.getDepth() > depth:
                        depth = son.getDepth()
                vis[tomPos[0] + 1][tomPos[1]] = True

            
            if (tomPos[0] - 1 >= 0 and 
                    currentNode.getState()[tomPos[0] - 1, tomPos[1]] != 1 and 
                    not vis[tomPos[0] - 1][tomPos[1]]):
                son = Node(currentNode.getState(), currentNode, "up", currentNode.getDepth() + 1, currentNode.getCost(), currentNode.getStar(), currentNode.getFlower())
                up = son.upMovement(tomPos)
                son.setNewCost(up)
                son.setTomPos(up)
                son.moveUp(tomPos)
                if son.compareCicles2(up):
                    queue.append(son)
                    if son.getDepth() > depth:
                        depth = son.getDepth()
                vis[tomPos[0] - 1][tomPos[1]] = True

        elapsedTime = process_time() - startTime
        elapsedTimeFormatted = "%.10f s." % elapsedTime
        self.setComputingTime(elapsedTimeFormatted)

        solution = currentNode.recreateSolutionWorld()  
        solutionWorld = solution[::-1]
        print("Expanded nodes: ", expandedNodes)
        print("Depth: ", depth)
        print("The final cost of the solution is: " + str(currentNode.getCost()))
        print(currentNode.recreateSolution())
        return [solutionWorld, expandedNodes, depth]
