

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
itertools.starmap is used instead of map() when argument parameters are already grouped in tuples from a single iterable (the data has been “pre-zipped”). The difference between map() and starmap() parallels the distinction between function(a,b) and function(*c).”





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




## Searching big logs

One recommmendation is grep and awk, as they are v fast. Or mmap as below

```
# https://stackoverflow.com/questions/66071560/searching-through-a-large-text-or-log-file-10gb
import logging
import os
import mmap
import re
logfilepath=filename=os.getcwd()+'/example.log'
logging.basicConfig(filename=logfilepath, encoding='utf-8', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
haha = 3
logging.warning(f'And this, too {haha}')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
print(f'written to {logfilepath}')

f = open(logfilepath, "r")
mm = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
search_res = re.search(b"message", mm)
print([search_res.start(), search_res.end()])
```





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

In CPython (aka base python), due to the Global Interpreter Lock, only one thread can execute Python code at once

Threads share the same memory space.




Writing to typed dict in using threading, though this only uses one thread at once:
```
# Could read distributed GCS files to append as memory is shared
import numba
import threading
value_float = numba.float64

typed_dict = Dict.empty(
    key_type=value_float,
    value_type=value_float
    )

def update_dict(n):
    global typed_dict
    typed_dict[n] = n + 1

# Create a thread for each operation
threads = []
for i in range(8):
    t = threading.Thread(target=update_dict, args=(i+1,))
    threads.append(t)

# Start the threads
for t in threads:
    t.start()

# Wait for the threads to finish
for t in threads:
    t.join()

print(typed_dict)
```

Q: how does thread write to shared object in memory?
A: only one thread operates at once


spawn: This method creates a new process by executing a new Python interpreter in a separate process. This is the most resource-intensive method, as it requires starting a new Python interpreter, but it is also the most flexible, as it allows you to create processes that are completely independent of the parent process.

fork: This method creates a new process by creating a copy of the current process using the os.fork() function. This method is faster and more efficient than spawn, but it is limited to Unix-based systems and requires the parent process to be written in Python.

forkserver: This method creates a new process by starting a separate process called a "server" that is responsible for creating new processes. This method is faster and more efficient than spawn, and it works on both Unix-based and Windows systems, but it requires a little more setup and is not as flexible as the other methods.




## multiprocess

Run separate processes - similar to Queue:
```
from multiprocessing import Process
def print_func(continent='Asia'):
    print('The name of continent is : ', continent)
if __name__ == "__main__":  # confirms that the code is under main function
    names = ['America', 'Europe', 'Africa']
    procs = []
    proc = Process(target=print_func)  # instantiating without any argument
    procs.append(proc)
    proc.start()
    # instantiating process with arguments
    for name in names:
        proc = Process(target=print_func, args=(name,))
        procs.append(proc)
        proc.start()
    print(f'procs ready to run: {procs}')
    # run the processes
    for proc in procs:
        proc.join()
```

A Queue is for one-way sending of objects; a Pipe is for two-way sending.

```
# in the case of Pipe(), everything happens wherever we call parent_conn.recv()
# whereas if using Process() alone it happens on p.join()
from multiprocessing import Process, Pipe

def f(conn, intval):
    conn.send([intval, None, 'hello'])
    conn.close()
    print(intval)

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    procs = []
    for i in range(3):
        p = Process(target=f, args=(child_conn,i,))
        procs.append(p)
        p.start()
        #print(parent_conn.recv())   # prints "[42, None, 'hello']"
    print('done')
    for p in procs:
        print(parent_conn.recv())
        p.join()
```

Using semaphore to limit number of processes to 2:
```
from time import sleep
from random import random
from multiprocessing import Process
from multiprocessing import Semaphore
 
# target function
def task(semaphore, number):
    # attempt to acquire the semaphore
    with semaphore:
        # simulate computational effort
        value = random() * 3
        sleep(value)
        # report result
        print(f'Process {number} got {value}')
 
# entry point
if __name__ == '__main__':
    # create the shared semaphore
    semaphore = Semaphore(2)
    # create processes
    processes = [Process(target=task, args=(semaphore, i)) for i in range(10)]
    # start child processes
    for process in processes:
        process.start()
    # wait for child processes to finish
    for process in processes:
        process.join()
```


Perform multiproc on an array of shared type.

May be possible to make 2d array from c_double and store that in custom dict-like or array-like Structure. 

May be able to treat a 1d array as a 2d array using a pointer()
```
from multiprocessing import Process, Lock
from multiprocessing.sharedctypes import Value, Array
from ctypes import Structure, c_double
from numba.typed import Dict
from numba.types import int64

class Point(Structure):
    _fields_ = [('node_id', c_double), ('node_value', c_double)]

def modify(A):
    for i in range(len(A)):
        A[i] = A[i] + 10
        
def process_structure(A):
    for a in A:
        print(a.node_id)

if __name__ == '__main__':
    
    print('start')
    lock = Lock()
    
    A = Array(c_double, [1.875,-6.25, 9.5], lock=lock)
    print(A)
            
    for i in range(3):
        p = Process(target=modify, args=(A,))
        p.start()
        
    for i in range(3):
        p.join()

    for a in A:
        print(a)
        
    # another process for our new Point structure  
    struct_array = Array(Point, [(1.875,-6.25), (-5.75,2.0), (2.375,9.5)], lock=lock)
    p = Process(target=process_structure, args=(struct_array,))
    p.start()
    p.join()
```

The main difference between mp.Pool.apply() and mp.Pool.apply_async() is that apply() blocks until the result is available, while apply_async() returns a ApplyResult object, which represents the result of the function call.


Using lock as context manager:
```
with some_lock:
    # do something...
```

