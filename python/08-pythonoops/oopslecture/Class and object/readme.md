# Classes and Objects

Classes are blueprints or templates for an object, containing `attributes` and `methods`.

## Components of a Class

1. Constructor function
2. Attributes
3. Methods
4. Dunder (magic) methods
5. `self` (reference variable)

## Syntax of Making a Class

In Python, a class is defined using the `class` keyword.
By convention, class names should be in PascalCase.

### Syntax

```python
class ClassName:
    # Class attribute (shared across instances)
    attribute_name = "value" 
    
    def method_name(self):
        print("This is a method")
```

### Example

```Python
class Book:
    title = "Rich Dad Poor Dad"
    price = 299

    def display_info(self):
        print(f"Book Name: {self.title}, Price: {self.price}")
```

## Object

An object is an instance of a class created as a real-world entity.

Syntax of Making an Object

```Python
object_name = ClassName()      # Object creation
object_name.attribute_name   # Accessing attributes
object_name.method_name()    # Calling methods
Code Example
Python
obj = Book()                   # Object created
print(obj.title)             # Accessing class attributes
obj.display_info()           # Accessing class methods
```

> [!CAUTION]
Attributes are accessed using dot notation without parentheses: obj.attri_name
Method calls require parentheses:  `obj.method_name()`
