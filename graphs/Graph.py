class Graph(dict):
    """ test"""
    def __init__(self,vs=None,es=None):
        if vs is None:
            vs=[]
        if es is None:
            es=[]
        for v in vs:
            self.add_vertex(v)
        for e in es:
            self.add_edge(e)

    def add_vertex(self,v):
    """ add vertex v to graph """
        self[v]={}

    def add_edge(self,e):
    """ add edge e to graph """
        v,w=e
        self[v][w]=e
        self[w][v]=e

    def get_edge(self,u,v):
    """ get edge between u,v and throw error if not"""
        try: 
            return self[u][v]
        except KeyError:
            return None
    def remove_edge(self,e):
    """ remove edge e from graph"""
        w,v=e
        del self[v][w]
        del self[w][v]

    def vertices(self):
    """ list all vertices of the graph """
        return self.keys()

#    def edges(self):
#        for keys in self.itervalues():
class Edge(tuple):
    def __new__(cls,e1,e2):
        return tuple.__new__(cls,(e1,e2))
    def __repr__(self):
        return 'Edge(%s,%s)' % (repr(self[0]),repr(self[1]))
    __str__=__repr__

class Vertex(object):
    def __init__(self,label=''):
        self.label=label

    def __repr__(self):
        return 'Vertex(%s)'% repr(self.label)

    __str__=__repr__

