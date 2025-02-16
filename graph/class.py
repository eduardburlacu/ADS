from collections import deque

class Graph:
    def __init__(self, V:int, edges:list[tuple[int, int]], directed:bool=False):
        """
        Create a graph with V vertices: 0,1,...,V-1

        :param V: The number of vertices. The vertices are numbered from 0 to V-1
        :param edges: list of tuples (v_in, v_out) representing the edges
        """
        self._V = V
        self._directed = directed

        self._graph = dict()

        for v in range(V):
            self._graph[v] = []

        for v_in, v_out in edges:
            self._graph[v_in].append(v_out)
            if not directed:
                self._graph[v_out].append(v_in)

        self._degree = [len(self.graph[v]) for v in range(V)]

    @property
    def V(self):
        return self._V

    @property
    def directed(self):
        return self._directed

    @property
    def degree(self):
        return self._degree

    @property
    def graph(self):
        return self._graph

    @staticmethod
    def check_directed(graph:[int,list[int]])->bool:
        for v in graph:
            for neighbor in graph[v]:
                if v not in graph[neighbor]:
                    return True
        return False

    @graph.setter
    def graph(self, value:dict[int, list[int]]):
        V = len(value)
        assert all([v in value for v in range(V)]), "The graph must have vertices numbered from 0 to V-1"
        assert all(
            [all([0<=neighbor<V for neighbor in value[vtx]]) for vtx in value]
        ), "The graph must have vertices numbered from 0 to V-1"
        self._directed = Graph.check_directed(value)
        self._V = V
        self._graph = value
        self._degree = [len(neighbor) for neighbor in value.values()]

    @property
    def adjacency_matrix(self):
        mtx = [[0 for _ in range(self.V)] for _ in range(self.V)]
        for v, neighbors in self.graph.items():
            for neighbor in neighbors:
                mtx[v][neighbor] = 1
        return mtx

    def __str__(self):
        out = "Graph: \n"
        for v, neighbors in self.graph.items():
            out += f"{v}: {neighbors}\n"
        return out

    def __repr__(self):
        return self.__str__()

    def bfs(self, source:int)->list[int]:
        assert 0<=source<self.V, "The source vertex must be in the graph"
        path = []
        queue = deque()
        queue.append(source)
        visited = set()
        while len(queue)>0:
            node = queue.popleft()
            if node not in visited:
                path.append(node)
                visited.add(node)
                for neighbor in self._graph[node]:
                    queue.append(neighbor)
        return path

    def dfs(self, source:int)->list[int]:
        assert 0<=source<self.V, "The source vertex must be in the graph"
        path = []
        stack = deque()
        stack.append(source)
        visited = set()
        while len(stack)>0:
            node = stack.pop()
            if node not in visited:
                path.append(node)
                visited.add(node)
                for neighbor in self._graph[node]:
                    stack.append(neighbor)
        return path

    def shortest_paths(self, source:int)->dict[int,int]:
        # we do bfs and keep track in the queue of the distance from the source
        assert 0<=source<self.V, "The source vertex must be in the graph"
        queue = deque()
        queue.append([source,0])
        visited = dict()
        while len(queue)>0:
            node, dist = queue.popleft()
            visited[node]=dist
            for neighbor in self._graph[node]:
                if neighbor not in visited:
                    visited[neighbor] = dist+1
                    queue.append([neighbor,dist+1])
        return visited


if __name__ == "__main__":
    V = 5
    edges = [(0,1), (0,2), (1,3), (2,3), (3,4)]
    graph = Graph(V, edges)
    print(graph)
    print(graph.graph)
    print(graph.adjacency_matrix)
    print(graph.bfs(0))
    print(graph.dfs(0))
    print(graph.shortest_paths(0))