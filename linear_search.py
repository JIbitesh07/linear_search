def linearsearch(arr,x):
    for i in range(0,len(arr)):
        if(arr[i]==x):
            return 1
        return 0

arr=[56,4,32,12,34]
x=int(input("enter a number"))

k=linearsearch(arr,x)
print(k)
if(k==1):
    print("present")
else:
    print("not present")
