"""
update merging and copying dictionary

the update method

d1.update(d2)
d1.update(iterable) #iterable must contain iterables with 2 elements (key,value)

d1.update(keywords-args)


d1.update(d2)

for every (k,v) in d2:
    if k not in d1,inserts(k,v) in d1
    if k in d1,updates the value of k in d1


d1={'a':1,'b':2}
d1={'b':20,'c':30}

d1.update(d2)

d1={'a':1,'b':20,'c':30}    

d1.update(b=20,c=30)

((,),(,))  ((,),[,])  [(,),(,)]
d1.update(iterable)


d1.update((k,ord(k) for k in 'bcd')))


Unpacking a dictinoary

def func(**kwargs):
    print(kwargs)

d={'a':1,'b':2}

func(**d)

d1={'a':1,'b':2}
d2={'a':10,(0,0):2}  # we cannot pass d2 to func it will not work deep understanding required
d3={'b':1,'c':2}


d={**d1,**d2,**d3}
d={'a':1,'b':2,'a':10,(0,0):2,'b':1,'c':2}
last update wins



Copying dictionary


Shallow objects
container object is a new object
copied containers elements keys/values shared references with original object

d_copy=d.copy()
d_copy={**d}
d_copy=dict(d)

d_copy={k:v for k,v in d.items()};


Deep Copies

If a shallow copy is not sufficient, we can create deep copies of dictinaries
no shared references
even with nested dictinoary


can do it ourselves

true deep copy
similiar to use copy.deepcopy


from copy import deepcopy
works with custom object,iterables dictionaries etc.


"""





d1={'a':1,'b':2}
d2={'c':3,'d':4}

d1.update(d2)
print(d1)

d1.update(b=20,c=30,x=40)

d1.update(ietrable)
d1.update([('c':2) ,('d',3),['e',4] ])

order is maintianed cde keys will always be in the last.
update(generator expression)

d1.update((i:ord(i)  for i in 'python'))
#keys python will added in last in dictionary
l1=[1,2,3]
l2='abc'
l=(*l1,*l2)
print(l);
l is new object

d={**d1,**d2}
#d2 will override the keys with keys of d1.
conf_default=dict.fromkeys('host','port','user','pwd','database',None)
# value of each of these keys will be None

conf_defaults={}
conf_global={'port':5432,'database':'deepdive'}

conf_dev= {
    'host':'localhost',
    'user':'test',
    'pwd':'test'
}


conf_prod= {
    'host':'prodhost',
    'user':'$prod_user',
    'pwd': '$prod_pwd',
    'database':'deepdive_prod'
}

# conf_defaults-->global --> dev/conf_prod


conf={**conf_defaults,**conf_global,**conf_dev}


#keys of conf dev is possible will overlap the other key value pair.

#passing key workd arguments to the function
def my_func(*,key_1,key_3,key_3):
    pass

d={'key_1':1,'key_2':2,'key_3':3}    
my_func(**d)


def my_func(**kwargs):
    for k,v in kwargs.items():
        print(k,v)

my_func(the order of keys matter here)


Copies of dicitonary

d= {'a':[1,2],'b':[3,4]}
d1=d.copy()

id(d),id(d1) #they are different object
but


id(d['a'])==id(d1['a'])  # they are different objects

d['a'] is d1['a']


from copy import deepcopy

d={
   'id':12345,
   'person':{
                'name': 'John',
                'age': 78
            },
    'posts':[100,105,200]        
  }

d_deep   = deepcopy(d);
d_shallow = d.copy();  

id(d) == id(d_deep) == id(d_shallow)
# all will be diiferent

 id(d['posts']) == id(d_shallow['posts']) == id(d_deep['posts'])
#same              same                      different

#same with tghe person key
d1 = {'a':[1,2],'b':[3,4]}
d  = {**d1,'c':100}
 # diffeent id

id(d['a'])==id(d1['a'])


# 3 ways fo doing a shallow copy

dict()
{**d} 

d1={k,v for k,v in d.items()}

from random import randomint

big_d={k: randint(1,100) for k in range(1_000_000)} 
len(big_d)
#1_000_000

def copy_unpacking(d):
    d1= {**d}

def copy_copy(d):
    d1= d.copy()

def copy_direct(d):
    d1= dict(d)

def copy_comrehension(d):
    d1= {k,v for k,v in d.items()}  

# All create shallow copies

def copy_deepcopy(d):
    d1= deepcopy(d)


from timeit import timeit
timeit('copy_unpacking(big_d)',globals=globals(),number=100)
timeit('copy_copy(big_d)',globals=globals(),number=100)
# 2 seconds
timeit('copy_comprehension(big_d)',globals=globals(),number=100)    
#significantly slow 5 seconds

timeit('copy_deepcopy(big_d)',globals=globals(),number=100) 
# 93 seconds
# shallow copy is slowe deep copy is very slow
# 