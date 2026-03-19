# 🧩 Top K Frequent Elements

## 🔗 Problem Link

[LeetCode - Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)

---

## 📘 Problem Description

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements.

You may return the answer in **any order**.

---

## 💡 Approach / Intuition

To solve this problem, we need to identify which elements appear most frequently in the array.

### Key ideas:

* Use a **hash map (dictionary)** to count how many times each number appears
* Sort the elements based on their frequency in **descending order**
* Extract the top `k` elements from the sorted result

This approach works well because it separates the problem into two clear steps:

1. Counting frequencies
2. Ranking elements by frequency

---

## ⚙️ Algorithm

1. Initialize an empty hashmap
2. Iterate through `nums`:

   * Count occurrences of each number
3. Sort the hashmap items based on frequency (value) in descending order
4. Extract only the keys (numbers) from the sorted list
5. Return the first `k` elements

---

## 🧠 Code

```python id="t9k2x1"
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # We will want the occurrences of each num which calls for a hashmap
        hashmap = {}
        
        # Loop through and count occurrences
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1

        # Sort keys based on frequency in descending order
        most_occured = [
            key for key, value in sorted(
                hashmap.items(),
                key=lambda item: item[1],
                reverse=True
            )
        ]
        
        # Return top k elements
        return most_occured[0:k]
```

---

## ⏱️ Complexity Analysis

* **Time Complexity:** `O(n log n)`

  * Counting frequencies: `O(n)`
  * Sorting: `O(n log n)`

* **Space Complexity:** `O(n)`

  * Hashmap stores up to `n` unique elements

---

## 🧪 Example

```id="ex1"
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

```id="ex2"
Input: nums = [1], k = 1
Output: [1]
```

---

## 📌 Key Takeaways

* Frequency counting is a common use case for **hash maps**
* Sorting helps rank elements by importance (frequency here)
* This solution is simple and readable, though not the most optimal

👉 Note: A more optimal solution using **heap or bucket sort** can achieve `O(n)` time complexity.
