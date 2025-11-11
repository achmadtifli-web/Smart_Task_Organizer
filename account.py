from database import read_lines, append_line, AKUN_FILE

def load_accounts():
    lines = read_lines(AKUN_FILE)
    accounts = {}
    for ln in lines:
        parts = ln.split("|")
        if len(parts) >= 2:
            uname = parts[0].strip()
            pwd = parts[1].strip()
            accounts[uname] = pwd
    return accounts

def register_account():
    accounts = load_accounts()
    print("\n=== Registrasi Akun ===")
    username = input("Masukkan Username: ").strip()
    if username == "":
        print("Username tidak boleh kosong.")
        return
    if username in accounts:
        print("Username sudah terdaftar.")
        return
    password = input("Masukkan Kata Sandi: ").strip()
    if password == "":
        print("Password tidak boleh kosong.")
        return
    append_line(AKUN_FILE, f"{username}|{password}")
    print("Akun anda berhasil didaftarkan.")

def login():
    accounts = load_accounts()
    print("\n=== Login Akun ===")
    username = input("Masukkan Username: ").strip()
    password = input("Masukkan Kata Sandi: ").strip()
    if username in accounts and accounts[username] == password:
        print(f'\nSelamat datang user {username} di Smart Task Organizer')
        return username
    else:
        print("Nama / Kata sandi yang dimasukkan tidak sesuai")
        return None