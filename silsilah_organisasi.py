# ==============================================================================
# PROYEK 1B - SKENARIO STUDI KASUS 2: SILSILAH ORGANISASI UIN SUSKA RIAU
# Struktur Data : General Tree (N-ary Tree) Berbasis OOP
# ==============================================================================


class PegawaiNode:
    """Representasi simpul (Node) entitas pegawai/jabatan dalam General Tree."""
    def __init__(self, id_pegawai: str, nama: str, jabatan: str):
        self.id_pegawai = id_pegawai
        self.nama = nama
        self.jabatan = jabatan
        self.parent = None
        self.children = []

    def __repr__(self):
        return f"[{self.id_pegawai}] {self.jabatan} ({self.nama})"


class SilsilahOrganisasiTree:
    """Representasi struktur Tree untuk mengelola hierarki Silsilah Organisasi."""
    def __init__(self, root_id: str, root_nama: str, root_jabatan: str):
        self.root = PegawaiNode(root_id, root_nama, root_jabatan)


   
    def insert_node(self, atasan_key: str, id_baru: str, nama_baru: str, jabatan_baru: str) -> bool:
        """Menyisipkan pegawai/jabatan baru di bawah atasan tertentu."""
        atasan_node = self.search_node(atasan_key)
        if atasan_node is None:
            print(f"[!] Gagal: Atasan '{atasan_key}' tidak ditemukan dalam struktur.")
            return False

        node_baru = PegawaiNode(id_baru, nama_baru, jabatan_baru)
        node_baru.parent = atasan_node
        atasan_node.children.append(node_baru)
        return True

    def delete_node(self, target_key: str) -> bool:
        """Menghapus simpul jabatan beserta sub-cabangnya (Pelengkap Rubrik Penilaian)."""
        target_node = self.search_node(target_key)
        if target_node is None or target_node == self.root:
            return False
        target_node.parent.children.remove(target_node)
        target_node.parent = None
        return True


    def search_node(self, keyword: str, current_node: PegawaiNode = None) -> PegawaiNode:
        """Mencari data pegawai berdasarkan ID, Nama, atau Jabatan secara rekursif (DFS)."""
        if self.root is None:
            return None
        if current_node is None:
            current_node = self.root

        key_lower = keyword.lower()
        if (key_lower == current_node.id_pegawai.lower() or
            key_lower == current_node.nama.lower() or
            key_lower == current_node.jabatan.lower() or
            key_lower in current_node.jabatan.lower() or
            key_lower in current_node.nama.lower()):
            return current_node

        for child in current_node.children:
            hasil = self.search_node(keyword, child)
            if hasil is not None:
                return hasil

        return None
    
    def preorder_traversal(self, node: PegawaiNode = None, hasil: list = None) -> list:
        """Preorder Traversal: Kunjungi Root -> Kunjungi seluruh anak dari kiri ke kanan."""
        if hasil is None:
            hasil = []
        if node is None:
            node = self.root

        hasil.append(node.jabatan)
        for child in node.children:
            self.preorder_traversal(child, hasil)
        return hasil

    def inorder_traversal(self, node: PegawaiNode = None, hasil: list = None) -> list:
        """Inorder Traversal General Tree: Anak Pertama -> Root -> Sisa Anak."""
        if hasil is None:
            hasil = []
        if node is None:
            node = self.root

        total_anak = len(node.children)
        if total_anak > 0:
            self.inorder_traversal(node.children[0], hasil)

        hasil.append(node.jabatan)

        for i in range(1, total_anak):
            self.inorder_traversal(node.children[i], hasil)
        return hasil

    
    def postorder_traversal(self, node: PegawaiNode = None, hasil: list = None) -> list:
        """Postorder Traversal: Kunjungi seluruh anak dari kiri ke kanan -> Kunjungi Root."""
        if hasil is None:
            hasil = []
        if node is None:
            node = self.root

        for child in node.children:
            self.postorder_traversal(child, hasil)
        hasil.append(node.jabatan)
        return hasil

    # ==========================================================================
    #  VISUAL & ANALISIS 
    # ==========================================================================
    def tampilkan_bagan(self, node: PegawaiNode = None, prefix: str = "", is_last: bool = True):
        """Mencetak visualisasi bagan struktur organisasi persis seperti gambar Soal 11."""
        if node is None:
            node = self.root
            print(f"\n{node.jabatan} [{node.nama}]")
        else:
            connector = "└── " if is_last else "├── "
            print(f"{prefix}{connector}{node.jabatan} [{node.nama}]")

        new_prefix = prefix + ("    " if is_last else "│   ") if node != self.root else ""
        total_anak = len(node.children)
        for idx, child in enumerate(node.children):
            apakah_terakhir = (idx == total_anak - 1)
            self.tampilkan_bagan(child, new_prefix, apakah_terakhir)

    def lacak_jalur_hierarki(self, node: PegawaiNode) -> str:
        """Melacak garis komando dari Rektor (Root) hingga ke simpul yang dicari."""
        jalur = []
        curr = node
        while curr is not None:
            jalur.append(curr.jabatan)
            curr = curr.parent
        jalur.reverse()
        return " -> ".join(jalur)

    def hitung_tinggi_tree(self, node: PegawaiNode = None) -> int:
        """Menghitung tinggi/kedalaman maksimum (height) dari Tree."""
        if node is None:
            node = self.root
        if not node.children:
            return 0
        return 1 + max(self.hitung_tinggi_tree(child) for child in node.children)


