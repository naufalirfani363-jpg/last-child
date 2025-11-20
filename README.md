# Program Manajemen Tabungan Barang

Program sederhana berbasis CLI (Command Line Interface) untuk mengelola tabungan barang impian Anda. Program ini menggunakan file teks sebagai penyimpanan data, sehingga tidak memerlukan database eksternal.

## Deskripsi

Program ini membantu Anda melacak progres tabungan untuk berbagai barang yang ingin dibeli. Anda dapat menambahkan barang baru, mencatat tabungan harian, melihat progres, dan mengelola riwayat tabungan. Semua data disimpan secara otomatis dalam file teks lokal.

## Fitur Utama

- **Tambah Barang Baru**: Daftarkan barang impian dengan nama dan harga target.
- **Tambah Tabungan**: Catat jumlah uang yang ditabung untuk barang tertentu.
- **Lihat Daftar Barang**: Tampilkan semua barang dengan progres tabungan dalam bentuk persentase dan progress bar visual.
- **Lihat Riwayat Tabungan**: Lihat semua catatan tabungan yang telah dilakukan.
- **Hapus Barang**: Hapus barang dari daftar beserta seluruh riwayatnya.
- **Penyimpanan Otomatis**: Data tersimpan dalam file teks (barang.txt dan riwayat.txt).

## Persyaratan Sistem

- Python 3.x
- Tidak ada dependensi eksternal (hanya menggunakan modul standar Python)

## Instalasi

1. Pastikan Python 3.x terinstal di sistem Anda.
2. Unduh atau salin file `main.py` ke folder yang diinginkan.
3. Jalankan program menggunakan perintah di bawah.

## Cara Menjalankan

1. Buka terminal atau command prompt.
2. Navigasi ke folder yang berisi `main.py`.
3. Jalankan perintah:
   ```
   python main.py
   ```
4. Ikuti menu yang muncul di layar.

## Struktur File

- `main.py`: File utama program Python.
- `barang.txt`: File penyimpanan data barang (dibuat otomatis saat pertama kali menjalankan program).
- `riwayat.txt`: File penyimpanan riwayat tabungan (dibuat otomatis saat pertama kali menjalankan program).

## Contoh Penggunaan

### Menambah Barang Baru
1. Pilih menu "1. Tambah Barang Baru".
2. Masukkan nama barang (contoh: "Laptop Gaming").
3. Masukkan harga target (contoh: 15000000).

### Menambah Tabungan
1. Pilih menu "2. Tambah Tabungan".
2. Pilih ID barang dari daftar yang ditampilkan.
3. Masukkan jumlah uang yang ditabung hari ini.

### Melihat Progres
1. Pilih menu "3. Lihat Daftar Barang".
2. Lihat tabel yang menampilkan nama barang, harga target, total tertabung, dan progres dalam persentase.

## Format Data

### barang.txt
Format: `ID|Nama|Harga Target|Total Tertabung|Tanggal Mulai`
Contoh:
```
1|Laptop Gaming|15000000|500000|2024-01-01
```

### riwayat.txt
Format: `ID Riwayat|ID Barang|Nama Barang|Jumlah|Waktu`
Contoh:
```
1|1|Laptop Gaming|500000|2024-01-01 10:30:00
```

## Catatan

- Program ini menggunakan file teks sebagai penyimpanan, sehingga data akan tetap tersimpan meskipun program ditutup.
- Pastikan tidak menghapus file `barang.txt` dan `riwayat.txt` secara manual, karena dapat menyebabkan kehilangan data.
- Program ini dirancang untuk penggunaan pribadi dan tidak memiliki fitur keamanan khusus.

## Lisensi

Program ini dibuat untuk tujuan edukasi dan penggunaan pribadi. Silakan gunakan sesuai kebutuhan Anda.

---

Dibuat dengan Python - Mudah, Sederhana, dan Efektif!
