import time
import random
import numpy

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


def writeresult(path,data):
    with open(path,'a+') as f:
        f.write(str(data)+'\n')
        

def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j+1] < arr[j]:
                 arr[j+1],arr[j]=arr[j],arr[j+1]


def comb(arr:numpy.array):
    step=len(arr)
    swap=True
    while swap or step > 1:
        step=int(step//1.247) 
        swap=False
        for i in numpy.arange(arr.size-step):
            j=i+step
            if arr[j] <  arr[i]:
                arr[j],arr[i]=arr[i],arr[j]
                swap=True


def quick_sort(arr):
    if len(arr) < 1:
        return arr
    else: 
        q=sum(arr)//len(arr)
        l=[]
        m=[]
        r=[]
        for i in arr:
            if i > q:
                r.append(i)
            elif i< q:
                l.append(i)
            else:
                m.append(i)
        return quick_sort(l)+m+quick_sort(r)

temp_arr=numpy.array(read_from_file(PATH_100000))

st=time.time()
comb(temp_arr)
ft=time.time()
rt=ft-st
writeresult(PATH_RESULT,f'combn100000 {rt}')