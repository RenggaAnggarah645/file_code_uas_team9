import random  # Mengimport library random untuk menghasilkan karakter acak
import string  # Mengimport library string untuk menggunakan kumpulan karakter ASCII
import tkinter as tk  # Mengimport library tkinter untuk membuat GUI
class PasswordGenerator:
    def __init__(self, length):
        self.length = length  # Panjang password yang diinginkan
        self.characters = string.ascii_letters + string.digits + string.punctuation  # Kumpulan karakter yang digunakan dalam pembuatan password
    def generate_password(self):
        password = ''  # Variabel untuk menyimpan password yang dihasilkan
        while True:
            # Menghasilkan karakter acak sebanyak panjang password yang diinginkan
            # dengan menggunakan kumpulan karakter yang telah ditentukan
            password = ''.join(random.choice(self.characters) for _ in range(self.length))
            # Memastikan bahwa password memenuhi persyaratan:
            # memiliki setidaknya satu huruf kecil, satu huruf besar, satu digit, dan satu karakter khusus
            if (any(c.islower() for c in password)
                    and any(c.isupper() for c in password)
                    and any(c.isdigit() for c in password)
                    and any(c in string.punctuation for c in password)):
                break  # Keluar dari loop jika password memenuhi persyaratan
        return password  # Mengembalikan password yang dihasilkan
def buatPassword():
    global label_hasil  # Mendeklarasikan variabel label_hasil sebagai variabel global
    panjangPass = int(entry_perintah.get())  # Mendapatkan panjang password dari input pengguna
    passwordBuat = PasswordGenerator(int(panjangPass))  # Membuat objek PasswordGenerator dengan panjang password yang diinginkan
    hasilnya = passwordBuat.generate_password()  # Menghasilkan password baru menggunakan objek PasswordGenerator
    if label_hasil is not None:
        label_hasil.destroy()  # Hapus label hasil sebelum membuat yang baru
    label_hasil = tk.Label(window, text="Password terbuat: " + hasilnya)  # Membuat label hasil dengan teks yang sesuai
    label_hasil.pack()  # Menampilkan label hasil dalam jendela
window = tk.Tk()  # Membuat jendela aplikasi menggunakan Tkinter
window.title("Membuat Password")  # Mengatur judul jendela
label_perintah = tk.Label(window, text="Berapa panjang password yang akan dibuat?")  # Membuat label untuk instruksi
label_perintah.pack()  # Menampilkan label instruksi dalam jendela
entry_perintah = tk.Entry(window)  # Membuat field input untuk panjang password
entry_perintah.pack()  # Menampilkan field input dalam jendela
button_buat = tk.Button(window, text="Buat", command=buatPassword)  # Membuat tombol "Buat" untuk memanggil fungsi buatPassword()
button_buat.pack()  # Menampilkan tombol "Buat" dalam jendela
label_hasil = None  # Variabel untuk menyimpan label hasil yang akan ditampilkan
window.mainloop()  # Memulai loop utama untuk menjalankan aplikasi tkinter