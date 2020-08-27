import heapq as q
import sys

class node:
    def __init__(self, g, distance, name, parent):
        self.g = g
        self.distance = distance
        self.name = name
        self.parent = parent

    def __lt__(self, value):
        if self.g < value.g:
            return True
        else:
            return False

route = []
dist = []


def display(x):
    if type(x.parent) == node:
        route.append(x.name)
        dist.append(x.distance)
        display(x.parent)
    else:
        route.append(x.name)
    return route[::-1], dist[::-1]

def cal(g, g1):
    return g+g1

def city(fName):
    list = {}
    file = open(fName, 'r')
    for lines in file.readlines():
        if lines != 'END OF INPUT':
            line = lines.split()
            if line[0] in list:
                list[line[0]].append((float(line[2]), line[1]))
            else:
                list[line[0]] = [(float(line[2]), line[1])]
            
            if line[1] in list:
                list[line[1]].append((float(line[2]), line[0]))
            else:
                list[line[1]] = [(float(line[2]), line[0])]
            
    return list

def heuristicValue(hName):
    heuristic = {}
    file = open(hName, 'r')
    for lines in file.readlines():
        if lines != 'END OF INPUT':
            line = lines.split()
            heuristic[line[0]] = (line[1])
    
    return heuristic

def uninfsearch(list, source, destination):
    fringe = []
    visited = []
    expanded = 0
    generated = 0
    max = 0
    root = node(0, 0, source, 'none')
    q.heappush(fringe, root)
    while len(fringe) != 0:
        if max < len(fringe):
            max = len(fringe)
        current = q.heappop(fringe)
        expanded += 1
        if current.name == destination:
            print(f'node expanded: {expanded}')
            print(f'node generated: {generated}')
            print(f'max node in memory: {max}')
            route, dist = display(current)
            print(f'distance: {sum(dist)} km')
            print(f'ROUTE:')
            for i in range(len(route)-1):
                print(f'{route[i]} to {route[i+1]} : {dist[i]} km')
            exit()
        else:
            if current.name not in visited:
                visited.append(current.name)
                for nextCity in list[current.name]:
                    generated += 1
                    temp = node(cal(
                        current.g, nextCity[0]), nextCity[0], nextCity[1], current)
                    q.heappush(fringe, temp)
    print(f'node expanded: {expanded}')
    print(f'node generated: {generated}')
    print(f'max node in memory: {max}')
    print('distance: infinity')
    print('ROUTE:')
    print('none')

def infsearch(list, source, destination, heuristic):
    fringe = []
    visited = []
    expanded = 0
    generated = 0
    max = 0
    root = node(0, 0, source, 'none')
    q.heappush(fringe, root)
    while len(fringe) != 0:
        expanded += 1
        if max < len(fringe):
            max = len(fringe)
        current = q.heappop(fringe)
        if current.name == destination:
            print(f'node expanded: {expanded}')
            print(f'node generated: {generated}')
            print(f'max node in memory: {max}')
            route, dist = display(current)
            print(f'distance: {sum(dist)} km')
            print(f'ROUTE:')
            for i in range(len(route)-1):
                print(f'{route[i]} to {route[i+1]} : {dist[i]} km')
            exit()
        else:
            if current.name not in visited:
                visited.append(current.name)
                for nextCity in list[current.name]:
                    generated += 1
                    temp = node(cal(
                        nextCity[0], heuristic[nextCity[1]]), nextCity[0], nextCity[1], current)
                    q.heappush(fringe, temp)
    print(f'node expanded: {expanded}')
    print(f'node generated: {generated}')
    print(f'max node in memory: {max}')
    print('distance: infinity')
    print('ROUTE:')
    print('none')

def main():
    if len(sys.argv) == 4:
        uninfsearch(city(sys.argv[1]), sys.argv[2], sys.argv[3])
    elif len(sys.argv) == 5:
        infsearch(city(
            sys.argv[1]), sys.argv[2], sys.argv[3], heuristicValue(sys.argv[4]))
    else:
        print('Enter Proper number of Arguments')

if __name__ == '__main__':
    main()