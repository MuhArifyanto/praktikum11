def tambah(nama, nilai):
    data_mahasiswa.append({"nama": nama, "nilai": nilai})

def tampilkan():
    for mahasiswa in data_mahasiswa:
        print(f"Nama: {mahasiswa['nama']}, Nilai: {mahasiswa['nilai']}")

def hapus(nama):
    global data_mahasiswa
    data_mahasiswa = [mahasiswa for mahasiswa in data_mahasiswa if mahasiswa['nama'] != nama]

def ubah(nama, nilai):
    for mahasiswa in data_mahasiswa:
        if mahasiswa['nama'] == nama:
            mahasiswa['nilai'] = nilai

data_mahasiswa = []

tambah("Arif", 85)
tambah("Narsih", 90)
tambah("Freya", 78)

tampilkan()

hapus("Narsih")

tampilkan()

ubah ("Arif", 90)

ubah ("Narsih", 95)

ubah("Freya", 82)