
# 🧩 Crawler Log Folder

## 🔗 Problem Link

[LeetCode - Crawler Log Folder](https://leetcode.com/problems/crawler-log-folder/)

---

## 📘 Problem Description

The LeetCode file system keeps logs each time a user performs a folder operation.

The operations are described as follows:

* `"../"` → Move to the parent folder (if possible)
* `"./"` → Stay in the current folder
* `"x/"` → Move into a child folder named `x`

Given a list of strings `logs`, return the **minimum number of operations needed to go back to the main folder** (root).

---

## 💡 Approach / Intuition

This problem can be solved by simulating folder navigation using a **stack**.

### Key ideas:

* Use a stack to track the current folder depth
* `"../"` → Move up one level (pop from stack if not empty)
* `"./"` → Do nothing
* `"x/"` → Move into a folder (push onto stack)
* The final depth (stack size) represents how far we are from root

---

## ⚙️ Algorithm

1. Initialize an empty stack
2. Iterate through each log in `logs`:

   * If `"../"`:

     * Pop from stack if it’s not empty
   * Else if `"./"`:

     * Do nothing
   * Else:

     * Push the folder onto the stack
3. Return the size of the stack

---

## 🧠 Code

```python id="q9v3lx"
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        # Have a stack to keep track of how deep we are in the folder structure
        stack = []

        # For each log in logs
        for log in logs:
            # If we go back into a parent folder then remove a log from the stack
            if log == "../":
                # Make sure that the stack exists
                if stack:
                    stack.pop()
            # If you remain in the same folder then don't do anything
            elif log == "./":
                pass
            # Else add on the log into the stack
            else:
                stack.append(log)
        # The length of the stack should be the amount of operations so return it
        return len(stack)
```

---

## ⏱️ Complexity Analysis

* **Time Complexity:** `O(n)`

  * We iterate through the logs once

* **Space Complexity:** `O(n)`

  * In the worst case, all logs are folder entries stored in the stack

---

## 🧪 Example

```id="x3m9rt"
Input: logs = ["d1/","d2/","../","d21/","./"]
Output: 2
```

```id="p7k4ns"
Input: logs = ["d1/","../","../","../"]
Output: 0
```

---

## 📌 Key Takeaways

* Stacks are perfect for **tracking hierarchical navigation**
* Always guard against popping from an empty stack
* Simulating the process step-by-step often leads to simple solutions

---
