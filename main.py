import math
import tkinter
import matplotlib.pyplot as plt
import json
import random
with open("./data.json", "r") as json_file:
    data = json.load(json_file)

x = []
y = []

for i in data:
    x.append(float(i["location"]["longitude"]))
    y.append(float(i["location"]["latitude"]))

# How many clusters
# k = int(input('How many clusters'))
k = 3
kx = []
ky = []

for i in range (1, k+1):
    # kx.append(random.uniform(-0.00288049, -0.286463))
    # ky.append(random.uniform(50.9106, 50.788))
    kx.append(random.uniform(-0.00388049, -0.290463))
    ky.append(random.uniform(50.8106, 50.908))

x_closer_to_k1 = []
y_closer_to_k1 = []
x_closer_to_k2 = []
y_closer_to_k2 = []
x_closer_to_k3 = []
y_closer_to_k3 = []


# Plotting the Graph
def plot_graph(q, *args):
  print(q)
  plt.style.use('seaborn')
  plt.xlabel('x')
  plt.ylabel('y')
  plt.scatter(x_closer_to_k1, y_closer_to_k1, s=5, c="#eb344c")
  plt.scatter(x_closer_to_k2, y_closer_to_k2, s=5, c="#3440eb")
  plt.scatter(x_closer_to_k3, y_closer_to_k3, s=5, c="#43eb34")
  plt.scatter(kx[0], ky[0], s=100, alpha=0.4, c="#eb344c") #Red
  plt.scatter(kx[1], ky[1], s=100, alpha=0.4, c="#3440eb") #Blue
  plt.scatter(kx[2], ky[2], s=100, alpha=0.4, c="#43eb34") #Green
  q = str(q)
  plt.savefig("""./examples/figure""" + q + """.png""")
  q = int(q)
  plt.show()

def find_closest(*args):
  n = 0
  for i in x:
    x_ = x[n]
    y_ = y[n]
    # Get me some points.
    def distance_to(*args):
      n = 0
      h = []
      for i in kx:
        h.append(math.sqrt(((x_ - kx[n])**2) + ((y_ - ky[n])**2)))
        n = n + 1
      if h[0] < h[1]:
        if h[0] < h[2]:
          x_closer_to_k1.append(x_)
          y_closer_to_k1.append(y_)
          if x_ in x_closer_to_k2:
            index = x_closer_to_k2.index(x_)
            if y_  == y_closer_to_k2[index]:
              x_closer_to_k2.remove(x_)
              y_closer_to_k2.remove(y_)
          if x_ in x_closer_to_k3:
            index = x_closer_to_k3.index(x_)
            if y_ == y_closer_to_k3[index]:
              x_closer_to_k3.remove(x_)
              y_closer_to_k3.remove(y_)
        else:
          x_closer_to_k3.append(x_)
          y_closer_to_k3.append(y_)
          if x_ in x_closer_to_k2:
            index = x_closer_to_k2.index(x_)
            if y_ == y_closer_to_k2[index]:
              x_closer_to_k2.remove(x_)
              y_closer_to_k2.remove(y_)
          if x_ in x_closer_to_k1:
            index = x_closer_to_k1.index(x_)
            if y_ == y_closer_to_k1[index]:
              x_closer_to_k1.remove(x_)
              y_closer_to_k1.remove(y_)
      else:
        if h[1] < h[2]:
          x_closer_to_k2.append(x_)
          y_closer_to_k2.append(y_)
          if x_ in x_closer_to_k3:
            index = x_closer_to_k3.index(x_)
            if y_ == y_closer_to_k3[index]:
              x_closer_to_k3.remove(x_)
              y_closer_to_k3.remove(y_)
          if x_ in x_closer_to_k1:
            index = x_closer_to_k1.index(x_)
            if y_ == y_closer_to_k1[index]:
              x_closer_to_k1.remove(x_)
              y_closer_to_k1.remove(y_)
        else:
          x_closer_to_k3.append(x_)
          y_closer_to_k3.append(y_)
          if x_ in x_closer_to_k2:
            index = x_closer_to_k2.index(x_)
            if y_ == y_closer_to_k2[index]:
              x_closer_to_k2.remove(x_)
              y_closer_to_k2.remove(y_)
          if x_ in x_closer_to_k1:
            index = x_closer_to_k1.index(x_)
            if y_ == y_closer_to_k1[index]:
              x_closer_to_k1.remove(x_)
              y_closer_to_k1.remove(y_)
    distance_to(x_, y_, kx, ky)
    n = n + 1

avg_xy = []

def find_avg(n, avg_xy, *args):
  sum_ = 0
  points = args[0]
  for i in points:
    sum_ = sum_ + i
  avg = sum_ / len(points)
  avg_xy.append(avg)

def move_to_center(avg_xy, kx, ky, *args):
  n = 0
  for i in (args):
    find_avg(n, avg_xy, args[n])
    n = n +1
  b = 0
  length = len(avg_xy)
  for i in range(0, length, 2):    
    kx.append(avg_xy[i])
    ky.append(avg_xy[i + 1])
    del kx[0]
    del ky[0]

def start(q, *args):
  while True:
    find_closest(x_closer_to_k1, y_closer_to_k1, x_closer_to_k2, y_closer_to_k2, x_closer_to_k3, y_closer_to_k3, x, y)
    q = q + 1
    plot_graph(q, x_closer_to_k1, y_closer_to_k1, x_closer_to_k2, y_closer_to_k2, x_closer_to_k3, y_closer_to_k3, kx, ky)
    for i in range (0, 3):
      avg_xy = []
      move_to_center(avg_xy, kx, ky, x_closer_to_k1, y_closer_to_k1, x_closer_to_k2, y_closer_to_k2, x_closer_to_k3, y_closer_to_k3)


q = 0
start(q, x_closer_to_k1, y_closer_to_k1, x_closer_to_k2, y_closer_to_k2, x_closer_to_k3, y_closer_to_k3, k, kx, ky)