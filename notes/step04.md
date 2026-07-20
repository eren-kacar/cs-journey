# Step 4 - Introduction to Linked Lists

## What I learned

- A Node stores two things: `data` and a reference to the next node (`next`).
- `next = None` means there is no next node (end of the list).
- A Linked List is made of multiple nodes connected by references.
- Nodes can be linked by assigning the `next` reference.
- The first node is usually called the `head`.
- A temporary variable (e.g. `current`) is used to traverse the list without losing the `head`.
- A Linked List can be traversed using a `while` loop until `current` becomes `None`.

## Practice

- Implemented a `Node` class in Python.
- Connected three nodes (`10 -> 20 -> 30`).
- Traversed the linked list using a `while` loop.