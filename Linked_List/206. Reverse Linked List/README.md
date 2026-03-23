# 🧩 Reverse Linked List

## 🔗 Problem Link

[LeetCode - Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

---

## 📘 Problem Description

Given the head of a **singly linked list**, reverse the list and return the reversed list.

---

## 💡 Approach / Intuition

To reverse a linked list, we need to **change the direction of each pointer**.

### Key ideas:

* Use two pointers:

  * `curr` → current node
  * `prev` → previous node (initially `None`)
* Iterate through the list and **reverse the `.next` pointer**
* Carefully store the next node before breaking the link

---

## ⚙️ Algorithm

1. Initialize:

   ```
   curr = head
   prev = None
   ```

2. While `curr` is not `None`:

   * Store next node:

     ```
     temp = curr.next
     ```

   * Reverse the pointer:

     ```
     curr.next = prev
     ```

   * Move `prev` forward:

     ```
     prev = curr
     ```

   * Move `curr` forward:

     ```
     curr = temp
     ```

3. Return:

   ```
   prev
   ```

---

## 🧠 Code

```python id="s1c9k3"
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize pointers
        curr = head
        prev = None

        # Traverse the list
        while curr:
            # Store next node
            temp = curr.next

            # Reverse the link
            curr.next = prev

            # Move pointers forward
            prev = curr
            curr = temp

        # prev will be the new head
        return prev
```

---

## ⏱️ Complexity Analysis

* **Time Complexity:** `O(n)`

  * We traverse the list once

* **Space Complexity:** `O(1)`

  * In-place reversal with no extra space

---

## 🧪 Example

```id="ex1"
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```

### Explanation:

```id="exp1"
Original: 1 → 2 → 3 → 4 → 5 → None

Step-by-step reversal:
1 → None
2 → 1 → None
3 → 2 → 1 → None
4 → 3 → 2 → 1 → None
5 → 4 → 3 → 2 → 1 → None
```

---

```id="ex2"
Input: head = [1,2]
Output: [2,1]
```

---

```id="ex3"
Input: head = []
Output: []
```

---

## 📌 Key Takeaways

* Always store `next` before modifying pointers
* Reversing a linked list is about **flipping directions one node at a time**
* The `prev` pointer becomes the new head
* This is a foundational **pointer manipulation** problem 🚀
