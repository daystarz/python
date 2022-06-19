class Graph:
    #constructor
    def __init__(self,num_nodes):
        self.num_nodes = num_nodes;
        self.data = [[] for _ in range(num_nodes)]
        self.weight = [[] for _ in range(num_nodes)]
        self.lsdb = []# for _ in range(num_nodes)]
        #9:55
        #self.weight = [[] for _ in range(num_nodes)]
        # for n1,n2 in edges:#pair
        #     self.data[n1].append(n2)
        #     self.data[n2].append(n1)

    def add_edges(self,n1,n2,weight):
            if n2 in self.data[n1]:
                index1 = self.data[n1].index(n2)
                temp_weight = self.weight[n1][index1]
                self.weight[n1][index1] = weight
                test = f"{n1},{n2},{temp_weight}"
                test2 = f"{n1},{n2},{weight}"
                index12 = self.lsdb.index(test)
                self.lsdb[index12] = test2

                index2 = self.data[n2].index(n1)
                self.weight[n2][index2] = weight

            else:
                self.data[n1].append(n2)
                test = f"{n1},{n2},{weight}"
                self.lsdb.append(test)
                self.weight[n1].append(weight)

                self.data[n2].append(n1)
                #self.lsdb[n2].append(test)
                self.weight[n2].append(weight)

    def remove_edges(self,n1,n2):
            index1 = self.data[n1].index(n2)
            weight1 = self.weight[n1][index1]
            test = f"{n1},{n2},{weight1}"
            self.data[n1].remove(n2)
            self.lsdb.remove(test)
            self.weight[n1].remove(weight1)

            index2 = self.data[n2].index(n1)
            weight2 = self.weight[n2][index2]
            self.data[n2].remove(n1)
            self.weight[n2].remove(weight2)

    def bfs(self,src):
        visited = [False] * len(self.data)
        queue = []

        visited[src] = True
        queue.append(src)
        i = 0

        while i < len(queue):
            for v in self.data[queue[i]]:
                if not visited[v]:
                    visited[v] =  True
                    queue.append(v)
            i+=1
        queue.remove(src)
        return queue
    def lsdb_update(self):
        num = []
        for i in self.lsdb:
            temp = i.split(",")
            n = int(temp[0]) + int(temp[1])
            num.append(n)

        #bubble sort
        for i in range (len(num)):
            for j in range(0,len(num) - i - 1):
                if num[j] > num[j+1]:
                    t =  num[j]
                    p = self.lsdb[j]

                    num[j] = num[j+1]
                    self.lsdb[j] = self.lsdb[j+1]

                    num[j+1] = t
                    self.lsdb[j+1] = p
        #print("Updated: ",self.lsdb)

    def get_neighbour(self,x):
        size = len(self.data[x])
        st = []
        for i in range(size):
            #return (x,self.data[x][i],self.weight[x][i])
            st.append(f"{self.data[x][i]},{self.weight[x][i]}")
        return st

    def print_lsdb(self):
        for word in self.lsdb:
            print(word)

    def __repr__(self) :
        return "\n".join(["{} {}".format(n,neighbors) for n,neighbors in enumerate(self.data)])

    def __str__(self):
        return repr(self)

#GLobal Functions
def num_con(arr):
    num = []
    i = 0
    for no in arr:
        num.append(i)
        i=i+1
    return num

def str_con(string,arr):
    temp = string.split(",")
    ret_str=f"{arr[int(temp[0])]},{arr[int(temp[1])]},{temp[2]}"
    return ret_str

def str_con_n(string,arr):
    temp = string.split(",")
    ret_str=f"{arr[int(temp[0])]},{temp[1]}"
    return ret_str

def n_update(arr):
    num =[]
    for i in arr:
        temp = i.split(",")
        n = int(temp[0])
        num.append(n)
    for i in range(len(num)):
        for j in range(0,len(num) - i - 1):
            if num[j] > num[j+1]:
                t =  num[j]
                p = arr[j]
                num[j]=num[j+1]
                arr[j]=arr[j+1]
                num[j+1] = t
                arr[j+1] = p
    return arr
#----------------------------------------------------------------------------------------------
def update_distances(graph, current, distance, parent=None):
    """Update the distances of the current node's neighbors"""
    neighbors = graph.data[current]
    weights = graph.weight[current]
    nodel = []
    for i, node in enumerate(neighbors):
        weight = weights[i]
        if distance[current] + weight < distance[node]:
            distance[node] = distance[current] + weight
            nodel.append[node]
            if parent:
                parent[node] = current
    return nodel

