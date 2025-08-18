/*

We can also slice general iterables(inclding iterators of course)

islice(iterable,start,end,step);
l=[1,2,3,4]

result= islice(l,0,3);
result is an lazy iterators

list(result);
[1,2,3]




SELECTING and FILTERING

filter(predicate,iterable)
when predicate is true


predicate can be None in which case it is the identity function 
  in other words truthy elements only will be retained.RANKS

filter returns a lazy iterators

iterator (item for item in iterable if pred(item))

filter(lambda x: x<4, [1,2,3,4,5,6,7])  its an iterator  =>   1,2,3
filter(None,[0,'','hello',100,False]) truthy value 'hello',100


filterfalse reverse of filter

data=['a','c','c','d','e']
selector=[True,False,1,0]

compress(data,selector)
a,c
returns truthy for selector

itertool.takewhile 


returns an itertors until predicates turns false after that it does not take any item
takewhile(lambda x : x<5,[1,3,5,2,1]);

1,3


dropwhile(lambda x : x<5,[1,3,5,2,1]);
5,2,1 lazy iterators












*/