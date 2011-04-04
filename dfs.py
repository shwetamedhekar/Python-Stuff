'''
@Description: Running dfs on a graph defined as an adjacency list.
@Author: Shweta Medhekar
@Created Date: Feb 2011
'''
import sys

def dfs(g):
    #print "\n\ninput : ",g
    key=g.keys()
    key.sort()#in asc order
    visited=[]
    visited.append(key[0])
    explore(key[0],g,visited)

    while(len(visited)<len(key)):
        val_nxt=get_next_element(key,visited)
        visited.append(val_nxt)
        explore(val_nxt,g,visited)

    print "\nVisited : ",visited
    

def explore(val, g, visited):
    #print "inside explore",val
    next_hop=g[val]
    next_hop.sort()
    #print "next_hop", next_hop

    next_element=get_next_element(next_hop,visited)

    for i in range (0,len(next_hop)):
        #print "next_element",next_element
        #print "visited",visited
        if(next_element==None): #cud not find the next element back 1 recurssion
            #print "end of search in this path"
            return 
        else:
            visited.append(next_element)
            explore(next_element,g,visited)
            next_element=get_next_element(next_hop,visited)
    return

def get_next_element(next_hop,visited):
    #get the next hop that is not yet visited
    next_element=None
    for i in next_hop:
        cnt=0
        for j in visited:
            if(i==j):#match found try next element
                break
            cnt=cnt+1
        if(cnt==len(visited)):#no match in visited for current this is the element we want
            next_element=i
            break
    return next_element


def main():
    input_graph={'A':['B','C','D'],
                 'B':['A','E','F'],
                 'C':['A','F'],
                 'D':['G','H'],
                 'E':['B','I','J'],
                 'F':['B','C'],
                 'G':['D','H'],
                 'H':['D','G'],
                 'I':['E','J'],
                 'J':['E','I'],
                 'K':['L'],
                 'L':['K']}

    print "The graph : ", input_graph
    
    dfs(input_graph)



if __name__ == "__main__":
    sys.exit(main())
