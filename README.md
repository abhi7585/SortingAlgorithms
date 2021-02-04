# SortingAlgorithms
A sorting algorithm is an algorithm that places the list elements in a certain order. Efficient sorting is critical for maximizing the performance of other algorithms that enable input data to be stored in sorted lists.

This package will help user to get the results of few sorting algorithms(will be updated in future). 

## Installation
```pip install SortingAlgorithms```

## How to use it?
First, use the above command to install the package. The package includes a few algorithms that can be used either to understand the working condition or to complete the goal by using a sorting algorithm.

Below is a brief example of how the package will be used to accomplish the goal.

```
from SortingAlgorithms import Algorithms as algo

data = [22, 5, 34, 12, 90, 33] 

print(algo.bubbleSort(array= data, ascending= True, steps= True))
```
Output:- 
```
step 1:-
j = 0 : [22, 5, 34, 12, 90, 33] 
Swapping: 5 with 22
j = 1 : [5, 22, 34, 12, 90, 33] 
j = 2 : [5, 22, 34, 12, 90, 33] 
Swapping: 12 with 34
j = 3 : [5, 22, 12, 34, 90, 33] 
j = 4 : [5, 22, 12, 34, 90, 33]
Swapping: 33 with 90


step 2:-
j = 0 : [5, 22, 12, 34, 33, 90]
j = 1 : [5, 22, 12, 34, 33, 90]
Swapping: 12 with 22
j = 2 : [5, 12, 22, 34, 33, 90]
j = 3 : [5, 12, 22, 34, 33, 90]
Swapping: 33 with 34


step 3:-
j = 0 : [5, 12, 22, 33, 34, 90]
j = 1 : [5, 12, 22, 33, 34, 90]
j = 2 : [5, 12, 22, 33, 34, 90]


step 4:-
j = 0 : [5, 12, 22, 33, 34, 90]
j = 1 : [5, 12, 22, 33, 34, 90]

step 5:-
j = 0 : [5, 12, 22, 33, 34, 90]


step 6:-


[5, 12, 22, 33, 34, 90]
```

The parameters which user can use while calling the functions are:
* array - The array of number is given as input.
* ascending - The order in which the array needs to sorted. Bydefault it is False i.e descending.
* steps - If working of sorting is need to be scene steps can be used. Bydefault it is False.

## Algorithms which are available in package:
1) Bubble Sort
2) Selection Sort
3) Insertion Sort

## Version Update details

1) version 1.0 - 04/02/2021 


## License

© 2021 Abhishek Tripathi

This repository is licensed under the MIT license. See LICENSE for details.