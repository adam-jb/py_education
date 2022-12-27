

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











