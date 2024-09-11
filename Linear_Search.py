def Linear_Search(arr,n):
    count=0
    for i in range(len(arr)):
        if arr[i]==n:
            count=1
            break
    if count==1:
        print("Element is found at",i)
    else:
        print("Element is not Found")



arr=list(map(int,input().split()))
n=int(input("Enter the element to be searched:"))
Linear_Search(arr,n)
