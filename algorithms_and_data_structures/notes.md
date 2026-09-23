# Notes on algorithms and data structures
in this file,I whote the content of my studys in algorithms and data structures (an area in which I am currently as of September 2026—investing heavily to increase my mastery)

## why i study it?
the language of the moment—frameworks change all the time—the foundation supporting it all, the algorithms and data structures, has remained practically the same since the days of Alan Turing.
Like any programmer who reaches a higher level of maturity, my primary concern has shifted from the choice of framework or language to the efficiency of the implementation. I realized there was a significant gap in my knowledge and am working to address it.

## the big o
### the problem
To analyze different solutions to a computational problem, we need a way to measure algorithm efficiency that accounts for interfering factors—such as the hardware or the programming language in which the solution was implemented (e.g., Python vs. C).
This notation helps software engineers categorize different computational algorithms by efficiency levels (spoiler: O(1) is ideal, while O(n!) is typically the worst-case scenario). 

### big o calculation 
To find the Big O of an algorithm, we will need two variable:
  n = input size 
  time_cost = time the algorithm takes to execute
Find the correlation between input size and execution time, and you will be able to classify the Big O

#### o(1) 
If the execution time remains stable regardless of the input size, we have an O(1) algorithm.
exemple
```python
def follow_my_github(n:int):
    print("thanks your number is;",n)
``` 
It doesn't matter if the function's input is zero or a trillion; the response time will be exactly the same.

#### o(n)
n O(n) algorithms, the input grows exponentially with the size of the input.
exemple
```python
 def display_array(array):
     for i in len(array):
        print(array[i])
```
the number of times the function will execute the code contained in the loop, and therefore its execution time is determined by the size of the input.

#### o(n²) 
The relationship between computational cost and input size is quadratic.
exemple
```python
def find_duplicates(target_list):
    duplicates = []

    for i in range(len(lista)):
        for j in range(i + 1, len(target_list)):
            if target_list[i] == target_list[j] and target_list[i] not in duplicates:
                duplicates.append(target_list[i])
    return duplicates

```

## linked lists
data structure that allows for rapid scaling, but at a higher memory cost 
A linked list is a data structure made of nodes. Each node stores a value and a reference to the next node. The list starts with a "head", which points to the first node. For example: "head → [10] → [20] → [30] → None".

To access an element, the list follows these references one by one, starting from the "head". This is called traversal and takes O(n) in the worst case. Inserting or removing a node can be O(1) when you already have a reference to the correct position, because you only need to change the connections between nodes. 

| Feature | Array / Vector | Linked List |
|---|---|---|
| Structure | Elements stored sequentially | Nodes connected by references |
| Access by index | **O(1)** | **O(n)** |
| Search | O(n) | O(n) |
| Insertion at the beginning | O(n) | **O(1)** |
| Removal at the beginning | O(n) | **O(1)** |
| Insertion in the middle | O(n) | O(1)* |
| Removal in the middle | O(n) | O(1)* |
| Insertion at the end | O(1)** | O(n)*** |
| Memory per element | Lower | Higher (`value` + `next`) |
| Memory locality | **Good** | Usually worse |
| Random access | **Excellent** | Poor |
| Best suited for | Frequent index access | Frequent insertions/removals |

in the file linked_list.py you will find an implementation of the structure created by me
