# AMMAR RASYAD KURNIA
# 2603667
# KELAS 1A

username = "admin"
password = "admin123"

while True:
    input_username = input("Masukkan username: ")
    input_password = input("Masukkan password: ")

    if input_username == username and input_password == password:
        print("Login berhasil!")
        break
    else:
        print("Username atau password salah. Silakan coba lagi.")