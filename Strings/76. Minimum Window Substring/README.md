# 🧩 Minimum Window Substring

## 🔗 Problem Link

[LeetCode - Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)

---

## 📘 Problem Description

Given two strings `s` and `t`, return the **smallest substring of `s`** such that every character in `t` (including duplicates) is included in the window.

If there is no such substring, return an empty string `""`.

---

## 💡 Approach / Intuition

This is a classic **sliding window** problem.

We want to find the **smallest window in `s`** that contains all characters from `t`.

### Key ideas:

* Use a hashmap (`countT`) to store the frequency of characters in `t`
* Use another hashmap (`window`) to track the current window in `s`
* Track:

  * `have`: how many characters currently match required frequency
  * `need`: total unique characters required
* Expand the window using a right pointer (`r`)
* Once all requirements are met (`have == need`), try shrinking from the left (`l`) to minimize the window

---

## ⚙️ Algorithm

1. If `t` is empty, return `""`
2. Build a frequency map `countT` for string `t`
3. Initialize:

   * `window` hashmap
   * `have = 0`, `need = len(countT)`
   * result pointers `res = [-1, -1]`
   * `resLen = infinity`
4. Use two pointers:

   * `l = 0`
   * Iterate `r` through `s`
5. Add `s[r]` to the window
6. If a character meets its required frequency, increment `have`
7. While `have == need`:

   * Update result if current window is smaller
   * Remove `s[l]` from window
   * If requirement breaks, decrement `have`
   * Move `l` forward
8. Return the smallest valid substring

---

## 🧠 Code

```python id="mw1n9k"
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # If t is empty, return empty string
        if t == "":
            return ""
        
        # Keep track of required counts and current window counts
        countT, window = {}, {}

        # Build frequency map for t
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        # Track how many conditions are satisfied
        have, need = 0, len(countT)

        # Result variables
        res, resLen = [-1, -1], float("infinity")

        # Left pointer
        l = 0

        # Expand window with right pointer
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # Check if this character satisfies requirement
            if c in countT and window[c] == countT[c]:
                have += 1

            # Try to shrink window when valid
            while have == need:
                # Update result if smaller window found
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # Remove left character from window
                window[s[l]] -= 1

                # Check if window is no longer valid
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1

                # Shrink window
                l += 1
        
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""
```

---

## ⏱️ Complexity Analysis

* **Time Complexity:** `O(n + m)`

  * `n = len(s)`, `m = len(t)`
  * Each character is processed at most twice (expand + shrink)

* **Space Complexity:** `O(m)`

  * Hashmap stores frequencies of characters in `t`

---

## 🧪 Example

```id="ex1"
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
```

### Explanation:

```
Valid windows that contain A, B, C:
"ADOBEC" (length 6)
"BANC"   (length 4) ← smallest
```

---

```id="ex2"
Input: s = "a", t = "aa"
Output: ""
```

### Explanation:

```
Not enough 'a' characters in s to satisfy t
```

---

## 📌 Key Takeaways

* Sliding window is essential for substring optimization problems
* Use two hashmaps:

  * One for requirements (`countT`)
  * One for current window (`window`)
* The `have == need` condition signals a valid window
* Always try to **shrink the window** after it becomes valid
