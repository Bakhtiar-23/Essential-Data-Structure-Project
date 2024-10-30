# Essential-Data-Structure-Project
This project implements fundamental data structures and algorithms in Python, including arrays, linked lists, stacks, queues, trees (binary, binary search, balanced), and hash tables. It offers hands-on experience in designing, implementing, and analyzing these structures to enhance understanding and performance analysis.

## Running the Project

To run the project, follow these steps:

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone https://github.com/Bakhtiar-23/Essential-Data-Structure-Project.git
2. cd Essential_Data_Structures_Project
3. python testing.py


### About the Project Objectives:
1- All necessary code in Python available in this repository
2- Suggested Structure for Documentation:
   Overview: Brief introduction to data structures and algorithms.
   a- Implemented Data Structures:
      - Array: Explanation, methods (insert, get), and usage example.
      - Linked List: Explanation, methods (append), and usage example.
      - Stack: Explanation, methods (push, pop), and usage example.
      - Queue: Explanation, methods (enqueue, dequeue), and usage example.
      - Binary Tree: Explanation, methods (insert, traversals), and usage example.
      - Hash Table: Explanation, methods (insert, get), and usage example.
   b- Implemented Algorithms:
       - Sorting Algorithms: Explain each algorithm (bubble sort, insertion sort, merge sort) with          examples.
       - Searching Algorithms: Explain linear and binary search with examples.

3- Test Cases and Validation Reports.

Suggested Test Cases:
   - Array Tests: Test insertion and retrieval.
   - Linked List Tests: Test appending and edge cases (e.g., empty list).
   - Stack Tests: Test pushing and popping, including underflow.
   - Queue Tests: Test enqueueing and dequeueing, including underflow.
   - Binary Tree Tests: Test insertions and traversal methods.
   - Hash Table Tests: Test insertion, retrieval, and handling collisions.
 
4- Performance Analysis Report

## Introduction
Performance analysis is crucial in algorithm design as it helps us understand the efficiency and scalability of our implemented data structures and algorithms. By evaluating the time and space complexities, we can determine the best algorithms to use for specific problems and identify potential bottlenecks in our solutions. This report presents the performance analysis of various sorting and searching algorithms implemented in the Essential Data Structures Project.

## Time Complexity
The following table summarizes the time complexities of the implemented sorting and searching algorithms:

| Algorithm          | Best Case  | Average Case  | Worst Case  |
|--------------------|------------|---------------|-------------|
| **Bubble Sort**    | O(n)       | O(n²)         | O(n²)       |
| **Insertion Sort** | O(n)       | O(n²)         | O(n²)       |
| **Merge Sort**     | O(n log n) | O(n log n)    | O(n log n)  |
| **Linear Search**   | O(1)       | O(n)          | O(n)        |
| **Binary Search**  | O(1)       | O(log n)      | O(log n)    |

### Explanation:
- **Bubble Sort** and **Insertion Sort** have quadratic time complexities, making them inefficient for large datasets. They perform better on nearly sorted data.
- **Merge Sort** provides a consistent O(n log n) time complexity, making it suitable for larger datasets due to its divide-and-conquer strategy.
- **Linear Search** checks each element sequentially, while **Binary Search** is more efficient with a logarithmic time complexity but requires the array to be sorted.

## Space Complexity
The following table summarizes the space complexities of the implemented algorithms:

| Algorithm          | Space Complexity |
|--------------------|------------------|
| **Bubble Sort**    | O(1)             |
| **Insertion Sort** | O(1)             |
| **Merge Sort**     | O(n)             |
| **Linear Search**   | O(1)             |
| **Binary Search**  | O(1)             |

### Explanation:
- **Bubble Sort** and **Insertion Sort** are in-place sorting algorithms, utilizing constant space.
- **Merge Sort** requires additional space proportional to the size of the array being sorted, making it less space-efficient than the other algorithms.
- Both search algorithms (Linear and Binary) use constant space.
## Graphs/Charts
To visualize the performance of sorting algorithms, the following graphs can be created. You can use libraries like `matplotlib` or `seaborn` in Python to generate these graphs.

### Sorting Algorithms Execution Time vs. Input Size
1. Generate random arrays of varying sizes (e.g., 100, 1000, 10000).
2. Measure the execution time for each sorting algorithm on these arrays.
3. Plot the results can be found in the file 'graph.py' in the project files







