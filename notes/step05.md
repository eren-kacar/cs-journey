# Step 5 - Linked List Operations

## What I Learned

In this step, I implemented several fundamental operations for a singly linked list and became more comfortable with traversing linked lists.

---

## append()

Implemented the `append()` method.

Algorithm:
1. Create a new node.
2. If the list is empty, make it the head.
3. Otherwise, traverse to the last node.
4. Connect the last node to the new node.

Time Complexity:
- O(n)

---

## print_list()

Implemented a method to print every element in the linked list.

Key idea:
- The linked list should know how to display its own data instead of exposing traversal logic outside the class.

---

## contains(value)

Implemented a search method.

Algorithm:
1. Start from the head.
2. Compare each node's data with the target value.
3. Return `True` if found.
4. Return `False` if the traversal finishes without finding it.

Time Complexity:
- O(n)

---

## length()

Implemented a method to count the number of nodes.

Algorithm:
1. Initialize a counter.
2. Traverse the list.
3. Increase the counter for each node.
4. Return the final count.

Time Complexity:
- O(n)

---

## sum()

Implemented a method that returns the sum of all values stored in the list.

Algorithm:
1. Initialize `total = 0`.
2. Traverse the list.
3. Add each node's data to `total`.
4. Return `total`.

Time Complexity:
- O(n)

---

## max()

Implemented a method that returns the largest value in the list.

Algorithm:
1. Return `None` if the list is empty.
2. Initialize `max_value` with the first node's value.
3. Traverse the list.
4. Update `max_value` whenever a larger value is found.
5. Return `max_value`.

Time Complexity:
- O(n)

---

## Important Concepts

- A linked list stores only the `head` reference.
- Each node stores:
  - `data`
  - `next`
- `self` represents the current object.
- Every object has its own instance variables.
- `next` stores a reference to another node, not a copy of it.
- Traversal is the foundation of most linked list algorithms.

---

## Complexity Summary

| Operation | Time |
|-----------|------|
| append() | O(n) |
| contains() | O(n) |
| length() | O(n) |
| sum() | O(n) |
| max() | O(n) |

---

## What I Realized

Most linked list algorithms share the same traversal pattern:

```python
current = self.head

while current is not None:
    # Do something

    current = current.next
```

The only thing that changes is **what I do with each node**.