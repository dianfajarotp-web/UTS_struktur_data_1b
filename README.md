# Proyek 1b - Silsilah Organisasi UIN Suska Riau

Repositori ini berisi kode program Python untuk memenuhi tugas Proyek 1 (Skenario Studi Kasus 2) pada mata kuliah Struktur Data, Program Studi Teknik Informatika, Fakultas Sains dan Teknologi, UIN Sultan Syarif Kasim Riau.

## Identitas Mahasiswa
* **Nama:** Dian Fajar
* **NIM:** [Isi NIM Anda]
* **Program Studi:** Teknik Informatika

## Deskripsi Program
Program ini mengimplementasikan struktur data **General Tree** berbasis *Object-Oriented Programming* (OOP) untuk memetakan hierarki jabatan di lingkungan UIN Suska Riau, mulai dari Rektor (Root) hingga Mahasiswa Bimbingan (Leaf).

Fitur yang diimplementasikan meliputi:
1. `insert_node()` : Menambahkan jabatan/pegawai baru di bawah atasan tertentu.
2. `search_node()` : Mencari data pegawai berdasarkan ID, nama, atau jabatan beserta pelacakan jalur silsilahnya.
3. `delete_node()` : Menghapus simpul jabatan dari struktur pohon.
4. **Algoritma Traversal** : Menampilkan urutan seluruh struktur organisasi menggunakan pendekatan *Pre-order*, *In-order*, dan *Post-order*.

## Cara Menjalankan Program
Pastikan Python sudah terinstal, lalu jalankan perintah berikut di terminal:
```bash
python silsilah_organisasi.py