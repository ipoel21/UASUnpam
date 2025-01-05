x = 1

def merge_sort(arr, indexSort):
    if len(arr) > 1:
        tengah = len(arr) // 2
        setengahKiri = arr[:tengah]
        setengahKanan = arr[tengah:]

        merge_sort(setengahKiri,indexSort)
        merge_sort(setengahKanan,indexSort)

        i = j = k = 0

        while i < len(setengahKiri) and j < len(setengahKanan):
            if setengahKiri[i][indexSort] <= setengahKanan[j][indexSort]:  
                arr[k] = setengahKiri[i]
                i += 1
            else:
                arr[k] = setengahKanan[j]
                j += 1
            k += 1

        while i < len(setengahKiri):
            arr[k] = setengahKiri[i]
            i += 1
            k += 1

        while j < len(setengahKanan):
            arr[k] = setengahKanan[j]
            j += 1
            k += 1
    # print("Hasil ke: ",sortKe, " ",arr )

# Contoh penggunaan
orders = [
    (1, "BSD", "Ciputat", "2025-01-01 07:00"),
    (2, "Pamulang", "Alam Sutra", "2025-01-01 08:00"),
    (3, "Serpong", "Pamulang", "2025-01-01 01:00"),
    (4, "Pamulang", "Ciledug", "2025-01-01 09:00"),
    (5, "Ciledug", "BSD", "2025-01-01 02:00")
]
print("=================================")
print("(Id, Penjemputan, Tujuan, Waktu)")
print("=================================")
for data in orders:
    print(data)

print("""kolom yang ingin di urutkan
1. Id
2. Lokasi Penjemputan
3. Lokasi Tujuan
4. Waktu Pemesanan """)

orderBy = int(input("Sort Berdasarkan : ")) - 1

merge_sort(orders, orderBy)
print("Data pesanan setelah diurutkan:")
print("=================================")
print("(Id, Penjemputan, Tujuan, Waktu)")
print("=================================")
for data in orders:
    print(data)
