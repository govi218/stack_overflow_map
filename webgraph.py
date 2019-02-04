import networkx as nx
from utils.hyperlinkparser import HyperlinkParser
from utils import HTMLUtils
from urllib.parse import urlparse

class WebGraph:
    
    def __init__(self):
        self.Graph = nx.Graph()
    
    def __is_rq(url, current_url):
        '''Determines whether two questions are related'''
        split_url = url.split('/')
        split_current_url = current_url.split('/')
        try:
            if split_current_url[-1] in split_url[-1]:
                return False
            return split_url[1] == "questions" and split_url[2].isnumeric()
        except:
            return False
    
    def __get_related_questions(self, stack_url):
        '''Gets related questions in Stack Exchange'''
        
            
        parser = HyperlinkParser()
        html = HTMLUtils.get_html(stack_url)
        parser.feed(html)
        parsed_url = urlparse(stack_url)
        url_list = parser.links
        rq = list(filter(lambda x: __is_rq(x, stack_url), url_list))
        return rq
    
    def add_rqs(self, node)
        if node not in self.Graph:
            raise("Stack_url not in graph")
        rqs = self.__get_related_questions(node)
        for question in rqs:
            self.Graph.add_node(question)
            self.Graph.add_edge(node, question)
        
            