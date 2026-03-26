# 🧩 Replace Elements with Greatest Element on Right Side

## 🔗 Problem Link

[LeetCode - Replace Elements with Greatest Element on Right Side](https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/)

---

## 📘 Problem Description

Given an array `arr`, replace every element in that array with the **greatest element among the elements to its right**, and replace the last element with `-1`.

Return the modified array.

---

## 💡 Approach / Intuition

A brute-force approach would check every element’s right side repeatedly, leading to an inefficient `O(n²)` solution.

Instead, we can optimize by traversing the array **from right to left**.

### Key ideas:

* Keep track of the **maximum value seen so far from the right**
* At each index:

  * Replace the current value with the stored `rightMax`
  * Update `rightMax` if the current element is larger
* Initialize `rightMax` as `-1` since the last element has no elements to its right

This works because when moving backward, we always know the maximum of everything to the right.

---

## ⚙️ Algorithm

1. Get the length of the array `n`
2. Initialize a result array `ans` of size `n`
3. Set `rightMax = -1`
4. Traverse the array from right to left:

   * Set `ans[i] = rightMax`
   * Update `rightMax = max(arr[i], rightMax)`
5. Return `ans`

---

## 🧠 Code

```python id="t9k2x1"
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Grab the number of numbers in the array
        n = len(arr)
        
        # Create a pre-allocated list for each number
        ans = [0] * n
        
        # Create a variable for the right max
        rightMax = -1

        # Look at every index of the array backwards
        for i in range(n-1, -1 , -1):
            # Set the answer array index equal to the rightMax
            ans[i] = rightMax
            
            # Update rightMax to be the max between current element and itself
            rightMax = max(arr[i], rightMax)
        
        # Return the answer
        return ans
```

---

## ⏱️ Complexity Analysis

* **Time Complexity:** `O(n)`

  * We traverse the array once

* **Space Complexity:** `O(n)`

  * We use an additional array `ans`

👉 Note: This can be optimized to `O(1)` extra space by modifying the input array in-place.

---

## 🧪 Example

```id="ex1"
Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
```

```id="ex2"
Input: arr = [400]
Output: [-1]
```

---

## 📌 Key Takeaways

* Traversing **backwards** can eliminate repeated work
* Keeping a running **maximum** is a powerful optimization pattern
* This transforms a potential `O(n²)` problem into `O(n)`
* In-place optimization is possible for better space efficiency