A primitive lock is in one of two states, “locked” or “unlocked”. It is created in the unlocked state. It has two basic methods, acquire() and release(). Can also acquire/release by using the lock as a context manager:
```
import threading

# Create a lock object
lock = threading.Lock()

# Define a shared resource
shared_resource = 0

def update_resource(value):
    global shared_resource
    # Acquire the lock to synchronize access to the shared resource
    with lock:    
        shared_resource += value

# Define a thread that updates the shared resource
def thread_function(value):
    for i in range(10):
        update_resource(value)

# Create and start two threads that will update the shared resource concurrently
thread1 = threading.Thread(target=thread_function, args=(1,))
thread2 = threading.Thread(target=thread_function, args=(2,))
thread1.start()
thread2.start()

# Wait for the threads to finish
thread1.join()
thread2.join()

# Print the final value of the shared resource
print(f"Final value of shared resource: {shared_resource}")
```

Event object for comms between threads: one thread signals an event and other threads wait for it.

A condition variable allows one or more threads to wait until they are notified by another thread. Otherwise works much like a lock.

Barrier object: to synchronize the execution of multiple threads and ensure that certain tasks are performed in a specific order. The below blocks the thread until the required number of threads (in this case, 3) have arrived at the barrier:
```
import threading

# Create a barrier with a capacity of 3 threads
barrier = threading.Barrier(3)

# Define a function that will be run by each thread
def thread_function(n):
    print(f"Thread {n} waiting at barrier...")
    # Wait for the other threads to arrive at the barrier
    barrier.wait()
    print(f"Thread {n} passed the barrier.")

# Create and start three threads
threads = []
for i in range(3):
    t = threading.Thread(target=thread_function, args=(i,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

```



THE GIL isn't held for threading when it comes to io. Haven't tested the below on larger files to confirm whether it is using multiple cores or not
```
# this may be using multiple cores for threading io
import threading

d = {}

def process_data(data):
    # Perform some I/O operations on the data
    result = data.lower()
    return result

def write_read_data_from_file(filename):
    with open(filename, 'w') as f:
        f.write('haha')
    
    with open(filename, 'r') as f:
        data = f.read()
        
    d[filename] = data
    return data

def thread_function(filename):
    data = write_read_data_from_file(filename)
    result = process_data(data)
    print(filename)
    
# Create a thread for each file
filenames = ['example_txts/file' + str(i) + '.txt' for i in range(20)]
threads = []
for filename in filenames:
    thread = threading.Thread(target=thread_function, args=(filename,))
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All threads have finished.")
```

Threads will run on different processors / cores as the operating system chooses, they just won't run concurrently. This includes concurrent.futures.threadpoolexecutor()

Numba gives option of releasing the gil. Which may be different to parallel=True:
```
@jit(nogil=True)
def f(x, y):
    return x + y
```


Use ProcessPoolExecutor to assign to multiple cores:
```
import concurrent.futures

# execute a task
def task(value):
    print(value)
    return value

# protect the entry point
if __name__ == '__main__':
    # create the pool with the default number of workers
    with concurrent.futures.ProcessPoolExecutor() as exe:
        # issue some tasks and collect futures
        futures = [exe.submit(task, i) for i in range(50)]
        # process results as tasks are completed
        for future in concurrent.futures.as_completed(futures):
            print(f'>got {future.result}')
        # issue one task for each call to the function
        for result in exe.map(task, range(50)):
            print(f'>got {result}')
    # report that all tasks are completed
    print('Done')
```




## multiprocessing.shared_memory

Avoids the need to send messages between processes containing that data.

Once you've made a shareablelist you can't append to it

You can overwrite data so long as it doesn't exceed the overall memory assigned

```
from multiprocessing.shared_memory import ShareableList
a = ShareableList(['howdy', b'HoWdY', -273.154, 100, None, True, 42])
a[2] = -78.5

# shows amount of memory assigned
print(a.shm)  



b = ShareableList([i for i in range(10_000)])
b[3] = 'ha'
print(b.shm)
```





## concurrent.futures

The asynchronous execution can be performed with threads, using ThreadPoolExecutor, or separate processes, using ProcessPoolExecutor. Both implement the same interface, which is defined by the abstract Executor class.

Gives ProcessPoolExecutor and ThreadPoolExecutor

Future instances are created by Executor.submit() and should not be created directly except for testing. See example of future object being returned below:
```
import concurrent.futures

# Define a function that returns the result of a long-running computation
def long_running_function(n):
    # Simulate a long-running computation by sleeping for n seconds
    import time
    time.sleep(n)
    return n * n

# Create a ThreadPoolExecutor with a single worker thread
with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
    # Submit a call to the long-running function to be executed asynchronously
    future = executor.submit(long_running_function, 1.2)

    # Wait for the result to be available
    result = future.result()
    print(f"Result: {result}")
```

concurrent.futures.wait() : Wait for the Future instances to complete. Related to syncing up all threads before continuing

Synchronization primitives are tools that can be used to coordinate the execution of multiple threads or processes and synchronize access to shared resources. They are often used to prevent race conditions. 

Synchronization primitives include:
- locks
- semaphores
- conditions
- events




## contextvars

Using context variables to hold different values for a single variable name for each thread

```
import concurrent.futures
import contextvars

# Create a ContextVar to store a user's ID
user_id = contextvars.ContextVar("user_id")

# Define a function that retrieves the user's ID from the ContextVar
def get_user_id():
    return user_id.get()

# Define a function that sets the user's ID in the ContextVar
def set_user_id(id):
    user_id.set(id)

# Create a ThreadPoolExecutor with a single worker thread
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    
    # Submit calls
    fut = []
    for i in range(4):
        f = executor.submit(set_user_id, i)
        f = executor.submit(get_user_id, )
        fut.append(f)
        
    # view results
    for f in fut:
        print(f.result())
```




