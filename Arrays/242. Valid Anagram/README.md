# 🧩 Valid Anagram

## 🔗 Problem Link

[LeetCode - Valid Anagram](https://leetcode.com/problems/valid-anagram/)

---

## 📘 Problem Description

Given two strings `s` and `t`, return `true` if `t` is an **anagram** of `s`, and `false` otherwise.

An anagram is a word or phrase formed by rearranging the letters of another, using all original letters exactly once.

---

## 💡 Approach / Intuition

To determine if two strings are anagrams, we need to check if they contain the **same characters with the same frequencies**.

### Key ideas:

* If the strings have different lengths → they cannot be anagrams
* Use **hash maps (dictionaries)** to count character frequencies
* Compare the frequency maps of both strings

If both maps are identical, the strings are anagrams.

---

## ⚙️ Algorithm

1. Check if lengths of `s` and `t` are equal

   * If not, return `False`
2. Create a hashmap for string `s` to count character occurrences
3. Create a hashmap for string `t`
4. Compare both hashmaps

   * If equal → return `True`
   * Else → return `False`

---

## 🧠 Code

```python id="p8x4sk"
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths differ, cannot be anagrams
        if len(s) != len(t):
            return False
        
        # Count characters in s
        s_hashmap = {}
        for char in s:
            if char not in s_hashmap:
                s_hashmap[char] = 1
            else:
                s_hashmap[char] += 1

        # Count characters in t
        t_hashmap = {}
        for char in t:
            if char not in t_hashmap:
                t_hashmap[char] = 1
            else:
                t_hashmap[char] += 1

        # Compare both maps
        return s_hashmap == t_hashmap
```

---

## ⏱️ Complexity Analysis

* **Time Complexity:** `O(n)`

  * We traverse both strings once

* **Space Complexity:** `O(n)`

  * We store character counts in hashmaps

---

## 🧪 Example

```id="a2k91d"
Input: s = "anagram", t = "nagaram"
Output: true
```

```id="z7m3qp"
Input: s = "rat", t = "car"
Output: false
```

---

## 📌 Key Takeaways

* Hash maps are useful for **frequency counting problems**
* Always check simple edge cases first (like length mismatch)
* Comparing two frequency maps is a clean and reliable approach

---
