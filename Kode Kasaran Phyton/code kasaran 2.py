from collections import deque

# Warna Terminal 
MERAH = "\033[91m"
HIJAU = "\033[92m"
KUNING = "\033[93m"
BIRU = "\033[94m"
RESET = "\033[0m"

# Class Ruang
class Ruangan:
    def __init__(self, kode, nama):
        self.kode = kode
        self.nama = nama

# Data Ruangan yang telah urut 
ruangan = [
    Ruangan("E2.01.02", "Ruang 2"),
    Ruangan("E2.01.03", "Ruang 3"),
    Ruangan("E2.01.04", "Ruang 4"),
    Ruangan("E2.01.05", "Ruang 5"),
    Ruangan("E2.01.06", "Ruang 6"),
    Ruangan("E2.01.07", "Ruang 7"),
    Ruangan("E2.01.08", "Ruang 8"),
    Ruangan("E2.01.09", "Ruang 9"),
    Ruangan("E2.01.10", "Ruang 10"),
    Ruangan("E2.02.02", "Lab Analisis Big Data"),
]

# Queue Booking
antrian_booking = deque()

#Data Booking
booking_data = []

#Slot Jam atau Rekomendasi Jam
slot_jam = [
    "07:00-08:40",
    "07:00-09:30",
    "08:00-10:00",
    "09:30-11:30",
    "09:30-12:00",
    "10:00-12:00",
    "13:00-15:00",
    "15:00-17:00"
]

#Binary Search Ruangan
def binary_search_ruangan(kode_ruang):
    kiri = 0
    kanan = len(ruangan) - 1

    while kiri <= kanan:
        tengah = (kiri + kanan) // 2

        if ruangan[tengah].kode == kode_ruang:
            return tengah
        elif ruangan[tengah].kode < kode_ruang:
            kiri = tengah + 1
        else:
            kanan = tengah - 1

    return -1

#Cek Apakah Slot Terbooking
def cek_booking(kode_ruang, hari, tanggal, jam):
    for booking in booking_data:
        if (
            booking["ruang"] == kode_ruang and
            booking["hari"].lower() == hari.lower() and
            booking["tanggal"] == tanggal and
            booking["jam"] == jam
        ):
            return booking
    return None

#Rekomendasi Slot Kosong
def rekomendasi_slot(kode_ruang, hari, tanggal):
    tersedia = []

    for jam in slot_jam:
        if not cek_booking(kode_ruang, hari, tanggal, jam):
            tersedia.append(jam)

    return tersedia

#Status Ruangan
def tampilkan_status_ruangan():
    print("\n=== STATUS RUANGAN ===")

    for ruang in ruangan:
        # Jika ruangan memiliki booking apa pun, status merah
        sudah_booking = any(
            booking["ruang"] == ruang.kode
            for booking in booking_data
        )

        if sudah_booking:
            print(f"{MERAH}{ruang.kode} - {ruang.nama} - TERBOOKING{RESET}")
        else:
            print(f"{HIJAU}{ruang.kode} - {ruang.nama} - TERSEDIA{RESET}")

#Booking Ruangan
def booking_ruangan():
    print("\n=== FORM BOOKING RUANGAN ===")

    nama = input("Nama pemesan       : ")
    kode_ruang = input("Kode ruangan       : ").upper()
    hari = input("Hari               : ")
    tanggal = input("Tanggal (dd/mm/yyyy): ")

    # Cari ruangan menggunakan Binary Search
    indeks = binary_search_ruangan(kode_ruang)

    if indeks == -1:
        print(f"{KUNING}Ruangan tidak ditemukan!{RESET}")
        return

    ruang = ruangan[indeks]

    print(f"\nRuangan dipilih: {ruang.kode} - {ruang.nama}")

    print("\nPilihan Jam:")
    for i, jam in enumerate(slot_jam, start=1):
        print(f"{i}. {jam}")

    try:
        pilihan = int(input("Pilih nomor jam   : "))
        jam = slot_jam[pilihan - 1]
    except (ValueError, IndexError):
        print(f"{KUNING}Pilihan jam tidak valid!{RESET}")
        return

    # Masukkan ke queue
    antrian_booking.append({
        "nama": nama,
        "ruang": kode_ruang,
        "hari": hari,
        "tanggal": tanggal,
        "jam": jam
    })

    print(f"{BIRU}\nBooking masuk ke antrian...{RESET}")

    # Proses queue (FIFO)
    data = antrian_booking.popleft()

    # Cek bentrok booking
    bentrok = cek_booking(
        data["ruang"],
        data["hari"],
        data["tanggal"],
        data["jam"]
    )

    if bentrok:
        print(
            f"{MERAH}\nRuangan {data['ruang']} sudah dibooking oleh "
            f"{bentrok['nama']} pada {bentrok['hari']}, "
            f"{bentrok['tanggal']} jam {bentrok['jam']}.{RESET}"
        )

        # Tampilkan rekomendasi jam kosong
        rekomendasi = rekomendasi_slot(
            data["ruang"],
            data["hari"],
            data["tanggal"]
        )

        if rekomendasi:
            print(f"{HIJAU}\nRekomendasi jam kosong:{RESET}")
            for jam_kosong in rekomendasi:
                print(f"- {jam_kosong}")
        else:
            print(f"{KUNING}Tidak ada slot kosong pada tanggal tersebut.{RESET}")
        return

    # Simpan booking
    booking_data.append(data)

    print(
        f"{HIJAU}\nBooking berhasil!{RESET}\n"
        f"Nama    : {data['nama']}\n"
        f"Ruangan : {data['ruang']}\n"
        f"Hari    : {data['hari']}\n"
        f"Tanggal : {data['tanggal']}\n"
        f"Jam     : {data['jam']}"
    )

#Tampilan Data Bookingannya
def tampilkan_booking():
    print("\n=== DATA BOOKING ===")

    if not booking_data:
        print("Belum ada booking.")
        return

    for i, booking in enumerate(booking_data, start=1):
        print(
            f"{i}. {booking['nama']} | "
            f"{booking['ruang']} | "
            f"{booking['hari']} | "
            f"{booking['tanggal']} | "
            f"{booking['jam']}"
        )

#Cari Ruangan
def cari_ruangan():
    kode = input("Masukkan kode ruangan: ").upper()

    indeks = binary_search_ruangan(kode)

    if indeks != -1:
        ruang = ruangan[indeks]
        print(
            f"{HIJAU}\nRuangan ditemukan!{RESET}\n"
            f"Kode  : {ruang.kode}\n"
            f"Nama  : {ruang.nama}\n"
            f"Indeks: {indeks}"
        )
    else:
        print(f"{MERAH}Ruangan tidak ditemukan.{RESET}")

#Menu utama atau fungsi
def menu():
    while True:
        tampilkan_status_ruangan()

        print("\n=== MENU BOOKING RUANG KELAS ===")
        print("1. Booking Ruangan")
        print("2. Lihat Data Booking")
        print("3. Cari Ruangan (Binary Search)")
        print("4. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            booking_ruangan()
        elif pilihan == "2":
            tampilkan_booking()
        elif pilihan == "3":
            cari_ruangan()
        elif pilihan == "4":
            print("Terima kasih telah menggunakan sistem booking.")
            break
        else:
            print(f"{KUNING}Pilihan tidak valid!{RESET}")

if __name__ == "__main__":
    menu()