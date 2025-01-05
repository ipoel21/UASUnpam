def binary_search(arr, target):
    kiri, kanan = 0, len(arr) - 1
    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        if arr[tengah] == target:
            return tengah
        elif arr[tengah] < target:
            kiri = tengah + 1
        else:
            kanan = tengah - 1
    return -1

def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

# Contoh penggunaan
dataset_a = [1, 3, 5, 7, 9, 11, 13, 15]
dataset_b = [12, 7, 5, 9, 1, 3, 11, 15]
print(f"Data Terurut {dataset_a}")
print(f"Data Tidak Terurut {dataset_b}")
target = int(input("Data yang ingin Di cari : "))
result1 = binary_search(dataset_a, target)
if(result1 == -1):
    print(f"Binary Search (Data Terurut) :  Data Tidak Di temukan")
else:
    print(f"Binary Search (Data Terurut) : Target {target} ditemukan di indeks: {result1}")
result2 = linear_search(dataset_b, target)
if(result2 == -1):
    print(f"Linear Search (Data Tidak Terurut) : Data Tidak Di temukan")
else:
    print(f"Linear Search (Data Tidak Terurut) : Target {target} ditemukan di indeks: {result2}")
