# What are dunder

- methods are special methods in python that start and end with double underscored, like `__init__` , `__str__` , `__add__` etc
- They automatically get called when you perfom certian action on an object
- **They helps you:**
  - Customize behavior of your class
  - Make your class object behave like built-in data types (like strings,lists, etc.)

> [!TIP]
> > in python **Variables** are also actually object which means  when we store the value and perform operation trigger their dunder methods to check use

```python
print(dir(int))
```
