from typing import List
print("hello world")


def permute(abc: List[int], start_index: int, list: List[List[int]]):
    length = len(abc)
    print("hello",abc, start_index, length)
    if start_index == length - 1 :
        list.append(abc[:])    
    else:    
        for i in range(start_index,length):
            print("range",i, start_index)
            abc[start_index],abc[i] = abc[i],abc[start_index]
            permute(abc, start_index+1, list)
            abc[start_index],abc[i] = abc[i],abc[start_index]

abc = [1,2,3]
list = []
permute(abc,0,list)
print(list)

