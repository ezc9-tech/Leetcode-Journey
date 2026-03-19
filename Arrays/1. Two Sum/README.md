# 🧩 Two Sum

## 🔗 Problem Link

[LeetCode - Two Sum](https://leetcode.com/problems/two-sum/)

---

## 📘 Problem Description

Given an array of integers `nums` and an integer `target`, return the **indices** of the two numbers such that they add up to the target.

* Each input has exactly one solution
* You may not use the same element twice
* You can return the answer in any order

---

## 💡 Approach / Intuition

A brute-force approach would check all pairs → `O(n²)`, which is inefficient.

Instead, we can use a **hash map** to optimize:

* Store each number and its index as we iterate

* For each number, calculate its **complement**:

  ```
  complement = target - num
  ```

* If the complement already exists in the hashmap:

  * We’ve found the two numbers → return their indices

This allows us to solve the problem in **one pass**.

---

## ⚙️ Algorithm

1. Initialize an empty hashmap
2. Loop through the array using `enumerate`
3. For each element:

   * Compute `target - num`
   * If it exists in the hashmap:

     * Return `[previous_index, current_index]`
   * Otherwise, store `num → index` in the hashmap
4. Return the result

---

## 🧠 Code

```python id="x9c2la"
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for index, num in enumerate(nums):
            if target - num in hashmap:
                return [hashmap[target - num], index]
            
            hashmap[num] = index
```

---

## ⏱️ Complexity Analysis

* **Time Complexity:** `O(n)`

  * We traverse the list once

* **Space Complexity:** `O(n)`

  * We store elements in a hashmap

---

## 🧪 Example

```id="l2p8dn"
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
```

```id="q7v3ks"
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

---

## 📌 Key Takeaways

* Hash maps are powerful for **lookup problems**
* Always think about trading space for time (`O(n²)` → `O(n)`)
* The “complement” pattern is very common in interview questions

---
