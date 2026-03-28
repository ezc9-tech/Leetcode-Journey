# 🧩 Move Zeroes

## 🔗 Problem Link

[LeetCode - Move Zeroes](https://leetcode.com/problems/move-zeroes/)

---

## 📘 Problem Description

Given an integer array `nums`, move all `0`'s to the **end** of it while maintaining the **relative order** of the non-zero elements.

You must do this **in-place** without making a copy of the array.

---

## 💡 Approach / Intuition

This problem is best solved using the **two-pointer technique**.

### Key ideas:

* Use a pointer `l` to track the position where the next **non-zero** element should go
* Iterate through the array with another pointer `r`
* When a non-zero element is found:

  * Swap it with the element at index `l`
  * Increment `l`

This ensures:

* All non-zero elements are shifted forward
* Zeros naturally move to the end
* The relative order of non-zero elements is preserved

---

## ⚙️ Algorithm

1. Initialize pointer `l = 0`
2. Loop through the array using pointer `r`
3. For each element:

   * If `nums[r]` is not `0`:

     * Swap `nums[l]` and `nums[r]`
     * Increment `l`
4. Continue until the end of the array

---

## 🧠 Code

```python id="m0v3z"
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Keep track of where the next non-zero should go
        l = 0

        # Traverse the array
        for r in range(len(nums)):
            # If current element is non-zero
            if nums[r] != 0:
                # Swap with the left pointer
                nums[l], nums[r] = nums[r], nums[l]
                # Move left pointer forward
                l += 1
```

---

## ⏱️ Complexity Analysis

* **Time Complexity:** `O(n)`

  * Single pass through the array

* **Space Complexity:** `O(1)`

  * In-place modification, no extra space used

---

## 🧪 Example

```id="ex1"
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
```

```id="ex2"
Input: nums = [0]
Output: [0]
```

---

## 📌 Key Takeaways

* The **two-pointer technique** is perfect for in-place array rearrangement
* Swapping avoids unnecessary shifts or extra space
* This approach maintains **relative ordering**, which is often a key constraint
* Efficient solution with **O(n)** time and **O(1)** space
