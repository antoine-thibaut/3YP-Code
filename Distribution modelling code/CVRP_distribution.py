#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 17:25:40 2021

@author: Antoine
"""

# NOTE: This code has all been copied from a source:
# https://github.com/industrial-ucn/jupyter-examples/blob/master/optimization/cvrp-gurobi.ipynb

import numpy as np
import matplotlib.pyplot as plt

n = 5                    # number of clients

xc = np.array([-1.21726,-1.19719,-1.19285,-1.4946,-1.24657,-1.26362])   # x coordinates 
yc = np.array([51.71164,51.72743,51.73705,51.78529,51.6224,51.74548])   # y coordinates
plt.plot(xc[0], yc[0], c='r', marker='s') # Plotting the depot
plt.scatter(xc[1:], yc[1:], c='b')        # Plotting all other coordinates 


N = [i for i in range(1, n+1)]                # Set of clients
V = [0] + N                                   # Set of nodes
A = [(i, j) for i in V for j in V if i != j]  # Set of arcs
c = {(i, j): np.hypot(xc[i]-xc[j], yc[i]-yc[j]) for i, j in A} # cost of travel over arc
Q = 10                                        # Vehicle capacity
q = {i: 10 for i in N}                        # Amount which has to be delivered to the customer

from gurobipy import Model, GRB, quicksum

mdl = Model('CVRP')

x = mdl.addVars(A, vtype=GRB.BINARY)      # Creating a dictionary with list of arcs
u = mdl.addVars(N, vtype=GRB.CONTINUOUS)


mdl.modelSense = GRB.MINIMIZE
mdl.setObjective(quicksum(x[i, j]*c[i, j] for i, j in A)) # Cost of all arcs

mdl.addConstrs(quicksum(x[i, j] for j in V if j != i) == 1 for i in N) # exactly one arc leaves each vertex associated with a customer
mdl.addConstrs(quicksum(x[i, j] for i in V if i != j) == 1 for j in N) # exactly one arc enters each vertex associated with a customer
mdl.addConstrs((x[i, j] == 1) >> (u[i]+q[j] == u[j])
               for i, j in A if i != 0 and j != 0) # Excluding connections to depot
mdl.addConstrs(u[i] >= q[i] for i in N)
mdl.addConstrs(u[i] <= Q for i in N)


mdl.Params.MIPGap = 0.1
mdl.Params.TimeLimit = 30  # seconds
mdl.optimize()

active_arcs = [a for a in A if x[a].x > 0.99]

for i, j in active_arcs:
    plt.plot([xc[i], xc[j]], [yc[i], yc[j]], c='g', zorder=0)
plt.plot(xc[0], yc[0], c='r', marker='s')
plt.scatter(xc[1:], yc[1:], c='b')
plt.savefig('CVRP.svg', format='svg', dpi=1200)







