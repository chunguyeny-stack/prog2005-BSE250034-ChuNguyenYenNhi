def sap_xep_gaim_dan(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
arr2 = [4, 7, 8, 30, 33, 7, 8, 11, 78]
sap_xep_gaim_dan(arr2)
print("Sau khi sắp xếp giảm dần:", arr2)
