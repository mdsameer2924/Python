# Classes and object

Classes are blueprint or template of an object which contain `attributes` and `method`

## Components of a Class

1. Constructor's function
2. attributes
3. methods
4. Dunder (magic method)
5. Self ➡ reference variable

## Syntax Of Making Class

**Syntax ⤵**

```python
class ClassName: # classname must be in pascal case 
    attributes_name="value" # this is not vairable this is attributes inside class
    method_name(self):
        print("this is an method")
```

**Example ⤵**

```python
class Book:
    title="Rich dad poor pad"
    price=299
    def display_info(self):
        print(f"bookName: {self.title} Price: {self.price}")

```

## Object

it is an instance of an Class which created as a real world entity

### Syntax of making object

**Syntax ⤵**

```python
object_name=ClassName() # now object is created
object_name.attributes_name # to access attributes
object_name.method_name() # to access methods
```

**Code Example ⤵**

```python
obj=Book() ## Object created 
print(obj.title) ## access class's attributes
obj.display_info() ## access class's methods 
```

> [!CAUTION]
>
> - attributes use  `obj.attri_name`
> - method usage required parenthesis `obj.method_name()`
