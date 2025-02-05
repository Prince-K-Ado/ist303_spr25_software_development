---
marp: true
theme: gaia
#size: 4:3
#_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
---

# Week 3: Python
Most of the class (Lubanovic Chs 4-8)
- General Python info
- Control and comparison operators
- Loops
- Strings (text objects)
- Lists and Tuples
- Dictionaries and sets


---
## General Python Structure
Python structures code with indentation (not brackets)
- recommend using spaces, not tabs (different text editors store tab chars differently)

---
### Statement syntax
Statements/conditions end in `:`
```
if 1 == 2:
  print("True")
```
compare  to C:
```
if (1==2) {
  printf("True");
}
```

---
### Comments
comment with `#` (hash/pound)
- `# This is a comment`
- will not be executed by the python interpreter

line continuation: `\` 
```
print("this is one \
line")
```

---

## Lubanovic Chapter 4: If

### `If` statement
- _execute code if a condition is met (evaluates to True)_ \
`if condition:` _...code to execute if true_

```
if 2 > 1: print("2 heads are better than 1")

if 2 > 1:
  print("2 heads are better than 1")
```

---
Additional control statements:
### `else`
- _allows code to be run when condition is NOT met (in if or any number of elif conditions)_ \
`else:` ...code to run if all preceding conditions are False
### `elif` 
- _'else if', allows additional conditions to check for true_ \
`elif condition:` ... code to run if elif condition is true

---
### Example - if_fruit.py
_powershell_> new-item if_fruit.py \
_mac/linux_> touch if_fruit.py
``````
# if_fruit.py

fruit = input("Enter a fruit: ")
if fruit == "orange":
  print(f"take a bite of {fruit}")
elif fruit == "apple":
  print(f"pass your {fruit} to a friend")
else:
  print(f"you forgot to bring your {fruit}")
  ``````

---
### True and False
_True_ and _False_ are special values in Python - you can see that they are objects of type 'bool' by typing `type(True)` in a python session. 


Capitalization matters - True is not TRUE or true


---
### Conditions: comparison operators
Return either `True` or `False`  
- `==`  equality
- `!=`  inequality
- `<`   less than
- `<=`  less than or equal
- `>`   greater than
- `>=`  greater than or equal

---
### Boolean operators
aka logical operators. Combine conditions using these operators for more complex testing.
- `and` : returns True if _both_ conditions are True
- `or` : returns True if _either_ condition is True
- `not` : returns True if the statement is true. Often used in conjunction with `in`.

---
_What do the following statements evaluate to?_
```
4 == 4 or 2 > 7
4 == "4"
True or False
True is False
True and False
```

---
#### Additional operators
- `in` : test membership in an object

```
'c' in 'branch'
```

---
#### Equality vs. Reference
- `is` : test if two variables refer to the same _object_ in memory 
- not to be confused with equality, `==`, which tests equality of _values_

try: 
```
a=[1,2,3]
b=[1,2,3]
a == b #equality of value
a is b #reference the same object?

