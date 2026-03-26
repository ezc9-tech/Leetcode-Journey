# 🧩 Implement Stack using Queues

## 🔗 Problem Link

[LeetCode - Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/)

---

## 📘 Problem Description

Implement a **Last-In-First-Out (LIFO)** stack using only **queues**.

You must implement the following functions:

* `push(x)` → Push element `x` onto stack
* `pop()` → Removes the element on top of the stack and returns it
* `top()` → Get the top element
* `empty()` → Returns whether the stack is empty

**Constraints:**

* You may only use standard queue operations (push to back, pop from front, size, empty)
* Depending on language, queue may not be native

---

## 💡 Approach / Intuition

A stack follows **LIFO**, but queues follow **FIFO**, so we need to simulate stack behavior using queues.

This solution uses a clever trick with a **nested deque structure**:

* Each `push` creates a new deque node:

  ```
  [current_value, previous_queue]
  ```

* This effectively creates a **linked-list-like chain** using queues

* The top of the stack is always at the **front**

For operations:

* **push:** Create a new deque with current value pointing to old queue
* **pop:** Remove the front element and update the queue reference
* **top:** Return the front element
* **empty:** Check if queue is `None`

This mimics stack behavior efficiently.

---

## ⚙️ Algorithm

1. Initialize `self.q = None`
2. For `push(x)`:

   * Create a deque → `[x, self.q]`
   * Assign it to `self.q`
3. For `pop()`:

   * Remove first element (`popleft`)
   * Update `self.q` to the next stored queue
4. For `top()`:

   * Return first element of deque
5. For `empty()`:

   * Return whether `self.q` is `None`

---

## 🧠 Code

```python id="k4m8zs"
from collections import deque

class MyStack:

    def __init__(self):
        self.q = None

    def push(self, x: int) -> None:
        self.q = deque([x, self.q])

    def pop(self) -> int:
        popped = self.q.popleft()
        self.q = self.q.popleft()
        return popped

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return not self.q
```

---

## ⏱️ Complexity Analysis

* **Time Complexity:**

  * `push`: `O(1)`
  * `pop`: `O(1)`
  * `top`: `O(1)`
  * `empty`: `O(1)`

* **Space Complexity:** `O(n)`

  * Each element is stored in a nested structure

---

## 🧪 Example

```id="a1b2c3"
Input:
push(1)
push(2)
top()
pop()
empty()

Output:
2
2
False
```

---

## 📌 Key Takeaways

* You can simulate different data structures using others with clever structuring
* This solution behaves like a **linked list using queues**
* Important to understand underlying behavior (FIFO vs LIFO)
* Not the standard approach — but a very creative one
