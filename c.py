from graph import Graph

def get_key(my_dict, val):
    for key, value in my_dict.items():
        if val == value:
            return key


# Open both the files
c_sol = open("c_sol.txt","a")       # solution
c     = open("c.txt","r")               # input data

# reading the inupt file and storing variables
lines = c.readlines()
first_line = lines[0]
D = int(first_line.split()[0])      # D: duration
I = int(first_line.split()[1])      # I: intersections
S = int(first_line.split()[2])      # S: streets
V = int(first_line.split()[3])      # V: cars
F = int(first_line.split()[4])      # F: bonus

# create a dictionary to store street name : end, start .... 
# by putting end,start in this order we can get all the roads leading to an intersection
# rater the the roads moving out from the intersection with the help of graphs.
routes_dict = {}                    # strees: [end,start]
for i in range(1,S):
    line = lines[i].split()
    routes_dict[line[2]] = [int(line[1]), int(line[0])]

# graph now stores the graph of our data, but in the reverse order
routes = list(routes_dict.values()) # stores all the routes
graph  = Graph(routes)
g_dict = graph.graph_dict           # store all the intersections that lead to an intersection

# w1: number of intersections found by the Graph
# writes w1
keys   = list(g_dict.keys())
values = list(g_dict.values())
w1     = str(len(keys))
c_sol.write(f'{w1} \n')


for i,key in enumerate(keys):
    w2    = key
    c_sol.write(f'{w2} \n')
    value = values[i]
    w3    = len(value)
    c_sol.write(f'{w3} \n')

    for j in range(w3):
        x = value[j]
        g_key = get_key(routes_dict,[key,x])
        w = f'{g_key} 1 \n'
        c_sol.write(w)

