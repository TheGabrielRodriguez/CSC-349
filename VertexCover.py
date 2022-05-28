
import sys

def main(argv):
    graph = {}
    file = open(argv, "r")
    content = file.readlines()
    for i in range(0, len(content)):
        line = content[i].rstrip('\n').split(' ')
        first = int(line[0])
        second = int(line[1])

        if first in graph.keys():
            graph[first].append(second)
        else:
            graph[first] = [second]

        if second in graph.keys():
            graph[second].append(first)
        else:
            graph[second] = [first]


    # generate all edges present in graph
    def edge_getter(graph):
        edges = []
        for node in graph: 
            for neighbour in graph[node]:
                if (node,neighbour) and (neighbour, node) not in edges:
                    edges.append((node,neighbour))
        return edges

    #### degree list for all vertices 
    def degree_getter(graph):
        edges = edge_getter(graph)
        degrees = {}
        for v in graph.values():
            for i in v:
                degrees[i] = 0
        for edge in edges:
            degrees[edge[0]] = degrees[edge[0]] + 1
            degrees[edge[1]] = degrees[edge[1]] + 1
        return degrees
    

    
    
    #### Log(n) Approximation Algorithm
    def log_n(graph):
        edges = edge_getter(graph)
        degrees = dict(sorted(degree_getter(graph).items()))
        cover_log = []
        while len(edges)>0:
            
            v = max(degrees, key=degrees.get)
            
            edges2 = [x for x in edges if x[0] == v or x[1] == v]

            for i in edges2:
               
                if i[0] != v:
                    degrees[i[0]] -= 1 
                elif i[1] != v: 
                    degrees[i[1]] -= 1
            degrees.pop(v, None)

            edges = [x for x in edges if x[0] != v and x[1] != v]
            
            if v not in cover_log:
                cover_log.append(v)

        return cover_log

           
    ########### end of Log(n)
   

    ##### 2-Approximation Algorithm
    def two_approx(graph):
        edges = edge_getter(graph)
        edges.sort(key=lambda y: y[1])
        cover_2 = []
        while len(edges) > 0:
            for edge in edges:
                edges = [x for x in edges if (x[0]!= edge[0] and x[1]!=edge[0] and x[0] != edge[1] and x[1] != edge[1])]
                if edge[0] not in cover_2 and edge[1] not in cover_2:
                    cover_2.append(edge[0])
                    cover_2.append(edge[1])

        return cover_2
    #####  end of 2-approx    
        
 
    

 


    '''Strategy for Brute Force'''
    ## Iterate through each vertex set in the subset
    '''for each v in subset of V
        remove v from edge list (keep track of which edges are covered; essentially)
        return vertex set that is a valid vertex cover
        return min the sorted min length vertex cover that has minimum length 
        '''
    ## keep track of which ones are "covered" with the given vertex set
    ## return subset that is a valid vertex cover 
    ## return min length vertex set
    #Brute Force (Exact) Vertex Cover Algorithm 
    def Brute(graph):
        edges = edge_getter(graph)
        vertice_set = list(graph.keys())


        def combinations(vertices):
            res = [[]] 
            for i in vertices:
                for j in res: 
                    res = res + [list(j) + [i]]  
            return res          

        c = combinations(vertice_set)
    

        def valid(v, e):
            for i in e:
                checker = False
                for j in v:
                    if i[1] == j or i[0]== j: 
                        checker = True
                if checker == False:
                    return False
            else:
                checker = True 
    
            return checker
        

        c.sort(key=len)
        indices = []
        for i in range(len(c)):
            boolean = valid(c[i],edges)
            if boolean == True:
                indices.append(i)
        return sorted(c[indices[0]])
  
    ln = str(log_n(graph))[1:-1].replace(",","")
    two = str(two_approx(graph))[1:-1].replace(",","")
    brute = str(Brute(graph))[1:-1].replace(",","")
    
    print("log-Approximation: " + ln + "\n" + "2-Approximation: " + two + "\n" + "Exact Solution: " + brute)

if __name__ == "__main__":
    main(sys.argv[1])

    
         


           
            
   
    
 
