from database import load_tasks, save_tasks
from validasi import normalize_status, normalize_level, valid_date
from view import find_task_by_id_for_user

def edit_task(username):
    print("\n=== Mengubah Task ===")
    tid = input("Masukkan id task yang ingin diubah: ").strip()
    t = find_task_by_id_for_user(username, tid)
    if not t:
        print("Task tidak ditemukan.")
        return
    print("Tekan Enter jika tidak ingin mengubah kolom tertentu.")
    new_status = input(f"Ubah Status task (Sudah/Belum) [{t['status']}]: ").strip()
    if new_status != "":
        ns = normalize_status(new_status)
        if ns:
            t["status"] = ns
        else:
            print("Status tidak valid, melewati perubahan status.")
    new_judul = input(f"Ubah judul task [{t['judul']}]: ").strip()
    if new_judul != "":
        t["judul"] = new_judul
    new_deskripsi = input(f"Ubah deskripsi task [{t['deskripsi']}]: ").strip()
    if new_deskripsi != "":
        t["deskripsi"] = new_deskripsi
    new_level = input(f"Ubah level kesulitan [{t['level']}]: ").strip()
    if new_level != "":
        nl = normalize_level(new_level)
        if nl:
            t["level"] = nl
        else:
            print("Level tidak valid, melewati perubahan level.")
    new_deadline = input(f"Ubah Deadline task (YYYY-MM-DD) [{t['deadline']}]: ").strip()
    if new_deadline != "":
        if valid_date(new_deadline):
            t["deadline"] = new_deadline
        else:
            print("Deadline tidak valid, melewati perubahan deadline.")
    # Save
    tasks = load_tasks()
    updated = []
    for it in tasks:
        if it["id"] == t["id"] and it["username"] == username:
            updated.append(t)
        else:
            updated.append(it)
    save_tasks(updated)
    print("Task berhasil diubah.")

