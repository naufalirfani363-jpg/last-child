import os
from datetime import datetime

# Nama file database
BARANG_FILE = "barang.txt"
RIWAYAT_FILE = "riwayat.txt"

def clear_screen():
    """Membersihkan layar console"""
    os.system('cls' if os.name == 'nt' else 'clear')

def init_database():
    """Inisialisasi file database jika belum ada"""
    if not os.path.exists(BARANG_FILE):
        with open(BARANG_FILE, "w") as f:
            pass
    if not os.path.exists(RIWAYAT_FILE):
        with open(RIWAYAT_FILE, "w") as f:
            pass

def get_next_id(file_path):
    """Mendapatkan ID berikutnya"""
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
    clear_screen()
    print("\n=== TAMBAH BARANG BARU ===")
    nama = input("Masukkan nama barang: ").strip()
    
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
    
    with open(BARANG_FILE, "a") as f:
        f.write(f"{barang_id}|{nama}|{harga}|0|{tanggal}\n")
    
    print(f"\nBarang '{nama}' berhasil ditambahkan!")
    print(f"Harga Target: Rp {harga:,}")
    print(f"Tanggal Mulai: {tanggal}")
    input("\nTekan Enter untuk kembali ke menu...")
    clear_screen()

def tambah_tabungan():
    clear_screen()
    if not os.path.exists(BARANG_FILE) or os.path.getsize(BARANG_FILE) == 0:
        print("\nTidak ada barang yang terdaftar.")
        input("\nTekan Enter untuk kembali...")
        clear_screen()
        return
    
    print("\n=== DAFTAR BARANG ===")
    lihat_barang(hide_menu=True)
    
    barang_id = input("\nPilih ID barang: ").strip()
    
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
        input("\nTekan Enter...")
        clear_screen()
        return
    
    while True:
        try:
            jumlah = int(input("Masukkan jumlah tabungan hari ini: Rp "))
            if jumlah <= 0:
                print("Jumlah harus lebih dari 0!")
                continue
            break
        except ValueError:
            print("Masukkan angka yang valid!")
    
    total_tertabung = int(barang_data[3]) + jumlah
    sisa = int(barang_data[2]) - total_tertabung
    
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
    
    riwayat_id = get_next_id(RIWAYAT_FILE)
    tanggal = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(RIWAYAT_FILE, "a") as f:
        f.write(f"{riwayat_id}|{barang_id}|{barang_data[1]}|{jumlah}|{tanggal}\n")
    
    print("\n" + "="*50)
    print(f"Berhasil menambahkan tabungan untuk {barang_data[1]}!")
    print(f"Total tertabung: Rp {total_tertabung:,}")
    print(f"Sisa: Rp {sisa:,}")
    if sisa <= 0:
        print("🎉 Target tabungan tercapai!")
    print("="*50)

    input("\nTekan Enter untuk kembali ke menu...")
    clear_screen()

def lihat_barang(hide_menu=False):
    """Menampilkan daftar barang dan progres tabungan"""
    if not os.path.exists(BARANG_FILE) or os.path.getsize(BARANG_FILE) == 0:
        print("\nBelum ada barang yang terdaftar.")
        return
    
    print("\n" + "="*60)
    print(f"{'ID':<5} {'NAMA BARANG':<20} {'HARGA TARGET':<15} {'TERKUMPUL':<15}")
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

                # Progress bar ukuran lebih kecil (10 blok)
                total_bar = 10
                filled = int((persentase / 100) * total_bar)
                empty = total_bar - filled

                # Isi bar
                bar = "█" * filled + "░" * empty

                # Persentase ditaruh di tengah bar
                progress_text = f"{persentase:.1f}%"
                bar_list = list(bar)
                mid = len(bar_list) // 2

                start_pos = mid - len(progress_text) // 2
                for i, ch in enumerate(progress_text):
                    if 0 <= start_pos + i < len(bar_list):
                        bar_list[start_pos + i] = ch

                bar_final = "".join(bar_list)

                # Tampilkan data
                print(f"{barang_id:<5} {nama:<20} Rp {harga:<12,} Rp {terkumpul:<12,}")
                print(f"      [{bar_final}]")
    
    print("="*60)
    
    if not hide_menu:
        input("\nTekan Enter untuk kembali...")
        clear_screen()



def lihat_riwayat():
    clear_screen()
    if not os.path.exists(RIWAYAT_FILE) or os.path.getsize(RIWAYAT_FILE) == 0:
        print("\nBelum ada riwayat tabungan.")
        input("\nTekan Enter...")
        clear_screen()
        return
    
    print("\n" + "="*70)
    print(f"{'ID':<5} {'BARANG':<20} {'JUMLAH':<15} {'WAKTU'}")
    print("-"*70)
    
    with open(RIWAYAT_FILE, "r") as f:
        for line in f:
            parts = line.strip().split("|")
            print(f"{parts[0]:<5} {parts[2]:<20} Rp {int(parts[3]):<12,} {parts[4]}")
    
    print("="*70)
    input("\nTekan Enter...")
    clear_screen()

def hapus_barang():
    clear_screen()
    if not os.path.exists(BARANG_FILE) or os.path.getsize(BARANG_FILE) == 0:
        print("\nTidak ada barang.")
        input("\nEnter...")
        clear_screen()
        return
    
    print("\n=== HAPUS BARANG ===")
    lihat_barang(hide_menu=True)
    
    barang_id = input("\nMasukkan ID barang: ").strip()
    
    barang_ditemukan = False
    with open(BARANG_FILE, "r") as f:
        for line in f:
            if line.startswith(barang_id + "|"):
                barang_ditemukan = True
                nama_barang = line.strip().split("|")[1]
                break
    
    if not barang_ditemukan:
        print("ID tidak ditemukan!")
        input("\nEnter...")
        clear_screen()
        return
    
    konfirmasi = input(f"Yakin hapus '{nama_barang}'? (y/n): ").lower()
    if konfirmasi != 'y':
        print("Batal.")
        input("\nEnter...")
        clear_screen()
        return
    
    # Hapus barang
    with open(BARANG_FILE, "r") as f:
        lines = [line for line in f if not line.startswith(barang_id + "|")]
    with open(BARANG_FILE, "w") as f:
        f.writelines(lines)

    # Hapus riwayat
    with open(RIWAYAT_FILE, "r") as f:
        riw = [line for line in f if line.split("|")[1] != barang_id]
    with open(RIWAYAT_FILE, "w") as f:
        f.writelines(riw)

    print(f"\nBarang '{nama_barang}' berhasil dihapus!")
    input("\nEnter...")
    clear_screen()

def main_menu():
    while True:
        clear_screen()
        print("="*50)
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
        
        if pilihan == "1": tambah_barang()
        elif pilihan == "2": tambah_tabungan()
        elif pilihan == "3": clear_screen(); lihat_barang()
        elif pilihan == "4": lihat_riwayat()
        elif pilihan == "5": hapus_barang()
        elif pilihan == "6":
            clear_screen()
            print("Terima kasih sudah menggunakan program!")
            break
        else:
            print("Pilihan tidak valid!")
            input("\nEnter...")
            clear_screen()

if __name__ == "__main__":
    init_database()
    clear_screen()
    print("SELAMAT DATANG DI PROGRAM TABUNGAN BARANG")
    print("Simpan impian Anda dengan menabung!")
    input("\nTekan Enter untuk melanjutkan...")
    main_menu()
