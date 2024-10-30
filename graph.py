import matplotlib.pyplot as plt
import numpy as np
import time
from algorithms import bubble_sort, insertion_sort, merge_sort

sizes = [100, 1000, 10000]
bubble_times = []
insertion_times = []
merge_times = []

for size in sizes:
    arr = np.random.randint(0, 10000, size)

    # Bubble Sort
    start_time = time.time()
    bubble_sort(arr.copy())
    bubble_times.append(time.time() - start_time)

    # Insertion Sort
    start_time = time.time()
    insertion_sort(arr.copy())
    insertion_times.append(time.time() - start_time)

    # Merge Sort
    start_time = time.time()
    merge_sort(arr.copy())
    merge_times.append(time.time() - start_time)

plt.figure(figsize=(10, 5))
plt.plot(sizes, bubble_times, label='Bubble Sort', marker='o')
plt.plot(sizes, insertion_times, label='Insertion Sort', marker='o')
plt.plot(sizes, merge_times, label='Merge Sort', marker='o')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Sorting Algorithms Execution Time vs. Input Size')
plt.legend()
plt.grid()
plt.savefig('sorting_time_analysis.png')  # Save the figure
plt.show()