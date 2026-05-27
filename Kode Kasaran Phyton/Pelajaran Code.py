from collections import deque
import pandas as pd

# Warna Terminal
MERAH = "\033[91m"
HIJAU = "\033[92m"
KUNING = "\033[93m"
RESET = "\033[0m"

# Class dan Ruang
class Ruangan:
    def __init__(self, kode, nama):
        self.kode = kode
        self.nama = nama

# Data Ruang
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
    Ruangan("E2.02.02", "Lab Analisis Big Data")
]

# Membaca File Excel
try:
    df = pd.read_excel("jadwal_kelas.xlsx")

    # Menghilangkan spasi pada nama kolom
    df.columns = df.columns.str.strip()

    jadwal_excel = df.to_dict("records")

    # Mengambil daftar jam dari Excel
    slot_jam = sorted(df["JAM"].dropna().unique().tolist())

    print("✓ Jadwal Excel berhasil dimuat")

except Exception as e:
    print("✗ Gagal membaca file Excel")
    print(e)

    jadwal_excel = []

    slot_jam = [
        "07:00-09:30",
        "09:30-12:00",
        "13:00-15:30"
    ]

# Queue
antrian_booking = deque()

# Data Booking User
booking_data = []

# Binary Search
def binary_search_ruangan(kode):

    kiri = 0
    kanan = len(ruangan) - 1

    while kiri <= kanan:

        tengah = (kiri + kanan) // 2

        if ruangan[tengah].kode == kode:
            return tengah

        elif ruangan[tengah].kode < kode:
            kiri = tengah + 1

        else:
            kanan = tengah - 1

    return -1

# Cek Booking
def cek_booking(kode_ruang, hari, jam):

    # Cek jadwal dari Excel
    for data in jadwal_excel:

        ruang_excel = str(data.get("RUANG", "")).strip()
        hari_excel = str(data.get("HARI", "")).strip()
        jam_excel = str(data.get("JAM", "")).strip()

        if (
            ruang_excel == kode_ruang
            and hari_excel.lower() == hari.lower()
            and jam_excel == jam
        ):
            return {
                "jenis": "kuliah",
                "matkul": data.get("MATA KULIAH", "-"),
                "kelas": data.get("ROMBEL KELAS", "-")
            }

    # Cek booking user
    for data in booking_data:

        if (
            data["ruang"] == kode_ruang
            and data["hari"].lower() == hari.lower()
            and data["jam"] == jam
        ):
            return {
                "jenis": "booking",
                "nama": data["nama"]
            }

    return None

# Rekomendasi Kelas Kosong
def rekomendasi_jam(kode_ruang, hari):

    kosong = []

    for jam in slot_jam:

        if cek_booking(kode_ruang, hari, jam) is None:
            kosong.append(jam)

    return kosong

# Status Ruangan
def tampilkan_status_ruangan():

    print("\n===== STATUS RUANGAN =====")

    hari = input("Masukkan Hari : ")

    print("\nPilih Jam:")

    for i, jam in enumerate(slot_jam, start=1):
        print(f"{i}. {jam}")

    try:
        pilihan = int(input("Pilih Jam : "))
        jam = slot_jam[pilihan - 1]
    except:
        print("Pilihan tidak valid")
        return

    print()

    for ruang in ruangan:

        status = cek_booking(
            ruang.kode,
            hari,
            jam
        )

        if status:

            print(
                f"{MERAH}{ruang.kode} - {ruang.nama} "
                f"(TERPAKAI){RESET}"
            )

        else:

            print(
                f"{HIJAU}{ruang.kode} - {ruang.nama} "
                f"(TERSEDIA){RESET}"
            )

# Booking Ruangan
def booking_ruangan():

    print("\n===== BOOKING RUANGAN =====")

    nama = input("Nama Pemesan : ")

    print("\nDaftar Ruangan")

    for ruang in ruangan:
        print(f"{ruang.kode} - {ruang.nama}")

    kode = input("\nKode Ruangan : ").upper()

    # Binary Search digunakan di sini
    indeks = binary_search_ruangan(kode)

    if indeks == -1:
        print("Ruangan tidak ditemukan")
        return

    hari = input("Hari : ")

    print("\nPilih Jam:")

    for i, jam in enumerate(slot_jam, start=1):
        print(f"{i}. {jam}")

    try:
        pilihan = int(input("Pilih Jam : "))
        jam = slot_jam[pilihan - 1]
    except:
        print("Pilihan tidak valid")
        return

    # Masuk Queue
    antrian_booking.append({
        "nama": nama,
        "ruang": kode,
        "hari": hari,
        "jam": jam
    })

    # FIFO Queue
    data = antrian_booking.popleft()

    bentrok = cek_booking(
        data["ruang"],
        data["hari"],
        data["jam"]
    )

    if bentrok:

        print(f"\n{MERAH}RUANGAN SUDAH TERPAKAI{RESET}")

        if bentrok["jenis"] == "kuliah":

            print("Kelas       :", bentrok["kelas"])
            print("Mata Kuliah :", bentrok["matkul"])

        else:

            print(
                "Sudah dibooking oleh :",
                bentrok["nama"]
            )

        rekomendasi = rekomendasi_jam(
            data["ruang"],
            data["hari"]
        )

        if rekomendasi:

            print("\nRekomendasi Jam Kosong:")

            for jam in rekomendasi:
                print("-", jam)

        return

    booking_data.append(data)

    print(
        f"\n{HIJAU}BOOKING BERHASIL{RESET}"
    )

# Data Booking
def tampilkan_booking():

    print("\n===== DATA BOOKING =====")

    if not booking_data:
        print("Belum ada booking")
        return

    for i, data in enumerate(
        booking_data,
        start=1
    ):

        print(
            f"{i}. "
            f"{data['nama']} | "
            f"{data['ruang']} | "
            f"{data['hari']} | "
            f"{data['jam']}"
        )

# Menu Utama
while True:

    print("\n==============================")
    print(" SISTEM BOOKING RUANGAN")
    print("==============================")
    print("1. Lihat Status Ruangan")
    print("2. Booking Ruangan")
    print("3. Lihat Data Booking")
    print("4. Keluar")

    pilihan = input("Pilih Menu : ")

    if pilihan == "1":

        tampilkan_status_ruangan()

    elif pilihan == "2":

        booking_ruangan()

    elif pilihan == "3":

        tampilkan_booking()

    elif pilihan == "4":

        print("Program selesai.")
        break

    else:

        print("Menu tidak tersedia.")