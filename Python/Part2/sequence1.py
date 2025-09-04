'''
what is a sequence 

we can refer to any item in sequence usinhg its index number VIP 
so we have concept of first second element and we have a concept of posotinal ordering. 
Python list have positional ordering and set do not,

List is a sequence type,
set are not sequence type.

Builtin sequence type

mutable     lists bytearrays 
immutable   strings tuples range bytes


Homegeneous vs Hetrogeneous Sequences 

Strings are homogeneos sequences 
   each element is of the same type (a character)   'python'


Lists are hetrogeneours sequences 
    each elements may be different type

What does it mean for an object to be iterable?????
  is its a container type of object and we can list out the elements in thayt object one by one;

But an iterable are generalyy not a sequence type iterables are more general  

Set is iterable but not sequence,
Iterables are general.



Standard sequence methods

method -> 
  x in s
  x not in s

  # check whether object is in sequence or not

method -> len(s)

method -> s1+s2

method -> 
s.index(x)

s.index(x,i)

s.index(x,i,j)

s[i]

s[i:j]

Immutable sequence may support hashing.

x = [1,2]  a = x+x  = [1,2,1,2]

x = 'python'  a = x+x  = 'pythonpython'

#beware of concatenation
x = [ [0,0] ]

x+x = [[0,0],[0,0]]  id of both of them is same

a = [1,2]*2 a -> [1,2,1,2]

a = 'python' a*2 -> 'pythonpython'

#this will create problem 
a = [ [0,0] ] a*2 [ [0,0] [0,0]  ]  




#coding

l = [1,2,3]
t = (1,2,3)
s = 'python'

//supports indexing
// iterable

for c in l:
for c in t:
for c in s:

s = {1,2,3,4}

for e in s:
  print(e)
  
  its iterable, but not a sequence type.mro
  

l = [1,2,3]
l[0] = 100 #mutable


'a' in ['a','b',100] -> True

[1,2,3]+(1,2,3) -> fail





