import os
from datetime import datetime

# Nama file database
BARANG_FILE = "barang.txt"
RIWAYAT_FILE = "riwayat.txt"

def init_database():
    """Inisialisasi file database jika belum ada"""
    if not os.path.exists(BARANG_FILE):
        with open(BARANG_FILE, "w") as f:
            pass  # Buat file kosong
    if not os.path.exists(RIWAYAT_FILE):
        with open(RIWAYAT_FILE, "w") as f:
            pass  # Buat file kosong

def get_next_id(file_path):
    """Mendapatkan ID berikutnya untuk entri baru"""
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        return 1
    
    max_id = 0
    with open(file_path, "r") as f:
        for line in f:
            if line.strip():
                parts = line.strip().split("|")
                current_id = int(parts[0])
                if current_id > max_id:
                    max_id = current_id
    return max_id + 1

def tambah_barang():
    """Menambahkan barang baru ke database"""
    print("\n=== TAMBAH BARANG BARU ===")
    nama = input("Masukkan nama barang: ").strip()
    
    # Validasi harga
    while True:
        try:
            harga = int(input("Masukkan harga target barang: Rp "))
            if harga <= 0:
                print("Harga harus lebih dari 0!")
                continue
            break
        except ValueError:
            print("Masukkan angka yang valid!")
    
    barang_id = get_next_id(BARANG_FILE)
    tanggal = datetime.now().strftime("%Y-%m-%d")
    
    # Simpan ke database barang
    with open(BARANG_FILE, "a") as f:
        f.write(f"{barang_id}|{nama}|{harga}|0|{tanggal}\n")
    
    print(f"\nBarang '{nama}' berhasil ditambahkan!")
    print(f"ID Barang: {barang_id}")
    print(f"Harga Target: Rp {harga:,}")
    print(f"Tanggal Mulai: {tanggal}")

def tambah_tabungan():
    """Menambahkan tabungan untuk barang tertentu"""
    if not os.path.exists(BARANG_FILE) or os.path.getsize(BARANG_FILE) == 0:
        print("\nTidak ada barang yang terdaftar. Silakan tambahkan barang terlebih dahulu.")
        return
    
    print("\n=== DAFTAR BARANG ===")
    lihat_barang(hide_menu=True)
    
    # Pilih barang
    barang_id = input("\nPilih ID barang untuk ditabung: ").strip()
    
    # Cari barang
    barang_ditemukan = False
    barang_data = []
    with open(BARANG_FILE, "r") as f:
        for line in f:
            parts = line.strip().split("|")
            if parts[0] == barang_id:
                barang_ditemukan = True
                barang_data = parts
                break
    
    if not barang_ditemukan:
        print("ID barang tidak ditemukan!")
        return
    
    # Input jumlah tabungan
    while True:
        try:
            jumlah = int(input("Masukkan jumlah uang yang ditabung hari ini: Rp "))
            if jumlah <= 0:
                print("Jumlah harus lebih dari 0!")
                continue
            break
        except ValueError:
            print("Masukkan angka yang valid!")
    
    # Update total tabungan
    total_tertabung = int(barang_data[3]) + jumlah
    sisa = int(barang_data[2]) - total_tertabung
    
    # Update database barang
    lines = []
    with open(BARANG_FILE, "r") as f:
        for line in f:
            parts = line.strip().split("|")
            if parts[0] == barang_id:
                parts[3] = str(total_tertabung)
                line = "|".join(parts) + "\n"
            lines.append(line)
    
    with open(BARANG_FILE, "w") as f:
        f.writelines(lines)
    
    # Simpan riwayat
    riwayat_id = get_next_id(RIWAYAT_FILE)
    tanggal = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(RIWAYAT_FILE, "a") as f:
        f.write(f"{riwayat_id}|{barang_id}|{barang_data[1]}|{jumlah}|{tanggal}\n")
    
    # Tampilkan hasil
    print("\n" + "="*50)
    print(f"Berhasil menambahkan tabungan untuk {barang_data[1]}!")
    print(f"Jumlah ditabung: Rp {jumlah:,}")
    print(f"Total tertabung: Rp {total_tertabung:,}")
    print(f"Sisa yang harus ditabung: Rp {sisa:,}")
    
    if sisa <= 0:
        print("\nSELAMAT! Tabungan barang Anda telah tercapai!")
        print(f"Anda berhasil mengumpulkan Rp {total_tertabung:,} untuk {barang_data[1]}")
    else:
        persentase = (total_tertabung / int(barang_data[2])) * 100
        print(f"Progres: {persentase:.1f}% tercapai")
    print("="*50)

