# Problem 18 - Maximum path sum I
import math
import time as T
start=T.time()

class MaximumPathSum:
  list = list()

  # ctor
  def __init__(self, input):
    lines = input.strip().splitlines()
    for l in lines:
      arr = list(map(int,l.split(' ')))
      self.list.append(arr)

  # search for whole
  def bfs(self):
    roads = list()
    # first route directly down
    road = [0] * len(self.list)
    roads.append(road[::])
    while road:
      lvl = len(road)
      val = road.pop()
      if (lvl > 1) and (val == 0):
        val = 1
        road.append(val)
      else:
        # lvl 1 or noway to go
        continue
      # fill till full road with zeros
      while len(road) < len(self.list):
        road.append(0)
      roads.append(road[::])
    return roads

  # find max route
  def routeMax(self, roads):
    max = -1
    maxroad = list()
    # go thru all roads
    for road in roads:
      pos = 0
      sum = 0
      for x in range(len(self.list)):
        if (road[x] == 1):
          pos += 1
        sum += self.list[x][pos]
      if (sum > max):
        max = sum
        maxroad = road  
    # return max sum and road also
    return (max, maxroad)

triangle = """
3
7 4
2 4 6
8 5 9 3
"""

triangle = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

# init & calc
pyramid = MaximumPathSum(triangle)
r = pyramid.bfs()
print (pyramid.routeMax(r), len(r))

print("Executed in {0:.2f} sec").format(T.time()-start)