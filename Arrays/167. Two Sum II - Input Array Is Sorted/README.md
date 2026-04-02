# 🧩 Two Sum II - Input Array Is Sorted

## 🔗 Problem Link

[LeetCode - Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

---

## 📘 Problem Description

Given a **1-indexed sorted array** of integers `numbers`, find two numbers such that they add up to a specific `target`.

Return the indices of the two numbers **(1-indexed)** as a list `[index1, index2]`.

You may assume:

* There is **exactly one solution**
* You **may not use the same element twice**
* The array is sorted in **non-decreasing order**

---

## 💡 Approach / Intuition

Because the array is already **sorted**, we can use the **two-pointer pattern**.

### Why this works:

* Start one pointer at the **left**
* Start another at the **right**
* Check the sum of both values
* If the sum is too small → move the left pointer right
* If the sum is too large → move the right pointer left
* If the sum matches the target → return the indices

This works because sorting gives us predictable movement:

* Moving left pointer right **increases** the sum
* Moving right pointer left **decreases** the sum

This lets us solve the problem in **one pass**.

---

## ⚙️ Algorithm

1. Initialize two pointers:

   * `l = 0`
   * `r = len(numbers) - 1`
2. While `l < r`
3. Calculate the sum of `numbers[l] + numbers[r]`
4. Compare the sum to `target`

   * If sum < target → move `l` right
   * If sum > target → move `r` left
   * Otherwise return `[l + 1, r + 1]`
5. Return the indices once found

---

## 🧠 Code

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Use two pointers since array is sorted
        l = 0
        r = len(numbers) - 1

        while l < r:
            current_sum = numbers[l] + numbers[r]

            if current_sum < target:
                l += 1
            elif current_sum > target:
                r -= 1
            else:
                return [l + 1, r + 1]
```

---

## ⏱️ Complexity Analysis

* **Time Complexity:** `O(n)`

  * Each pointer moves at most once across the array

* **Space Complexity:** `O(1)`

  * Only two pointers are used

---

## 🧪 Example

```text
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
```

### Walkthrough

* `2 + 15 = 17` → too large → move right pointer
* `2 + 11 = 13` → too large → move right pointer
* `2 + 7 = 9` → found answer

Return:

```text
[1,2]
```

---

## 📌 Key Takeaways

* Since the array is **sorted**, use the **two-pointer pattern**
* Left pointer increases the sum
* Right pointer decreases the sum
* This avoids the `O(n²)` brute-force solution
* A classic interview problem for recognizing **sorted array patterns**