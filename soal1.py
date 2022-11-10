def hitungBiaya(tipekamar, lamamenginap):
    hargaKamar = [700000, 600000, 800000]
    harga = lamamenginap * hargaKamar[tipekamar-1]
    if harga > 700000:
        diskon = harga * 30 / 100
    elif harga > 500000:
        diskon = harga * 20 / 100
    elif harga > 300000:
        diskon = harga * 10 / 100

    harga_setelah_diskon = harga - diskon
    print(f"Total : Rp. {harga_setelah_diskon}")

listKamar = ["1. Deluxe Double Bed", "2. Deluxe Single Bed", "3. Queen", "4. Keluar Aplikasi"]
while True:
    print(listKamar)
    print("Pilih kamar : ")
    tipekamar = int(input())
    if tipekamar == 4:
        break
    print("Masukkan berapa hari menginap")
    lamamenginap = int(input())
    hitungBiaya(tipekamar, lamamenginap)
    
    