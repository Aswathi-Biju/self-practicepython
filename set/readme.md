# Introduction to Sets in Python

## What is a Set?
A **set** is a built-in data type in Python used to store multiple unique elements in an **unordered** collection. Sets are mutable (modifiable), but the elements within them must be immutable (e.g., numbers, strings, tuples).

---

## Characteristics of Sets
1. **Unordered**: Sets do not maintain the order of elements.
2. **No Duplicates**: Sets automatically remove duplicate elements.
3. **Mutable**: Sets can be modified after creation (elements can be added or removed).
4. **Heterogeneous**: Sets can contain elements of different data types (e.g., integers, strings, tuples).

---

## Syntax
Sets are defined using curly braces `{}` or the `set()` constructor.

### Example:
```python
# Creating sets
my_set = {1, 2, 3, 4}
empty_set = set()  # Note: {} creates a dictionary, not a set
mixed_set = {1, "Python", 3.14}

# Using the set() constructor
constructed_set = set([4, 5, 6])
