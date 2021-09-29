class Graph:
    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()
    def make_undirected(self):
        for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                self.graph_dict.setdefault(b, {})[a] = dist
    def connect(self, A, B, distance=1):
        self.graph_dict.setdefault(A, {})[B] = distance
        if not self.directed:
            self.graph_dict.setdefault(B, {})[A] = distance
    def get(self, a, b=None):
        links = self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)
    def nodes(self):
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)
class Node:
    
    def __init__(self, name:str, parent:str):
        self.name = name
        self.parent = parent
        self.g = 0 # Distance to start node
        self.h = 0 # Distance to goal node
        self.f = 0 # Total cost
    def __eq__(self, other):
        return self.name == other.name
    def __lt__(self, other):
         return self.f < other.f
    def __repr__(self):
        return ('({0},{1})'.format(self.name, self.f))
def astar_search(graph, heuristics, start, end):
    
    open = []
    closed = []
    start_node = Node(start, None)
    goal_node = Node(end, None)
    open.append(start_node)
    while len(open) > 0:
        open.sort()
        current_node = open.pop(0)
        closed.append(current_node)
        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node.name + ': ' + str(current_node.g))
                current_node = current_node.parent
               
            path.append(start_node.name + ': ' + str(start_node.g))
            
            return path[::-1]
        neighbors = graph.get(current_node.name)
        for key, value in neighbors.items():
            neighbor = Node(key, current_node)
            if(neighbor in closed):
                continue
            neighbor.g = current_node.g + graph.get(current_node.name, neighbor.name)
            neighbor.h = heuristics.get(neighbor.name)
            neighbor.f = neighbor.g + neighbor.h
            if(add_to_open(open, neighbor) == True):
                open.append(neighbor)
           
        print("Current Node: ",current_node)
        print("Children: ",neighbors)
        print("Explored list: ",closed[1:]) 
        print("Frontier: ",open)
        
        print("\n")
    return None
def add_to_open(open, neighbor):
    for node in open:
        if (neighbor == node and neighbor.f > node.f):
            return False
    return True
def main():
    g = Graph()
    g.connect('Los Angeles', 'San Francisco', 383)
    g.connect('Los Angeles', 'Austin', 1377)
    g.connect('Los Angeles', 'Bakersville', 153)
    g.connect('San Francisco', 'Bakersville', 283)
    g.connect('San Francisco', 'Seattle', 807)
    g.connect('Seattle', 'Santa Fe', 1463)
    g.connect('Seattle', 'Chicago', 2064)
    g.connect('Bakersville', 'Santa Fe', 864)
    g.connect('Austin', 'Dallas', 195)
    g.connect('Santa Fe', 'Dallas', 640)
    g.connect('Boston', 'Austin', 1963)
    g.connect('Dallas', 'New York', 1548)
    g.connect('Austin', 'Charlotte', 1200)
    g.connect('Charlotte', 'New York', 634)
    g.connect('New York', 'Boston', 225)
    g.connect('Boston', 'Chicago', 983)
    g.connect('Chicago', 'Santa Fe', 1272)
    g.connect('Boston', 'San Francisco', 3095)

    g.make_undirected()
    city = {}
    city['Austin'] = 182
    city['Charlotte'] = 929
    city['San Francisco'] = 1230
    city['Los Angeles'] = 1368
    city['New York'] = 800
    city['Chicago'] = 1670
    city['Seattle'] = 120
    city['Santa Fe'] = 560
    city['Bakersville'] = 1282
    city['Boston'] = 1551
    city['Dallas'] = 0
    path = astar_search(g, city, 'Seattle', 'Dallas')
    print(path)
    print()
if __name__ == "__main__":
    main()
