file = open("input/day-12-input.txt")
lines = [line.strip() for line in file.readlines()]

class Node:
    def __init__(self, name, small):
        self.name = name
        self.small = small
        self.neighbours = []

    def add_neighbour(self, neighbour):
        if neighbour not in self.neighbours:
            self.neighbours.append(neighbour)

def is_small_cave(name):
    return ord(name[0]) > 97

nodes = {}
small_caves = []
nodes["start"] = Node("start", False)
nodes["end"] = Node("end", False)

# add all the nodes into nodes  
for line in lines:
    start = line.split("-")[0]

    if start not in nodes:
        nodes[start] = Node(start, is_small_cave(start))
        
        if is_small_cave(start):
            small_caves.append(nodes[start])
        
# add the neighbours of a node
for line in lines:
    start = line.split("-")[0]
    end = line.split("-")[1]

    node = nodes[start]

    if end not in nodes:
        nodes[end] = Node(end, is_small_cave(end))

        if is_small_cave(end):
            small_caves.append(nodes[end])

    n = nodes[end]
    node.add_neighbour(n)
    n.add_neighbour(node)

paths = []

# checks if a given node/cave can be visited more than once
def valid(node, chosen_small_cave, path):
    if not node.small:
        return True
    elif node != chosen_small_cave:
        return not node.name in path
    else:
        i = path.find(node.name)
        if i == -1:
            return True
        else:
            return path[i+1:].find(node.name) == -1

def visit(node, path, small_cave):
    if node.name != "start":
        s = path + "," + node.name

        if node.name == "end":
            if s not in paths:
                paths.append(s)
        elif valid(node, small_cave, path):
            for n in node.neighbours:
                visit(n, s, small_cave)

for n in nodes["start"].neighbours:
    for c in small_caves:
        visit(n, "start", c)

print("number of paths: {}".format(len(paths)))
