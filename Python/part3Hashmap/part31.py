"""
3 ways we may want to viw the data in dictionary

keys only  d.keys()
values only  d.values()

key/value pair (key,value)

reult is iterable
d={'1':1,'2':2,'3':3}

list(d.keys())  ['a','b','c']
list(d.values())  [1,2,3]
list(d.items())   [('1':1),('2':2),('3':3)]

order of all the 3 are smae


the views are dyanamic 
the reflect any change in dictionary


d={'1':1,'2':2,'3':3}

keys=list(d.keys())  ['a','b','c']
values=list(d.values())  [1,2,3]
items=list(d.items())   [('1':1),('2':2),('3':3)]

d['1']=10
print(keys,values,items) // All new values updated


d={'1':1,'2':2,'3':3}

keys=list(d.keys()) 
values=list(d.values()) 
items=list(d.items())  
print(keys,values,items) 
d['1']=10
print(keys,values,items) 


['1', '2', '3'] [1, 2, 3] [('1', 1), ('2', 2), ('3', 3)]
['1', '2', '3'] [1, 2, 3] [('1', 1), ('2', 2), ('3', 3)]

More than just iterable 

the keys view is more than an iterable
the keys() behaves just like a set

makes sense keys are unique 



union,intersection,difference of these key views just like sets

the values() does not behave like a set
they do not  have to be unique and hashable

items behave like a set
elemeents of items are quarenteed to be unique

if all the values are hashable it bahaves like a set


set operations

s1={"a","b","c"}
s2={"b","c","d"}

s1|s2 {'a','b','c','d'}
s1 & s2
s1 - s2

sets do not have guranteed order 
dictionaries have ordered

d1.keys()|d2.keys()
since its a set

no gurantee of any order.



"""




# Dictionary Views Coding

"""
s1={1,2,3}
s2={2,3,3}
s1|s2

s1-s2
s2-s1

d1={'a':1,'b':2,'c':3}
d2=dict(zip('cde',[30,4,5]))

d1,d2

for key in d1:
	print(key)

for k,v in d1.items():
    print(k,v)

d1={'a':1,'b':2,'c':3}

keys= d1.keys()
print(keys);

d1['r']=11;

print(keys);


dict_keys(['a', 'b', 'c'])
dict_keys(['a', 'b', 'c', 'r'])


the keys are actually an iterable

thats why they are updated.


the order of keys items and values are always consistent


list(d1.keys())==list(zip(d1.keys(),d1.values()))
True

d1={'a':1,'b':2,'c':3}
d2={'c':10,'d':20,'e':30}

union= d1.keys() | d2.keys()

type(union)
set

the order will not be maintained


d1=dict(zip('abc',[1,2,3]))
d2=dict(zip('cde',[30,4,5]))
d1,d2

print(d1,d2);

print(d1.items()|d2.items())
d2['c']=3
print(d1.items()|d2.items())

# you will not find ('c',3) twice

{'a': 1, 'b': 2, 'c': 3} {'c': 30, 'd': 4, 'e': 5}
{('d', 4), ('b', 2), ('c', 30), ('a', 1), ('e', 5), ('c', 3)}
{('d', 4), ('b', 2), ('a', 1), ('e', 5), ('c', 3)}

d1.values() | d2.values()

//error this | is not supported for d1.values()


items sometimes behave like a set sometimes not
d1={'a':1}
hash(d1.items()[0])  hashable
d3={'a':[1,2],'b':[3,4]}
d4={'c':[5,6],'d':[3,4]}

hash(d3.items()[])  not hashable
now this time 


d3.items() | d4.items()
now this time they will give me error 
since items are not hashable this time 

create a dic from 2 dictioanry we want dict to have keys from both dictionary and value of the key from both
the dictionary


d1={'a':1,'b':2,'c':3}
d2={'b':2,'c':3,'d':4}

k1=d1.keys()
k2=d2.keys()

k1&k2

new_dict={}
for key in d1.keys()&d2.keys():
	new_dict[key]=(d1[key],d2[key])
print(new_dict)

new_dict={key:d1[key],d2[key]   for key in d1.keys()&d2.keys()}	

retain the only keys also

d1={'a':1,'b':2,'c':3}
d2={'b':2,'c':30,'d':4}


if values are same pick anyone 
but if values are not same pick from seocnd dictionary only.


for i in d1.keys()|d2.keys():
	if i in d1 and i in d2:
		dict[i]=d2[i]
    else:
    	if i in d1:
    		dict[i]=d1[i];
        else:
            dict[i]=d2[i];  


pick only from the scecond which only exist in the first.

d1={'a':1,'b':2,'c':3,'d':4}
d2={'b':2,'c':30,'d':4,'e':4}

create a dictionary which contains d and e

for i in d1.keys()-d2.keys()|d2.keys()-d1.keys():
	print("i",i)


his solution 

union=         d1.keys()|d2.keys()
intersection=  d1.keys()&d2.keys()

for i in union-intersection:
    print(i);


for i in union^intersection:
    print(i);

now how to pick up the value we know each key is in either dictionaryw we dont know which one.
pick up from both dictionary and retain which is not none

d1.get(i,'None')

dict={}
for i in union-intersection:
    if d1.get(i,'None')=='None':
    	dict[i]=d1[i];
    else:
    	dict[i]=d2[i];

 Same
 
for i in union-intersection:
	x=d1.get('i','None') or d2.get('i','None') 
    dict[i]=x

print(dict);  


his way

for i in d1.keys()^d2.keys():
	x=d1.get('i','None') or d2.get('i','None') 
    dict[i]=x;

print(dict);      

        	
"""