# ==============================================================================
# INISIALISASI DATA 18 SIMPUL 
# ==============================================================================
def bangun_data_uin_suska() -> SilsilahOrganisasiTree:
    tree = SilsilahOrganisasiTree("UIN-01", "Prof. Dr. Hairunas, M.Ag.", "Rektor (Root)")

    # Level 1: Bawahan Langsung Rektor
    tree.insert_node("Rektor (Root)", "UIN-02", "Ketua Senat", "Senat Universitas")
    tree.insert_node("Rektor (Root)", "UIN-03", "WR I", "Wakil Rektor I (Bidang Akademik)")
    tree.insert_node("Rektor (Root)", "UIN-04", "WR II", "Wakil Rektor II (Bidang Administrasi Umum & Keuangan)")
    tree.insert_node("Rektor (Root)", "UIN-05", "WR III", "Wakil Rektor III (Bidang Kemahasiswaan & Kerja Sama)")
    tree.insert_node("Rektor (Root)", "FST-01", "Dekan FST", "Dekan Fakultas Sains dan Teknologi")

    # Level 2: Bawahan Dekan Fakultas Sains dan Teknologi
    tree.insert_node("Dekan Fakultas Sains dan Teknologi", "FST-02", "WD I", "Wakil Dekan I (Bidang Akademik & Kelembagaan)")
    tree.insert_node("Dekan Fakultas Sains dan Teknologi", "FST-03", "WD II", "Wakil Dekan II (Bidang AUPK)")
    tree.insert_node("Dekan Fakultas Sains dan Teknologi", "FST-04", "WD III", "Wakil Dekan III (Bidang Kemahasiswaan)")
    tree.insert_node("Dekan Fakultas Sains dan Teknologi", "TIF-01", "Kaprodi TIF", "Ketua Program Studi Teknik Informatika")

    # Level 3: Bawahan Ketua Program Studi Teknik Informatika
    tree.insert_node("Ketua Program Studi Teknik Informatika", "TIF-02", "Sekprodi TIF", "Sekretaris Program Studi")
    tree.insert_node("Ketua Program Studi Teknik Informatika", "TIF-03", "Kalab Komputer", "Kepala Laboratorium Komputer")
    tree.insert_node("Ketua Program Studi Teknik Informatika", "TIF-04", "Koord Dosen", "Koordinator Dosen")

    # Level 4: Bawahan Kepala Lab Komputer & Koordinator Dosen
    tree.insert_node("Kepala Laboratorium Komputer", "LAB-01", "Staf Asisten", "Asisten Laboratorium")
    tree.insert_node("Kepala Laboratorium Komputer", "LAB-02", "Staf Teknisi", "Teknisi Laboratorium")
    tree.insert_node("Koordinator Dosen", "DSN-01", "Dosen PA", "Dosen Pembimbing Akademik")
    tree.insert_node("Koordinator Dosen", "DSN-02", "Dosen MK", "Dosen Pengampu Mata Kuliah")

    # Level 5: Bawahan Dosen Pembimbing Akademik
    tree.insert_node("Dosen Pembimbing Akademik", "MHS-01", "Dian Fajar", "Mahasiswa Bimbingan (Leaf)")

    return tree


# ==============================================================================
# EKSEKUSI LANGSUNG 
# ==============================================================================
def jalankan_mode_ringkas(tree: SilsilahOrganisasiTree):
    print("\n" + "="*70)
    print("MODE RINGKAS (OPSI A): CETAK LANGSUNG SELURUH HASIL TUGAS")
    print("="*70)

    print("\n[1] VISUALISASI BAGAN STRUKTUR ORGANISASI:")
    tree.tampilkan_bagan()

    print("\n[2] UJI OPERASI PENCARIAN (search_node):")
    target = "Kepala Laboratorium Komputer"
    hasil_cari = tree.search_node(target)
    if hasil_cari:
        print(f"    -> Ditemukan : {hasil_cari}")
        print(f"    -> Atasan    : {hasil_cari.parent.jabatan}")
        print(f"    -> Bawahan   : {[c.jabatan for c in hasil_cari.children]}")
        print(f"    -> Jalur     : {tree.lacak_jalur_hierarki(hasil_cari)}")

    print("\n[3] HASIL PRE-ORDER TRAVERSAL:")
    for i, jab in enumerate(tree.preorder_traversal(), 1):
        print(f"    {i:2d}. {jab}")

    print("\n[4] HASIL IN-ORDER TRAVERSAL:")
    for i, jab in enumerate(tree.inorder_traversal(), 1):
        print(f"    {i:2d}. {jab}")

    print("\n[5] HASIL POST-ORDER TRAVERSAL:")
    for i, jab in enumerate(tree.postorder_traversal(), 1):
        print(f"    {i:2d}. {jab}")


