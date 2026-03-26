# 🥪 Number of Students Unable to Eat Lunch

## 🔗 Problem Link

[LeetCode - Number of Students Unable to Eat Lunch](https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/)

---

## 📘 Problem Description

You are given two arrays:

* `students` → represents student preferences (`0` = circular sandwich, `1` = square sandwich)
* `sandwiches` → represents sandwiches in a stack (top is first element)

### Rules:

1. Students stand in a queue
2. If the front student prefers the top sandwich, they take it and leave
3. Otherwise, they go to the end of the queue
4. Process continues until no student wants the top sandwich

### Goal:

Return the **number of students unable to eat**

---

## 💡 Approach / Intuition

Instead of simulating the queue rotation (which can be inefficient), we can use a **greedy counting approach**.

### Key Insight:

* The **order of students does not matter**
* Only the **count of preferences** matters

### Strategy:

* Count how many students prefer each type (`0` and `1`)
* Iterate through the sandwiches:

  * If a sandwich type is still preferred by some student → serve it
  * Otherwise → stop immediately (remaining students can't eat)

This works because once no student wants the current sandwich, the system gets stuck.

---

## ⚙️ Algorithm

1. Initialize `res = len(students)`
2. Create a frequency map using `Counter(students)`
3. Iterate through each sandwich `s`:

   * If `hashmap[s] > 0`:

     * Decrement count
     * Decrease `res`
   * Else:

     * Return `res` (no student wants this sandwich)
4. Return `res`

---

## 🧠 Code

```python id="k9x2lm"
from collections import Counter
from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        hashmap = Counter(students)

        for s in sandwiches:
            if hashmap[s] > 0:
                hashmap[s] -= 1
                res -= 1
            else:
                return res

        return res
```

---

## ⏱️ Complexity Analysis

* **Time Complexity:** `O(n)`

  * Single pass through sandwiches
  * Counter creation is `O(n)`

* **Space Complexity:** `O(1)`

  * Only storing counts for `0` and `1`

---

## 🧪 Example

```id="x7y8z9"
Input:
students = [1,1,0,0]
sandwiches = [0,1,0,1]

Output:
0
```

---

## 📌 Key Takeaways

* You don’t always need to simulate — **counting can replace queue behavior**
* Recognizing when **order doesn’t matter** is powerful
* Greedy + frequency counting often simplifies problems
* Early stopping condition is critical for efficiency 🚀

---

If you want, I can also:

* Add **diagrams**
* Show the **brute force simulation approach**
* Or convert this into a **Notion / GitHub-ready template**