import random
import timeit
def deter(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
def rand(arr,low,high):
    ind=random.randint(low,high)
    arr[ind],arr[high]=arr[high],arr[ind]
    return deter(arr,low,high)
def quick(arr,low,high,selector):
    if low<high:
        pivot=selector(arr,low,high)
        quick(arr,low,pivot-1,selector)
        quick(arr,pivot+1,high,selector)
if __name__=="__main__":
    arr=[]
    n=int(input('Enter the no of elements:'))
    for i in range(n):
        arr.append(int(input()))    
    arr2=arr.copy()
    ch=0
    while ch!=3:
        print('1.deter\n2.rand\n3.exit')
        ch=int(input())
        if ch==1:                  # worst (O(n^2))
            deterministic=timeit.timeit("quick(arr2,0,len(arr)-1,deter)",globals=globals(),number=10)
            print(arr2)
            print(f'deterministic approach: {deterministic:.6f} seconds')
        elif ch==2:               #average  (O(n \log n))
            randomize=timeit.timeit("quick(arr,0,len(arr)-1,rand)",globals=globals(),number=10)
            print(arr)
            print(f'randomized approach: {randomize:.6f} seconds')
        elif ch==3:
            exit(0)
        else:
            print('Enter valid choice')
'''
Summary
If you are sorting random data: Randomized quick sort is likely to be faster and more efficient.
If you are sorting data that is already sorted or nearly sorted: Deterministic quick sort may perform poorly, while randomized quick sort will still maintain good performance.


Execution Time:
For randomly generated input, you will likely find that the randomized quick sort (rand) performs better than the deterministic quick sort (deter) in terms of time taken.
If the input is sorted or nearly sorted, the deterministic version may take significantly longer due to its worst-case time complexity.

'''