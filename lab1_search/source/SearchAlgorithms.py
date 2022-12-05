from importlib.machinery import all_suffixes
from msilib.schema import Error
from matplotlib.pyplot import close
from numpy import empty
from Space import *
from Constants import *
import time
import math

def DFS(g:Graph, sc:pygame.Surface):
    print('Implement DFS algorithm')

    open_set:list[Node] = [g.start]
    closed_set:list[Node] = []
    father = [None]*g.get_len()
    
    while open_set:

        node = open_set.pop()

        if node not in closed_set:

            node.set_color(yellow)
            node.draw(sc)
            pygame.display.flip()
            time.sleep(0.1)

            closed_set.append(node)
            if g.is_goal(node):
                break

            neighbors:list[Node] = g.get_neighbors(node)

            for neighbor_node in neighbors:

                if neighbor_node not in closed_set:
                    open_set.append(neighbor_node)
                    father[neighbor_node.value] = node
                    neighbor_node.set_color(red)
                    neighbor_node.draw(sc)
                    pygame.display.flip()
                    time.sleep(0.1)

            node.set_color(blue)
            node.draw(sc)
            pygame.display.flip()
            time.sleep(0.1)
    
    g.start.set_color(orange)
    g.goal.set_color(purple)
    g.start.draw(sc)
    g.goal.draw(sc)
    pygame.display.flip()
    time.sleep(0.1)

    node = g.goal
    father_node = father[node.value]

    while father_node is not None:

        x1 = node.x
        y1 = node.y
        x2 = father_node.x
        y2 = father_node.y
        pygame.draw.line(sc, green, (x1, y1), (x2, y2), 2)
        if father_node != g.start:
            father_node.set_color(grey)
        father_node.draw(sc)
        node.draw(sc)
        pygame.display.flip()
        time.sleep(0.1)

        node = father_node
        father_node = father[father_node.value]
    
    print("DFS algorithm completed!")

def BFS(g:Graph, sc:pygame.Surface):
    print('Implement BFS algorithm')

    open_set:list[Node] = [g.start]
    closed_set:list[Node] = []
    father = [None]*g.get_len()

    while open_set:

        node = open_set.pop()
        if node not in closed_set:

            node.set_color(yellow)
            node.draw(sc)
            pygame.display.flip()
            time.sleep(0.05)

            closed_set.append(node)
            if g.is_goal(node):
                break

            neighbors:list[Node] = g.get_neighbors(node)

            for neighbor_node in neighbors:

                if neighbor_node not in closed_set and neighbor_node not in open_set:
                    open_set.insert(0, neighbor_node)
                    father[neighbor_node.value] = node
                    neighbor_node.set_color(red)
                    neighbor_node.draw(sc)
                    pygame.display.flip()
                    time.sleep(0.05)

            node.set_color(blue)
            node.draw(sc)
            pygame.display.flip()
            time.sleep(0.05)
    
    g.start.set_color(orange)
    g.goal.set_color(purple)
    g.start.draw(sc)
    g.goal.draw(sc)
    pygame.display.flip()
    time.sleep(0.05)

    node = g.goal
    father_node = father[node.value]

    while father_node is not None:

        x1 = node.x
        y1 = node.y
        x2 = father_node.x
        y2 = father_node.y
        pygame.draw.line(sc, green, (x1, y1), (x2, y2), 2)
        if father_node != g.start:
            father_node.set_color(grey)
        father_node.draw(sc)
        node.draw(sc)
        pygame.display.flip()
        time.sleep(0.05)

        node = father_node
        father_node = father[father_node.value]
    
    print("BFS algorithm completed!")
    
def key_cost(e):
    return e[0]

