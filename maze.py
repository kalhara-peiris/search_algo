import random
maze=[
     ["01","07","13","19","25","31"],
     ["02","08","14","20","26","32"],
     ["03","09","15","21","27","33"],
     ["04","10","16","22","28","34"],
     ["05","11","17","23","29","35"],
     ["06","12","18","24","30","36"],
     ]

#making starting points(only from first 1 nodes)
while True:
  row=random.randint(0,5)
  col=random.randint(0,1)
  if row==5 & col==1:
    continue
  else:
    break
maze[row][col]="ST"

#goal node
row_goal=random.randint(0,5)
col_goal=random.randint(4,5)
maze[row_goal][col_goal]="GO"

count=0
#Barriers
while True:
  if count==4:
    break
  row_barrier=random.randint(0,5)
  col_barrier=random.randint(0,5)
  if maze[row_barrier][col_barrier]!="BA":
    maze[row_barrier][col_barrier]="BA"
    count+=1
  else:
    continue

print()

for i in range(6):
  for j in range(6):
    print(maze[i][j],end=" ")
  print()  
print()

#visiting list 

visited_list=[]
visited_nodes=[]
print(row,col)
visited_nodes.extend([row,col])
visited_list.append(visited_nodes)
visited_list.clear()
print(visited_list)


