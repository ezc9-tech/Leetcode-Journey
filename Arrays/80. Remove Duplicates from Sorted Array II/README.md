# 🧩 Remove Duplicates from Sorted Array II

## 🔗 Problem Link

[LeetCode - Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)

---

## 📘 Problem Description

Given an integer array `nums` sorted in **non-decreasing order**, remove some duplicates **in-place** such that each unique element appears **at most twice**.

The relative order of the elements should be kept the same.

Return `k` such that the first `k` elements of `nums` contain the final result.

---

## 💡 Approach / Intuition

This problem extends the classic duplicate removal problem by allowing **up to two occurrences** of each element.

### Key ideas:

* Use a pointer `k` to track the position where the next valid element should go
* Iterate through each number in `nums`
* Allow insertion if:

  * We haven’t placed at least 2 elements yet (`k < 2`), OR
  * The current number is **not equal** to the element at `nums[k - 2]`

This works because:

* If a number appears more than twice, it will match the element two positions back
* This ensures we keep **at most two duplicates**

---

## ⚙️ Algorithm

1. Initialize `k = 0`
2. Loop through each element `num` in `nums`
3. For each element:

   * If `k < 2` OR `num != nums[k - 2]`:

     * Assign `nums[k] = num`
     * Increment `k`
4. Return `k`

---

## 🧠 Code

```python id="r3mDup2"
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Keep track of the k number of elements
        k = 0

        # Go through every element in nums
        for num in nums:
            # Allow at most 2 duplicates
            if k < 2 or num != nums[k - 2]:
                nums[k] = num
                k += 1

        return k
```

---

## ⏱️ Complexity Analysis

* **Time Complexity:** `O(n)`

  * Single pass through the array

* **Space Complexity:** `O(1)`

  * In-place modification with constant extra space

---

## 🧪 Example

```id="ex1"
Input: nums = [1,1,1,2,2,3]
Output: k = 5, nums = [1,1,2,2,3,_]
```

```id="ex2"
Input: nums = [0,0,1,1,1,1,2,3,3]
Output: k = 7, nums = [0,0,1,1,2,3,3,_,_]
```

---

## 📌 Key Takeaways

* This is a **two-pointer / overwrite pattern** problem
* Comparing with `nums[k - 2]` is the key trick to limiting duplicates
* Works because the array is **sorted**
* Efficient solution with **O(n)** time and **O(1)** space