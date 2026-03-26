# 🧩 Valid Palindrome (Two-Pointer Approach)

## 🔗 Problem Link

[LeetCode - Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

---

## 📘 Problem Description

Given a string `s`, determine if it is a **palindrome**, considering only **alphanumeric characters** and ignoring cases.

Return `true` if it is a palindrome, otherwise return `false`.

---

## 💡 Approach / Intuition

Instead of creating a new filtered string, we can solve this **in-place** using the **two-pointer technique**.

### Key ideas:

* Use two pointers:

  * `l` starting from the beginning
  * `r` starting from the end
* Skip any **non-alphanumeric characters**
* Compare characters (case-insensitive)
* Move pointers inward after each comparison

This avoids extra space and keeps the solution efficient.

---

## ⚙️ Algorithm

1. Initialize two pointers:

   * `l = 0`
   * `r = len(s) - 1`
2. While `l < r`:

   * Move `l` forward until it points to an alphanumeric character
   * Move `r` backward until it points to an alphanumeric character
   * Compare `s[l].lower()` and `s[r].lower()`

     * If not equal → return `False`
   * Move both pointers inward (`l++`, `r--`)
3. If all checks pass → return `True`

---

## 🧠 Code

```python id="t9k2x1"
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # We need a left and right pointer for both ends of the string
        l, r = 0, len(s) - 1

        # Because we only need to check until l meets r
        while l < r:
            # Skip non-alphanumeric characters on the left
            while l < r and not s[l].isalnum():
                l += 1

            # Skip non-alphanumeric characters on the right
            while l < r and not s[r].isalnum():
                r -= 1

            # Compare characters (case-insensitive)
            if s[l].lower() != s[r].lower():
                return False

            # Move inward
            l += 1
            r -= 1

        # If all checks passed, it's a palindrome
        return True
```

---

## ⏱️ Complexity Analysis

* **Time Complexity:** `O(n)`

  * Each character is visited at most once

* **Space Complexity:** `O(1)`

  * No extra space is used (in-place check)

---

## 🧪 Example

```id="ex1"
Input: s = "A man, a plan, a canal: Panama"
Output: true
```

```id="ex2"
Input: s = "race a car"
Output: false
```

---

## 📌 Key Takeaways

* Two-pointer technique is ideal for **string comparisons**
* Skipping invalid characters avoids preprocessing
* This approach improves space from `O(n)` → `O(1)`
* Always consider in-place solutions for optimization

