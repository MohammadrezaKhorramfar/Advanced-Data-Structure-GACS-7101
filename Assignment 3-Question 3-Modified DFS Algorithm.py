import xlrd 
from collections import defaultdict
loc = ("data2.xlsx") 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0)  
n_v=int(sheet.cell_value(0, 0))
n_edge=int(sheet.cell_value(0, 1))
adj = [[0 for x in range(n_v)] for x in range(n_v)] 
visit=[0]*n_v
color=[0]*n_v
parent=[0]*n_v
d=[0]*n_v
f=[0]*n_v
adj_num=[0]*n_v
dfs=[]

def dfs_visit(u):
   global t
   color[u]=1
   t=t+1
   d[u]=t
   for i in range(adj_num[u]):
       v=adj[u][i]
       if color[v]==0:
           dfs.append(v)
           print("tree:","v",u+1,",v",v+1)
           parent[v]=u
           dfs_visit(v)
       else:
          if color[v]==1:
            print("back:","v",u+1,",v",v+1)
          else:
              if color[v]==2:
                   if d[u]<d[v]:
                        print("forward:","v",u+1,",v",v+1)
                   else:
                        print("cross","v",u+1,",v",v+1)
   color[u]=2
   f[u]=t
   t=t+1
   
##Main Function
t=0      
for i in range(1,n_edge+1):
     a1=int(sheet.cell_value(i, 0))
     a2=int(sheet.cell_value(i, 1))
     print("(v",a1,",v",a2,")")
     a1=a1-1
     a2=a2-1
     adj[a1][adj_num[a1]]=a2 
     adj_num[a1]=adj_num[a1]+1
print("Type of the edges:Cross - Forward - Back - Tree")
for i in range(n_v):
     if color[i]==0:
         dfs.append(i)
         dfs_visit(i) 
for i in range(n_v):
    dfs[i]+=1
print("dfs list is:",dfs)
