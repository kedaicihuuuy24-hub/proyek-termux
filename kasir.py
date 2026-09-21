from datetime import datetime

while True:
    print()
    print("=== KASIR KEDAI ===")
    print("1. Seblak       Rp10.000")
    print("2. Mie Nyemek   Rp10.000")
    print("3. Baso Mercon  Rp10.000")
    print("0. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "0":
        print("Terima kasih!")
        break

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
        print("Menu tidak tersedia!")
        continue

    jumlah = int(input("Jumlah: "))
    total = harga * jumlah

    print()
    print("=== STRUK ===")
    print("Menu   :", menu)
    print("Jumlah :", jumlah)
    print("Total  : Rp", total)

    bayar = int(input("Uang bayar: Rp "))

    if bayar < total:
        print("Uang tidak cukup!")
        print("Kekurangan: Rp", total - bayar)
        continue

    kembalian = bayar - total
    print("Kembalian: Rp", kembalian)

    waktu = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    with open("transaksi.txt", "a") as file:
        file.write("================================\n")
        file.write("Waktu     : " + waktu + "\n")
        file.write("Menu      : " + menu + "\n")
        file.write("Jumlah    : " + str(jumlah) + "\n")
        file.write("Total     : Rp " + str(total) + "\n")
        file.write("Uang bayar: Rp " + str(bayar) + "\n")
        file.write("Kembalian : Rp " + str(kembalian) + "\n")
        file.write("================================\n\n")

    print("Transaksi berhasil disimpan.")
