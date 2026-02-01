## 0001 - Two Sum

Given an array of integers and a target, find the indices of two numbers that add up to the target.

---

### Approach 1 (Optimal): Hash Map
Use a single pass with a hash map to track seen numbers. For each number, check if its complement (target - num) exists in the map. If it does, we found our pair. If not, add the current number to the map.

**Key insight**: Instead of checking all pairs (O(n²)), we trade space for time by storing previously seen numbers in a hash map.

### Approach 2: Brute Force
Check every pair of numbers to see if they add up to the target. For each element, iterate through all remaining elements and check if their sum equals the target.

**Drawback**: O(n²) time complexity, but uses O(1) space.

---

## Complexity

| Approach | Time | Space |
|----------|------|-------|
| Hash Map | O(n) | O(n) |
| Brute Force | O(n²) | O(1) |