def UCS(g:Graph, sc:pygame.Surface):
    print('Implement UCS algorithm')

    open_set:list[(float, Node)] = []
    open_set.append((0, g.start))  
    closed_set:list[Node] = []
    father = [None]*g.get_len()
    cost = [100000]*g.get_len()

    while open_set:

        path_cost, node = open_set.pop()
        if node not in closed_set: 

            node.set_color(yellow)
            node.draw(sc)
            pygame.display.flip()
            time.sleep(0.05)

            closed_set.append(node)
            if g.is_goal(node):
                break

            neighbors:list[Node] = g.get_neighbors(node)
            x1 = node.x
            y1 = node.y

            for neighbor_node in neighbors:

                if neighbor_node not in closed_set:

                    x2 = neighbor_node.x
                    y2 = neighbor_node.y
                    cal_cost = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

                    if cost[neighbor_node.value] > cal_cost + path_cost:
                        #try:
                            #i = open_set.index((cost[neighbor_node.value], neighbor_node))
                        #except ValueError:
                        cost[neighbor_node.value] = cal_cost + path_cost
                        open_set.append((cost[neighbor_node.value], neighbor_node))
                        #else:
                            #cost[neighbor_node.value] = cal_cost + path_cost
                            #try:
                                #open_set[i][0] = cost[neighbor_node.value] # wrong ?
                            #except:
                                #print("Khong assign dc")
                            #else:
                                #print(f"Assign thanh cong {open_set[i][0]} = {cost[neighbor_node.value]}")

                        #finally:
                        father[neighbor_node.value] = node
                        open_set.sort(key=key_cost, reverse=True)        

                    neighbor_node.set_color(red)
                    neighbor_node.draw(sc)
                    pygame.display.flip()
                    time.sleep(0.05)

            node.set_color(blue)
            node.draw(sc)
            pygame.display.flip()
            time.sleep(0.05)

    g.start.set_color(orange)
    g.goal.set_color(purple)
    g.start.draw(sc)
    g.goal.draw(sc)
    pygame.display.flip()
    time.sleep(0.05)

    node = g.goal
    father_node = father[node.value]

    while father_node is not None:

        x1 = node.x
        y1 = node.y
        x2 = father_node.x
        y2 = father_node.y
        pygame.draw.line(sc, green, (x1, y1), (x2, y2), 2)
        if father_node != g.start:
            father_node.set_color(grey)
        father_node.draw(sc)
        node.draw(sc)
        pygame.display.flip()
        time.sleep(0.05)

        node = father_node
        father_node = father[father_node.value]
    
    print("UCS algorithm completed!")

def AStar(g:Graph, sc:pygame.Surface):
    print('Implement A* algorithm')

    open_set:list[(float, Node)] = []
    open_set.append((100000, g.start))  
    closed_set:list[Node] = []
    father = [None]*g.get_len()
    cost = [100000]*g.get_len()
    heuristic = [100000]*g.get_len()

    while open_set:

        estimated_path_cost, node = open_set.pop()
        if node not in closed_set: 

            path_cost = estimated_path_cost - heuristic[node.value]
            node.set_color(yellow)
            node.draw(sc)
            pygame.display.flip()
            time.sleep(0.05)

            closed_set.append(node)
            if g.is_goal(node):
                break

            neighbors:list[Node] = g.get_neighbors(node)
            x1 = node.x
            y1 = node.y

            for neighbor_node in neighbors:

                if neighbor_node not in closed_set:

                    x2 = neighbor_node.x
                    y2 = neighbor_node.y
                    cal_cost = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
                    x_goal = g.goal.x
                    y_goal = g.goal.y
                    heuristic[neighbor_node.value] = math.sqrt((x_goal - x2)**2 + (y_goal - y2)**2)
                    
                    if cost[neighbor_node.value] > cal_cost + path_cost:

                        cost[neighbor_node.value] = cal_cost + path_cost
                        open_set.append((cost[neighbor_node.value] + heuristic[neighbor_node.value], neighbor_node))
                        father[neighbor_node.value] = node
                        open_set.sort(key=key_cost, reverse=True)       
  
                    neighbor_node.set_color(red)
                    neighbor_node.draw(sc)
                    pygame.display.flip()
                    time.sleep(0.05)

            node.set_color(blue)
            node.draw(sc)
            pygame.display.flip()
            time.sleep(0.05)

    g.start.set_color(orange)
    g.goal.set_color(purple)
    g.start.draw(sc)
    g.goal.draw(sc)
    pygame.display.flip()
    time.sleep(0.05)

    node = g.goal
    father_node = father[node.value]

    while father_node is not None:

        x1 = node.x
        y1 = node.y
        x2 = father_node.x
        y2 = father_node.y
        pygame.draw.line(sc, green, (x1, y1), (x2, y2), 2)
        if father_node != g.start:
            father_node.set_color(grey)
        father_node.draw(sc)
        node.draw(sc)
        pygame.display.flip()
        time.sleep(0.05)

        node = father_node
        father_node = father[father_node.value]

    print("A* algorithm completed!")