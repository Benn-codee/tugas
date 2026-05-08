nilai_lulus = 75
nama_univ = "Universitas Katolik Darma Cendika"

class datamahasiswa:
    def __init__(self, nama_mahasiswa, nilai):
        self.nama_mahasiswa = nama_mahasiswa
        self.nilai = nilai

    def cek_kelulusan(self):
        if self.nilai >= nilai_lulus:
            return "Lulus"
        return "Tidak Lulus"

def info(mahasiswa):
    status_mahasiswa = mahasiswa.cek_kelulusan()
    print(f"Univ    : {nama_univ}")
    print(f"Nama    : {mahasiswa.nama_mahasiswa}")
    print(f"Nilai   : {mahasiswa.nilai}")
    print(f"Status  : {status_mahasiswa}")

mahasiswa_baru = datamahasiswa("Duro", 80)
info(mahasiswa_baru)