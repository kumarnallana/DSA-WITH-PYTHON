# 🚀 DSA with Python

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![DSA Practice](https://img.shields.io/badge/DSA-LeetCode%20%7C%20Patterns-orange.svg)](#)
[![Code Style](https://img.shields.io/badge/Code%20Style-PEP8-green.svg)](https://peps.python.org/pep-0008/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-Yes-brightgreen.svg)](#)

A structured and curated repository of **Data Structures and Algorithms (DSA)** implemented in Python. This repository focuses on pattern-based problem solving, optimal time and space complexity, and clean, type-hinted code suitable for technical interviews and competitive programming.

---

## 📂 Repository Structure

```text
DSA_WTH_PYTHON/
│
├── basic_level/               # Fundamental problem solutions & LeetCode problems
│   ├── 26-Remove-Duplicates.py
│   ├── 27-Remove-Element.PY
│   ├── 80-Remove-Duplicates-II.py
│   ├── 387_frst_unique_char.py
│   ├── 643-Max-Avg-SubArr.py
│   ├── container_wth_water.py
│   ├── longest_subString.py
│   ├── Valid_Palindrome.py
│   └── ...
│
├── basic_patterns/            # Reusable algorithmic building blocks
│   ├── fixed_sliding_window.py
│   ├── frst_non_repeating_num.py
│   ├── second_largest.py
│   └── unique_val_count.py
│
├── python/                    # Core DSA design patterns & paradigms
│   ├── two_pointers.py
│   ├── fast_and_slow_pointers.py
│   ├── sliding_window.py
│   ├── kadane_algorithm.py
│   ├── monotonic_stack.py
│   ├── top_k_elements.py
│   ├── level_order_traversal.py
│   └── reverse_list.py
│
├── outlier_pratice_section/   # Targeted interview exercises & mock assessments
│   ├── return_largest_even.py
│   ├── return_frst_repeating.py
│   ├── particular_char_count.py
│   ├── char_greather_than.py
│   └── stack.py
│
└── intermediate_level/        # Complex data structures, trees, and graphs (In Progress)
```

---

## 🧠 Patterns & Techniques Covered

| Pattern / Paradigm | Description | Key Problems / Files |
| :--- | :--- | :--- |
| **Two Pointers** | Opposite and same-direction pointer techniques for sorted arrays & palindromes | `container_wth_water.py`, `two_pointers.py`, `Valid_Palindrome.py` |
| **Sliding Window** | Fixed & dynamic window techniques for subarray/substring optimization | `fixed_sliding_window.py`, `643-Max-Avg-SubArr.py`, `longest_subString.py` |
| **Fast & Slow Pointers** | Cycle detection and midpoint identification | `fast_and_slow_pointers.py` |
| **Kadane's Algorithm** | Dynamic programming approach for maximum subarray sum in $O(N)$ time | `kadane_algorithm.py` |
| **Monotonic Stack** | Efficiently finding next/previous greater or smaller elements in $O(N)$ | `monotonic_stack.py`, `stack.py` |
| **Frequency Hashing** | Constant time $O(1)$ lookups for counting, unique elements, and duplicates | `387_frst_unique_char.py`, `unique_val_count.py` |
| **Binary Search** | Logarithmic time search across sorted spaces | `sqaure_root.py` |
| **BFS / Level Order** | Queue-based tree and graph traversal | `level_order_traversal.py` |

---

## 🛠️ Code Conventions & Highlights

- **Python Type Hints**: Explicit function signatures (`def func(nums: list[int]) -> int:`) for readability and type safety.
- **In-Place Optimizations**: Focus on achieving $O(1)$ auxiliary space where applicable (e.g., in-place array manipulation).
- **Edge Case Coverage**: Solutions account for empty inputs, negative numbers, single-element collections, and duplicates.

---

## 💻 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/kumarnallana/DSA-WITH-PYTHON.git
cd DSA-WITH-PYTHON
```

### 2. Run any script
All files are standalone and can be executed directly with Python 3:
```bash
python basic_level/frst_non_repeating_char.py
python python/kadane_algorithm.py
python outlier_pratice_section/return_largest_even.py
```

---

## 📌 Roadmap

- [x] Basic Array & String Two Pointers
- [x] Sliding Window Fundamentals
- [x] Monotonic Stack & Kadane's Algorithm
- [ ] Linked Lists & Advanced Pointer Patterns
- [ ] Binary Trees & Binary Search Trees (BST)
- [ ] Graphs (DFS / BFS / Topological Sort)
- [ ] Dynamic Programming (1D & 2D)

---

## 👤 Author

- **Sasi Kumar Nallana**
- GitHub: [@kumarnallana](https://github.com/kumarnallana)
