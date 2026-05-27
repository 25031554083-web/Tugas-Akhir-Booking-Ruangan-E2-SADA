import pandas as pd

# ── ROMBEL dari Google Sheets ──────────────────────────────
rombel_list = [
    "INT 24","2024 A","2024 B","2024 C","2024 D","2024 E","INT 25",
    "2025 A","2025 B","2025 C","2025 D","2025 E","2025 F","2025 G"
]
rombel_df = pd.DataFrame({
    "kode_rombel": rombel_list,
    "nama_rombel": [f"Sains Data {r}" for r in rombel_list],
    "jurusan": ["Sains Data"] * len(rombel_list),
    "angkatan": [
        2024,2024,2024,2024,2024,2024,
        2025,2025,2025,2025,2025,2025,2025,2025
    ]
})
rombel_df.to_csv("data_rombel.csv", index=False)
print("✅ data_rombel.csv dibuat:", len(rombel_df), "rombel")

# ── RUANG dari Google Sheets ─────────────
ruang_list = [
    ("E2.01.02","Ruang E2.01.02","40","Gedung E2 Lt.1"),
    ("E2.01.04","Ruang E2.01.04","40","Gedung E2 Lt.1"),
    ("E2.01.06","Ruang E2.01.06","40","Gedung E2 Lt.1"),
    ("E2.01.07","Ruang E2.01.07","40","Gedung E2 Lt.1"),
    ("E2.01.08","Ruang E2.01.08","40","Gedung E2 Lt.1"),
    ("E2.01.09","Ruang E2.01.09","40","Gedung E2 Lt.1"),
    ("E2.01.10","Ruang E2.01.10","40","Gedung E2 Lt.1"),
    ("E2.02.02/LAB","Lab E2.02.02","30","Gedung E2 Lt.2"),
]
ruang_df = pd.DataFrame(ruang_list, columns=["kode_ruang","nama_ruang","kapasitas","gedung"])
ruang_df.to_csv("data_ruang.csv", index=False)
print("✅ data_ruang.csv dibuat:", len(ruang_df), "ruang")