def pick_next_node(distance, visited):
    """Pick the next univisited node at the smallest distance"""
    min_distance = float('inf')
    min_node = None
    for node in range(len(distance)):
        if not visited[node] and distance[node] < min_distance:
            min_node = node
            min_distance = distance[node]
    return min_node

def shortest_path(graph, source, dest):
    """Find the length of the shortest path between source and destination"""
    #all node unvisted
    visited = [False] * len(graph.data)
    #
    distance = [float('inf')] * len(graph.data)
    parent = [None] * len(graph.data)
    queue = []
    idx = 0
    test = []

    queue.append(source)
    distance[source] = 0
    visited[source] = True
    j = 0
    nodel = []

    while idx < len(queue) and not visited[dest]:
        current = queue[idx]
        #update_distances(graph, current, distance, parent)

        #---------------Use Update distance function from above-----------
        neighbors = graph.data[current]
        weights = graph.weight[current]

        for i, node in enumerate(neighbors):
            weight = weights[i]
            if distance[current] + weight < distance[node]:
                distance[node] = distance[current] + weight
                nodel.append(node)
                if parent:
                    parent[node] = current
        #-------------------
        test.append(current)

        next_node = pick_next_node(distance, visited)

        if next_node is not None:
            visited[next_node] = True
            if j == 0:
                first_node = next_node
            queue.append(next_node)
        idx += 1
    if len(nodel) > 1:
        first_node = nodel[1]
    if len(queue) == 1:
        first_node = queue[0]

    print(f"{dest} is {nodel}")

    return f"{dest},{first_node},{distance[dest]}",distance
#-----------------------------------------------------------
def bubble_sort(arr):
    num = []
    for i in arr:
        temp = i.split(",")
        n = int(temp[0]) + int(temp[1])
        num.append(n)

    # bubble sort
    for i in range(len(num)):
        for j in range(0, len(num) - i - 1):
            if num[j] > num[j+1]:
                t = num[j]
                p = arr[j]

                num[j] = num[j+1]
                arr[j] = arr[j+1]

                num[j+1] = t
                arr[j+1] = p






    # visited = [False] * len(graph.data)
    # dist = [float('inf')] * len(graph.data)
    # queue = []
    # dist[src] = 0
    # queue.append(src)
    # i = 0
    # j = 0

    # while i < len(queue) and not visited[target] and not visited[target]:
    #     current = queue[i]
    #     visited[current] = True
    #     i = i + 1

    #     update_distances(graph,current,dist)
    #     #find the first univisted node with the smallest distance
    #     next_node = pick_next_node(dist,visited)
    #     if j == 0:
    #         first_node = next_node
    #         j = j+1
    #     if next_node:
    #         queue.append(next_node)

    #     return dist[target]






if __name__ == '__main__':

    #all the inputs
    word = []
    stop = 'END'
    link = 'LINKSTATE'
    while True:
        val = input()
        if val == stop:
            break
        word.append(val)

    node = []

    # array of nodes
    new_word = word.copy()
    step = 'LINKSTATE'
    i = 0
    while True:
        temp = word[i]
        if temp == step or i > len(word):
            break
        node.append(temp)
        new_word.remove(temp)
        i = i + 1
    #print('output', node)
    new_word.remove('LINKSTATE')
    if "UPDATE" in new_word:
        new_word.remove('UPDATE')

    num_arr = num_con(node) # 0 1 2 3
    num_nodes = len(node)
    g = Graph(num_nodes)

    for i in new_word:
        my_list = i.split(" ")#x z 7 x,y
        if not my_list[2] == "-1":
            weight = int(my_list[2])
            n1 = node.index(my_list[0])
            n2 = node.index(my_list[1])
            g.add_edges(n1, n2, weight)
            g.lsdb_update()
        else:
            n1 = node.index(my_list[0])
            n2 = node.index(my_list[1])
            g.remove_edges(n1,n2)
            g.lsdb_update()


        checker = len(my_list)
        if checker == 4:
            li = []
            t = my_list[3]
            my_list2 = t.split(",")
            len(my_list2)
            for i in my_list2:
                if i in node:
                    p = node.index(i)
                    print(f"{i} Neighbour Table:")
                    st = g.get_neighbour(p)
                    new_st = n_update(st)
                    for j in new_st:
                        print(str_con_n(j,node))
                    print("")

                    print(f'{i} LSDB')
                    if g.data[p]: #IF ELEMENT EXIST
                        t = "\n".join(["{}".format(n) for n in g.lsdb])
                        s = t.split("\n")
                        if len(s) > 1:
                            for j in s:
                                print(str_con(j,node))
                        else:
                            print(str_con(t,node))
                    print("")
                    print(f"{i} Routing Table")
                    r_st = []
                    for i in g.data[p]:
                        a,b = shortest_path(g,p,i)
                        r_st.append(a)
                    bubble_sort(r_st)
                    for i in r_st:
                        print(str_con(i,node))
                    #print(b)

                    print("")
                    # for i in range (len(g.data[p])):
                    #     print("Path")
                    #     print(shortest_path(g,p,i))
                    #     print("")

