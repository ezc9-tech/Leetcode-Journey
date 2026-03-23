# 🧩 Find Minimum in Rotated Sorted Array

## 🔗 Problem Link

[LeetCode - Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

---

## 📘 Problem Description

Suppose an array of **distinct integers** is sorted in ascending order and then rotated at some pivot.

For example:

```
[0,1,2,4,5,6,7] → rotated → [4,5,6,7,0,1,2]
```

Given the rotated sorted array `nums`, return the **minimum element** in the array.

You must write an algorithm that runs in **O(log n)** time.

---

## 💡 Approach / Intuition

Since the array was originally sorted, we can take advantage of **binary search**.

### Key ideas:

* The array is split into **two sorted portions**
* One side will always be properly sorted
* The **minimum value lies in the unsorted portion**
* Compare the **middle element with the rightmost element** to decide direction

### Why compare with `nums[r]`?

* If `nums[m] < nums[r]` → right side is sorted → minimum is at `m` or to the left
* If `nums[m] > nums[r]` → minimum is in the right half (excluding `m`)

---

## ⚙️ Algorithm

1. Initialize pointers:

   ```
   l = 0
   r = len(nums) - 1
   ```

2. While `l < r`:

   * Compute middle:

     ```
     m = l + (r - l) // 2
     ```

   * If `nums[m] < nums[r]`:

     * Minimum is in left half (including `m`)
     * Move `r = m`

   * Else:

     * Minimum is in right half (excluding `m`)
     * Move `l = m + 1`

3. When loop ends:

   * `l == r`, pointing to the minimum

4. Return:

   ```
   nums[l]
   ```

---

## 🧠 Code

```python id="s1c9k3"
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Initialize left and right pointers
        l = 0
        r = len(nums) - 1

        # Binary search until pointers meet
        while l < r:
            # Find middle index
            m = l + (r - l) // 2

            # If middle element is less than right,
            # the minimum is in the left half (including m)
            if nums[m] < nums[r]:
                r = m
            else:
                # Otherwise, the minimum is in the right half
                l = m + 1

        # l == r, pointing to the minimum element
        return nums[l]
```

---

## ⏱️ Complexity Analysis

* **Time Complexity:** `O(log n)`

  * Binary search halves the search space each step

* **Space Complexity:** `O(1)`

  * No extra space is used

---

## 🧪 Example

```id="ex1"
Input: nums = [3,4,5,1,2]
Output: 1
```

### Explanation:

```
Array is rotated

Left = 0, Right = 4
Mid = 2 → nums[2] = 5

5 > 2 → minimum is in right half

Eventually pointers converge at index of 1
```

---

```id="ex2"
Input: nums = [4,5,6,7,0,1,2]
Output: 0
```

---

```id="ex3"
Input: nums = [11,13,15,17]
Output: 11
```

### Explanation:

```
Array is not rotated
Minimum is the first element
```

---

## 📌 Key Takeaways

* Binary search works beyond just sorted arrays—it can be adapted for **rotated arrays**
* Comparing with the **rightmost element** helps identify the unsorted portion
* When `l == r`, you've found the answer
* Always think about which half is **guaranteed sorted** in these problems 🚀