def lihat_barang(hide_menu=False):
    """Menampilkan daftar barang dan progres tabungan"""
    if not os.path.exists(BARANG_FILE) or os.path.getsize(BARANG_FILE) == 0:
        print("\nBelum ada barang yang terdaftar.")
        return
    
    print("\n" + "="*60)
    print(f"{'ID':<5} {'NAMA BARANG':<20} {'HARGA TARGET':<15} {'TERKUMPUL':<15} {'PROGRES'}")
    print("-"*60)
    
    with open(BARANG_FILE, "r") as f:
        for line in f:
            if line.strip():
                parts = line.strip().split("|")
                barang_id = parts[0]
                nama = parts[1]
                harga = int(parts[2])
                terkumpul = int(parts[3])
                
                # Hitung progres
                persentase = (terkumpul / harga) * 100
                progress_bar = "█" * int(persentase/10) + "░" * (10 - int(persentase/10))
                
                print(f"{barang_id:<5} {nama:<20} Rp {harga:<12,} Rp {terkumpul:<12,} {persentase:.1f}%")
                print(f"      [{''.join(progress_bar)}]")
    
    print("="*60)
    
    if not hide_menu:
        input("\nTekan Enter untuk kembali ke menu...")

def lihat_riwayat():
    """Menampilkan riwayat tabungan"""
    if not os.path.exists(RIWAYAT_FILE) or os.path.getsize(RIWAYAT_FILE) == 0:
        print("\nBelum ada riwayat tabungan.")
        return
    
    print("\n" + "="*70)
    print(f"{'ID':<5} {'BARANG':<20} {'JUMLAH':<15} {'WAKTU'}")
    print("-"*70)
    
    with open(RIWAYAT_FILE, "r") as f:
        for line in f:
            if line.strip():
                parts = line.strip().split("|")
                print(f"{parts[0]:<5} {parts[2]:<20} Rp {int(parts[3]):<12,} {parts[4]}")
    
    print("="*70)
    input("\nTekan Enter untuk kembali ke menu...")

def hapus_barang():
    """Menghapus barang dari database"""
    if not os.path.exists(BARANG_FILE) or os.path.getsize(BARANG_FILE) == 0:
        print("\nTidak ada barang yang terdaftar.")
        return
    
    print("\n=== HAPUS BARANG ===")
    lihat_barang(hide_menu=True)
    
    barang_id = input("\nMasukkan ID barang yang akan dihapus: ").strip()
    
    # Cek apakah barang ada
    barang_ditemukan = False
    with open(BARANG_FILE, "r") as f:
        for line in f:
            if line.startswith(barang_id + "|"):
                barang_ditemukan = True
                nama_barang = line.strip().split("|")[1]
                break
    
    if not barang_ditemukan:
        print("ID barang tidak ditemukan!")
        return
    
    konfirmasi = input(f"Yakin ingin menghapus barang '{nama_barang}'? (y/n): ").lower()
    if konfirmasi != 'y':
        print("Penghapusan dibatalkan.")
        return
    
    # Hapus dari database barang
    lines = []
    with open(BARANG_FILE, "r") as f:
        for line in f:
            if not line.startswith(barang_id + "|"):
                lines.append(line)
    
    with open(BARANG_FILE, "w") as f:
        f.writelines(lines)
    
    # Hapus riwayat terkait
    riwayat_lines = []
    with open(RIWAYAT_FILE, "r") as f:
        for line in f:
            if not line.split("|")[1] == barang_id:
                riwayat_lines.append(line)
    
    with open(RIWAYAT_FILE, "w") as f:
        f.writelines(riwayat_lines)
    
    print(f"\nBarang '{nama_barang}' dan seluruh riwayatnya berhasil dihapus!")

def main_menu():
    """Menampilkan menu utama"""
    while True:
        print("\n" + "="*50)
        print("PROGRAM MANAJEMEN TABUNGAN BARANG".center(50))
        print("="*50)
        print("1. Tambah Barang Baru")
        print("2. Tambah Tabungan")
        print("3. Lihat Daftar Barang")
        print("4. Lihat Riwayat Tabungan")
        print("5. Hapus Barang")
        print("6. Keluar")
        print("="*50)
        
        pilihan = input("Pilih menu (1-6): ").strip()
        
        if pilihan == "1":
            tambah_barang()
        elif pilihan == "2":
            tambah_tabungan()
        elif pilihan == "3":
            lihat_barang()
        elif pilihan == "4":
            lihat_riwayat()
        elif pilihan == "5":
            hapus_barang()
        elif pilihan == "6":
            print("\nTerima kasih telah menggunakan program ini!")
            print("Data tabungan Anda telah disimpan secara otomatis.")
            break
        else:
            print("Pilihan tidak valid! Silakan pilih 1-6.")

if __name__ == "__main__":
    # Inisialisasi database
    init_database()
    
    # Jalankan program utama
    print("="*50)
    print("SELAMAT DATANG DI PROGRAM TABUNGAN BARANG".center(50))
    print("="*50)
    print("Simpan impian Anda dengan menabung secara teratur!")
    
    main_menu()