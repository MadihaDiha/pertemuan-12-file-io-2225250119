# Pertemuan 12 - File I/O Python

**Nama:** Madiha  
**NIM:** 2225250119  
**Kelas:** 3E  
**Mata Kuliah:** Algoritma dan Pemrograman

## Tujuan

Mempelajari operasi file (*File I/O*) dalam Python, meliputi menulis file, membaca file, menambahkan isi file, memproses data per baris, menangani file yang tidak ditemukan, menangani kesalahan input menggunakan `ValueError`, serta mengolah data nilai mahasiswa dan menyimpan hasil rekap ke dalam file.

## Struktur Folder

```text
pertemuan-12-file-io-2225250119/
├── README.md
├── .gitignore
├── data/
│   ├── catatan.txt
│   ├── nilai.txt
│   └── hasil_rekap.txt
├── latihan/
│   ├── 01_tulis_file.py
│   ├── 02_baca_file.py
│   ├── 03_append_file.py
│   ├── 04_proses_baris.py
│   ├── 05_file_not_found.py
│   └── 06_value_error.py
└── tugas/
    └── rekap_nilai_file.py
```

## Materi yang Dipelajari

1. Menulis data ke dalam file menggunakan mode `w`.
2. Membaca isi file menggunakan mode `r`.
3. Menambahkan data ke dalam file menggunakan mode `a`.
4. Memproses isi file baris demi baris menggunakan perulangan `for`.
5. Menggunakan `strip()` untuk menghapus spasi dan karakter baris baru.
6. Memisahkan data menggunakan `split()` dan mengonversi nilai menggunakan `float()`.
7. Menangani kesalahan file yang tidak ditemukan menggunakan `FileNotFoundError`.
8. Menangani kesalahan konversi input menggunakan `ValueError`.
9. Membaca, memvalidasi, dan menuliskan rekap nilai mahasiswa ke dalam file.
10. Menguji program melalui terminal VS Code serta mengelola tugas menggunakan Git dan GitHub.

## Deskripsi Latihan

| **File** | **Keterangan** |
|---|---|
| `01_tulis_file.py` | Menulis teks Algoritma dan Pemrograman serta Pertemuan 12 ke dalam file `catatan.txt`. |
| `02_baca_file.py` | Membaca dan menampilkan isi file `catatan.txt` baris demi baris. |
| `03_append_file.py` | Menambahkan teks baru ke dalam file `catatan.txt` tanpa menghapus isi sebelumnya. |
| `04_proses_baris.py` | Membaca data nilai dari file, memisahkan NIM dan nilai, lalu mengonversi nilai menjadi tipe `float`. |
| `05_file_not_found.py` | Menangani kondisi ketika file yang ingin dibaca tidak ditemukan. |
| `06_value_error.py` | Memvalidasi input nilai dan menangani kesalahan jika input bukan berupa angka. |
| `rekap_nilai_file.py` | Membaca dan memvalidasi data nilai mahasiswa, kemudian menuliskan hasil rekap ke file `hasil_rekap.txt`. |

## Cara Menjalankan Program

Pastikan Python sudah terpasang di komputer dan terminal VS Code berada di folder utama proyek.

### 1. Menjalankan File Latihan

Jalankan setiap program menggunakan perintah berikut secara terpisah:

```bash
python latihan/01_tulis_file.py
```

```bash
python latihan/02_baca_file.py
```

```bash
python latihan/03_append_file.py
```

```bash
python latihan/04_proses_baris.py
```

```bash
python latihan/05_file_not_found.py
```

```bash
python latihan/06_value_error.py
```

### 2. Menjalankan Program Tugas

Jalankan perintah berikut pada terminal VS Code:

```bash
python tugas/rekap_nilai_file.py
```

Pastikan file `data/nilai.txt` sudah berisi data mahasiswa dengan format NIM dan nilai yang dipisahkan oleh tanda koma sebelum menjalankan program pemrosesan data dan rekap nilai.

## Hasil Pengujian Latihan

| **No.** | **Program** | **Hasil Pengujian** |
|---|---|---|
| 1 | Menulis file | Berhasil menulis teks dan menampilkan pesan `File berhasil ditulis.` |
| 2 | Membaca file | Berhasil menampilkan `Algoritma dan Pemrograman` dan `Pertemuan 12`. |
| 3 | Append file | Berhasil menambahkan teks dan menampilkan pesan `Data berhasil ditambahkan.` |
| 4 | Memproses baris data | Program dijalankan untuk membaca dan memproses data nilai mahasiswa dari file. |
| 5 | File tidak ditemukan | Berhasil menampilkan pesan `File tidak ditemukan.` |
| 6 | ValueError | Input `90` berhasil dikonversi menjadi `90.0`. |

## Hasil Pengujian Praktik

Program praktik `rekap_nilai_file.py` digunakan untuk membaca data nilai mahasiswa dari file `data/nilai.txt`, memvalidasi data, dan menyimpan hasil rekap ke dalam file `data/hasil_rekap.txt`.

| **Operasi** | **Input** | **Hasil Pengujian** |
|---|---|---|
| Membaca data | `data/nilai.txt` | Program menjalankan proses pembacaan data nilai mahasiswa. |
| Validasi data | Data nilai dalam file | Data diperiksa agar sesuai dengan format yang ditentukan. |
| Menulis rekap | `data/hasil_rekap.txt` | Berhasil membuat atau menulis hasil rekap ke file keluaran. |
| Menampilkan status | Proses penulisan rekap | Menampilkan pesan `Rekap berhasil ditulis ke data/hasil_rekap.txt.` |

Berdasarkan hasil pengujian, program tugas berhasil dijalankan melalui terminal VS Code dan berhasil menuliskan hasil rekap ke file keluaran. Hasil rekap berisi data yang berhasil dibaca dan diproses dari file `data/nilai.txt`.

## Kuis Formatif - Pertemuan 12

Kuis formatif membahas materi operasi file dalam Python, meliputi fungsi mode `w`, `r`, dan `a`, proses membaca file baris demi baris, penggunaan `strip()` dan `split()`, penanganan kesalahan menggunakan `FileNotFoundError` dan `ValueError`, serta pengolahan dan penyimpanan data ke dalam file.

## Refleksi

Melalui pertemuan ini, saya mempelajari cara melakukan operasi file menggunakan Python, mulai dari menulis, membaca, hingga menambahkan isi file. Saya juga memahami cara memproses data per baris, memisahkan data menggunakan `split()`, dan mengonversi nilai menggunakan `float()`.

Selain itu, saya mempelajari penanganan kesalahan menggunakan `FileNotFoundError` ketika file tidak ditemukan dan `ValueError` ketika input tidak dapat dikonversi menjadi angka. Pada kegiatan tugas, saya menerapkan operasi file untuk membaca data nilai mahasiswa, melakukan validasi, dan menyimpan hasil rekap ke dalam file baru. Materi ini membantu saya memahami pengolahan data secara terstruktur dan penyimpanan data secara permanen menggunakan Python.