#---------------------------------------------------------------------------------------------------------------#
            # first_print = my_list2[0]
            # second_print = my_list2[1]
            # p1 = node.index(my_list2[0])
            # p2 = node.index(my_list2[1])

            # print(f"{first_print} Neighbour Table:")
            # st = g.get_neighbour(p1)
            # new_st = n_update(st)
            # for i in new_st:
            #     print(str_con_n(i,node))
            # print("")

            # print(f'{first_print} LSDB')
            # if g.data[p1]: #IF ELEMENT EXIST
            #     t = "\n".join(["{}".format(n) for n in g.lsdb])
            #     s = t.split("\n")
            #     if len(s) > 1:
            #         for i in s:
            #             print(str_con(i,node))
            #     else:
            #         print(str_con(t,node))
            # print("")

            # print(f"{second_print} Neighbour Table:")
            # st = g.get_neighbour(p2)
            # new_st = n_update(st)
            # for i in new_st:
            #     print(str_con_n(i,node))
            # print("")

            # print(f'{second_print} LSDB:')
            # if g.data[p2]: #IF ELEMENT EXIST
            #     t = "\n".join(["{}".format(n) for n in g.lsdb])
            #     s = t.split("\n")
            #     if len(s) > 1:
            #         for i in s:
            #             print(str_con(i,node))
            #     else:
            #         print(str_con(t,node))
            # print("")

#---------------------------------------------------------------------------------------------------------------------#
    # arr = ['X','Y','Z']
    # num_nodes = 2
    # g = Graph(3);
    # g.add_edges(0,2,7)
    # g.lsdb_update()
    # print('X LSDB')
    # #print(g.bfs(0))
    # if g.data[0]: #IF ELEMENT EXIST
    #     t = "\n".join(["{}".format(n) for n in g.lsdb])
    #     s = t.split("\n")
    #     if len(s) > 1:
    #         for i in s:
    #             print(str_con(i,arr))
    #     else:
    #         print(str_con(t,arr))


    # print("")
    # print("Y LSDB")
    # #print(g.bfs(1))
    # if g.data[1]:
    #     t = "\n".join(["{}".format(n) for n in g.lsdb])
    #     s = t.split("\n")
    #     if len(s) > 1:
    #         for i in s:
    #             print(str_con(i,arr))
    #     else:
    #         print(str_con(t,arr))
    # print("")
    # g.add_edges(0,1,2)
    # g.lsdb_update()
    # g.add_edges(1,2,1)
    # g.lsdb_update()
    # print('X LSDB')
    # #print(g.bfs(0))
    # if g.data[0]:
    #     t = "\n".join(["{}".format(n) for n in g.lsdb])
    #     s = t.split("\n")
    #     if len(s) > 1:
    #         for i in s:
    #             print(str_con(i,arr))
    #     else:
    #         print(str_con(t,arr))
    # print('')
    # print('Z LSDB')
    # #print(g.bfs(2))
    # if g.data[2]:
    #     t= "\n".join(["{}".format(n) for n in g.lsdb])
    #     s = t.split("\n")
    #     if len(s) > 1:
    #         for i in s:
    #             print(str_con(i,arr))
    #     else:
    #         print(str_con(t,arr))
    # print('')

    # #print(g.lsdb)
    # print(g)
    # g.print_neighbour(0);




    #edges = [(0,1),(0,4),(1,2),(1,3),(1,4),(2,3),(3,4)]
