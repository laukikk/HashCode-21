import matplotlib.pyplot as plt

from graph import Graph

def get_key(my_dict, val):
    for key, value in my_dict.items():
        if val == value:
            return key


# Open both the files
sol = open("f_sol.txt","w")       # solution
fil = open("f.txt","r")           # input data

# reading the inupt file and storing variables
lines = fil.readlines()
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
routes_len  = {}
for i in range(1,S+1):
    line = lines[i].split()
    routes_dict[line[2]] = [int(line[1]), int(line[0])]
    routes_len[line[2]]  = int(line[3])

# create a dictionary to store occurance of each street
street_dict = {}
for i in range(S+1,S+1+V):
    line = lines[i].split()
    n = int(line[0])                # indicates the numer of streets traversed by each car
    for j in range(n):
        street = line[j+1]          # name of the current street
        if street in street_dict.keys():
            street_dict[street] += 1
        else:
            street_dict[street] = 1

############################################################################################

# loop for weighting the roads as per how mnay different cars use it
routes_dict_1 = routes_dict.copy()
g_street = {}
for i in range(S):
    key = list(routes_dict.keys())[i]
    if key not in street_dict.keys():
        g_street[key] = 0
        del routes_dict_1[key]
    elif street_dict[key] >= 25 and street_dict[key] < 70:
        g_street[key] = 2
    elif street_dict[key] >= 70 and street_dict[key] < 170:
        g_street[key] = 3
    elif street_dict[key] >= 170 and street_dict[key] < 250:
        g_street[key] = 5
    elif street_dict[key] >= 250 and street_dict[key] < 360:
        g_street[key] = 10
    elif street_dict[key] >= 360:
        g_street[key] = 20
    else:
        g_street[key] = 1

# loop concerning road length
for i in range(len(g_street.keys())):
    key = list(g_street.keys())[i]
    if routes_len[key] <= 9:
        g_street[key] += 0
    else:
        g_street[key] += 0

###########################################################################
# plotting histograms
fig = plt.hist(street_dict.values(),max(street_dict.values()))      # road occurences
plt.savefig('f.jpg')
plt.close()
fig = plt.hist(routes_len.values(),max(routes_len.values()))        # street length
plt.savefig('f1.jpg')

# graph now stores the graph of our data, but in the reverse order
routes = list(routes_dict_1.values()) # stores all the routes
graph  = Graph(routes)
g_dict = graph.graph_dict           # store all the intersections that lead to an intersection

# w1: number of intersections found by the Graph
# writes w1
keys   = list(g_dict.keys())
values = list(g_dict.values())
w1     = str(len(keys))
sol.write(f'{w1} \n')


for i,key in enumerate(keys):
    w2    = key
    sol.write(f'{w2} \n')
    value = values[i]
    w3    = len(value)
    sol.write(f'{w3} \n')

    for j in range(w3):
        x          = value[j]
        street     = get_key(routes_dict,[key,x])
        street_num = g_street[street]
        if street_num != 0:
            w      = f'{street} {street_num} \n'
            sol.write(w)

