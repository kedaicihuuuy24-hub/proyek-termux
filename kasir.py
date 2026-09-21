print("=== KASIR KEDAI ===")
print("1. Seblak       Rp10.000")
print("2. Mie Nyemek   Rp10.000")
print("3. Baso Mercon  Rp10.000")

pilihan = input("Pilih menu: ")
jumlah = int(input("Jumlah: "))

if pilihan == "1":
    menu = "Seblak"
    harga = 10000
elif pilihan == "2":
    menu = "Mie Nyemek"
    harga = 10000
elif pilihan == "3":
    menu = "Baso Mercon"
    harga = 10000
else:
    print("Menu tidak tersedia")
    exit()

total = harga * jumlah

print()
print("Total belanja: Rp", total)

bayar = int(input("Uang bayar: Rp "))

if bayar < total:
    print("Uang tidak cukup!")
    print("Kekurangan: Rp", total - bayar)
else:
    kembalian = bayar - total

    print()
    print("=== STRUK ===")
    print("Menu      :", menu)
    print("Jumlah    :", jumlah)
    print("Total     : Rp", total)
    print("Uang bayar: Rp", bayar)
    print("Kembalian : Rp", kembalian)
