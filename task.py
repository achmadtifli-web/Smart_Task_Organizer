from database import TASK_FILE, next_task_id, append_line, compose_task_line
from validasi import normalize_level, valid_date

def add_task(username):
    print("\n=== Menambah Task Baru ===")
    tid = next_task_id()
    judul = input("Masukkan judul task: ").strip()
    if judul == "":
        print("Judul tidak boleh kosong. Batal.")
        return
    deskripsi = input("Masukkan Deskripsi task (Opsional): ").strip()
    level = input("Berikan Level kesulitan task (Mudah/Sedang/Sulit): ").strip()
    level = normalize_level(level)
    if level is None:
        print("Level tidak valid. Gunakan: Mudah, Sedang, atau Sulit. Batal.")
        return
    deadline = input("Masukkan Deadline Task (YYYY-MM-DD): ").strip()
    if not valid_date(deadline):
        print("Format deadline tidak valid. Batal.")
        return
    status = "Belum"
    t = {
        "id": tid,
        "username": username,
        "judul": judul,
        "deskripsi": deskripsi,
        "level": level,
        "deadline": deadline,
        "status": status
    }
    append_line(TASK_FILE, compose_task_line(t))
    print("Task berhasil ditambahkan.")