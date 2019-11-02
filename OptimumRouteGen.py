#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 13:16:49 2019

@author: aarjugoyal
"""

import heapq
from math import sqrt
# Node class 
class Node: 
   
    # Function to initialize the node object 
    def __init__(self, X_val, Y_val, Z_val=None, parent_node=None): 
        self.X_val = X_val  # Assign X_val 
        self.Y_val = Y_val  # Assign Y_val
        self.Z_val = Z_val  # Assign Z_val
        self.next = None    # Initialize next as null
        self.parent = parent_node
        self.child = None
    def isEqual(self, goal_node):
        if self.X_val == goal_node.X_val and self.Y_val == goal_node.Y_val:
            #print "self X ",self.X_val,"goal_node X ",goal_node.X_val
            #print "self Y ",self.Y_val,"goal_node Y ",goal_node.Y_val
            return True
        else:
            return False
        
    def print_node(self):
        print ("X: ",self.X_val,"Y: ",self.Y_val, "Z: ",self.Z_val)
   
# Linked List class 
class Queue: 
     
    # Function to initialize the Linked  
    # List object 
    def __init__(self):  
        self.head = None
        self.tail = None
        
    
    def append(self, new_node): 
        if self.head == None:
            self.head = new_node

        if self.tail != None:
            self.tail.next = new_node

        self.tail = new_node
     
    def push(self, new_node): 
        new_node.next = self.head 
        self.head = new_node
        if self.tail == None:
            self.tail = new_node
            
    def pop(self):
        if self.head == None:
            return
        
        pop_node = self.head
        self.head = pop_node.next
        return pop_node
    
    def IsEmpty(self):
         if self.head == None:
             return True
         else:
             return False
  
 
   # 4. If the Linked List is empty, then make the 
   #    new node as head 
   
def heuristic(node_n, goal_node):
    n_X = node_n.X_val
    n_Y = node_n.Y_val
    n_Z = node_n.Z_val
    g_X = goal_node.X_val
    g_Y = goal_node.Y_val
    g_Z = goal_node.Z_val
    heuristic = sqrt(((n_X - g_X)**2 + (n_Y - g_Y)**2 + (n_Z - g_Z)**2))
    return heuristic                
    
def A_star_algo(landing_site_node, goal_node):
    #print("in A*")
    A_star_queue_open = []
    
    #Keeping a discovered array, 0 means 1st time, 1 means open queue, 2 means closed
    Discovered = [[] for i in range(Rows)]
    for i in range(Rows):
    #print Elevation_values
        for j in range(Columns):
            Discovered[i].append(0)
            
            
    
    heapq.heappush(A_star_queue_open,(0,(0,landing_site_node)))
    #Indicating that the node is in open queue
    Discovered[landing_site_node.Y_val][landing_site_node.X_val] = 1
    
    while(True):
        if not A_star_queue_open:
            return 0
        
        current_total_cost, (current_path_cost, current_node) = heapq.heappop(A_star_queue_open)
        current_node.print_node()
        if current_node.isEqual(goal_node):
            return current_node 
        
        #if current_node.parent != None:
            #print "Parent node ", (current_node.parent.X_val, current_node.parent.Y_val), "Path cost ", current_path_cost
#        if current_node.isEqual(goal_node):
#            goal_node.print_node()
#            return current_node
        
        X_val = current_node.X_val
        Y_val = current_node.Y_val
        Z_val = current_node.Z_val
        
        children = []
        if Y_val + 1 < Rows:
            if X_val - 1 >= 0:
                if abs(Terrain_map[Y_val+1][X_val-1] - Z_val) <= Threshold:
                    new_node = Node(X_val-1,Y_val+1,Terrain_map[Y_val+1][X_val -1],current_node)
                    path_cost = current_path_cost + 14 + abs(Terrain_map[Y_val+1][X_val-1] - Z_val)
                    children.append((path_cost,new_node))
                    
                    
            if abs(Terrain_map[Y_val+1][X_val]  - Z_val) <= Threshold:
                    new_node = Node(X_val,Y_val+1,Terrain_map[Y_val+1][X_val],current_node)
                    path_cost = current_path_cost + 10 + abs(Terrain_map[Y_val+1][X_val]  - Z_val)
                    children.append((path_cost,new_node))
    
            #print (X_val+1,Y_val+1)
            if X_val + 1 < Columns:
                if abs(Terrain_map[Y_val+1][X_val+1] - Z_val) <= Threshold:
                    new_node = Node(X_val+1,Y_val+1,Terrain_map[Y_val+1][X_val+1],current_node)
                    path_cost = current_path_cost + 14 + abs(Terrain_map[Y_val+1][X_val+1] - Z_val)
                    children.append((path_cost,new_node))
        
        #print (X_val+1,Y_val)            
        if X_val + 1 < Columns:
                if abs(Terrain_map[Y_val][X_val+1] - Z_val) <= Threshold:
                    new_node = Node(X_val+1,Y_val,Terrain_map[Y_val][X_val + 1],current_node)
                    path_cost = current_path_cost + 10 + abs(Terrain_map[Y_val][X_val+1] - Z_val)
                    children.append((path_cost,new_node))
        
                   
        if Y_val - 1 >= 0:
            #print (X_val-1,Y_val-1)
            if X_val - 1 >= 0:
                if abs(Terrain_map[Y_val-1][X_val -1] - Z_val) <= Threshold:
                    new_node = Node(X_val-1,Y_val-1,Terrain_map[Y_val-1][X_val -1],current_node)
                    path_cost = current_path_cost + 14 + abs(Terrain_map[Y_val-1][X_val -1] - Z_val)
                    children.append((path_cost,new_node))
                    
            #print (X_val,Y_val-1)        
            if abs(Terrain_map[Y_val-1][X_val] - Z_val) <= Threshold:
                    new_node = Node(X_val,Y_val-1,Terrain_map[Y_val-1][X_val],current_node)
                    path_cost = current_path_cost + 10 + abs(Terrain_map[Y_val-1][X_val] - Z_val)
                    children.append((path_cost,new_node))
            
            #print (X_val+1,Y_val-1) 
            if X_val + 1 < Columns:
                if abs(Terrain_map[Y_val-1][X_val+1] - Z_val) <= Threshold:
                    new_node = Node(X_val+1,Y_val-1,Terrain_map[Y_val-1][X_val+1],current_node)
                    path_cost = current_path_cost + 14 + abs(Terrain_map[Y_val-1][X_val+1] - Z_val)
                    children.append((path_cost,new_node))
        
        #print (X_val-1,Y_val) 
        if X_val - 1 >= 0:
                if abs(Terrain_map[Y_val][X_val - 1] - Z_val) <= Threshold:
                    new_node = Node(X_val-1,Y_val,Terrain_map[Y_val][X_val - 1],current_node)
                    path_cost = current_path_cost + 10 + abs(Terrain_map[Y_val][X_val - 1] - Z_val)
                    children.append((path_cost,new_node))
        
        while children:
            child_path_cost, child_node = children.pop()
            heuristic_cost = heuristic(child_node,goal_node)
            child_total_cost = heuristic_cost + child_path_cost
            child_X_val = child_node.X_val
            child_Y_val = child_node.Y_val
            if Discovered[child_Y_val][child_X_val] == 0: #Neither closed nor open. Put it in open
                heapq.heappush(A_star_queue_open,(child_total_cost,(child_path_cost,child_node)))
                Discovered[child_Y_val][child_X_val] = 1
            elif Discovered[child_Y_val][child_X_val] == 1: #In open queue
                for i in range(len(A_star_queue_open)):
                    if child_node.isEqual(A_star_queue_open[i][1][1]):
                        if child_total_cost < A_star_queue_open[i][0]:
                            A_star_queue_open[i] = (child_total_cost,(child_path_cost,current_node))
                            heapq.heapify(A_star_queue_open)
                            
            #print child_node.print_node()   
        #print ufs_queue_closed
        Discovered[current_node.Y_val][current_node.X_val] = 2
    
def BFS(landing_site_node):
    #print("in BFS")
    BFS_queue = Queue()
    
    global bfs_queue_closed
    bfs_queue_closed = []
    
    #Keep a matrix for all visited nodes
    Discovered = [[] for i in range(Rows)]
    for i in range(Rows):
    #print Elevation_values
        for j in range(Columns):
            Discovered[i].append(0)
    #print Discovered    
    BFS_queue.push(landing_site_node)
    Discovered[Y_LS][X_LS] =1
    while(True):
        if BFS_queue.IsEmpty() == True:
            return bfs_queue_closed
        current_node = BFS_queue.pop()
        #current_node.print_node()
        
        X_val = current_node.X_val
        Y_val = current_node.Y_val
        node_Z = current_node.Z_val
        #Going in clockwise direction to ckack all possible neighbour nodes 
        if Y_val + 1 < Rows:
            #print (X_val-1,Y_val+1)
            if X_val - 1 >= 0:
                if Discovered[Y_val+1][X_val-1] == 0 and abs(Terrain_map[Y_val+1][X_val-1] - node_Z) <= Threshold:
                    new_node = Node(X_val-1,Y_val+1,Terrain_map[Y_val+1][X_val -1],current_node)
                    BFS_queue.append(new_node)
                    Discovered[Y_val+1][X_val-1] = 1
                
            
            #print (X_val,Y_val+1)
            if Discovered[Y_val+1][X_val] == 0 and abs(Terrain_map[Y_val+1][X_val]  - node_Z) <= Threshold:
                    new_node = Node(X_val,Y_val+1,Terrain_map[Y_val+1][X_val],current_node)
                    BFS_queue.append(new_node)
                    Discovered[Y_val+1][X_val] = 1
                    
    
            #print (X_val+1,Y_val+1)
            if X_val + 1 < Columns:
                if Discovered[Y_val+1][X_val+1] == 0 and abs(Terrain_map[Y_val+1][X_val+1] - node_Z) <= Threshold:
                    new_node = Node(X_val+1,Y_val+1,Terrain_map[Y_val+1][X_val+1],current_node)
                    BFS_queue.append(new_node)
                    Discovered[Y_val+1][X_val+1] = 1
                    
        
        
        #print (X_val+1,Y_val)            
        if X_val + 1 < Columns:
                if Discovered[Y_val][X_val+1] == 0 and abs(Terrain_map[Y_val][X_val+1] - node_Z) <= Threshold:
                    new_node = Node(X_val+1,Y_val,Terrain_map[Y_val][X_val + 1],current_node)
                    BFS_queue.append(new_node)
                    Discovered[Y_val][X_val+1] = 1
                    
        
                   
        if Y_val - 1 >= 0:
            #print (X_val-1,Y_val-1)
            if X_val - 1 >= 0:
                if Discovered[Y_val-1][X_val -1] == 0 and abs(Terrain_map[Y_val-1][X_val -1] - node_Z) <= Threshold:
                    new_node = Node(X_val-1,Y_val-1,Terrain_map[Y_val-1][X_val -1],current_node)
                    BFS_queue.append(new_node)
                    Discovered[Y_val-1][X_val -1] = 1
                    
                    
            #print (X_val,Y_val-1)        
            if Discovered[Y_val-1][X_val] == 0 and abs(Terrain_map[Y_val-1][X_val] - node_Z) <= Threshold:
                    new_node = Node(X_val,Y_val-1,Terrain_map[Y_val-1][X_val],current_node)
                    BFS_queue.append(new_node)
                    Discovered[Y_val-1][X_val] = 1
                    
            if X_val + 1 < Columns:
                if Discovered[Y_val-1][X_val+1] == 0 and abs(Terrain_map[Y_val-1][X_val+1] - node_Z) <= Threshold:
                    new_node = Node(X_val+1,Y_val-1,Terrain_map[Y_val-1][X_val+1],current_node)
                    BFS_queue.append(new_node)
                    Discovered[Y_val-1][X_val+1] = 1
                    
        #print (X_val-1,Y_val) 
        if X_val - 1 >= 0:
                if Discovered[Y_val][X_val - 1] == 0 and abs(Terrain_map[Y_val][X_val - 1] - node_Z) <= Threshold:
                    new_node = Node(X_val-1,Y_val,Terrain_map[Y_val][X_val - 1],current_node)
                    BFS_queue.append(new_node)
                    Discovered[Y_val][X_val - 1] = 1
                    
        bfs_queue_closed.append(current_node)
    
    

                        
def UFS(landing_site_node):
    #print("in UFS")
    ufs_queue_open = []
    global ufs_queue_closed
    ufs_queue_closed = []
    
    #Keeping a discovered array, 0 means 1st time seeing it, 1 means open queue, 2 means closed
    Discovered = [[] for i in range(Rows)]
    for i in range(Rows):
        for j in range(Columns):
            Discovered[i].append(0)
            
            
    #Push the landing node
    heapq.heappush(ufs_queue_open,(0,landing_site_node))
    
    #Indicating that the node is in open queue
    Discovered[landing_site_node.Y_val][landing_site_node.X_val] = 1
    
    while(True):
        if not ufs_queue_open:
            return ufs_queue_closed;
        current_path_cost, current_node = heapq.heappop(ufs_queue_open)
        
        X_val = current_node.X_val
        Y_val = current_node.Y_val
        Z_val = current_node.Z_val
        
        children = []
        if Y_val + 1 < Rows:
            if X_val - 1 >= 0:
                if abs(Terrain_map[Y_val+1][X_val-1] - Z_val) <= Threshold:
                    new_node = Node(X_val-1,Y_val+1,Terrain_map[Y_val+1][X_val -1],current_node)
                    path_cost = current_path_cost + 14
                    children.append((path_cost,new_node))
                    
                    
            if abs(Terrain_map[Y_val+1][X_val]  - Z_val) <= Threshold:
                    new_node = Node(X_val,Y_val+1,Terrain_map[Y_val+1][X_val],current_node)
                    path_cost = current_path_cost + 10
                    children.append((path_cost,new_node))
    
            if X_val + 1 < Columns:
                if abs(Terrain_map[Y_val+1][X_val+1] - Z_val) <= Threshold:
                    new_node = Node(X_val+1,Y_val+1,Terrain_map[Y_val+1][X_val+1],current_node)
                    path_cost = current_path_cost + 14
                    children.append((path_cost,new_node))
        
                    
        if X_val + 1 < Columns:
                if abs(Terrain_map[Y_val][X_val+1] - Z_val) <= Threshold:
                    new_node = Node(X_val+1,Y_val,Terrain_map[Y_val][X_val + 1],current_node)
                    path_cost = current_path_cost + 10
                    children.append((path_cost,new_node))
        
                   
        if Y_val - 1 >= 0:
            if X_val - 1 >= 0:
                if abs(Terrain_map[Y_val-1][X_val -1] - Z_val) <= Threshold:
                    new_node = Node(X_val-1,Y_val-1,Terrain_map[Y_val-1][X_val -1],current_node)
                    path_cost = current_path_cost + 14
                    children.append((path_cost,new_node))
                    
                  
            if abs(Terrain_map[Y_val-1][X_val] - Z_val) <= Threshold:
                    new_node = Node(X_val,Y_val-1,Terrain_map[Y_val-1][X_val],current_node)
                    path_cost = current_path_cost + 10
                    children.append((path_cost,new_node))
            
            if X_val + 1 < Columns:
                if abs(Terrain_map[Y_val-1][X_val+1] - Z_val) <= Threshold:
                    new_node = Node(X_val+1,Y_val-1,Terrain_map[Y_val-1][X_val+1],current_node)
                    path_cost = current_path_cost + 14
                    children.append((path_cost,new_node))
        
        if X_val - 1 >= 0:
                if abs(Terrain_map[Y_val][X_val - 1] - Z_val) <= Threshold:
                    new_node = Node(X_val-1,Y_val,Terrain_map[Y_val][X_val - 1],current_node)
                    path_cost = current_path_cost + 10
                    children.append((path_cost,new_node))
        
        while children:
            child_path_cost, child_node = children.pop()
            child_X_val = child_node.X_val
            child_Y_val = child_node.Y_val
            if Discovered[child_Y_val][child_X_val] == 0: #Neither closed nor open. Put it in open
                heapq.heappush(ufs_queue_open,(child_path_cost,child_node))
                Discovered[child_Y_val][child_X_val] = 1
            elif Discovered[child_Y_val][child_X_val] == 1: #In open queue
                for i in range(len(ufs_queue_open)):
                    if child_node.isEqual(ufs_queue_open[i][1]):
                        if child_path_cost < ufs_queue_open[i][0]:
                            ufs_queue_open[i] = (child_path_cost,current_node)
                            heapq.heapify(ufs_queue_open)
                            
            #print child_node.print_node()   
        ufs_queue_closed.append(current_node)
        Discovered[current_node.Y_val][current_node.X_val] = 2
        
    
    for i in range(len(ufs_queue_closed)):
        print "here"
        ufs_queue_closed[i].print_node()
    return ufs_queue_closed


    
read_file = open("input17.txt")
output_file = open("myoutput17.txt","w")
Algorithm_name = read_file.readline().strip()

#Get the dimensions of Terrrain Map
Map_coordinates = read_file.readline().strip()
#print Map_coordinates
Columns, Rows = [int(x) for x in Map_coordinates.split()] 

#Get the coordinates of Landing site
Landing_site = read_file.readline().strip()
#print Landing_site
X_LS, Y_LS = [int(x) for x in Landing_site.split()] 


#The Threshold
Threshold = int(read_file.readline().strip())
#print Threshold

#Get the number of target site, this tells us to run a loop to get that many target coordinates and store
Num_target_site = int(read_file.readline().strip())
#print Num_target_site
#Form a two dimensional array for storing all target sites
Target_sites =[[] for i in range(Num_target_site)]

for i in range(Num_target_site):
    New_site = read_file.readline().strip()
    New_site = [int(x) for x in New_site.split()] 
    Target_sites[i].append(New_site[0])
    Target_sites[i].append(New_site[1])

#print Target_sites

#Form a matrix for storing the terrain map
Terrain_map = [[] for i in range(Rows)]
for i in range(Rows):
    Elevation_values = read_file.readline().strip()
    Elevation_values = [int(x) for x in Elevation_values.split()]
    #print Elevation_values
    for j in range(Columns):
        Terrain_map[i].append(Elevation_values[j])
        
#print Terrain_map
    
landing_site_node = Node(X_LS,Y_LS,Terrain_map[Y_LS][X_LS], None)

if Algorithm_name == 'A*':
#    for i in range(Num_target_site):
#        target_node = Node(Target_sites[i][0],Target_sites[i][1],Terrain_map[Target_sites[i][1]][Target_sites[i][0]])
#        target_node.print_node()
#        final_string = ""
#        coordinates = []
#        found_target = A_star_algo(landing_site_node,target_node)
#        if found_target == 0:
#            final_string = "FAIL"
#        else:
#            while found_target != None:
#                coordinates.append((found_target.Y_val,found_target.X_val))
#                found_target = found_target.parent
#            while coordinates:
#                (T_Y_val, T_X_val) = coordinates.pop()
#                final_string = final_string + str(T_X_val) + "," + str(T_Y_val) + " "
#        print final_string
#        output_file.write(final_string)
#        output_file.write('\n')
    target_node = Node(Target_sites[3][0],Target_sites[3][1],Terrain_map[Target_sites[3][1]][Target_sites[3][0]])
    target_node.print_node()
    final_string = ""
    coordinates = []
    found_target = A_star_algo(landing_site_node,target_node)
    if found_target == 0:
        final_string = "FAIL"
    else:
        while found_target != None:
            coordinates.append((found_target.Y_val,found_target.X_val))
            found_target = found_target.parent
        while coordinates:
            (T_Y_val, T_X_val) = coordinates.pop()
            final_string = final_string + str(T_X_val) + "," + str(T_Y_val) + " "
    print final_string
    output_file.write(final_string)
    output_file.write('\n')
elif Algorithm_name == 'BFS':
    
    print("BFS")
    global bfs_queue_closed
    bfs_queue_closed = []
    bfs_queue_closed = BFS(landing_site_node)
    #print ufs_queue_closed
    for i in range(Num_target_site):
        target_node = Node(Target_sites[i][0],Target_sites[i][1])
        target_node.print_node()
        final_string = ""
        coordinates = []
        flag = 0
        for j in range(len(bfs_queue_closed)):
            if target_node.isEqual(bfs_queue_closed[j]):
                found_target = bfs_queue_closed[j]
                flag = 1
                coordinates = []
                while found_target != None:
                    coordinates.append((found_target.Y_val,found_target.X_val))
                    found_target = found_target.parent
                while coordinates:
                    (T_Y_val, T_X_val) = coordinates.pop()
                    final_string = final_string + str(T_X_val) + "," + str(T_Y_val) + " "
                break
                
        if flag == 0:
            final_string = "FAIL"
        print final_string
        output_file.write(final_string)
        output_file.write('\n')
        
    
elif Algorithm_name == 'UCS':
    print("UCS")
    global ufs_queue_closed
    ufs_queue_closed = []
    ufs_queue_closed = UFS(landing_site_node)

    for i in range(Num_target_site):
        target_node = Node(Target_sites[i][0],Target_sites[i][1])
        target_node.print_node()
        final_string = ""
        flag = 0
        for j in range(len(ufs_queue_closed)):
            if target_node.isEqual(ufs_queue_closed[j]):
                found_target = ufs_queue_closed[j]
                flag = 1
                coordinates = []
                while found_target != None:
                    coordinates.append((found_target.Y_val,found_target.X_val))
                    found_target = found_target.parent
                while coordinates:
                    (T_Y_val, T_X_val) = coordinates.pop()
                    final_string = final_string + str(T_X_val) + "," + str(T_Y_val) + " "
                break
                
        if flag == 0:
            final_string = "FAIL"
        print final_string
        output_file.write(final_string)
        output_file.write('\n')

read_file.close()
output_file.close()
  
