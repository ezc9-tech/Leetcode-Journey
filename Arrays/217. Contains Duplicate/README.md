# 🧩 Contains Duplicate

## 🔗 Problem Link

[LeetCode - Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

---

## 📘 Problem Description

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

---

## 💡 Approach / Intuition

To efficiently check for duplicates, we can use a **hash set**.

* A set only stores **unique elements**
* As we iterate through the array:

  * If the element is **not in the set**, we add it
  * If the element is **already in the set**, we’ve found a duplicate → return `True`

This allows us to detect duplicates in a single pass.

---

## ⚙️ Algorithm

1. Initialize an empty set
2. Loop through each number in the array
3. For each number:

   * If it exists in the set → return `True`
   * Otherwise, add it to the set
4. If no duplicates are found, return `False`

---

## 🧠 Code

```python id="d3k91s"
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Use a set to track seen elements
        hashset = set()
        
        for num in nums:
            if num not in hashset:
                hashset.add(num)
            else:
                return True
        
        return False
```

---

## ⏱️ Complexity Analysis

* **Time Complexity:** `O(n)`

  * We traverse the list once

* **Space Complexity:** `O(n)`

  * In the worst case, we store all elements in the set

---

## 🧪 Example

```
Input: nums = [1,2,3,1]
Output: true
```

```
Input: nums = [1,2,3,4]
Output: false
```

---

## 📌 Key Takeaways

* Sets are ideal for **duplicate detection**
* This problem is a classic example of using **hashing for optimization**
* Always consider trading space for time in interview problems

---
