
def baca_data(nama_file):
    data = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor_baris, baris in enumerate(file, start=1):
                baris = baris.strip()

                if not baris:
                    continue

                try:
                    nim, teks_nilai = baris.split(",")
                    nilai = float(teks_nilai)

                    data.append({
                        "nim": nim.strip(),
                        "nilai": nilai
                    })

                except ValueError:
                    print(f"Format data pada baris {nomor_baris} tidak valid.")

    except FileNotFoundError:
        print(f"File {nama_file} tidak ditemukan.")

    return data


def tulis_rekap(nama_file, data):
    try:
        with open(nama_file, "w", encoding="utf-8") as file:
            file.write("REKAP NILAI MAHASISWA\n")
            file.write("====================\n")

            for mahasiswa in data:
                file.write(
                    f"{mahasiswa['nim']}, {mahasiswa['nilai']:.2f}\n"
                )

            if data:
                rata_rata = sum(m["nilai"] for m in data) / len(data)
                file.write(f"\nJumlah data: {len(data)}\n")
                file.write(f"Rata-rata nilai: {rata_rata:.2f}\n")
            else:
                file.write("\nTidak ada data yang valid.\n")

        print(f"Rekap berhasil ditulis ke {nama_file}.")

    except OSError as error:
        print(f"Gagal menulis file: {error}")


input_file = "data/nilai.txt"
output_file = "data/hasil_rekap.txt"

# Alur utama
data_nilai = baca_data(input_file)
tulis_rekap(output_file, data_nilai)
