# Step 6 - prepend()

## What I Learned

In this step, I implemented the `prepend()` method for a singly linked list.

Unlike `append()`, which inserts a new node at the end, `prepend()` inserts a new node at the beginning of the list.

---

## prepend()

Algorithm:

1. Create a new node.
2. Make the new node point to the current head.
3. Update the head to the new node.

Implementation:

```python
def prepend(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
```

Time Complexity:
- O(1)

---

## Why the Order Matters

The order of the two assignments is critical.

Correct order:

```python
new_node.next = self.head
self.head = new_node
```

If the order is reversed:

```python
self.head = new_node
new_node.next = self.head
```

the new node will point to itself, and the original list will become unreachable.

---

## Empty List Case

No special case is required.

If the list is empty:

```text
head
 │
 ▼
None
```

then

```python
new_node.next = self.head
```

simply becomes

```python
new_node.next = None
```

which is exactly what we want.

---

## Complexity

| Operation | Time |
|-----------|------|
| prepend() | O(1) |

---

## What I Realized

`prepend()` is much more efficient than `append()` in a singly linked list without a tail pointer.

- `prepend()` → O(1)
- `append()` → O(n)

I also learned that when working with references, **the order of assignments can completely change the behavior of the program**.