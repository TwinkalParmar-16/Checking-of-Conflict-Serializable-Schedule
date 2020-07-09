from collections import defaultdict 

#-------------------------variables-------------------------------------
TRANS=0
DATA=0
matrix=[]

#three set as white, grey and black
wSet=[]
gSet=[]
bSet=[]

#--------------------------------Class to represent a graph------------------------------------------- 
class Graph: 
	def __init__(self,vertices): 
		self.graph = defaultdict(list) # adjacency List 
		self.V = vertices #No. of vertices 

	# add a edge to graph 
	def addEdge(self,u,v): 
		self.graph[u].append(v) 

	# recursive function  
	def topologicalSortUtil(self,v,visited,stack): 

		# current node = visited. 
		visited[v] = True

		# Recur for all the vertices adjacent to this vertex 
		for i in self.graph[v]: 
			if visited[i] == False: 
				self.topologicalSortUtil(i,visited,stack) 

		# Push current vertex to stack which stores result 
		stack.insert(0,v) 

	# The function to do Topological Sort. It uses recursive 
	# topologicalSortUtil() 
	def topologicalSort(self): 
		# Mark all the vertices as not visited 
		visited = [False]*self.V 
		stack =[] 

		 
		# Sort starting from all vertices one by one 
		for i in range(self.V): 
			if visited[i] == False: 
				self.topologicalSortUtil(i,visited,stack) 

		# Print contents of the stack 
		print (stack) 


#----------------------------------------functions--------------------------------------------------
#extra \n removal
def remove_n(list):
    for i in range(len(list)):
      list[i]=list[i].strip()
    return list

#extra space removal
def remove_space(list):
     if '' in list:
          while '' in list:
               list.remove('')
     return list

#DFS algorithm for detecting cycle
def dfs(curr):
   #moving curr to white set to grey set.
   if curr in wSet:
    wSet.pop(wSet.index(curr))
    gSet.append(curr)

   for v in range(TRANS):
      if(matrix[curr][v] != 0): #for all neighbour vertices
           
         if((v in bSet) and (bSet.index(v) != bSet[-1])):
            continue    #if the vertices are in the black set
         if((v in gSet) and (gSet.index(v) != gSet[-1])):
            return 1    #it is a cycle
         if(dfs(v)):
            return 1    #cycle found


   #moving v to grey set to black set.
   if curr in gSet:
    gSet.pop(gSet.index(curr))
    bSet.append(curr)
   return 0
           
   
#detecting cycle in matix
def hasCycle():
   for i in range(TRANS):
     wSet.append(i) #initially add all node into the white set
   while(len(wSet)>0):
      for current in range(TRANS):
         if((current in wSet) and (wSet.index(current) != wSet[-1])):
            if(dfs(current)):
               return 1
   return 0


    
print("---------------------------------------------PRE-PROCESSING PART-----------------------------------------------")    
#opening the input file
file=open("input5.txt",'r')
input_data=file.readlines()
print("Raw Input :- ",input_data)

#removing extra \n
input_data=remove_n(input_data)

#removing extra spces  
if '' in input_data:
    while '' in input_data:
        input_data.remove('')

print("Input File :- ",input_data)

#counting the number of transaction and data used in schedule
transaction_string=input_data[0]
data_string=input_data[1]

TRANS=transaction_string.count(',')+1
DATA=data_string.count(',')+1

print("TRANS :- ",TRANS)
print("DATA :- ",DATA)

#making matrix of size TRANS for graph

R = TRANS 
C = TRANS 
#initialzing with 0 values 
for i in range(R):          
    a =[] 
    for j in range(C):       
         a.append(0) 
    matrix.append(a) 
  
# For printing the matrix 
print("Matrix for Graph :- ")
for i in range(R): 
    for j in range(C): 
        print(matrix[i][j], end = " ") 
    print() 

#transaction series
trans_list=input_data[3:]
print("Transaction Series List :- ",trans_list)

trans_no_list=[] # to store transaction number
operation_type_list=[] # to store type of operation (read or write)
data_used_list=[] # to store data (A,B,C.....etc)

#to fill the lists mentioned above
x=len(trans_list)
i=0
for i in range(x):
    temp_string=trans_list[i]
    #T1:R(A)
    #T 1 : R ( A )
    #0 1 2 3 4 5 6
    trans_no_list.append(temp_string[1]) 
    operation_type_list.append(temp_string[3])
    data_used_list.append(temp_string[5])

print("TRANS     OPERATION     DATA")
i=0
for i in range(x):
    print("     ",trans_no_list[i],"          ",operation_type_list[i],"          ",data_used_list[i])

