import random
maze=[
     [1,7,13,0,0,0],
     [2,8,0,0,0,0],
     [3,8,0,0,0,0],
     [4,10,0,0,0,0],
     [5,11,0,0,0,0],
     [6,12,0,0,0,0],
     ]


#making starting points(only from first 1 nodes)
while True:
  row=random.randint(0,5)
  col=random.randint(0,1)
  if row==5 & col==1:
    continue
  else:
    break
maze[row][col]=1

#goal node
row_goal=random.randint(0,5)
col_goal=random.randint(4,5)
maze[row_goal][col_goal]=3

count=0
#Barriers
while True:
  if count==4:
    break
  row_barrier=random.randint(0,5)
  col_barrier=random.randint(0,5)
  if maze[row_barrier][col_barrier]==0:
    maze[row_barrier][col_barrier]=2
    count+=1
  else:
    continue


for i in range(6):
  print(maze[i])

