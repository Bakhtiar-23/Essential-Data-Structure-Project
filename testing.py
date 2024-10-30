# test.py

from data_structures import Array, LinkedList, Stack, Queue, BinaryTree, HashTable
from algorithms import bubble_sort, insertion_sort, merge_sort, linear_search, binary_search

if __name__ == "__main__":
    # Test Array
    array = Array(5)
    array.insert(0, 10)
    array.insert(1, 20)
    print("Array:", array)

    # Test Linked List
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    print("Linked List:", ll)

    # Test Stack
    stack = Stack()
    stack.push(1)
    stack.push(2)
    print("Stack:", stack)

    # Test Queue
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    print("Queue:", queue)

    # Test Binary Tree
    bt = BinaryTree()
    bt.insert(10)
    bt.insert(5)
    bt.insert(15)
    print("In-order Traversal:", bt.in_order_traversal(bt.root))

    # Test Hash Table
    ht = HashTable(10)
    ht.insert("key1", "value1")
    print("Hash Table:", ht.get("key1"))

    # Test Sorting Algorithms
    arr = [5, 3, 8, 6, 2]
    print("Bubble Sort:", bubble_sort(arr.copy()))
    print("Insertion Sort:", insertion_sort(arr.copy()))
    print("Merge Sort:", merge_sort(arr.copy()))

    # Test Searching Algorithms
    print("Linear Search:", linear_search(arr, 3))
    print("Binary Search:", binary_search(sorted(arr), 6))
