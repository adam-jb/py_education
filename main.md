

## iterators

To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.



## containers

In Python, a container object is an object that can hold other objects. Some examples of container objects include lists, tuples, sets, and dictionaries.



## bytearray vs bytes

Bytestrings can have similar methdos to strings, in strip, split, expandtabs, replace, join, partition, startswith, index, isalnum, isalpha, zfill (which adds prefix of zeroes), and more

A minority of others are specific to bytestrings: centre, and more

In Python, a bytes object is an immutable sequence of bytes, while a bytearray object is a mutable sequence of bytes. Otherwise they are the same.

```
## Making bytes and bytearray objects: note you always need to use 'b' prefix to tell it its bytes
my_bytes = b'Hello, world!'
my_bytearray = bytearray(b'Hello, world!')
```

Being immutable, bytes are faster than bytearrays

Times you might use bytearrays:
1. If you are reading binary data from a file and you need to modify the data before writing it back to the file, you might use a bytearray object to hold the data.
2. If you are working with user-generated binary data and you need to be able to modify the data based on user input, you might use a bytearray object to hold the data.





## Memoryviews

The buffer protocol is a way for Python objects to expose their memory as a contiguous block of bytes that can be accessed and modified using the memoryview class

Objects that implement the buffer protocol are required to have a __buffer__() method that returns a memoryview object that represents the object's memory as a contiguous block of bytes.

Apart from packages like numpy, looks to be for binary data

Can be used with standard library 'array' package

Memoryview uses a small amount of memory as a sort of overhead of the object itself, which is released when the memoryview is no longer used, as per release() method




## Frozenset

frozensets are sets which are immutable and hashable

```
hash(frozenset([1,2,3]))
```

Has all the set operations: isdisjoint(), issuperset(), 


```
# Test whether the set is a proper superset of other, that is, set >= other and set != other:
set > other_set


# Test whether the set is a proper sub of other, that is, set <= other and set != other.
set < other_set


# Return a new set with elements in either the set or other but not both.
symmetric_difference(set, other_set)
```




## Dictionary views

The objects returned by dict.keys(), dict.values() and dict.items() are view objects

```
#d.items() is a view: an iterator over the dict, so can change it inplace:
for k,v in d.items():
    d[k] = 2

```

A custom mapping object behaves like a mutable mapping object, such as a dictionary. And you can add extra features inc:
- Implement a mapping object that stores its data in a particular way, such as in a database or on disk
- Implement a mapping object that has specific methods or properties for working with the data, such as sorting or filtering the data
- Implement a mapping object that has additional security or error-checking features, such as data encryption or data validation
- Implement a mapping object that is optimized for a particular use case, such as a mapping object that has a faster insertion or lookup time




Q: in python, what is a singleton object?
A: an object that has only one instance

The implementation of a singleton object in Python is not thread-safe, and it may not work correctly in a multi-threaded environment. To implement a thread-safe singleton object, you will need to use additional synchronization mechanisms, such as locks or atomic variables.



The __init__() method is also known as the constructor method.


(from the exceptions docs page) Programmers are encouraged to derive new exceptions from the Exception class or one of its subclasses, and not from BaseException



 In Python, a frame is a data structure that represents an execution context. It contains information about the function being executed, the local variables in that function, and the state of the program at the point where the function was called.



```
# use try/finally to make sure cleanup 100% always happens - by putting it under try:
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')
```



"ExceptionGroup" = a custom exception class that includes multiple exception types as attributes. It is not a built-in exception type in Python, but rather a concept that you can implement in your own code.

```
# this example ExceptionGroup takes any length errors (so could treat it as a list of errors)
class ExceptionGroup(Exception):
    def __init__(self, message, *errors):
        super().__init__(message)
        self.message = message
        self.errors = errors

# to catch and view all errors
def function_that_raises_exception():
    try:
        raise ValueError("ValueError exception message.")
    except Exception as e:
        raise ExceptionGroup("ExceptionGroup message.", e)
try:
    function_that_raises_exception()
except ExceptionGroup as e:
    print(e.message)
    for error in e.errors:
        print(error)

```




## Difflib

The difflib module is generally used to compare the sequence of the strings. But we can also use it to compare other data types as long as they are hash-able

SequenceMatcher class shows how similar two strings are;

Differ class shows how much they differ

Git likely uses unified_diff class to see what would have to be dropped and added to go from first string to second





## unicodedata

Provides lookup of names to unicode characters




## textwrap

Use textwrap to make messages fit a certain number of characters

```
import textwrap
textwrap.shorten("Hello world", width=10, placeholder="...")
````



## Zoneinfo

For timezoens. Might be a daylight-savings-safe alternative to datetime

```
from zoneinfo import ZoneInfo
from datetime import datetime, timedelta

dt = datetime(2020, 10, 31, 12, tzinfo=ZoneInfo("America/Los_Angeles"))
print(dt)

dt.tzname()
```




## collections

A ChainMap class is provided for quickly linking a number of mappings so they can be treated as a single unit. It is often much faster than creating a new dictionary and running multiple update() calls.

```
from collections import ChainMap
baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
cmp = ChainMap(adjustments, baseline)
cmp.get('art')
```


Counter class is used for adding things
```
from collections import Counter

cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1
print(cnt)

# Find the ten most common words in Hamlet
import re
words = re.findall(r'\w+', open('http://www.buildingjavaprograms.com/code_files/3ed/ch06/hamlet.txt').read().lower())
Counter(words).most_common(10)
```



## __setitem__ method

Is for assigning a key/value pair to a class

```
d = {}

