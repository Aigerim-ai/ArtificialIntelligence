# Artificial-Intelligence
Assignment 1
In this assignment, there are two python files: 

as1_bfs.py: we have already implemented the basic BFS algorithm, which can work properly with the non-loopy path.
as1_test.py: you can use this file to test your implementation. In this file, we included two data structures that reflect the tree. These are also the trees that we will use to grade your implementation.
Tasks: two functions need to be implemented:

def traverse(tree, init): BFS traversal function. This func accepts two inputs: the tree to traverse and the initial state. We already provided an example of how to run this func in the as1_test.py. Your task is to modify it to run with the loopy path. So far, if you try to traverse the tree_2 without a valid modification, your program crashes. (2 points)
def pathfinder(tree, init, goal): still BFS traversal function. However, this func accepts three inputs: the tree, the initial state, and the goal state. Your task is to find the solution from the initial state to the goal state even we have the loopy path in the tree. (3 points)

Assignment 2
In this assignment, we will consider the problem of finding the shortest path for a robot vacuum on an 8x8 grid. The detailed instructions are included in the PA2_instruction.pdf file and python files that will guide you through the assignment.

The code for this assignment includes the following files:

PA2_search.py: you will edit this file which contains methods for A* an UCS algorithms.
PA2_test.py: this file is used to visualize the results and test the A* and UCS algorithms.
Files to Edit and Submit: You will fill in portions of PA2_search.py only during the assignment, and submit it. You should submit this file with your code and comments. Please do not change the other files in this distribution or submit any of our original files other than this file.
In PA2_search.py file, there are ###### START OF YOUR CODE HERE/#### END OF YOUR CODE#### tags denoting the start and end of code sections you should fill out. Take care to not delete or modify these tags. Otherwise, your assignment may not be properly graded.

Complete UCsearch() and aStarSearch() functions in the PA2_search.py file.

Although there are multiple solutions with A* and UCS, make sure that you achieve the same cost for these methods.

To test your implementation, run your code with: python PA2_test.py

Assignment 3
In this assignment, there are three python files that implement the MINIMAX algorithm:

as3_tree.py: this class transforms a list of data into a tree. Do not change this file.
as3_mnx.py: you will work on this file and submit this file only.
as3_test.py: you can use this file to test your implementation. In this file, we included a list of data that provides the terminal value for the tree. 
Tasks: two tasks need to be fulfilled:

There are four (4) logical errors, which are intentionally put inside the file: as3_mnx.py. You have to find ALL the errors and fix them. Otherwise, your code will not work correctly. For example, the result of the best terminal value in the root should be '3' instead of '6'. (2 points)
Implement the additional code (also in the file: as3_mnx.py) to return the traversed_solution in the form of an array. For example: ['A', 'X', 'Y'], with A is the root node, X is the child of A, Y is the leaf node containing the best terminal value (which is 3). Apparently, Y the child of X. (3 points)
Remember to put the best terminal value and the traversed_solution into the object res, which is an instance of the class Result. We have already included an example of how to use this object in the file: as3_mnx.py (from line 33 to line 39). 
