
#Consuming Iterators Manually 
s='i sleep all the night and i work all day';

for char in s:
   print(char)


iter_s= iter(s);# now this returns an ietrator 
next(iter_s);
# s is an iterable 


with open("file.csv") as file:
	for line in file:
		print(line);

with open("file.csv") as file:
	file_iter=iter(file);
	headerName = next(file_iter).strip('\n').split(';')
    headerTypes = next(file_types).strip('\n').split(';');
    headerValues = next(file_iter).strip('\n').split(';');
    print('ddsd',headerName,headerTypes,headerValues);

from collections import namedtuple
cars=[];
with open("file.csv") as file:
	file_iter=iter(file); #returns an iterator
	headerName = next(file_iter).strip('\n').split(';')
    headerTypes = next(file_types).strip('\n').split(';');
    Car=namedtuple(headerName);
    for line in file_iter:
    	headerValues = line.strip('\n').split(';');
        headerValues=cat_row(headerTypes,headerValues);
        cars.push(Car(*headerValues));
        print('ddsd',headerName,headerTypes,headerValues);    



def cat_row(data_type,data_row):
	return [cast_object(data_type,value) for data_type,value in zip(data_type,data_row)];

def cast_object(data_type,value):
	if data_type == 'DOUBLE':
		return float(value);
	elif data_type == 'INT':
		return int(value);
	else:
		return str(value);				