# Use the [] operator to set a value in the dictionary
d["key"] = "value"

# This is equivalent to calling the __setitem__ method
d.__setitem__("key", "value")
```




## ChainMap

Combines dictionaries without actually moving memory around, which dict.update() does

```
from collections import ChainMap
baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
cmp = ChainMap(adjustments, baseline)
cmp.get('art')
```




## Counter

Used for tallying things

```
from collections import Counter

cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1
print(cnt)

# Find the ten most common words in Hamlet
import re
words = re.findall(r'\w+', open('http://www.buildingjavaprograms.com/code_files/3ed/ch06/hamlet.txt').read().lower())
Counter(words).most_common(10)

```



## Deque

An approach to using deques is to maintain a sequence of recently added elements by appending to the right and popping to the left:

A round-robin scheduler can be implemented with input iterators stored in a deque. Values are yielded from the active iterator in position zero. If that iterator is exhausted, it can be removed with popleft(); otherwise, it can be cycled back to the end with the rotate() method:

```
from collections import deque
d = deque('ghi')                 # make a new deque with three items
for elem in d:                   # iterate over the deque's elements
    print(elem.upper())

d.append('j')                    # add a new entry to the right side
d.appendleft('f')                # add a new entry to the left side
print(d)

d.pop()
d.popleft()
d.extend('jkl'
d
```



## defaultdict

A defaultdict in Python is a subclass of the built-in dict class that provides a default value for keys that do not exist in the dictionary.

```
from collections import defaultdict

# Create a defaultdict with a default value of 0
d = defaultdict(int)

# Access a key that does not exist in the dictionary
print(d["key"])  # Output: 0

# Set a value for the key
d["key"] = 1
print(d["key"])  # Output: 1
```




## weakref

In Python, a weak reference is a reference to an object that does not prevent the object from being garbage collected. When the object is no longer being used elsewhere in the program, it can be garbage collected, and the weak reference will be automatically removed. Sort of like a pointer. 

```
import weakref

class MyClass:
    def __init__(self, value):
        self.value = value
        
    def multi(self):
        self.value = self.value * 2

obj = MyClass(10)
weak_ref = weakref.ref(obj)

obj = weak_ref()
print(obj.value)  # prints 10
print(obj.multi())  # prints 10
print(obj.value)  # prints 10
```

(from gpt) There are several situations where weak references can be useful in Python:

Avoiding memory leaks: When you have a reference to an object that is no longer needed, but you don't want to delete it immediately, you can use a weak reference to allow the object to be garbage collected when it is no longer needed. This can help prevent memory leaks in your program.

Caching objects: Weak references can be used to implement a cache of objects that can be discarded when memory becomes scarce. This can be useful, for example, when you want to store the results of expensive computations for later reuse, but you don't want to use up all of the available memory.

Implementing circular references: When you have two objects that reference each other, it can be difficult to determine when they are no longer needed and can be garbage collected. Using weak references can allow the objects to be garbage collected when they are no longer needed, even if they are still referenced by each other.

Implementing observer patterns (this seems useful): Weak references can be used to implement observer patterns, where one object (the observer) is notified when another object (the subject) changes. Using weak references allows the observer to be garbage collected when it is no longer needed, even if the subject is still alive.




## Enums

Feel similar to dictionaries: to store key/value pairs

```
from enum import Enum
Color = Enum('Color', ['RED', 'GREEN', 'BLUE'])
for c in Color:
    print(c.name)
    print(c.value)
list(Color)

keywords = Enum('Keys', {'delta':'red', 'alpha':'blue'})
for c in keywords:
    print(c.name)
    print(c.value)
```

Benefits to using enums in Python:

Improved readability: Enums can make your code more readable by giving names to values that might otherwise be represented by magic numbers or constants. This can make it easier to understand the meaning of the values and how they are used in the code.

Better organization: Enums can help you organize related values and keep them together in one place, making it easier to manage and maintain your code.

Type safety: Enums are a type-safe way to represent values, since they can only take on one of the predefined values. This can help prevent errors due to incorrect or invalid values being passed to your functions or methods.

Improved performance: Enums can be faster than using strings or other objects to represent values, since they are stored as integers internally and do not require the overhead of creating and manipulating objects.




## types

```
### Can assign a function to a new types class as a method
import types

# Define a new type called 'MyType'
MyType = types.new_class('MyType')

# Define a method for the type
def greet(self):
    print(f'Hello, my name is {self.name}')

# Set the method as an attribute of the type
MyType.greet = greet

# Create an instance of the type
obj = MyType()
obj.name = 'Alice'

# Call the method on the instance
obj.greet()  # prints "Hello, my name is Alice"
```



## checking input for type

```
def check_integer(x):
    if not isinstance(x, int):
        raise TypeError('Input must be an integer')
check_integer(10)



# checking with unittest class
import unittest
class TestCheckInteger(unittest.TestCase):
    def test_check_integer(self):
        self.assertIsInstance(10, int)
        self.assertIsInstance(5 * 5, int)

TestCheckInteger().test_check_integer()
```



## suggest typing for inputs

Using types.GenericAlias

```
import types
IntList = types.GenericAlias('IntList', list[int])

def test_function(x: IntList):
    """Add 1 to all values in list of ints"""
    if not isinstance(x[0], int):
        raise TypeError('Input must be an integer')
    return [c+1 for c in x]

test_function([1,2,3])
```



## collections.abc

A newly written class can inherit directly from one of the abstract base classes. The class must supply the required abstract methods.




































