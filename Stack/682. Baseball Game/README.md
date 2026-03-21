---

# 🧩 Baseball Game

## 🔗 Problem Link

[LeetCode - Baseball Game](https://leetcode.com/problems/baseball-game/)

---

## 📘 Problem Description

You are keeping track of scores for a baseball game with strange rules.

Given a list of strings `operations`, each operation represents a score record:

* An integer → Record a new score
* `"+"` → Record a score that is the **sum of the previous two scores**
* `"D"` → Record a score that is **double the previous score**
* `"C"` → Invalidate the previous score (remove it)

Return the **sum of all valid scores**.

---

## 💡 Approach / Intuition

This problem is best handled using a **stack**, since we need to frequently access and modify the most recent scores.

### Key ideas:

* Use a stack to store valid scores
* `"+"` → Add the last two scores
* `"D"` → Double the last score
* `"C"` → Remove the last score
* Numbers → Convert to integer and push to stack
* Final answer is the sum of the stack

---

## ⚙️ Algorithm

1. Initialize an empty stack `scores`
2. Iterate through each operation in `operations`:

   * If `"+"`:

     * Append sum of last two elements
   * If `"C"`:

     * Pop the last element
   * If `"D"`:

     * Append double the last element
   * Else:

     * Convert to integer and append
3. Return the sum of the stack

---

## 🧠 Code

```python id="n5t8qp"
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # We need a stack to keep track of the scores
        scores = []
        
        # For every operation
        for oper in operations:
            # If it is a + then remove two scores from the stack and add them
            # Then add the result of the sum of the two to the stack
            if oper == "+":
                scores.append(scores[-1] + scores[-2])
            # If it is a C then remove the score from the stack
            elif oper == "C":
                scores.pop()
            # If it is a D then double the last score and append them to the stack
            elif oper == "D":
                scores.append(scores[-1] * 2)
            # Else add an int conversion of the oper to the stack
            else:
                scores.append(int(oper))
        # Return the sum of all the scores to get the total and return it
        return sum(scores)
```

---

## ⏱️ Complexity Analysis

* **Time Complexity:** `O(n)`

  * We iterate through the operations once

* **Space Complexity:** `O(n)`

  * The stack stores all valid scores

---

## 🧪 Example

```id="r2m8kx"
Input: operations = ["5","2","C","D","+"]
Output: 30
```

```id="u9q4zs"
Input: operations = ["5","-2","4","C","D","9","+","+"]
Output: 27
```

---

## 📌 Key Takeaways

* Stacks are ideal for **tracking recent operations**
* Always ensure the stack has enough elements before accessing (`+`, `D`)
* Problems involving “undo” or “last actions” often use stacks

---
