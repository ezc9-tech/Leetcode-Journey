# 🧩 Concatenation of Array

## 🔗 Problem Link

[LeetCode - Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/)

---

## 📘 Problem Description

Given an integer array `nums` of length `n`, return an array `ans` of length `2n` where:

* `ans[i] == nums[i]` for `0 <= i < n`
* `ans[i + n] == nums[i]` for `0 <= i < n`

In simple terms, the result is the original array **concatenated with itself**.

---

## 💡 Approach / Intuition

This problem is very straightforward: we just need to duplicate the array and append it to itself.

### Key ideas:

* We want the same sequence of elements repeated twice
* Python makes this easy using **list unpacking (`*`)**
* Alternatively, you could also use `nums + nums`

---

## ⚙️ Algorithm

1. Take the input array `nums`
2. Concatenate it with itself
3. Return the resulting array

---

## 🧠 Code

```python id="g7k2q9"
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Return a new list that contains nums twice
        return [*nums, *nums]
```

---

## ⏱️ Complexity Analysis

* **Time Complexity:** `O(n)`

  * We copy all elements once to create the new array of size `2n`

* **Space Complexity:** `O(n)`

  * A new array of size `2n` is created

---

## 🧪 Example

```id="ex1"
Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
```

```id="ex2"
Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
```

---

## 📌 Key Takeaways

* Python’s `*` operator allows **clean list concatenation**
* This is a simple example of array manipulation
* Always look for built-in operations that simplify code
