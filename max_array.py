arr = list(map(int,input("Enter elements : ").split()))
L=0
H=len(arr)-1

while L<=H:
    mid = (L+H)//2
    L=mid+1

print("max-element : ",arr[H])