#checking for comflic serializablity

#step1-creating TRANS number of nodes
print("--------------------------------------------------Step1 :- ")
print(matrix)

#step2-conflict opertation(W(x)-->R(x))
print("--------------------------------------------------Step2 :- ")
i=0
j=0
for i in range(x):
    if operation_type_list[i]=='W':
        for j in range(i+1,x,1):
            if operation_type_list[j]=='R' :
                #checking conflict operation condition
                #condition1-different transaction
                #condition2-same data item
                #condition3-at least one of them is write
                if (trans_no_list[i] !=trans_no_list[j]) and (data_used_list[i]==data_used_list[j]):
                    print("INDEX :- ",i,"  ",j)
                    print("TRANS :- ",trans_no_list[i],"  ",trans_no_list[j])
                    print("DATA :- ",data_used_list[i],"  ",data_used_list[j])
                    print("OPERATIONS :- ",operation_type_list[i],"  ",operation_type_list[j])
                    From=int(trans_no_list[i])
                    To=int(trans_no_list[j])
                    print("Conflict Operation Found at indez : ",From," ",To)
                    #edge index : 0 1 2 3.......  Transaction : 1 2 3 4 .......
                    #index=trans-1
                    matrix[From-1][To-1]=1
                    print("Matrix :- ",matrix)
                    

#step3-conflict opertation(R(x)-->W(x))
print("--------------------------------------------------Step3 :- ")
i=0
j=0
for i in range(x):
    if operation_type_list[i]=='R':
        for j in range(i+1,x,1):
            if operation_type_list[j]=='W' :
                #checking conflict operation condition
                #condition1-different transaction
                #condition2-same data item
                #condition3-at least one of them is write
                if (trans_no_list[i] !=trans_no_list[j]) and (data_used_list[i]==data_used_list[j]):
                    print("INDEX :- ",i,"  ",j)
                    print("TRANS :- ",trans_no_list[i],"  ",trans_no_list[j])
                    print("DATA :- ",data_used_list[i],"  ",data_used_list[j])
                    print("OPERATIONS :- ",operation_type_list[i],"  ",operation_type_list[j])
                    From=int(trans_no_list[i])
                    To=int(trans_no_list[j])
                    print("Conflict Operation Found at indez : ",From," ",To)
                    #edge index : 0 1 2 3.......  Transaction : 1 2 3 4 .......
                    #index=trans-1
                    matrix[From-1][To-1]=1
                    print("Matrix :- ",matrix)

#step4-conflict opertation(W(x)-->W(x))
print("--------------------------------------------------Step4 :- ")
i=0
j=0
for i in range(x):
    if operation_type_list[i]=='W':
        for j in range(i+1,x,1):
            if operation_type_list[j]=='W' :
                #checking conflict operation condition
                #condition1-different transaction
                #condition2-same data item
                #condition3-at least one of them is write
                if (trans_no_list[i] !=trans_no_list[j]) and (data_used_list[i]==data_used_list[j]):
                    print("INDEX :- ",i,"  ",j)
                    print("TRANS :- ",trans_no_list[i],"  ",trans_no_list[j])
                    print("DATA :- ",data_used_list[i],"  ",data_used_list[j])
                    print("OPERATIONS :- ",operation_type_list[i],"  ",operation_type_list[j])
                    From=int(trans_no_list[i])
                    To=int(trans_no_list[j])
                    print("Conflict Operation Found at indez : ",From," ",To)
                    #edge index : 0 1 2 3.......  Transaction : 1 2 3 4 .......
                    #index=trans-1
                    matrix[From-1][To-1]=1
                    print("Matrix :- ",matrix)

#step5
#no cycle:conflict serializable
#cycle:not conflict serializable        
print("--------------------------------------------------Step5 :- ")
print("")
print("")
print("-----------------------------Final Results----------------------")
print("")
print("")
res=0
res = hasCycle();
if(res):
      print("Cycle Detected ::: Non-Conflicting Schedule")
      print("Matrix :- ")
      print(matrix)
      #cycle
      i=0
      j=0
      for i in range(R): 
       for j in range(C):
          if matrix[i][j]==1: 
           print("T",i+1,"--->","T",j+1)  

else:
      print("No Cycle Detected ::: Conflicting Schedule")
      #topological sorting
      g = Graph(TRANS)
      for i in range(R):
        for j in range(C):
          if matrix[i][j]==1:
           g.addEdge(i,j)
      print ("Topological Sort :-")
      g.topologicalSort()
       






