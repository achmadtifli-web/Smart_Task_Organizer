from database import load_tasks
import datetime

def stats_for_user(username):
    tasks = [t for t in load_tasks() if t["username"] == username]
    total = len(tasks)
    selesai = sum(1 for t in tasks if t["status"].lower() == "sudah")
    belum = total - selesai

    # hindari pembagian nol
    if total > 0:
        pct_selesai = f"{(selesai/total*100):.1f}%"
        pct_belum = f"{(belum/total*100):.1f}%"
    else:
        pct_selesai = pct_belum = "0%"

    # by level
    mudah = sum(1 for t in tasks if t["level"].lower() == "mudah")
    sedang = sum(1 for t in tasks if t["level"].lower() == "sedang")
    sulit = sum(1 for t in tasks if t["level"].lower() == "sulit")

    # nearest deadline
    nearest_date = None
    nearest_titles = []

    for t in tasks:
        try:
            d = datetime.datetime.strptime(t["deadline"], "%Y-%m-%d").date()
            if nearest_date is None or d < nearest_date:
                nearest_date = d
                nearest_titles = [t["judul"]]
            elif d == nearest_date:
                nearest_titles.append(t["judul"])
        except:
            pass

    print("\n=== Statistik Akun ===")
    print(f"Username: {username}")
    print(f"Total tugas: {total}")
    print(f"Selesai: {selesai} ({pct_selesai})")
    print(f"Belum selesai: {belum} ({pct_belum})")

    print("\nBerdasarkan tingkat kesulitan:")
    print(f"- Mudah: {mudah}")
    print(f"- Sedang: {sedang}")
    print(f"- Sulit: {sulit}")

    if nearest_date:
        print(f"\nDeadline terdekat ({nearest_date.isoformat()}):")
        for judul in nearest_titles:
            print(f'- "{judul}"')
    else:
        print("\nTidak ada deadline terdeteksi.")
