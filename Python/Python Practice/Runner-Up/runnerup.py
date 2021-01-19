if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr1=set(arr)
    arr1=sorted(arr1,reverse=True)
    print(arr1[1])
    