# ── JADWAL EXISTING (dari Sheets) ─────────────
jadwal = [
    # Senin
    ("2025 A","Senin","07:00","09.30","E2.02.02/LAB", "Struktur Data Dan Algoritma"),
    ("2025 C","Senin","07:00","09:30","E2.01.09","Kalkulus Lanjut"),
    ("2025 D","Senin","07:00","09:30","E2.01.02","Teori Probabilitas"),
    ("2025 G","Senin","07:00","09:30","E2.01.08","Interaksi Manusia Dan Komputer"),
    ("2025 A","Senin","09:30","12:00","E2.02.02/LAB","Interaksi Manusia Dan Komputer")
    ("2025 D","Senin","09:30","12:00","E2.01.04","Kalkulus Lanjut"),
    ("2025 F","Senin","09:30","12:00","E2.01.08","Teori Probabilitas"),
    ("2025 G","Senin","09:30","12:00","E2.01.02","Teori Probabilitas"),
    ("INT 25","Senin","09:30","12:00","E2.01.10","Teori Probabilitas"),
    ("2024 A","Senin","13:00","15:30","E2.01.02","Penambangan Data"),
    ("2024 B","Senin","13:00","15:30","E2.01.04","Penambangan Data"),
    ("2024 D","Senin","13:00","15:30","E2.01.08","Analisis Data Eksploratif"),
    ("2024 E","Senin","13:00","15:30","E2.01.07","Pembelajaran Mesin"),
    ("2025 A","Senin","13:00","15:30","E2.01.06","Teori Probabilitas"),
    ("2025 B","Senin","13:00","15:30","E2.02.02/LAB","Struktur Data Dan Algoritma"),
    ("2025 F","Senin","13:00","15:30","E2.01.09","Interaksi Manusia Dan Komputer"),
    ("INT 25","Senin","13:00","15:30","E2.01.10","Kalkulus Lanjut"),
    # Selasa
    ("2024 B","Selasa","07:00","09:30","E2.01.02","Analisis Data Eksploratif"),
    ("2024 E","Selasa","07:00","09:30","E2.01.04","Penambangan Data"),
    ("2025 B","Selasa","07:00","09:30","E2.01.08","Interaksi Manusia Dan Komputer"),
    ("2025 C","Selasa","07:00","09:30","E2.02.02/LAB","Struktur Data Dan Algoritma"),
    ("2025 E","Selasa","07:00","09:30","E2.01.09","Interaksi Manusia Dan Komputer"),
    ("INT 24","Selasa","07:00","09:30","E2.01.10","Pengolahan Citra Digital"),
    ("2024 A","Selasa","09:30","12:00","E2.01.02","Analisis Multivariat"),
    ("2024 C","Selasa","09:30","12:00","E2.01.08","Analisis Multivariat"),
    ("2024 D","Selasa","09:30","12:00","C01.04.03","Pembelajaran Mesin"),
    ("2024 E","Selasa","09:30","12:00","E2.01.09","Analisis Data Eksploratif"),
    ("2025 D","Selasa","09:30","12:00","E2.02.02/LAB","Struktur Data Dan Algoritma"),
    ("INT 25","Selasa","09:30","12:00","sksksk","Interaksi Manusia Dan Komputer"),
    ("2025 E","Selasa","09:30","12:00","E2.01.04","Etika Kecerdasan Artifisial"),
    ("2024 A","Selasa","13:00","15:30","E2.01.02","Pengolahan Citra Digital"),
    ("2024 C","Selasa","13:00","15:30","C01.04.03","Data Warehouse"),
    ("2024 D","Selasa","13:00","15:30","E2.01.08","Penambangan Data"),
    ("2025 B","Selasa","13:00","15:30","E2.01.04","Teori Probabilitas"),
    ("2025 D","Selasa","13:00","15:30","E2.02.02/LAB","Interaksi Manusia Dan Komputer"),
    ("2025 F","Selasa","13:00","15:30","E2.01.09","Kalkulus Lanjut"),
    ("INT 24","Selasa","13:00","15:30","E2.01.10","Pembelajaran Mesin"),
    # Rabu
    ("2024 B","Rabu","07:00","09:30","E2.01.02","Pembelajaran Mesin"),
    ("2024 C","Rabu","07:00","09:30","E2.01.08","Pengolahan Citra Digital"),
    ("2024 D","Rabu","07:00","09:30","E2.01.09","Data Warehouse"),
    ("2024 E","Rabu","07:00","09:30","E2.02.02/LAB","Data Warehouse"),
    ("2025 C","Rabu","07:00","09:30","E2.01.04","Etika Kecerdasan Artifisial"),
    ("INT 24","Rabu","07:00","09:30","E2.01.10","Analisis Data Eksploratif"),
    ("2024 B","Rabu","09:30","12:00","E2.01.04","Analisis Multivariat"),
    ("2024 D","Rabu","09:30","12:00","E2.01.09","Pengolahan Citra Digital"),
    ("2024 E","Rabu","09:30","12:00","E2.01.02","Pengolahan Citra Digital"),
    ("INT 24","Rabu","09:30","12:00","E2.02.02/LAB","Penambangan Data"),
    ("2025 A","Rabu","10:20","12:00","E2.01.08","Etika Kecerdasan Artifisial"),
    ("INT 25","Rabu","10:20","12:00","E2.01.10","Etika Kecerdasan Artifisial"),
    ("2024 A","Rabu","13:00","15:30","E2.02.02/LAB","Data Warehouse"),
    ("2024 D","Rabu","13:00","15:30","E2.01.04","Analisis Multivariat"),
    ("2025 B","Rabu","13:00","15:30","E2.01.09","Kalkulus Lanjut"),
    ("2025 C","Rabu","13:00","15:30","E2.01.08","Teori Probabilitas"),
    ("2025 F","Rabu","13:00","15:30","E2.01.02","Struktur Data Dan Algoritma"),
    ("INT 24","Rabu","13:00","15:30","E2.01.10","Data Warehouse"),
    # Kamis
    ("2024 B","Kamis","07:00","09:30","E2.01.02","Pengolahan Citra Digital"),
    ("2024 C","Kamis","07:00","09:30","E2.02.02/LAB","Pembelajaran Mesin"),
    ("2024 E","Kamis","07:00","09:30","E2.01.04","Analisis Multivariat"),
    ("2025 E","Kamis","07:00","09:30","E2.01.09","Teori Probabilitas"),
    ("INT 24","Kamis","07:00","09:30","E2.01.08","Analisis Multivariat"),
    ("INT 25","Kamis","07:00","09:30","E2.02.02/LAB","Struktur Data Dan Algoritma"),
    ("2024 A","Kamis","09:30","12:00","E2.01.02","Analisis Data Eksploratif"),
    ("2025 E","Kamis","09:30","12:00","E2.01.08","Kalkulus Lanjut"),
    ("2025 C","Kamis","09:30","12:00","E2.01.09","Interaksi Manusia Dan Komputer"),
    ("2025 G","Kamis","09:30","12:00","E2.02.02/LAB","Struktur Data Dan Algoritma"),
    ("2025 F","Kamis","09:30","12:00","E2.01.04","Etika Kecerdasan Artifisial"),
    ("2025 A","Kamis","13:00","15:30","E2.01.07","Kalkulus Lanjut")
    ("2024 A","Kamis","13:00","15:30","E2.01.02","Pembelajaran Mesin"),
    ("2024 B","Kamis","13:00","15:30","E2.01.09","Data Warehouse"),
    ("2024 C","Kamis","13:00","15:30","E2.01.08","Penambangan Data"),
    ("2025 D","Kamis","13:00","15:30","E2.01.04","Etika Kecerdasan Artifisial"),
    ("2025 G","Kamis","13:00","15:30","E2.01.06","Kalkulus Lanjut"),
]

import uuid
from datetime import datetime
rows = []
for r, h, jm, js, ru, mk in jadwal:
    rows.append({
        "id_booking"   : str(uuid.uuid4())[:8].upper(),
        "rombel"       : r,
        "hari"         : h,
        "jam_mulai"    : jm,
        "jam_selesai"  : js,
        "ruang"        : ru,
        "mata_kuliah"  : mk,
        "status"       : "aktif",
        "waktu_booking": "2026-01-01 00:00:00"
    })

jadwal_df = pd.DataFrame(rows)
jadwal_df.to_csv("data_booking.csv", index=False)
print("✅ data_booking.csv dibuat:", len(jadwal_df), "jadwal existing")
print("\nDone! Semua file siap.")