## subprocess

subprocess functions are intended to replace os.system() and os.spawn*

Main funcs are run() and Popen()

The main difference is that subprocess.run() executes a command and waits for it to finish, while with subprocess.Popen you can continue doing your stuff while the process finishes and then just repeatedly call Popen.communicate() yourself to pass and receive data to your process

subprocess.run() just wraps Popen and Popen.communicate() so you don't need to make a loop to pass/receive data or wait for the process to finish.

```
# Runs 'ls -la' bash command
import subprocess
subprocess.run(["ls", "-la"])


# as above, where 'out' is a subprocess.CompletedProcess class holding the output
out = subprocess.run(["ls", "-la"])
out.stdout

subprocess.Popen(["ls", "-la"])

```



## signal

signal.signal() function allows defining custom handlers to be executed when a signal is received.

A Python signal handler does not get executed inside the low-level (C) signal handler. Instead, the low-level signal handler sets a flag which tells the virtual machine to execute the corresponding Python signal handler at a later point(for example at the next bytecode instruction). 

The below will run signal_handler() before ending it when terminates the code with ctrl+c
```
import signal

# Define a signal handler function
def signal_handler(signum, frame):
    print(f"\nReceived signal {signum} so elegantly ending the program")

# Register the signal handler for the SIGINT signal (Ctrl+C)
signal.signal(signal.SIGINT, signal_handler)

# Wait for a signal to be received
print("Waiting for signal...")
signal.pause()
```



## asyncio

a Future represents an eventual result of an asynchronous operation.

often wrap a coroutine into a task, eg:
```
async def the_func(a):
    print(a)
the_task = asyncio.create_task(the_func(1))
```

```
# prefacing a func def with 'async' makes it a coroutine
async
asyncio.run(aysnc)

```

 shield() wraps a task (which wraps a coroutine) which makes it harder to cancel the execution of the coroutine


Can force a task to timeout:
```
async with asyncio.timeout(10):
	await long_running_task()
```

```
# input is an iterable
done, pending = await asyncio.wait(input)
```

asyncio.to_thread()  To run a coroutine in another thread

An event loop runs in a thread (typically the main thread) and executes all callbacks and Tasks in its thread. While a Task is running in the event loop, no other Tasks can run in the same thread. When a Task executes an await expression, the running Task gets suspended, and the event loop executes the next Task.

Thread-safe code is code that will work even if many Threads are executing it simultaneously.

Key functions:
```
# run() 	
# Create event loop, run a coroutine, close the loop.
async def main():
    await asyncio.sleep(1)
    print('hello')

asyncio.run(main())



# Task
# A Future-like object that runs a Python coroutine. Not thread-safe
# Can do things like cancel a task
import asyncio
async def do_thing():
    print('hi')

task = asyncio.create_task(do_thing())
task.cancel()
try:
	print(asyncio.current_task())     # view current task on thread
    await task
except asyncio.CancelledError:
    print("main(): cancel_me is cancelled now")


# wait_for: timeouts
asyncio.wait_for()


# schedule and wait for multiple tasks concurrently
asyncio.gather()


# run function in a new thread. Unclear when would use this over threading library
asyncio.to_thread()




# Submit a coroutine to the given event loop. Thread-safe.
# can be used to submit a coroutine to another event loop
# function is meant to be called from a different OS thread than the one where the event loop is running
run_coroutine_threadsafe()



# asyncio.as_completed() runs awaitable objects from an iterable concurrently. Return an iterator of coroutines.
import asyncio
async def do_thing(i):
    print('hi')
    return i

tasks = []
for i in range(100):  
    task = asyncio.create_task(do_thing(i))
    tasks.append(task)

for coro in asyncio.as_completed(tasks):
    earliest_result = await coro 
    print(earliest_result)   # this only prints when above line is done for all 100. 
                            # earliest_result is an int, but all 100 vals are printed (it may be different for each 
                            # coroutine)



# view running event loop or that set by the current policy, or switch to one or make new one
asyncio.get_running_loop()
asyncio.get_event_loop()
asyncio.set_event_loop()
asyncio.new_event_loop()








```






## mmap

Memory-mapped file objects behave like both bytearray and like file objects. You can use mmap objects in most places where bytearray are expected; for example, you can use the re module to search through a memory-mapped file. 



Use mmap to read in all rows of logs starting with 'ERROR'
```
import re
import mmap
import os
logfilepath=filename=os.getcwd()+'/example.log'

with open(logfilepath, "r") as f:
    mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    # Search for the pattern "error" in the file
    start = mm.find(b"ERROR")
    end = mm.find(b"\n", start)
    error_lines = []
    
    while start != -1 and end != -1:
        
        # Extract the line containing the pattern and decode it
        line = mm[start:end].decode()
        
        # Append the line to the list of error lines
        error_lines.append(line)
        
        # Search for the next occurrence of the pattern
        start = mm.find(b"ERROR", end)
        end = mm.find(b"\n", start)
        print(start)
        
    # Close the memory-mapped file
    mm.close()

# Print the list of error lines
print(error_lines)
```


