"""
d[key]=value
if the key does not exit it will create or it will replace the key

d[key_does_exit]
#exception key_error occured

d.get(key_does_exist)
#None if key not found


d.get(key,default)
if no default is given 'None' is returned
membership testing to check if the key actually exist or not

key in d 
key not in d
len(d)

d.clear(); d is empty now

del d[key]  Removing Elements from a Dictionary
d.pop(key) removes the key from dictionary and returns a values
if the key does not exist KeyError exception may occur 
to solve this

d.pop(key,default)


Another way to remove items from dictionary

Python3.6

d.popitem() returns a tuple key and value
KeyError
prior 3.6 it removes any item from dictionary after 3.6 it removes last item from dictionary

last inserted first out

inserting key with default

d={'a':1,'b':3}
#insert only if key does not exist

if c not in d:
	d['c']=0

combine this with newly inserted value , or existing value if already there.

def insert_if_not_present(d,key,value):
	if key not in d:
		d[key]=value
		return value
	else:
	    return d[key]

instead 

result= d.setdefault(key,value)
	    	



"""


text= ''

counts= dict();

for i in text:
	counts[i]=counts.get(c,0)+1

print(counts);

for i in text:
    key=c.lower().strip();
    counts[key]=counts.get(key,0)+1

d==dict.fromkeys('abcd',0);

del(d['z'])
// Key Error

result=d.pop('z')
//KeyError key does not exist

result=d.pop('z',0);
d=dict({i:i**2 for i in range(1,5)});


d.popitem();

d={'a':1,'b':2,'c':3}
result=d.setdefault('d',4);
print(result);


import string;

print(string.ascii_lowercase)
print(string.ascii_uppercase)

import string;

print(string.ascii_lowercase)
print(string.ascii_uppercase)

d={i:0 for i in string.ascii_lowercase};
print(d);


text='importSTringABCDEFGH???@#$%&IJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
category={};
for c in text:
    if c != ' ':
        if c in string.ascii_lowercase:
            key='lower'
        elif c in string.ascii_uppercase:
            key='upper'
        else:
            key='other'
        
        if key not in category:
            category[key]=set();
        
        category[key].add(c);
    
    
for key in category: 
    print(f'{key}: ',''.join(category[key]))
        

categories={};

for c in text:
	key= cat_key(c);
	if key:
		categories.setdefault(key,set()).add(c);


def cat_key(c):
	cat_1={' ':None}
	cat_2=dict.fromkeys(string.ascii_lowercase,'lower')
	cat_3=dict.fromkeys(string.ascii_uppercase,'upper')

	# categories= dict(chain(cat_1.items(),cat_2.items(),cat_3.items()  ))
	categories= {**cat_1,**cat_2,**cat_3}
    
    return categories.get(c,'other')
dict4=dict.fromkeys(string.ascii_uppercase,'Upper')

print(**dict4)


# clear dictionary
d=dict(zip('abc','def'));



