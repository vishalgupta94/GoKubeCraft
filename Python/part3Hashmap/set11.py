"""
an unordered collection of distinct objects.


there is no particular ordering in a set
   {1,3,5}   {5,1,3}    {3,5,1}  are all the same sets (equal)

   they are equla to each other.

   {1,1,3}  not possible element 1 is repeated


   All set elements must be hashable
   elements are not equal we can check using (==)



   membership 
   x in s
   x is not in s

   in operator is actually a question that returns True and False


Unions and Intersections

s1 union s2

all elements either in s1 or s2 or may be both
s=s1 | s2

s1.union(s2)
s1&s2 intersection

s1={1,2,3}
s2={3,4,5}

s1-s2 {1,2}
s2-s1 {4,5}

symmetric 


(s1|s2) - (s1&s2)
  s1^s2
set() empty set {} creates an empty dictionary

s1-s2
 nothing

no elements 

len(s1 & s2) -> 

s1.isdisjoint(s2)  True

SuperSets and Sibsets

A set s1 is a subset of s2 if all the elements of s1 are in s2 


s1<=s2                   #s1 is a subset of s2.
s1.issubset(s2)          {1,2,3}  <= {1,2,3}  True

A set is a proper of s2 if s1 is a subset of s2 and s1 is not equal to s2.


s1 < s2

proper subset 
s1 is subset of s2
s2 is subset of s1
                    {1,2,3}  <= {1,2,3}    False
                    {1,2,3}  <= {1,2,3,4}  True 








s1 >= s2
s1.issuperset(s2)
A set is a superset of s2 if s2 is a subset of s1
                           superset





A set is a proper superset of s2 if s2 is a subset of s1
                                  proper superset

s1 > s2




"""