Get whole line of log featuring 'ASCII'
```
import re
import mmap
import os
logfilepath=filename=os.getcwd()+'/example.log'

with open(logfilepath, "r") as f:
    mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    # Search for the pattern "error" in the file
    start = mm.find(b"ASCII")
    end = mm.find(b"\n", start)
    
    # rfind() searches from the end ('start' in this case) to the beginning: ie, in reverse 
    line_start = mm.rfind(b'\n', 0, start)
    
    error_lines = []
    
    while start != -1 and end != -1:
        
        # Extract the line containing the pattern and decode it
        line = mm[line_start:end].decode()
        
        # Append the line to the list of error lines
        error_lines.append(line)
        
        # Search for the next occurrence of the pattern
        start = mm.find(b"ASCII", end)
        previous_instance_end = end
        end = mm.find(b"\n", start)
        line_start = mm.rfind(b'\n', previous_instance_end, start)
        
    # Close the memory-mapped file
    mm.close()

# Print the list of error lines
print(error_lines)
```


To use context managers and read one line at a time
```
with open(logfilepath, "r+b") as f:
    # memory-map the file, size 0 means whole file
    with mmap.mmap(f.fileno(), 0) as mm:
        print(mm.readline())
        print(mm.readline())
```


To loop through each line:
```
with open(logfilepath, "r+b") as f:
    with mmap.mmap(f.fileno(), 0) as mm:
        myline = mm.readline()
        while myline:
            print(myline)
            myline = mm.readline()
        mm.close()   
```



## unittest

Methods in a class inheriting from unittest.TestCase should start with 'test' so unittest can pick up on them. 

Use assertRaises() to verify that a specific exception gets raised

The basic building blocks of unit testing are test cases — single scenarios that must be set up and checked for correctness. To make your own test cases you must write subclasses of TestCase or use FunctionTestCase. eg:
```
# this checks our Widget has the right dimensions
import unittest
import numpy as np

def Widget():
    ar = np.random.rand(50,50)
    return ar

class DefaultWidgetSizeTestCase(unittest.TestCase):
    def test_default_widget_size(self):
        widget = Widget()
        self.assertEqual(widget.shape, (50, 50))

if __name__ == '__main__':
    unittest.main()
```

Can add lines to create widget so only make it once:
```
import unittest
import numpy as np

def Widget():
    ar = np.random.rand(50,50)
    return ar

class DefaultWidgetSizeTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget()
        
    def test_default_widget_size(self):
        self.assertEqual(self.widget.shape, (50, 50))
        
    def tearDown(self):
        del self.widget

if __name__ == '__main__':
    unittest.main()
```

```
# run tests using all files _test.py in 'tests' folder
python -m unittest discover -p "*_test.py" tests

# same in current dir
python -m unittest discover -p "*_test.py" .
```

Test code can be run standalone from the command line, and should be 

Can set to skip tests under certain conditions by decorating the methods in a unittest.TestCase class:
```
@unittest.skip
@unittest.skipIf
@unittest.skipUnless
@unittest.expectedFailure    # will only pass if the test fails
```

Use subTest method of self (which comes with unittest.TestCase) to keep running all tests even if one fails, rather than stopping on the first failure
```
class NumbersTest(unittest.TestCase):
    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)
```

