# AMMAR RASYAD KURNIA
# 2603667
# KELAS 1A

username = "admin"
password = "admin123"
lucky_num = 67

while True:
    input_username = input("Masukkan username: ")
    input_password = input("Masukkan password: ")

    if input_username == username and input_password == password or input_username == username and int(input_password) == lucky_num:
        print("Login berhasil!")
        break
    else:
        print("Username atau password salah. Silakan coba lagi.")