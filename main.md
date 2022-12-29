

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

ABC provides abstract base classes that can be used to test whether a class provides a particular interface; for example, whether it is hashable or whether it is a mapping.

ABC may still force you to implement methods yourself: inheriting the method tells other coders what your new class is trying to do.

A newly written class can inherit directly from one of the abstract base classes. The class must supply the required abstract methods.

```
All special methods (with "magic names" that begin and end in __) are not meant to be called directly

# __contains__ lets you call 'in' operator
class thing():
    def __init__(self):
        self.val = ['a', 'b']
        
    def __contains__(self, x):
        return x in self.val

'b' in thing()
```

List of all the available reversibles (Container, Hashable, Iterable, etc): https://docs.python.org/3/library/collections.abc.html


```
from dataclasses import dataclass

@dataclass
class InventoryItem:
    """Class for keeping track of an item in inventory."""
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand
    
InventoryItem('adam', 15, 2).total_cost()
```



## itertools

[All functions listed here](https://docs.python.org/3/library/itertools.html)

```
import itertools
for i in itertools.repeat(10, 3):
    print(i)


for i in itertools.accumulate([1,2,3,4,5]):
    print(i)


# chain() treats multiple sequences as a single sequence
for i in itertools.chain('ABC', 'DEF','aaa'):
    print(i)


# add from_iterable() to pass a list of sequences to chain()
for i in itertools.chain.from_iterable(['ABC', 'DEF','aaa']):
    print(i)


# filter where is a 1 not 0 in corresponding list
for i in itertools.compress('ABCDEF', [1,0,1,0,1,1]):
    print(i)


# all combinations in all orders
for p in itertools.permutations('ABCD', 2):
    print(p)

# all combinations in one order
for p in itertools.combinations('ABCD', 2):
    print(p)


# each value multiplied by each other value. Can do this for as many orders as 'repeat' specifies
for p in itertools.product('ABCD', repeat=2):
    print(p)


# applies each tuple as params for func ('pow' in this case)
for i in itertools.starmap(pow, [(2,5), (3,2), (10,3)]):
    print(i)


# subsetting
for i in itertools.islice('ABCDEFG', 3, None):
    print(i)



# Key function tells groupby() which bit of tuples to use to identify keys
key_func = lambda x: x[0]
L = [("a", 1), ("a", 2), ("b", 3), ("b", 4)]

for key, group in itertools.groupby(L, key_func):
    for g in group:
        print(g)
    print(key)



# combine iterables to tuples: fills shorter inputs rather than dropping them as 'list(zip('ABCD', 'xyK'))' does
for i in itertools.zip_longest('ABCD', 'xyK', fillvalue='-'):
    print(i)



```




## functools

The functools module is for higher-order functions: functions that act on or return other functions. In general, any callable object can be treated as a function for the purposes of this module.

Use @singledispatchmethod to make a method single dispatch

```
# same as memoise
from functools import cache
@cache
def factorial(n):
    return n * factorial(n-1) if n else 1
print(factorial(2))
print(factorial.cache_info())
print(factorial.cache_parameters())
print(factorial.cache_clear())
print(factorial.cache_info())



# using @property
class C:
    def __init__(self):
        self._x = 'ha'

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    # allows setting value of Cinstance.x
    @x.setter
    def x(self, value):
        self._x = value
   
    # allows deleting value of Cinstance.x
    @x.deleter
    def x(self):
        del self._x
    
c = C()
del c.x
c.x = 4
c.x



# can combine @property and @cache
class DataSet:
    def __init__(self, sequence_of_numbers):
        self._data = sequence_of_numbers
    @property
    @cache
    def stdev(self):
        return statistics.stdev(self._data)




# lru_cache = memoizing callable that saves up to the maxsize most recent calls
from functools import lru_cache 
@lru_cache
def count_vowels(sentence):
    return sum(sentence.count(vowel) for vowel in 'AEIOUaeiou')
count_vowels('hahahan os')


# total_ordering decorator takes __eq__ and one of __lt__/__gt__/etc and extrapolates operations for all other greater/less/equal  
import functools
@functools.total_ordering
class Student:
    def _is_valid_operand(self, other):
        return (hasattr(other, "lastname") and
                hasattr(other, "firstname"))
    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return ((self.lastname.lower(), self.firstname.lower()) ==
                (other.lastname.lower(), other.firstname.lower()))
    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return ((self.lastname.lower(), self.firstname.lower()) <
                (other.lastname.lower(), other.firstname.lower()))
s = Student()
s.lastname = 'aa'
s.firstname = 'bb'
print(s < s)
print(s >= s)



# reduce() takes a start value x (0 in this case) does something with each y value, accumulating 
from functools import reduce
reduce(lambda x, y: x+y, [1, 2, 3, 4, 5], 0)



## @singledispatch makes one fun(), and depending on the input type a different version of the below will be 
## called. Basically: overloading the function
from functools import singledispatch
@singledispatch
def fun(arg, verbose=False):
    if verbose:
        print("Let me just say,", end=" ")
    print(arg)
    
@fun.register
def _(arg: int | float, verbose=False):
    if verbose:
        print("Strength in numbers, eh?", end=" ")
    print(arg)

from typing import Union
@fun.register
def _(arg: Union[list, set], verbose=False):
    if verbose:
        print("Enumerate this:")
    for i, elem in enumerate(arg):
        print(i, elem)





# use @functools.wraps to make a decorator
def log_function(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Called {func.__name__} with arguments {args} and keyword arguments {kwargs}")
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_function
def add(x, y):
    return x + y

print(add(1, 2))
# Output:
# Called add with arguments (1, 2) and keyword arguments {}
# add returned 3


```



## operator

To write many operations with written commands rather than symbols. [Reference here](https://docs.python.org/3/library/operator.html)

```
import operator
operator.truediv(2,3)
operator.contains('aaaa','a')
```



## pathlib

gives object oriented approach to handling file pathways

Can do things to look around the tree of the current dir for files, and for file names or types which match certain patterns

```
from pathlib import Path
p = Path('.')
print([x for x in p.iterdir() if x.is_dir()])
print([x for x in p.iterdir()])

# get .md files in this directory tree
list(p.glob('**/*.md'))

path = Path('/tmp')
for item in path.iterdir():
    print(item)

path = Path('/tmp/example.txt')
path.write_text('Hello, world!\nhaha')
    
path = Path('/tmp/example.txt')
with path.open() as f:
    print(f.readline())
    print(f.readline())
    
path = Path('/tmp/example.txt')
if path.exists():
    print('The file exists')
else:
    print('The file does not exist')

contents = path.read_text()
print(f'contents: {contents}')

```


## fileinput

To iterate over lines from multiple input streams¶

```
# read multiple files as single input
import fileinput
with fileinput.input(files=['filename.txt', 'filename.txt']) as f:
    for line in f:
        print(line)
```


## filecmp

Compare similarity of files. May rely on difflib module

```
import filecmp

# see if two files are same
filecmp.cmp('filename.txt', 'filename.txt')

# returns match, mismatch, errors for specified files (3rd param) between 2 directories (params 1 and 2)
filecmp.cmpfiles('', '', ['filename.txt'])
```



## tempfile

If you need to store files or make directories for temporary use

Files and folders are deleted at the closing of the context manager below

```
import tempfile

with tempfile.TemporaryFile() as fp:
    fp.write(b'Hello world!')
    fp.seek(0)
    fp.read()

with tempfile.TemporaryDirectory() as tmpdirname:
    print('created temporary directory', tmpdirname)
```



## linecache

Used to read specific line from a file

```
import linecache
linecache.getline('file.txt', 4)
```



## shutil

copies files: copyfileobj, copyfile, copy, copy2, copytree (copy all files in dir)

copies permissions and logs of files: copymode, copystat

deletes or moves files: rmtree, move

change permissions: chown

get stats: disk_usage, which





## pickle

pickletools.optimize for faster performance

```
# raise pickle error
raise pickle.UnpicklingError("unsupported persistent object")


import pickle
pickle.dumps('sometext', protocol=pickle.HIGHEST_PROTOCOL)



# use pickletools.optimize. Is:
# shorter, takes less transmission time, requires less storage space, and unpickles more efficiently.
import pickletools
more_efficient_pickle_bytestring = pickletools.optimize(pickle.dumps('sometext', protocol=pickle.HIGHEST_PROTOCOL))
pickle.loads(more_efficient_pickle_bytestring)

```




## shelve

shelve opens a key/value db which can store all finds of objects, all of which are pickled into a db file

may be simplier alternative to sqlite3 for key/values

```
import shelve
with shelve.open('spam') as db:
    print(db.get('eggs'))
    db['eggs2'] = 'eggs_and_bacon'
    print(db.get('eggs2'))
```

 If the optional writeback parameter is set to True, all entries accessed are also cached in memory, and written back on sync() and close(); this can make it handier to mutate mutable entries in the persistent dictionary, but, if many entries are accessed, it can consume vast amounts of memory for the cache, and it can make the close operation very slow since all accessed entries are written back. Example of this:

```
import shelve
with shelve.open('spam', writeback=True) as db:
    print(db.get('eggs'))
    db.sync()        					 ### adding this line to manually sync db
    db['eggs2'] = 'eggs_and_bacon'
    print(db.get('eggs2'))
```



## dbm

works a lot like shelve, as shelve uses dbm in the background

```
### example from docs
import dbm

# Open database, creating it if necessary.
with dbm.open('cache', 'c') as db:

    # Record some values
    db[b'hello'] = b'there'
    db['www.python.org'] = 'Python Website'
    db['www.cnn.com'] = 'Cable News Network'

    # Note that the keys are considered bytes now.
    assert db[b'www.python.org'] == b'Python Website'
    # Notice how the value is now in bytes.
    assert db['www.cnn.com'] == b'Cable News Network'

    # Often-used methods of the dict interface work too.
    print(db.get('python.org', b'not present'))
    
    # Storing a non-string key or value will raise an exception (most
    # likely a TypeError).
    db['www.yahoo.com'] = 'a'
```




## sqlite3

A cursor is a control structure that enables traversal over the records in a database. A cursor can be thought of as a pointer to a specific position within a result set of a database query.

Call con.commit() on the connection object to commit the transaction:

URI: uniform reference identifier

```
import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()
cur.execute("CREATE TABLE movie(title, year, score)")
res = cur.execute("SELECT name FROM sqlite_master")
print(res.fetchone())
res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")
print(res.fetchone() is None)
cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")
con.commit()
data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]
cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
con.commit() 
for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
    print(row)




# using context manager
with sqlite3.connect("tutorial.db") as con:
    print(con.execute("select * from movie").fetchall())



# making a python function and calling it in sqlite with con.create_functionw
import hashlib
def md5sum(t):
    return hashlib.md5(t).hexdigest()
con = sqlite3.connect(":memory:")
con.create_function("md5", 1, md5sum)
for row in con.execute("SELECT md5(?)", (b"foo",)):
    print(row)

```



## archiving

lzip, bzip2, gzip, and lzma are all compression algorithms that can be used to reduce the size of a file. 

```
import zlib, gzip, lzma, bz2
print(zlib.compress(b'aa'))
print(gzip.compress(b'aa'))
print(lzma.compress(b'aa'))
print(bz2.compress(b'aa'))


print(zlib.decompress(zlib.compress(b'aa')))
print(bz2.decompress(bz2.compress(b'aa')))
```




## configparser


```
## makes ini file in the next chunk
import configparser
config = configparser.ConfigParser()
config['one.thing'] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}
config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Port'] = '50022'     # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here
config['DEFAULT']['ForwardX11'] = 'yes'
with open('example.ini', 'w') as configfile:
  config.write(configfile)
```


example.ini:
```
[one.thing]
serveraliveinterval = 45
compression = yes
compressionlevel = 9
forwardx11 = yes

[bitbucket.org]
user = hg

[topsecret.server.com]
port = 50022
forwardx11 = no
```


Read in ini file and convert to dict:
``` 
config = configparser.ConfigParser()
config.read('example.ini')
config_dict = {s:dict(config.items(s)) for s in config.sections()}
config_dict
```


Can use ${string_interpolation} to add custom file paths to .ini file
```
[Paths]
home_dir: /Users
my_dir: ${home_dir}/lumberjack
my_pictures: ${my_dir}/Pictures

[Escape]
# use a $$ to escape the $ sign ($ is the only character that needs to be escaped):
cost: $$80
```




## confuse

to read in yaml files

```
import confuse

# Load the configuration file using the confuse.Configuration class
config = confuse.Configuration('my_app', __name__)

# Access the values in the configuration using the [] operator
database_url = config['database']['url'].get()
```




## hashlib

implements many secure hash and message digest algorithms. Included are the FIPS secure hash algorithms SHA1, SHA224, SHA256, SHA384, and SHA512 (defined in FIPS 180-2) as well as RSA’s MD5 algorithm.

The terms “secure hash” and “message digest” are interchangeable.

```
# hashlib
from hashlib import sha256, blake2b, md5
s = sha256()
s.update(b"Nobody inspects")
print(s.digest())

# as above but in one line
print(sha256(b"Nobody inspects").digest())
print(sha256(b"Nobody inspects").hexdigest())
print(blake2b(b"Nobody inspects").hexdigest())
print(md5(b"Nobody inspects").hexdigest())

print(hashlib.algorithms_available)
```




## hmac

hashlib looks generally preferable to hmac

```
import hmac
hmac.digest(b'key1',msg=b'haha',digest='md5')
```


## secrets

The secrets module is used for generating cryptographically strong random numbers suitable for managing data such as passwords, account authentication, security tokens, and related secrets.

```
import secrets
# make random bytestring of length 16
secrets.token_bytes(16) 
secrets.token_hex(16)


# generate 8 letter alphanumeric password
import string
import secrets
alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(8))
print(password)

# Generate a hard-to-guess temporary URL containing a security token suitable for password recovery applications:
import secrets
url = 'https://example.com/reset=' + secrets.token_urlsafe()
url


# create random set of words
import secrets
# On standard Linux systems, use a convenient dictionary file.
# Other platforms may need to provide their own word-list.
with open('/usr/share/dict/words') as f:
    words = [word.strip() for word in f]
    password = ' '.join(secrets.choice(words) for i in range(4))
```



## os

provides a portable way of using operating system dependent functionality. Basically lets you do lots of things linux CLI would allow

best to find functions from chatgpt or in [the docs](https://docs.python.org/3/library/os.html)

```
os.path.exists(path)

os.path.expanduser('~/Desktop/pythonlearning2023')   # Expands the '~' character in a path to the user's home directory.

# view all directories and files in directories
for base, dirs, files in os.walk(os.path.expanduser('~/Desktop/pythonlearning2023')):
    print(base, dirs)

os.fork() - Creates a new process.

os.popen(command) - Opens a pipe to or from the specified command.


```






## filelock

Locks file

```
## applying a file lock
from filelock import Timeout, FileLock
import time

# make a file
open("high_ground.txt", "w")
open("high_ground.txt.lock", "w")

# edit the file with a lock
lock = FileLock("high_ground.txt.lock")
with lock:
    with open("high_ground.txt", "a") as f:
        time.sleep(20)
        f.write("You were the chosen one.")
```

If you have the above running, the below (if run as part of a different process) will wait until the lock is released

```
from filelock import FileLock
file_name = 'test.txt'
lock_name = file_name + '.lock'
with FileLock(lock_name):
    with open(file_name, 'a+') as f:
        f.write('Hello World')
```



## io

Q: difference between io.StringIO() and open() ?
A: The difference is: open takes a file name (and some other arguments like mode or encoding), io.StringIO takes a plain string and both return file-like objects. Hence:

- Use open to read files
- Use StringIO when you need a file-like object and you want to pass the content of a string.


io.DEFAULT_BUFFER_SIZE sets buffer size

io.FileIO for reading generic files

```
# reads in raw file: docs say its rare you'll do this
f = open("myfile.jpg", "rb", buffering=0)

import io
f = io.StringIO("some initial text data")
for i in f:
    print(i)
    
f = io.BytesIO(b"some initial binary data: \x00\x01")
for i in f:
    print(i)


# example specifying text encoding for open()
def read_text(path, encoding=None):
    encoding = io.text_encoding(encoding)  # stacklevel=2
    with open(path, encoding) as f:
        return f.read()


# getbuffer() returns a read/write-able view of the contents of the buffer without copying them.
b = io.BytesIO(b"abcdef")
view = b.getbuffer()
view[2:4] = b"56"
b.getvalue()


```
Buffer flush = transfer of computer data from a temporary storage area to the computer's permanent memory.

Text I/O over a binary storage (such as a file) is significantly slower than binary I/O over the same storage, because it requires conversions between unicode and binary data using a character codec

Default buffer size = amount of data that is read or written to the buffer at a time.

A larger buffer size can result in faster data transfer, as more data can be transferred in each operation. However, it can also consume more memory, as the buffer will be larger. 

The default buffer size for the io library is typically 8192 bytes. One way to set it:
> f = open('file.txt', 'r', buffering=1024)





## logging

Logging provides a set of convenience functions for simple logging usage. These are debug(), info(), warning(), error() and critical(). 

File names can be a period-separated hierarchical value, like foo.bar.baz (though it could also be just plain foo, for example). Loggers that are further down in the hierarchical list are children of loggers higher up in the list. For example, given a logger with a name of foo, loggers with names of foo.bar, foo.bar.baz, and foo.bam are all descendants of foo.

Can use handlers to do things in event of logging

there is one lock to serialize access to the module’s shared data

For storing info on exception handling you should do something about: logging.error(), logging.exception() or logging.critical()

For storing general info on goings on: logging.info() (or logging.debug() 

This code makes a log file and writes to it:
```
# this needs to run in python terminal: won't work in jupyter
# if you run it twice it appends by default
import logging
import os
logfilepath=filename=os.getcwd()+'/example.log'
logging.basicConfig(filename=logfilepath, encoding='utf-8', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
haha = 3
logging.warning(f'And this, too {haha}')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
print(logfilepath)
```


Can store configs for logging in a conf file
```
import logging.config
logging.config.fileConfig('logging.conf')
```

Where logging.conf might look something like:
```
[loggers]
keys=root,simpleExample

[handlers]
keys=consoleHandler

[formatters]
keys=simpleFormatter
```

Events of severity WARNING and greater will be printed to sys.stderr. According to the docs, this is regarded as the best default behaviour.

Can use handlers to send messages to different locations and file types. 






## getpass

input string without echoing

```
import getpass
a = getpass.getpass()
print(a)
```



## curses

Way of presenting things like option screen to user in CLI and getting inputs

```
import curses
screen = curses.initscr()
# Update the buffer, adding text at different locations
screen.addstr(0, 0, "This string gets printed at position (0, 0)")
screen.addstr(3, 1, "Try Russian text: Привет")  # Python 3 required for unicode
screen.addstr(4, 4, "X")
screen.addch(5, 5, "Y")
# Changes go in to the screen buffer and only get
# displayed after calling `refresh()` to update
screen.refresh()
curses.napms(3000)
curses.endwin()
```



## platform

Gets info on hardware and software OS and python versions

```
# sumbunall platform functions
import platform
platform.architecture()
platform.machine()
platform.node()
platform.platform()
platform.processor()
platform.python_build()
platform.python_compiler()
platform.python_version()
platform.system()
platform.uname()
```



## threading














Use of Union[list, set] ?


concurrent read/write access to objects vs multiple simultaneous read accesses


differnce between registering and inheriting in python?





## other things

persistence = save the state of an object or data structure to a file or database, so that it can be restored later

serialisation = converting an object or data structure into a format that can be easily stored or transmitted, such as a string of bits or bytes

constructor = special method that is called when an object is created. Its purpose is to initialize the object's state, which includes setting any initial values for the object's attributes (i.e., instance variables).

Thread-safe = ability of a piece of code, data structure, or API to be used safely by multiple threads concurrently


```
## To view source code for a module or function
import inspect
import io
from pprint import pprint
pprint(inspect.getsource(io))
```