a=[5,6,7]
b=a
a is b
```

---
#### True and False
The following evaluate to **False**:
|    |    |    |
|----|----|----|
| `False`  -boolean | `0`  -zero integer | `0.0`  -zero float |
| `None`  -Null | `''`  -empty string | `[]`  -empty list |
|`()`  -empty tuple | `{}`  -empty dict |`set()`  -empty set|


**All other values evaluate to True**
_this is extremely helpful for evaluating statements such as `if` or `while`_

---
# Chapter 5: Strings
- strings are immutable (can't be changed in place). Once defined, a string object cannot be edited.

- `str()` function converts object to string
- multiline strings: start and end with three quote marks  `'''` or `"""`
  - (whichever you use the start and end must be the same)
- concatenate (combine) strings with `+`
- duplicate a string with `*`

---
### String indexing and slicing
In Python, brackets `[]` are used to access elements of _subscriptable_ objects. 

A ___subscriptable___ object is composed of smaller, independently accessible items/objects. Strings are composed of characters, lists are composed of elements, etc. Integers are not composed of any smaller objects. 

The format uses square brackets: `object[]`, this is the same for both **indexing** and **slicing**. Indexing is used if a single value is passed in, slicing utilizes `:` within the brackets.

---
### Indexing
Access a character by its corresponding index value (remember that Python is `0` indexed, meaning that the first position is accessed by index value `0`): 

### `mystring[0]`
  - can use integer values OR expressions
  - any expression that evaluates to a single integer will return the character at that index
  - you can use negative index values to start counting from the end of the object; `mystring[-1]` returns the last character in _mystring_

---
**Slicing (Strings)**
Similar to an index, but rather than a single item it accesses multiple items by specifying a _start_ and _end_ index position:

#### `mystring[start:end]`
- _inclusive_ of start, _exclusive_ of end [ , )
- omitting start/end parameter defaults to start/end of the string
  - `mystring[:5]` returns characters from the start to index position 5
  - `mystring[2:]` returns characters from index position 2 to the end
- `mystring[:]` simply returns `mystring`

---
one of the following results in an error; can you guess which?
```
"park"[0]    # option 1
"park"[4]    # option 2
"park"[1:]   # option 3
"park"[:3]   # option 4
```

---
### Advanced slicing
Slicing also supports a third parameter, called _step_. The step parameter specifies which items to return as it traverses the object; a step of 2 returns _every other_ character.

#### `mystring[start:end:step]`
- start and end same as slicing (start and end index position)
- **step**: the number of index places to move; default is 1, 2 would be every other character
 
  - `mystring[::]` and `mystring[::1]` both return `mystring`  
  - _What is happening in these cases?_

---
####  Example of advanced slicing:
- `'hahaha'[1:6:2]` outputs `'aaa'`  

**in plain english**: starting at the beginning of the string, go until you reach index position 6, returning every other letter.

_Note "until you reach" the defined endpoint, not AFTER you pass the endpoint_

---
#### Advanced slicing examples to try
What do you think the following will return?
- `len('hahaha')`
- `'hahaha'[1:5:2]`
- `'hahaha'[1::2]`  (no endpoint defined)
- `'poodle'[::-1]` (no start or end)
- `'poodle'[23]`
- `'poodle'[:23]` (notice the difference from above)
- `'poodle'[23::-1]`

---
### String editing
Strings are _immutable_, meaning a string object cannot be edited in place.

To illustrate, try the following in an interactive python session:
```
mystring = 'poodle'
mystring.replace('p', 'd')
mystring
``` 
What happened?

---
What about assigning by index value?
```
mystring[1] = 'w'
``````

---
While a string object cannot be edited in place, variable names can be re-used and assigned to a new object. Consider:
```
mystring = mystring.replace('p', 'd')
``` 
The variable _mystring_ now points to the newly created object that was made by performing the replace function on the original value of _mystring_.

This is the most common way of "changing" immutable object types in Python.

_can you think of a way to replace the first instance of 'p' with 'd' using indexing?_

---
#### Escape character `\`
- newline is `\n`
- tab is `\t`
- _how would you represent a `\` character within a string?_

---
### Manipulating strings: String methods 
In Python, the various data types are classes that are already coded for you (enter `type("cat")` to see this). 

Each class has a set of functions that are called _methods_.
Methods are accessed via the format:

- `object.methodName(args)`

---
### String methods
String methods take a string object and perform actions on that string based on arguments passed to it in `( )`

The replace method from before is an example: 

`mystring.replace('p', 'd')` where `mystring` is the name of your string object, `'p'` and `'d'` are function arguments - the characters you want to replace and what to replace it with, respectively.

---
String Method - Replace
- `.replace()` 
  - takes 2 arguments, replacing instances of the first with the second
  - searches for a single match criteria ("cat" will replace the substring "cat" in its entirety, not "c" and "a" and "t")

---
String Method - Split
- `.split()` 
  - takes one argument, splitting the string at each instance of the specified character(s)
  - single match criteria
  - returns a list
  - split character(s) are removed
  - calling .split() without an argument will split into words

---
String Method - Join
- `.join()`
  - takes one argument, a **list** of strings, and concatenates them into a single string
  - use with an empty string to join a list (convert to string): \
  `''.join(list)` 

---
String Method - Strip
- `.strip()`
  - removes whitespace from beginning and end of string

---
String Method - Translate (1/2)
- `.translate()`
  - allows substitution and removal of multiple characters
  - returns a string where specified characters are replaced with characters described in a _mapping table_ 
  - use `str.maketrans(x,y,z)` to create the mapping table object
  - str.maketrans takes 3 arguments:
    - x: string of characters to replace
    - y: string of replacement characters (same length as x)
    - z: string of characters to remove

---
String Method - Translate (2/2)
  - Can combine table creation and translate functions:
  `mystring.translate(str.maketrans('', '', 'chars to replace'))`
  _removes everything in 'chars to replace'_
  - use python string library for additional utility (add these in lieu of 'chars to replace' above)
    - `import string`
    - `string.whitespace` - all whitespace characters, `' \t\n\r\x0b\x0c'`
    - `string.punctuation` - all punctuation characters, `'!"#$%&\'()*+,-./:;<=>?@[\\]^_{|}~'`

---
### Python search and select string methods (1/2)
The following are called using the method syntax:
_mystring.functionName()_
- `.startswith('text')`

- `.endswith('text')`
- `.find('text')` / `.rfind('text')`
  - provides offset (integer value) of the first/last  instance of the search text, returns `-1` if not found

---
### Python search and select string methods (2/2)
- `.index('text')` / `.rindex('text')`
  - provides offset (integer value) of the first/last instance of the search text, returns an exception if not found
- `.count('text')` 
  - count the number of times 'text' appears in the string object

---
#### String search and select examples
```
# search a string with find
if "no sea".find("c") == -1:  
  print("i did not find a c")

# search a string with count
if "no sea".count("c") == 0:  
  print("i did not find a c")

# search a string with in
if "c" not in "no sea":
  print("i did not find a c")

"bumblebee".count("b")

"bumblebee".index("w")

"bumblebee".index("b")

"bumblebee".rindex("b")
```

---
#### RECAP: Options for searching strings in Python

- slicing with `[ ]` (covered previously)
- string methods listed above: count( ), find( ), index( )
- regex (requires _re_ library, covered later)

---
### Python len() function
Not a string method, but useful with strings. It is a Python built-in function that can take a string as an argument.

### `len(mystring)`
- return the number of characters in mystring \
_this is a Python built-in function_

---
#### Case & Alignment string functions
- _upper, lower, etc._
- _details avaliable in Ch 5 of Lubanovic text_

---
### Formatting Strings
**Format strings (f strings)** allow you to easily pass in variable values and expressions into strings (Python 3.6+)

F strings begin with an `f` (no quotes), followed by quotes to begin your string and can have variable references inside curly brackets `{ }`. They follow the format:
#### `f"this string uses a {var}"`

---
### f strings (cont'd)
- expressions are allowed within curly brackets `{ }`
  - `f'check out my capitalized string: {mystring.capitalize()}'`
  - `f'the first 4 characters in mystring are: {mystring[:4]}'`

- great with `print` statements

- helpful for debugging
  - in python 3.8+ can use the `=` after a variable name in curly brackets as a shortcut to print a variable name and its value:
  `f'{mystring =}'`

---
Can combine use of f strings and the`.find()` or `.index()` string methods to print descriptive text around where matches occur

```
mystr = "anywhere the wind blows"
 
f'the character before the first w is: {mystr[mystr.find('w')-1]}' 

# slice example
f'the 3 characters before the first w are: {mystr[mystr.find('w')-3:mystr.find('w')]}' 
```

---
### [Go to Lubanovic Ch. 6 Slides](week03_slides.md)






