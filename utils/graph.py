class Graph(object):
    
    '''A set of vertices and edges'''
    
    def __init__(self):
        self.graph = {}
        self.parser = MyHTMLParser()
    
    def nodes(self):
        """ returns the vertices of a graph """
        return list(self.graph.keys())
    
    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()
        
    def add_node(self, node):
        """ If the vertex "vertex" is not in 
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. 
            Otherwise nothing has to be done. 
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def __generate_edges(self):
        """ A static method generating the edges of the 
            graph "graph". Edges are represented as sets 
            with one (a loop back to the vertex) or two 
            vertices 
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.graph[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges
    
    # @staticmethod
    # def is_related_question2(url, current_url):
    #     split_url = url.split('/')
    #     split_current_url = current_url.split('/')
    #     try:
    #         if split_current_url[-1] in split_url[-1]:
    #             return False
    #         return split_url[1] == "questions" and split_url[2].isnumeric()
    #     except:
    #         return False
    
    
    # def get_related_questions(self, stack_url):
    #     '''Gets related questions in Stack Exchange'''
        
    