# ==============================================================================
#  MENU INTERAKTIF VISUAL 
# ==============================================================================
def jalankan_mode_interaktif(tree: SilsilahOrganisasiTree):
    while True:
        print("\n" + "="*65)
        print("   SISTEM MANAJEMEN SILSILAH ORGANISASI - UIN SUSKA RIAU")
        print("="*65)
        print("1. Tampilkan Visualisasi Bagan Struktur Organisasi (Tree)")
        print("2. Tambah Jabatan/Pegawai Baru (insert_node)")
        print("3. Cari Data Pegawai/Jabatan & Lacak Hierarki (search_node)")
        print("4. Hapus Jabatan/Pegawai (delete_node)")
        print("5. Tampilkan Hasil Pre-order, In-order, dan Post-order Traversal")
        print("6. Tampilkan Analisis Bentuk & Efisiensi Tree (Bahan Analisis)")
        print("0. Keluar")
        print("-" * 65)
        pilihan = input("Pilih menu (0-6): ").strip()

        if pilihan == "1":
            tree.tampilkan_bagan()
        elif pilihan == "2":
            atasan = input("Masukkan Nama/Jabatan Atasan : ").strip()
            id_b   = input("Masukkan ID Pegawai Baru     : ").strip()
            nama_b = input("Masukkan Nama Pegawai Baru   : ").strip()
            jab_b  = input("Masukkan Nama Jabatan Baru   : ").strip()
            if tree.insert_node(atasan, id_b, nama_b, jab_b):
                print(f"[✓] Berhasil menambahkan '{jab_b}' di bawah '{atasan}'.")
        elif pilihan == "3":
            kata_kunci = input("Masukkan Nama/Jabatan/ID yang dicari: ").strip()
            node = tree.search_node(kata_kunci)
            if node:
                print("\n--- DATA DITEMUKAN ---")
                print(f"ID Pegawai      : {node.id_pegawai}")
                print(f"Nama Pejabat    : {node.nama}")
                print(f"Jabatan         : {node.jabatan}")
                print(f"Atasan Langsung : {node.parent.jabatan if node.parent else 'Tidak Ada (Root)'}")
                print(f"Jumlah Bawahan  : {len(node.children)} entitas")
                print(f"Jalur Silsilah  : {tree.lacak_jalur_hierarki(node)}")
            else:
                print(f"[!] Data dengan kata kunci '{kata_kunci}' tidak ditemukan.")
        elif pilihan == "4":
            target = input("Masukkan Nama/Jabatan yang ingin dihapus: ").strip()
            if tree.delete_node(target):
                print(f"[✓] Jabatan '{target}' beserta sub-cabangnya berhasil dihapus.")
            else:
                print(f"[!] Gagal menghapus '{target}' (Tidak ditemukan atau merupakan Root).")
        elif pilihan == "5":
            print("\n--- 1. PRE-ORDER TRAVERSAL ---")
            print(" -> ".join(tree.preorder_traversal()))
            print("\n--- 2. IN-ORDER TRAVERSAL ---")
            print(" -> ".join(tree.inorder_traversal()))
            print("\n--- 3. POST-ORDER TRAVERSAL ---")
            print(" -> ".join(tree.postorder_traversal()))
        elif pilihan == "6":
            semua_node = tree.preorder_traversal()
            tinggi = tree.hitung_tinggi_tree()
            print("\n--- ANALISIS KARAKTERISTIK & EFISIENSI TREE ---")
            print(f"• Jenis Tree            : General Tree (N-ary Tree)")
            print(f"• Total Simpul (N)      : {len(semua_node)} simpul jabatan")
            print(f"• Tinggi/Kedalaman (h)  : {tinggi} level (Root di level 0 hingga Leaf di level {tinggi})")
            print(f"• Bentuk Struktur Tree  : Condong (Unbalanced/Skewed) ke cabang Dekan FST")
            print(f"• Kompleksitas Pencarian: O(1) Best Case (di Root), O(N) Worst Case (DFS Rekursif)")
            print(f"• Kompleksitas Traversal: O(N) Waktu dan O(h) Ruang Memori Stack Rekursi")
        elif pilihan == "0":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("[!] Pilihan tidak valid.")


if __name__ == "__main__":
    uin_tree = bangun_data_uin_suska()
    print("Pilih Mode Eksekusi Program:")
    print("[1] Mode Eksekusi Langsung / Ringkas (Gaya Opsi A)")
    print("[2] Mode Menu Interaktif Visual (Gaya Opsi B)")
    mode = input("Masukkan pilihan (1/2, tekan Enter untuk default Mode 1): ").strip()
    if mode == "2":
        jalankan_mode_interaktif(uin_tree)
    else:
        jalankan_mode_ringkas(uin_tree)