# 🧩 Crawler Log Folder

## 🔗 Problem Link

[LeetCode - Crawler Log Folder](https://leetcode.com/problems/crawler-log-folder/)

---

## 📘 Problem Description

The file system logs operations whenever a user navigates between folders.

Each operation is represented as a string:

* `"../"` → Move to the parent folder (if possible)
* `"./"` → Stay in the current folder
* `"x/"` → Move into a child folder named `x`

Given an array `logs`, return the **minimum number of steps needed to go back to the root folder**.

---

## 💡 Approach / Intuition

We can simulate folder navigation using a **stack** to track the current depth.

### Key ideas:

* Each folder we enter increases depth → push onto stack
* `"../"` moves up one level → pop from stack (if not empty)
* `"./"` does nothing
* The final stack size represents how far we are from the root

---

## ⚙️ Algorithm

1. Initialize an empty stack
2. Loop through each log in `logs`:

   * If `"../"`:

     * Pop from the stack if it's not empty
   * Else if `"./"`:

     * Do nothing
   * Else:

     * Push the folder name onto the stack
3. Return the size of the stack

---

## 🧠 Code

```python
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

  * In the worst case, all logs are stored in the stack

---

## 🧪 Example

```
Input: logs = ["d1/","d2/","../","d21/","./"]
Output: 2
```

```
Input: logs = ["d1/","../","../","../"]
Output: 0
```

---

## 📌 Key Takeaways

* Stacks are ideal for **tracking directory depth**
* Always check before popping to avoid errors
* Simulation problems are often easiest when modeled step-by-step
