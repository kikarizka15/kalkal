import matplotlib.pyplot as plt
import matplotlib.animation as animation

# =====================================
# TITIK ATAS
# =====================================

points_atas = {
    "A": [2, 3],
    "B": [2, 4],
    "C": [3, 4],
    "D": [3, 3]
}

# =====================================
# FIGURE
# =====================================

fig, ax = plt.subplots(figsize=(6,8))

ax.set_xlim(-5, 5)
ax.set_ylim(-6, 6)

# sumbu x dan y
ax.axhline(0)
ax.axvline(0)

ax.grid()

# scatter atas
scatter_atas = ax.scatter([], [], s=100)

# scatter bawah (hasil cermin)
scatter_bawah = ax.scatter([], [], s=100)

texts = []

# data awal
x_atas = [p[0] for p in points_atas.values()]
y_atas = [p[1] for p in points_atas.values()]


# =====================================
# ANIMASI
# =====================================

def update(frame):

    global texts

    # hapus text lama
    for t in texts:
        t.remove()

    texts = []

    # ==========================
    # GERAK TITIK ATAS
    # ==========================

    y_baru = []

    for y in y_atas:

        # turun perlahan
        turun = y - frame * 0.03

        y_baru.append(turun)

    # update titik atas
    scatter_atas.set_offsets(list(zip(x_atas, y_baru)))

    # ==========================
    # CERMIN SUMBU X
    # ==========================

    y_cermin = []

    for y in y_baru:

        # refleksi sumbu x
        y_reflect = -y