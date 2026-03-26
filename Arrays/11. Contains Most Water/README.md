# 🧩 Container With Most Water

## 🔗 Problem Link

[LeetCode - Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

---

## 📘 Problem Description

Given an integer array `height` of length `n`, where each element represents a vertical line on a chart, find two lines that together with the x-axis form a container that holds the **most water**.

Return the **maximum amount of water** a container can store.

---

## 💡 Approach / Intuition

A brute-force approach would check every pair of lines, resulting in `O(n²)` time complexity.

Instead, we can use the **two-pointer technique** to optimize the solution.

### Key ideas:

* Start with two pointers at both ends of the array
* The area is determined by:

  * The **shorter height** between the two lines
  * The **distance** between them
* Move the pointer pointing to the **shorter line**, since:

  * Moving the taller line won’t increase the area
  * Only moving the shorter line gives a chance for a larger area

---

## ⚙️ Algorithm

1. Initialize two pointers:

   * `l = 0`
   * `r = len(height) - 1`
2. Initialize `maxArea = 0`
3. While `l < r`:

   * Calculate area:

     ```
     area = (r - l) * min(height[l], height[r])
     ```
   * Update `maxArea`
   * If `height[l] < height[r]`:

     * Move left pointer (`l++`)
   * Else:

     * Move right pointer (`r--`)
4. Return `maxArea`

---

## 🧠 Code

```python id="t9k2x1"
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Look at both ends of the array
        l, r = 0, len(heights) - 1
        
        # Keep track of the max area
        maxArea = 0

        # You can stop once l and r meet
        while l < r:
            # Calculate the area
            area = (r - l) * min(heights[l], heights[r])
            
            # Update max area if needed
            maxArea = max(area, maxArea)
            
            # Move the pointer pointing to the smaller height
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        # Return the max area
        return maxArea
```

---

## ⏱️ Complexity Analysis

* **Time Complexity:** `O(n)`

  * Each pointer moves at most `n` times

* **Space Complexity:** `O(1)`

  * No extra space is used

---

## 🧪 Example

```id="ex1"
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
```

```id="ex2"
Input: height = [1,1]
Output: 1
```

---

## 📌 Key Takeaways

* Two-pointer technique can drastically reduce complexity from `O(n²)` → `O(n)`
* Always consider how **moving pointers affects the result**
* The limiting factor is the **shorter height**, not the taller one
* Greedy decisions (moving the smaller height) lead to the optimal solution