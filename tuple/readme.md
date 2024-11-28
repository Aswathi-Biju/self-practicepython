# Introduction to Tuples in Python

## What is a Tuple?
A **tuple** is a built-in data type in Python used to store multiple items in a single variable. Tuples are similar to lists but with one key difference: **tuples are immutable** (cannot be changed after creation).

---

## Characteristics of Tuples
1. **Ordered**: Tuples maintain the order of elements.
2. **Immutable**: Once created, elements in a tuple cannot be added, removed, or modified.
3. **Allow Duplicates**: Tuples can contain duplicate elements.
4. **Heterogeneous**: Tuples can store elements of different data types (e.g., integers, strings, floats).

---

## Syntax
Tuples are defined using parentheses `()` or the `tuple()` constructor.

### Example:
```python
# Creating tuples
my_tuple = (1, 2, 3)
empty_tuple = ()
mixed_tuple = (1, "Hello", 3.14)

# Using the tuple() constructor
constructed_tuple = tuple([4, 5, 6])
