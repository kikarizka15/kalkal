# **Sistem Persamaan Linear**

## **1. Persamaan Linear**
**Definisi**

Persamaan linear adalah persamaan yang bisa ditulis dalam bentuk standar:

$$\begin{equation*}
a_1x_1+a_2x_2+\cdots +a_nx_n\text{,}
\end{equation*}$$

di mana:

- variabel hanya berpangkat 1
- tidak ada perkalian antar variabel
- koefisien adalah bilangan real

Jika tidak bisa ditulis dalam bentuk ini → nonlinear.

## **2. Sistem Persamaan Linear**
**Definisi**

Sistem persamaan linear = kumpulan beberapa persamaan linear yang melibatkan variabel yang sama.

Biasanya ditulis dengan:
- persamaan dalam bentuk standar
- variabel sejajar dalam kolom

## **3. Solusi Sistem Linear**
**Apa itu solusi?**

Solusi adalah sekumpulan nilai variabel yang membuat semua persamaan benar sekaligus.

Jika sistem punya solusi → konsisten

Jika tidak punya solusi → inkonsisten

**Kemungkinan bentuk solusi**

Suatu sistem linear hanya punya tiga kemungkinan:

1. Tidak ada solusi
contoh:

$$
\begin{cases}
x + y = 2 \\
x + y = 5
\end{cases}
$$

<iframe src="https://www.geogebra.org/calculator/wdrqh9ph?embed" width="800" height="600" allowfullscreen style="border: 1px solid #e4e4e4;border-radius: 4px;" frameborder="0"></iframe>

2. Tepat satu solusi
contoh:

$$
\begin{cases}
x + y = 5 \\
x - y = 1
\end{cases}
$$

<iframe src="https://www.geogebra.org/calculator/nqynwap5?embed" width="800" height="600" allowfullscreen style="border: 1px solid #e4e4e4;border-radius: 4px;" frameborder="0"></iframe>

3. Tak hingga banyak solusi
contoh:

$$
\begin{cases}
x + y = 4 \\
2x + 2y = 8
\end{cases}
$$

<iframe src="https://www.geogebra.org/calculator/jq6wumd9?embed" width="800" height="600" allowfullscreen style="border: 1px solid #e4e4e4;border-radius: 4px;" frameborder="0"></iframe>

## **4. Eliminasi Gauss**
Serangkaian langkah yang disebut operasi baris yang mempertahankan penyelesaian sistem

$$
\begin{cases}
x_1 - x_2 + x_3 = 3 \\
2x_1 + x_2 + 8x_3 = 18 \\
4x_1 + 2x_2 - 3x_3 = -2
\end{cases}
$$

==

$$
\left[
\begin{array}{ccc|c}
1 & -1 & 1 & 3 \\
2 & 1 & 8 & 18 \\
4 & 2 & -3 & -2
\end{array}
\right]
$$

**Setelah eliminasi Gauss (bentuk tangga)**

$$
\begin{cases}
x_1 - x_2 + x_3 = 3 \\
x_2 + 2x_3 = 4 \\
x_3 = 2
\end{cases}
$$

$$
\left[
\begin{array}{ccc|c}
1 & -1 & 1 & 3 \\
0 & 1 & 2 & 4 \\
0 & 0 & 1 & 2
\end{array}
\right]
$$

**Eliminasi Gauss menggunakan bentuk python**

python
import numpy as np

def eliminasi_gauss(A):
    A = A.astype(float)
    n = len(A)

    for i in range(n):

        if A[i][i] == 0:
            for j in range(i+1, n):
                if A[j][i] != 0:
                    A[[i, j]] = A[[j, i]]
                    break

        pivot = A[i][i]
        A[i] = A[i] / pivot

        for j in range(i+1, n):
            faktor = A[j][i]
            A[j] = A[j] - faktor * A[i]

    return A