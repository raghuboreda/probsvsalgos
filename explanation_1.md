Problem_1
=========
sqrt function: Idea is to do a binary search for a number whose square is slightly 
less than the target number.
Time Complexity:
O(logN) ==> Where N is the integer whose square root we are seeking. Since it's 
binary search and at every iteration we are reducing the possible numbers to half
previous iteration

Space Complexity:
O(logN) ==> We are only passing array pointer, start index, end index at every
iteration. There could be logN iterations and this will take logN stack space.

Problem_2
=========
rotated_array_search
Idea is to do a binary search for the target.
Time Complexity
O(logN) Where N is the number of elements in the array we are searching for.
Space Complexity
O(logN) Where N is the number of elements in the array.

Problem_3
=========
rearrange_digits
idea is to use store all digits in a min-heap datastructure. pop one digit at a 
time from the min-heap to make the two numbers which give the maximum sum.
Time Complexity
O(NlogN) where N is the number of elements in the input array.
NlogN is the time taken to build the heap structure. It takes logN time to pop
an element from the heap.

Space Complexity
O(1). No extra space is needed.

Problem_4
=========
sort_012
Idea is to have 3 pointers. one pointer to track 0's from the beginning of the
array and second pointer to track 2's from the end of the array. We use the
third pointer to inspect each element.

Time Complexity
O(N) => We do this in single traversal as required by problem.

Space Complexity
O(1) => Only in-place swaps. No new memory is needed.

Problem 5
=========
Auto completion using Trie datastructure
Time Complexity
O(mn) - Where m is the longest word and n is the number of words stored in the
        trie data structure.
Space Complexity
O(m) - Does depend on the length of longest word. As at each level, you have an maximum
       of 26 child nodes. It can become a big number if the number of levels 
       increase.

Problem 6
=========
Time Complexity
O(N) where N is number of elements in input array
Space Complexity
O(1) - Constant space. No need for any extra space

Problem 7
=========
Idea is to store the nodes in the path in a trie like datastructure

Time Complexity
O(logN) Where N is number of nodes in the tree and nodes are seperated by
        '/' in the given path
Space Complexity
O(N) Where N is number of unique node's added to the route trie data structure



