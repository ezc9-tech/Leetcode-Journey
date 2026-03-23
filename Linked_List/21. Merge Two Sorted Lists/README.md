# 🧩 Merge Two Sorted Lists

## 🔗 Problem Link

[LeetCode - Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

---

## 📘 Problem Description

You are given the heads of two **sorted linked lists** `list1` and `list2`.

Merge the two lists into one **sorted linked list** and return its head.

The new list should be made by **splicing together the nodes** of the first two lists.

---

## 💡 Approach / Intuition

This problem is similar to merging two sorted arrays, but with **linked lists**.

### Key ideas:

* Use a **dummy node** to simplify handling the head of the new list
* Maintain a pointer (`node`) to build the merged list
* Compare values from both lists and attach the smaller one
* Move forward in the list from which you took the node
* Once one list is exhausted, attach the remaining nodes from the other list

---

## ⚙️ Algorithm

1. Create a dummy node:

   ```
   list3 = node = ListNode()
   ```

2. While both lists are not empty:

   * If `list1.val < list2.val`:

     * Attach `list1` to `node.next`
     * Move `list1` forward

   * Else:

     * Attach `list2` to `node.next`
     * Move `list2` forward

   * Move `node` forward

3. After the loop:

   * Attach remaining nodes:

     ```
     node.next = list1 or list2
     ```

4. Return:

   ```
   list3.next
   ```

---

## 🧠 Code

```python id="s1c9k3"
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to build the result list
        list3 = node = ListNode()

        # Traverse both lists
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next

            # Move the pointer forward
            node = node.next

        # Attach any remaining elements
        node.next = list1 or list2

        # Return the merged list (skip dummy node)
        return list3.next
```

---

## ⏱️ Complexity Analysis

* **Time Complexity:** `O(n + m)`

  * We traverse both lists once

* **Space Complexity:** `O(1)`

  * No extra space is used (in-place merge)

---

## 🧪 Example

```id="ex1"
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

### Explanation:

```id="exp1"
Compare 1 and 1 → take from list2
Compare 1 and 3 → take from list1
Compare 2 and 3 → take from list1
Compare 4 and 3 → take from list2
Compare 4 and 4 → take from list2
Append remaining 4
```

---

```id="ex2"
Input: list1 = [], list2 = []
Output: []
```

---

```id="ex3"
Input: list1 = [], list2 = [0]
Output: [0]
```

---

## 📌 Key Takeaways

* Dummy nodes simplify linked list problems significantly
* Always move the pointer after attaching a node
* `list1 or list2` is a clean way to append remaining elements
* This is a classic **two-pointer technique** for linked lists 🚀
