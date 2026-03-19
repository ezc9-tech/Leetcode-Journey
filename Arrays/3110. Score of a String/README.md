# 🧩 Score of a String

## 🔗 Problem Link

[LeetCode - Score of a String](https://leetcode.com/problems/score-of-a-string/)

---

## 📘 Problem Description

Given a string `s`, return the **sum of the absolute differences** between the ASCII values of adjacent characters.

In other words, for each pair of neighboring characters in the string, compute:

```
abs(ord(s[i]) - ord(s[i+1]))
```

Then sum up all the results.

---

## 💡 Approach / Intuition

To calculate the score, we need to compare each character with the one right after it.

### Key ideas:

* Use the `ord()` function to convert characters into their ASCII values
* Iterate through the string while comparing **adjacent characters**
* Keep a running total of the absolute differences

A **two-pointer approach** works nicely here:

* Left pointer (`l`) tracks the previous character
* Right pointer iterates through the rest of the string

---

## ⚙️ Algorithm

1. Initialize a pointer `l = 0`
2. Initialize `total = 0`
3. Loop through the string starting from index `1`:

   * For each character, compute:

     ```
     abs(ord(s[l]) - ord(current_char))
     ```
   * Add the result to `total`
   * Increment `l`
4. Return `total`

---

## 🧠 Code

```python id="s1c9k3"
class Solution:
    def scoreOfString(self, s: str) -> int:
        # Use a left pointer to track the previous character
        l = 0

        # Keep track of total score
        total = 0
        
        # Iterate through string starting from second character
        for char in s[1:]:
            # Add absolute difference of ASCII values
            total += abs(ord(s[l]) - ord(char))
            
            # Move left pointer forward
            l += 1
        
        return total
```

---

## ⏱️ Complexity Analysis

* **Time Complexity:** `O(n)`

  * We iterate through the string once

* **Space Complexity:** `O(1)`

  * No extra space is used beyond a few variables

---

## 🧪 Example

```id="ex1"
Input: s = "hello"
Output: 13
```

### Explanation:

```
| 'h' - 'e' | = |104 - 101| = 3
| 'e' - 'l' | = |101 - 108| = 7
| 'l' - 'l' | = |108 - 108| = 0
| 'l' - 'o' | = |108 - 111| = 3

Total = 3 + 7 + 0 + 3 = 13
```

```id="ex2"
Input: s = "zaz"
Output: 50
```

---

## 📌 Key Takeaways

* `ord()` is useful for converting characters to ASCII values
* Comparing **adjacent elements** is a common pattern
* Two-pointer techniques can simplify sequential comparisons
