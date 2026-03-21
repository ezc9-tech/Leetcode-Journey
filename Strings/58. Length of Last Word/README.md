# 🧩 Length of Last Word

## 🔗 Problem Link

[LeetCode - Length of Last Word](https://leetcode.com/problems/length-of-last-word/)

---

## 📘 Problem Description

Given a string `s` consisting of words and spaces, return the **length of the last word** in the string.

A word is defined as a maximal substring consisting of **non-space characters only**.

---

## 💡 Approach / Intuition

To find the length of the last word, we need to **ignore trailing spaces** and then isolate the final word.

### Key ideas:

* Use `.strip()` to remove leading and trailing spaces
* Split the string into words using spaces
* The last word will be the final element in the list
* Return the length of that word

---

## ⚙️ Algorithm

1. Remove leading and trailing spaces using `strip()`
2. Split the string into a list of words using `split(" ")`
3. Access the last word using `words[-1]`
4. Return the length of the last word

---

## 🧠 Code

```python id="k4n82p"
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # So first we need to clean up the string
        s = s.strip()
        # Then we need to split the string into a list
        words = s.split(" ")
        # Then return the length of the last word
        return len(words[-1])
```

---

## ⏱️ Complexity Analysis

* **Time Complexity:** `O(n)`

  * We traverse the string during strip and split operations

* **Space Complexity:** `O(n)`

  * We store the split words in a list

---

## 🧪 Example

```id="b1x9qp"
Input: s = "Hello World"
Output: 5
```

```id="m7k2zs"
Input: s = "   fly me   to   the moon  "
Output: 4
```

---

## 📌 Key Takeaways

* String preprocessing (like `strip`) is crucial for clean input handling
* Splitting strings is a simple way to isolate words
* Always consider edge cases like trailing spaces

---