If writing tests, good reference is the [assertion methods available](https://docs.python.org/3/library/unittest.html#assert-methods)




## typing

For type hinting

Basic func specifying types - these are for info only and aren't enforced by python:
```
def greeting(name: str) -> str:
    return 'Hello ' + name
greeting('adam')
```

This will show float and list[float] as inputs when you hover over function in jupyter with shift_tab. Plus the docstring:
```
Vector = list[float]

def scale(scalar: float, vector: Vector) -> Vector:
    """
    Function which scales inputs by a factor 'scalar'

    scale = input float value
    vector = the thing we multiply by
    """
    return [scalar * num for num in vector]

# passes type checking; a list of floats qualifies as a Vector.
new_vector = scale(2.0, [1.0, -4.2, 5.4])
```

Available types include:
```
dict
tuple
set
str
float
int
list
```

collections.abc provides types including:
```
Mapping
Sequence
Callable
Sized
Iterable 
Iterator
```

typing also lets you make NewType for custom type to hint at

[More types are here](https://docs.python.org/3/library/typing.html#special-typing-primitives)





## python development mode

The Python Development Mode introduces additional runtime checks that are too expensive to be enabled by default.

Dev mode is more verbose only with warnings: if everything is perfect the printout should look the same.

To run asynciotest.py in dev mode:
```
python3 -X dev asynciotest.py
```

What does dev mode do? 
- Will tell you where you don't explicitly close a file (if not using a context manager)
- Other things no doubt...




## Text embeddings in pytorch

nn.Embedding layer takes as input a list of integer indices, and returns the corresponding embeddings for these indices as output.

nn.Embedding layer in PyTorch is trainable. This means that the embedding vectors that the nn.Embedding layer maps the input indices to can be modified during training by gradient descent.

Example:
```
import torch
import torch.nn as nn

# Define the embedding layer
embedding_layer = nn.Embedding(num_embeddings=1000, embedding_dim=128)

# Define some input text
text = ["This is some text <END>", "Here is another sentence boom!"]

# Create a vocabulary dict of word to integers
vocab = {}
vocab.update({word: index for index, word in enumerate(sorted(set([word for sentence in text for word in sentence.split()])))})

# Convert the text to a tensor
text_tensor = torch.tensor([[vocab[word] for word in sentence.split()] for sentence in text])

# Pass the text tensor through the embedding layer
embeddings = embedding_layer(text_tensor)

print(f'embeddings shape: {embeddings.shape}')
print(f'text_tensor shape: {text_tensor.shape}')
print(embeddings)
```



## Writing to distributed log files

May be best to write to a separate log file for each process to avoid race conditions. 

Or have a worker which writes all the log messages, and the other workers send to that via a queue. To do this would want to:
- make two queues: one which specifies tasks for workers; other which specifies logs to write
- create worker process which listens for queue on while loop, and writes messages to logs
- create worker processes which listen for queue to do work tasks, then send messages to log queue
All this is done in the below:
```
import multiprocessing as mp
import logging
import os
import time

def logger_process(queue): 
    # setup
    logfilepath=filename=os.getcwd()+'/example.log'
    logging.basicConfig(filename=logfilepath, encoding='utf-8', level=logging.DEBUG)
    print('logger worker ready')
    
    # Loop indefinitely
    while True:
        # Get the next item from the queue
        msg = queue.get()
        print(f'msg: {msg}')
        
        if msg == 'CLOSE':
            break
        else:
            print(f'logging: {msg}')
            logging.info(msg)
     
def task_process(queue, logging_queue): 

    # Loop indefinitely
    while True:
        # Get the next item from the queue
        msg = queue.get()
        if msg == 'CLOSE':
            break
        else:
            print(f'do something with msg {msg}')
            logging_queue.put(f'msg log of {msg}')

def main():
    # Create queues
    logging_queue = mp.Queue()
    tasks_queue = mp.Queue()

    # Create a logger process
    logger_worker_process = mp.Process(target=logger_process, args=(logging_queue,))
    logger_worker_process.start()

    # Create process for main tasks
    task_worker_process = mp.Process(target=task_process, args=(tasks_queue,logging_queue, ))
    task_worker_process.start()

    # send some tasks to main tasks
    # Put some items in the queue
    tasks_queue.put("item 1")
    tasks_queue.put("item 2")
    tasks_queue.put("item 3")

    tasks_queue.put("CLOSE")
    time.sleep(1)
    logging_queue.put("CLOSE")


if __name__ == "__main__":
    main()
```



## socketserver

The socketserver module simplifies the task of writing network servers

In class below, ThreadingMixIn class comes first, since it overrides a method defined in UDPServer
```
class ThreadingUDPServer(ThreadingMixIn, UDPServer):
    pass
```



## Making a load balancer in python

Ideas:
- use multiprocessing to create new workers in response to new requests
- make cache to store most recent

To allow the user to access the HTML text, you can modify the MyHandler class to include the necessary HTTP headers and send them to the client along with the HTML code.
```
import socketserver
import requests

class MyHandler(socketserver.BaseRequestHandler):
    def handle(self):
        html_code = '<html><body>Hello World!</body></html>'
        
        # If you wanted to fwd the request to the endpoint
        #endpoint_url = "http://localhost:9900"
        #response = requests.get(endpoint_url)
        
        # Build the HTTP response
        response = f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: {len(html_code)}\r\n\r\n{html_code}"
        print(f'response:\n{response}')

        # Send the HTTP response to the client
        self.request.sendall(response.encode())
        
class LoadBalancer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    def process_request(self, request, client_address):
    #def process_request(self):
        print('hi')
        print(f'request: {request}')
        print(f'client_address: {client_address}')
        
        # this ensures MyHandler() is called, as MyHandler is the RequestHandlerClass of this class
        self.RequestHandlerClass(request, client_address, self)
        
if __name__ == "__main__":
    # Create a load balancer server
    server = LoadBalancer(("0.0.0.0", 8080), MyHandler)
    # Start the server
    server.serve_forever()

```

And the above modified to handle errors:
```

import socketserver
import requests

class MyHandler(socketserver.BaseRequestHandler):
    def handle(self):

        endpoint_url = "http://localhost:9900"
        try:
            response = requests.get(endpoint_url)
            self.request.sendall(response.encode())
            return 0
        except requests.ConnectionError:
            # Return an HTTP response with a status code "503 Service Unavailable" if the endpoint is not reachable
            http_response = "HTTP/1.1 503 Service Unavailable\r\nContent-Type: text/plain\r\nContent-Length: 20\r\n\r\nEndpoint is unreachable"
            self.request.sendall(http_response.encode())
            return 1
        except requests.Timeout:
            # Return an HTTP response with a status code "504 Gateway Timeout" if the request to the endpoint times out
            http_response = "HTTP/1.1 504 Gateway Timeout\r\nContent-Type: text/plain\r\nContent-Length: 19\r\n\r\nEndpoint timed out"
            self.request.sendall(http_response.encode())
            return 1
        
class LoadBalancer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    def process_request(self, request, client_address):
    #def process_request(self):
        print('hi')
        print(f'request: {request}')
        print(f'client_address: {client_address}')
        
        # this ensures MyHandler() is called, as MyHandler is the RequestHandlerClass of this class
        self.RequestHandlerClass(request, client_address, self)
        
if __name__ == "__main__":
    # Create a load balancer server
    server = LoadBalancer(("0.0.0.0", 8080), MyHandler)
    # Start the server
    server.serve_forever()

    


```




## logging with timeit

timeit.repeat() is the func

```
import logging
import os
import timeit
logfilepath=filename=os.getcwd()+'/example.log'
logging.basicConfig(filename=logfilepath, encoding='utf-8', level=logging.DEBUG)
timed = timeit.repeat("8*8", repeat=2, number=1)   # number = number of times func will be called
logging.info(f'So should this time: {timed}')
```



## Get GPU and CPU usage each second

Could log this

```
import subprocess
import psutil
import time
from datetime import datetime

# Function to get GPU usage
def get_gpu_usage():
    # Run the "nvidia-smi" command and get the output
    output = subprocess.run(["nvidia-smi", "--query-gpu=utilization.gpu", "--format=csv,noheader"], capture_output=True)
    # Split the output into lines
    lines = output.stdout.decode("utf-8").strip().split("\n")
    # Parse the GPU usage from the output
    usage = [int(line.strip().split(",")[0]) for line in lines]
    return usage

# Function to get CPU usage
def get_cpu_usage():
    # Get the CPU usage using the "psutil" module
    usage = psutil.cpu_percent()
    return usage

# Main loop
current_second = datetime.now().second
while True:
    # Get the GPU and CPU usage
    gpu_usage = get_gpu_usage()
    cpu_usage = get_cpu_usage()

    # Print the usage information
    print(datetime.now().strftime('%d/%m/%y %S/%M/%H'))
    print("GPU usage: {}%".format(gpu_usage))
    print("CPU usage: {}%".format(cpu_usage))

    # Sleep until next second
    while current_second == datetime.now().second:
        time.sleep(0.001)          # better to sleep for frac of second than pass: less CPU intensive
    current_second = datetime.now().second
```


## pynccl

Same concepts as MPI

```
pynccl.init_rank()   #makes a 'communicator' object 


nk = pynccl.NcclWrp(kn, rank, gpu_i)     # this seems to be the main pynccl object


nk.get_nuid()   


nk.set_nuid()


nk.init_comm()


nk.stream_sync()


nk.do_all_gather()


nk.abort_comm()

```

In an all_gather operation, each process sends a piece of data to all other processes, and all processes receive data from all other processes. So all processes get all the results (I think).




## How does Reinforcement Learning with Human Feedback (RLHF) apply to transformers?

Unfinished notes from this article: https://huggingface.co/blog/rlhf

Human augmented text = 

The training dataset of prompt-generation pairs for the RM is generated by sampling a set of prompts from a predefined dataset

Human annotators are used to rank the generated text outputs from the LM

There are multiple methods for ranking the text. One method that has been successful is to have users compare generated text from two language models conditioned on the same prompt. The comparison is often done with an Elo rating system.

Elo rating system is a method for calculating the relative skill levels of players in zero-sum games such as chess. 

Method: fine-tuning some or all of the parameters of a copy of the initial LM with a policy-gradient RL algorithm, Proximal Policy Optimization (PPO)

many of the core RL advancements to do RLHF have been figuring out how to update such a large model with a familiar algorithm (PPO)

Training includes a divergence term penalizes the RL policy from moving substantially away from the initial pretrained model with each training batch, which can be useful to make sure the model outputs reasonably coherent text snippets.

Maximises reward metrics of reward (as judged by human labelling) minus KL divergence




## make pytorch dataloader with multiple workers

```
import torch
import torch.utils.data

# Define a PyTorch dataset
class MyDataset(torch.utils.data.Dataset):
    def __init__(self):
        # Load data
        self.data = torch.randn(20, 10)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

def main():
    # Create the dataset
    dataset = MyDataset()

    # Define a PyTorch dataloader
    dataloader = torch.utils.data.DataLoader(
        dataset,
        batch_size=10,
        shuffle=True,
        num_workers=4  # Use 4 worker processes
    )

    # Iterate over the dataloader
    for batch in dataloader:
        print(batch)

if __name__ == "__main__":
    main()
```



## jax

All jax objects are immutable






## AWS networking

firewall = network security system that controls incoming and outgoing network traffic based on predetermined security rules. Can include IP address, protocol used, port number

virtual private cloud (VPC) = virtual network dedicated to your AWS account used by resources

subnet = Each VPC network consists of one or more IP address range called subnets. Subnets are regional resources, and have IP address ranges associated with them.

group = A group is a collection of entities, where each entity can be either another group or a user

security group = specifically for controlling access to organizational resources. Collection of rules applied to 1+ users

access control list = mechanism you can use to define who has access to your buckets and objects, as well as what level of access they have.

Customer Gateways = A customer gateway connects your on-premises data center to a virtual private cloud (VPC). A VPN connection uses the Internet to connect your on-premises data center to a VPC. A Direct Connect connection uses a dedicated network connection to connect your on-premises data center to a VPC.

Virtual Private Gateways = logical representation of a VPN




## How does a Virtual Private Network (VPN) work?

The VPN server authenticates the client

The VPN server and the client establish a secure connection using a VPN protoco

Once the secure connection is established, the client can access the resources on the private network as if it were connected directly to the private network.

VPN can forward data to other servers in private network





## Generators
```
# this is a generator
def gen_nums(): 
    n=0
    while n < 4: 
        yield n
        n += 1

for i in gen_nums():
    print(i)
```



## TDD

Test driven development. Notes from chapter of Powerful Python

Says TDD is a mindset that you get into, and it makes it easier to write code in a state of flow: write the test for it, then the code, then repeat. 

Author: "TDD helps me get into an cognitive state that seems accelerated, so that I can more easily maintain my mental focus, and produce quality code faster."

Example of test of new class:
```
# run with: python3 -m unittest unit_test.py
import unittest

class Angle():
    def __init__(self, angle):
        self.degrees = angle
        
    def __repr__(self):
        return str(self.degrees) + ' degrees'

class TestAngle(unittest.TestCase): 
    def test_degrees(self):
        small_angle = Angle(60)
        self.assertEqual(60, small_angle.degrees)
```

Perhaps unit testing is best for seeing how your widget behaves generally. It won't tell you if you're getting results which look about right but aren't perfect. 

The setup() and teardown() methods you create for your testing class can be complicated (eg: making a new folder structure) 



## Decorators from classes

```
# making a decorator from a class
class PrintLog:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        print('CALLING: {}'.format(self.func.__name__)) 
        return self.func(*args, **kwargs)

@PrintLog
def nf(strr):
    print(strr)
nf('hi')
```
Our own decorator classes can inherit from other decorator classes:
```
import sys
class ResultAnnouncer:
    stream = sys.stdout 
    prefix = "RESULT"
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        value = self.func(*args, **kwargs)
        self.stream.write('{}: {}\n'.format(self.prefix,value))
        return value

class StdErrResultAnnouncer(ResultAnnouncer): 
    stream = sys.stderr
    prefix = "ERROR QS"
    
@StdErrResultAnnouncer
def pt():
    print('po')
pt()
```

Not a decorator but storing info in an object 
```
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 1
    def __call__(self, *args, **kwargs):
        print('# of calls: {}'.format(self.count)) 
        self.count += 1
        return self.func(*args, **kwargs)

caller = CountCalls(print)
for i in range(3):
    caller('aaa')
```

Can also make decorators to apply to classes: this one automatically adds the '__repr__' method to show the class name and it's value
```
# here 'klass' is the name of the class being decorated
def autorepr(klass):
    def klass_repr(self):
        return '{}, {}'.format(klass.__name__ + ' instance', self.value)
    klass.__repr__ = klass_repr
    return klass

@autorepr
class Penny():
    def __init__(self, value):
        self.value = value

print(Penny(3))
```

Says the worst ever python antipattern is using try/except without a specific exception to catch, as per:
```
try: 
	(do something)
except: 
	pass
```

@property in a class is somewhat like a method which is pretending to be a property of the class
```
class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    @property
    def fullname(self):
        return self.firstname + " " + self.lastname
    
Person('john', 'smith').fullname
#Person('john', 'smith').fullname()  # would be this without property decorator

```


## NeoX

Chunks of code from NeoX
```
# @distributed_test to distribute testing
from torch.testing import distributed_test
```

Making a dataclass to store key/values
```
from dataclasses import dataclass
@dataclass
class NeoXArgsDeepspeedConfig():
    deepspeed: bool = True
    train_batch_size: int = None
```


## Leetcode

Main take home from doing leetcode: 
- lots of little mistakes like typos or using wrong names for things will get me in trouble
- watch out for taking modulus of zero
- generally thinking I've got it working when I haven't

Pivot index = index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right. The below finds the pivot index:
```
# this finds the overall sum, then looks for the point which is halfways between that
class Solution(object):
    def pivotIndex(self, nums):
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1
```

The below makes a calendar which checks for double bookings:
```
class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:

        # check for double booking
        def is_overlap(start, end, old_start, old_end):
            if start < old_end and end > old_start:
                return 1
            else:
                return 0

        counter = 0
        for booking in self.bookings:
            counter += is_overlap(start, end, booking['start'], booking['end'])

        if counter == 0:
            self.bookings.append({'start':start, 'end':end})
            return True

        return False 
```

The below tells you if two strings are isomorphic:
```
def isIsomorphic(s: str, t: str) -> bool:

    letter_map = {}
    for i in range(len(s)):
        if s[i] in letter_map.keys():
            print(letter_map[s[i]])
            if letter_map[s[i]] != t[i]:
                return False
            
        if t[i] in letter_map.values():
            try:
                if letter_map[s[i]] != t[i]:
                    return False
            except KeyError:
                return False

        letter_map[s[i]] = t[i]

    new_word = ''
    for letter in s:
        new_word += letter_map[letter]

    return new_word == t
isIsomorphic('badc', 'baeg')
```

Inelegant solution to reverse order of linked list:
```
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []

        if head is None:
            return None
        
        print(head)
        while head is not None:
            l.append(head.val)
            head = head.next
        
        # reverse the list
        ln = ListNode(val=l[0],next=None)
        for val in l[1:]:
            ln = ListNode(val = val, next = ln)
        print(ln)

        return ln
```
To check if a graph is acyclic.

Make adjacency matrix: connections for each node
    
Then use depth first search: start from each node which doesn't have dependenices and see if everywhere can be visited.



Tells you if a sequence is monotonic:
```
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        i = 0
        is_decreasing = nums[i+1] < nums[i]
        same = nums[i+1] == nums[i]
        while same:
            if i == len(nums) - 1:
                return True
            
            is_decreasing = nums[i+1] < nums[i]
            same = nums[i+1] == nums[i]
            i += 1

        if is_decreasing:
            for i in range(1, len(nums)):
                if nums[i] > nums[i-1]:
                    return False

        if not is_decreasing:
            for i in range(1, len(nums)):
                if nums[i] < nums[i-1]:
                    return False

        return True
```

Find first position of string in larger string
```
S = 'hahaha' # Source String 
k = 'a' # String to be searched
import re
pattern = re.compile(k)
r = pattern.search(S)
r.start()
```

Method to do something to class on hash() 
```
class ha():
    v = 3
    def __hash__(self):
        return self.v
    
hash(ha())
```

To completely override sys.path create a ._pth file. In the ._pth file specify one line for each path to add to sys.path
```
import sys
sys.path
```


## Importlib

To import from file system, zip archives, and other locations such as databases. The below loads a package from a database:
```
import importlib.abc
import importlib.util

class DatabaseModuleLoader(importlib.abc.Loader):
    def create_module(self, spec):
        # Retrieve the module code from the database
        code = retrieve_module_code_from_database(spec.name)
        # Create a new module object
        module = types.ModuleType(spec.name)
        # Execute the module code in the context of the module object
        exec(code, module.__dict__)
        # Return the module object
        return module
    
    def exec_module(self, module):
        # No need to execute the code again, as it was already executed in create_module()
        pass
    
    def is_package(self, fullname):
        # Check if the module is a package by querying the database
        return is_package_in_database(fullname)
    
    def get_code(self, fullname):
        # Retrieve the module code from the database
        return retrieve_module_code_from_database(fullname)
    
    def get_source(self, fullname):
        # Retrieve the module source code from the database
        return retrieve_module_source_from_database(fullname)

# Create a module spec for the module to be loaded
spec = importlib.util.spec_from_loader('my_module', DatabaseModuleLoader())
# Use the module spec to load the module
module = importlib.util.module_from_spec(spec)
# Execute the module's code in the context of the module object
spec.loader.exec_module(module)
```


## ipaddress

```
import ipaddress

# returns an ipaddress object
addr = ipaddress.ip_address('192.168.0.1')

# can also make networks, and explode or compress the IP address
```
A network definition consists of a mask and a network address

IP network masks: "A prefix /<nbits> is a notation that denotes how many high-order bits are set in the network mask. A net mask is an IP address with some number of high-order bits set."

The below shows you all available IP addresses in the network given the size of the net mask
```
list(ipaddress.ip_network('192.0.2.0/29').hosts())  

list(ipaddress.ip_network('192.0.2.0/23').hosts())  
```
Host mask is the logical opposite of the network mask, eg: 255.255.255.0 (network) becomes 0.0.0.255 (host)




## breakpoint

breakpoint() in script will pause it for debug in terminal. type 'next' to continue execution

```
print(222)
breakpoint()
print(111)
```



## faulthandler

The below prints the traceback to STDERR (ie, the console)
```
import faulthandler

def some_function():
    # some code here
    try:
        # code that may raise an exception
        1 / 0  # this will raise a ZeroDivisionError
    except Exception as e:
        # print the traceback of the current thread
        faulthandler.dump_traceback(e)

some_function()
```
Use faulthandler.register() to dump traceback on reception of a signal




## trace

The below runs fault_handler.py with extra tracing:  
```
python -m trace --count -C . --report --file f.txt fault_handler.py
```

Using tracer.run() on main() below will get you more debug info on error than default
```
import sys
import trace

# create a Trace object, telling it what to ignore, and whether to
# do tracing or line-counting or both.
tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=0,
    count=1)

def main():
    1 / 0
    return 1

# run the new command using the given tracer
tracer.run('main()')
#main()

# make a report, placing output in the current directory
r = tracer.results()
r.write_results(show_missing=True, coverdir=".")
```



## tracemalloc

The tracemalloc.take_snapshot() function in Python is used to take a snapshot of the current state of the memory allocator. This snapshot can be used to later analyze the memory usage of a program and identify potential memory leaks.




## pyflakes

Static analyser of code: looks for any syntax errors or undefined variables

To run it on a script:
```
pyflakes forflakes.py
```


## pylink

Does more than pyflakes: checks for syntax errors and styles

To run:
```
pylint forflakes.py
```


## pycodestyle

Checks for formatting only, not what the code actually does

To run:
```
pycodestyle forflakes.py
```


## bandit

Finds common security issues in Python code

To run:
```
bandit forflakes.py
```

Builds an Abstract Syntax Tree (AST) from code files and runs appropriate plugins against the AST nodes. Once Bandit has finished scanning all the files, it generates a report.




## inspect

```
inspect.signature(func_name)    for viewing signature (aka input arguments and their types) of a function

# has various functions for telling you things about an object or function, eg:
inspect.isawaitable(obj_name)
```



## sys for auditing events

The below triggers and handles an audit event. The audit_handler() is a callback triggered by the audit event
```
import sys

def audit_handler(event, args):
  print(f'Audit event triggered: {event}')
  print(f'Event arguments: {args}')

# Set the audit hook function
sys.addaudithook(audit_handler)

# Trigger an audit event
sys.audit('example_event', {'arg1': 'value1', 'arg2': 'value2'})
```



## cProfile and pstats

pstats is a way to extract info needed from cProfile findings

```
import cProfile
import pstats

def my_function():
    1*2
    print('hi')

# Run the code being profiled using cProfile, storing result in obj 'profiling_results'
cProfile.run("my_function()", "profiling_results")

# Load the profiling results into a pstats.Stats object
stats = pstats.Stats("profiling_results")

# Use the pstats.Stats object to analyze the profiling results
stats.strip_dirs()
stats.sort_stats("time")
stats.print_stats(20)
```








multiprocessing is less good for io as doesn't share memory: but what if you're using shared_memory?

Use of Union[list, set] ?


concurrent read/write access to objects vs multiple simultaneous read accesses


differnce between registering and inheriting in python?




```
## To view source code for a module or function
import inspect
import io
from pprint import pprint
pprint(inspect.getsource(io))
```




## other things

semaphore = synchronization object that controls access by multiple processes or threads. Typically used to synchronize access to a shared resource, such as a shared memory location or a file, in order to prevent data races and other synchronization issues.

persistence = save the state of an object or data structure to a file or database, so that it can be restored later

serialisation = converting an object or data structure into a format that can be easily stored or transmitted, such as a string of bits or bytes

constructor = special method that is called when an object is created. Its purpose is to initialize the object's state, which includes setting any initial values for the object's attributes (i.e., instance variables).

Thread-safe = ability of a piece of code, data structure, or API to be used safely by multiple threads concurrently

multiplexing = technique that allows multiple streams of data to be transmitted over a single communication channel or link. It is often used in networking and communication systems to efficiently utilize resources and maximize the amount of data that can be transmitted in a given time.

memory-mapped files = memory maps let you access the contents of the file using standard memory access operations, even if the entire file does not fit in memory. The operating system will automatically page the contents of the file in and out of memory as needed.

Test discovery = process of finding and running test cases in a test suite.

regression test = checking changes made in the codebase do not impact the existing software functionality.

primitive calls = calls not induced via recursion

audit event = specific type of system event, such as a function call or attribute access, that is generated by the Python interpreter.



# References 

[Exception hierarchy for reference](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)











