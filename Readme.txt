Please import xlrd library because we used excel file as our input
Please store the code and the three excel files in the same directory
Please Run the code
I arrange three input files
Please change the name of the files in line 3 from data to data1 and data2 to see diffrent inputs
Line 4= we will open our file
Line 5= the number of our sheet in the excel file will be assigned to sheet
in the excel file,I assigned the firs row and first and second column to the number of vertices and edges
then I create the adjacency matrix that is n x n
Then we create our 1D array for visit that will be used in the DFS function
Also we create our array for color
And we create an array for parent of the nodes
Then create the values for the start and finishing time
And also we have a adjacent array because we need the number of vertices that is connected to the i vertex
And at the line 15 we create dfs array to show the traverse of the tree,we assign the vertices to this array as we visit them
Line 43=> we set the time to 0 as we did in our pseudcode 
Then we read our edges from the excel file
We start from 1 bcause in our excel, the first line(0) is for the number of vertices and edges
then we assigne them to a1 and a2 and then we print our edges of the graph
Then we put them in our adjacent matrix
The adjacent number a1 is the number of adjacent edges of a1
Then we create a for loop like the pseudocode  
We assigne the colors to 0 = white , 1 = gray amd 2 = black
so if the color of the node i was white so we add the node to our dfs array and then call the dfs_visit
We go to line 17
first we need to have the time of the traversal of the node so we have a global variable t
Then we check for the color of the vertices(v) and check their type base on the pseudocode
d[u] is the dicovery time and f[u] is the finishing time
In the line 26, we add the u and v by one because in python they start from 0 and we add them by 1 to show them like it was shown in the assignment pdf