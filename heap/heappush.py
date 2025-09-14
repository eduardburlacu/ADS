def heappush(arr:list[int], val:int)->None:
    arr.append(val)
    #Sift-up
    node = len(arr)-1
    parent = (node-1) //2
    while parent>=0 and arr[parent] > arr[node]:
        arr[node], arr[parent] = arr[parent], arr[node]
        node = parent
        parent = (node-1)//2

if __name__ == "__main__":
    arr = [3, 0, 9, 4, 5, 6, 7, 8, 1, 2]
    heappush(arr, -1)
    print(arr) 