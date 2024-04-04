#Sadia Abdulhalim - 60098686
#Eman - 60099832 & Rakif - 60099184


from aqueue import Queue

class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = []
        self.path = []

    def add_vertex(self, v):
        self.vertices[v] = None

    def remove_vertex(self, v):
        new_edges = []
        self.vertices.remove(v)
        for e in self.edges:
            if not v in e:
                new_edges.append(e)
        self.edges = new_edges

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
           edge = (u, v)
           if not edge in self.edges:
                self.edges.append(edge)

    def get_edge(self, u, v):
        for e in self.edges:
            if u in e and v in e:
                return e
        return None

    def incident_edges(self, u):
        result = []
        for e in self.edges:
            if u in e:
                result.append(e)
        return result

    def reset_dfs(self):
        for v in self.vertices:
            self.vertices[v] = False

    def bfs_find_path(self, src, dst):
        q = Queue()
        parent = {}
        parent[src] = None
        self.vertices[src] = True
        q.enqueue(src)
        while not q.empty():
            v = q.dequeue()
            edges = self.incident_edges(v)
            for e in edges:
                if e[0] == v:
                    u = e[1]
                else:
                    u = e[0]
                if not self.vertices[u]:
                    self.vertices[u] = True
                    q.enqueue(u)
                    parent[u] = v
        path = [dst]
        while parent[dst]:
            path.append(parent[dst])
            dst = parent[dst]
        path.reverse()
        print("Path:",path)


    def debug(self):
        print("vertices: ", self.vertices)
        print("edges: ", self.edges)




m = Graph()
m.add_vertex("1")
m.add_vertex("2")
m.add_vertex("3")
m.add_vertex("4")
m.add_vertex("5")
m.add_vertex("6")
m.add_vertex("7")
m.add_vertex("8")
m.add_vertex("9")
m.add_vertex("10")
m.add_vertex("11")
m.add_edge("1","2")
m.add_edge("1","3")
m.add_edge("3","4")
m.add_edge("4","5")
m.add_edge("4","6")
m.add_edge("3","7")
m.add_edge("7","8")
m.add_edge("7","9")
m.add_edge("9","11")
m.add_edge("9","10")
m.reset_dfs()
m.bfs_find_path("1", "10")

