def binary_search_nex_lanrger(data, target):
    low = 0
    high = len(data) - 1
    next_larger = None

    while low <= high:
        mid = (low + high) // 2

        if data[mid] > target:
            nex_lanrger = data[mid]
            high = mid - 1
        else:
            low = mid + 1

    return nex_lanrger

my_list = [2, 4, 6, 8, 10, 12, 14]
target = 7

result = binary_search_nex_lanrger(my_list, target)

if result:
    print(f"Elemen terkecil yang lebih besar dari {target}: {result}")
else:
    print(f"Tidak ada elemen yang lebih besar dari {target} dalam daftar.")
