import time
import random
PATH_100='lesson3/arrays/100.txt'
PATH_1000='lesson3/arrays/1000.txt'
PATH_10000='lesson3/arrays/10000.txt'
PATH_100000='lesson3/arrays/100000.txt'
PATH_1000000='lesson3/arrays/1000000.txt'
PATH_RESULT='lesson3/arrays/res.txt'
def write_to_file(path,size):
    arr=[random.randint(-10000,10000) for i in range(size)]
    with open(path,'w') as f:
        for i in arr:
            f.write(str(i)+'\n')
def read_from_file(path):
    a=[]
    with open(path,'r') as f:
        for i in f:
          a.append(int(i))
    return a


def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j+1] < arr[j]:
                 arr[j+1],arr[j]=arr[j],arr[j+1]

temp_arr=read_from_file(PATH_100)
st=time.time()
#
ft=time.time()
rt=ft-st
print(rt)