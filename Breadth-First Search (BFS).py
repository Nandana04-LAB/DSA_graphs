class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class Graph:
    def __init__(self):
        self.vertices: list = []
        self.adjacency_list: dict = {}
        self.prev: dict = {}
        self.distance: dict = {}
        self.colors: dict = {}
        self.entry: dict = {}
        self.exit: dict = {}
        self.time: int = 0

    def add_vertex(self, label: str):
        self.vertices.append(label)
        self.adjacency_list[label]: list = []
        self.prev[label] = None
        self.distance[label] = 0
        self.colors[label] = "white"

    def add_edge(self, label1: str, label2: str):
        self.adjacency_list[label1].append(label2)
        self.adjacency_list[label2].append(label1)

    def dfs(self, label: str):
        s: Stack = Stack()
        s.push(label)
        self.colors[label] = "gray"
        self.time += 1
        self.entry[label] = self.time
        while not s.is_empty():
            tmp: str = s.peek()
            neighbour: str = self.find_unvisited_neighbour(tmp)
            if neighbour is not None:
                self.prev[neighbour] = tmp
                self.distance[neighbour] = self.distance[tmp] + 1
                self.colors[neighbour] = "gray"
                self.time += 1
                self.entry[neighbour] = self.time
                s.push(neighbour)
            else:
                s.pop()
                self.time += 1
                self.exit[tmp] = self.time
                self.colors[tmp] = "black"

    def return_path(self, label: str) -> str:
        if self.prev[label] is None:
            return label
        else:
            return self.return_path(self.prev[label]) + " -> " + label

    def find_unvisited_neighbour(self, tmp) -> str:
        for n in self.adjacency_list[tmp]:
            if self.colors[n] == "white":
                return n
        return None


# Example usage
graph = Graph()

my_vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
# add vertices
for i in range(len(my_vertices)):
    graph.add_vertex(my_vertices[i])

graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('A', 'D')
graph.add_edge('C', 'D')
graph.add_edge('C', 'G')
graph.add_edge('D', 'G')
graph.add_edge('D', 'H')
graph.add_edge('B', 'E')
graph.add_edge('B', 'F')
graph.add_edge('E', 'I')

graph.dfs("A")
print(graph.return_path("H"))

