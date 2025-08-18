"""
hah(obj) some interger sys.ahs_info.width
if not integer we will receive an error
int float complex binary Decimal Fraction -> immutable
string

If an object is hashable
    the hash object must be an integer value
    if  two objects compare equal(==) the hashes must be equal.

Important
two object that are not equal mat still have same hash value.

later creating our own custom hashes    




{
	key1:value1,
	key2:value2,
	key3:value3,
	key4:value4
}

any hashable object any object

dict(key1=value1,key2=value2,key3=value3)


{
	(0,0): 'origin'
}

dict() here we cannot create a key with tuple (0,0)

built dictionary using dictionary comprehension

same basic syntax   ->  enclosed in  {}
                    ->  elements must be specified as key:value

{str(i): i**2 for i in range(1,5)};
{str(i): i**2 
         for i in range(1,5)
         if i%2 ==0 }
{
	'2':4,
	'3':9
}

Creating dictionary fromkeys()
class method on dictionary

creates a dictionary with specified keys all assigned to the same value

d= dict.fromkeys(iterable,value);

iterable
contains the keys
hashable elements

d= dict.fromkeys([(0,0),'a',100],'N/A');
d= dict.fromkeys([i**2 for i in range(1,5)],'N/A');


"""



a={'k1':100,'k2':200};
type(a)
#dict


# python3.5 or abouve the insertion order is maintained.
# print(a) now the order in which the keys were inserted may not be the one we are seeing.
hash((1,2,3))
# hashvalue

hash((1,2,3))
# same hashvalue

d={(1,2,3):'this is a tuple'};

hash(t1)===hash(t2)

t1 is t2
#False
id(t1),id(t2)
# they are not the same value

d[t1]==d[t2]
# same value
# its using equality of the keys 

def my_funct():
	pass

hash(my_funct)
#-922

d={my_funct:[10,20,30]}

def fn_add(a,b):
	return a+b;

def fn_inv(a):
	return 1/a;

def fn_mul(a,b):
	return a*b;		



d={fn_add:(10,20),fn_inv:(10,),fn_mul:(10,20)}

for f in d:
    print(f(*d[f]))


for f,items in d.items():
    print(f(*items))


print("Hello World")
d= dict(x=100,a=200);

d=dict([('x',100),('a',200)]);
d={'x':100,'a':200}
id(d)
dict=dict(d);
id(dict)
#id of both will be different
we made a copy of dictinary


d={'c':[1,2,3]}
dict=dict(d={'c':[1,2,3]})

d['c'].append(5)

#now these changes will be visible in dict
#because its shallow copy

d['c'] is dict('c'):
its true

but since dict was a dictionary what happened
its a shallow copy



#using comprehension for dict


keys=['a','b','c']
values=(1,2,3)

for k,v in zip(keys,values):
	print("key",k,"   ",v)

dict1={k,v for k,v in zip(keys,values)}	

ke='abcd'
ve=range(1,5)

for k,v in zip(ke,ve):
    print(k,v)


x_coords= (-2,-1,0,1,2);    
y_coords= (-2,-1,0,1,2);

grid=[(x,y) for x in x_coords
            for y in x_coords]

print("grid",grid);            

import math:

sqrt_2= math.hypoteneous(1,1);

import math
grid=[(x,y) for x in x_coords
            for y in x_coords]

print("grid",grid);  

for i in grid:
    print(math.hypot(*i))

grid_extended=[(x,y,math.hypot(x,y)) for x,y in grid]
print(grid_extended)  

grid_extended_dict={(x,y):math.hypot(x,y) for x,y in grid}
print(grid_extended)  



d1= dict.fromkeys([(0,0),'a',100],'N/A');
d2= dict.fromkeys([i**2 for i in range(1,5)],'N/A');
d3= dict.fromkeys('python')