# **Sistem Persamaan Linear**

## **1. Persamaan Linear**

**Definisi**

Persamaan linear adalah persamaan yang dapat ditulis dalam bentuk:

$$
a_1x_1+a_2x_2+\cdots+a_nx_n=b
$$

dengan:

- variabel berpangkat satu
- tidak ada perkalian antar variabel
- koefisien berupa bilangan real

Jika tidak memenuhi syarat tersebut maka disebut persamaan nonlinear.

---

## **2. Sistem Persamaan Linear**

**Definisi**

Sistem persamaan linear adalah kumpulan beberapa persamaan linear yang melibatkan variabel yang sama.

Contoh:

$$
\begin{cases}
2x+y=7\\
x-y=2
\end{cases}
$$

---

## **3. Solusi Sistem Linear**

### Apa itu solusi?

Solusi adalah nilai variabel yang memenuhi seluruh persamaan dalam sistem secara bersamaan.

- Memiliki solusi → **konsisten**
- Tidak memiliki solusi → **inkonsisten**

### Kemungkinan Bentuk Solusi

#### 1. Tidak Ada Solusi

$$
\begin{cases}
2x+y=4\\
2x+y=8
\end{cases}
$$

<iframe src="https://www.geogebra.org/calculator/u6qdsybs?embed" width="800" height="600" allowfullscreen style="border: 1px solid #e4e4e4;border-radius: 4px;" frameborder="0"></iframe>

Kedua garis sejajar sehingga tidak berpotongan.

---

#### 2. Tepat Satu Solusi

$$
\begin{cases}
3x+y=7\\
x-y=1
\end{cases}
$$

<iframe src="https://www.geogebra.org/calculator/kqur4xby?embed" width="800" height="600" allowfullscreen style="border: 1px solid #e4e4e4;border-radius: 4px;" frameborder="0"></iframe>

Kedua garis berpotongan di satu titik.

---

#### 3. Tak Hingga Banyak Solusi

$$
\begin{cases}
x+2y=6\\
2x+4y=12
\end{cases}
$$

<iframe src="https://www.geogebra.org/calculator/kmhdhpkp?embed" width="800" height="600" allowfullscreen style="border: 1px solid #e4e4e4;border-radius: 4px;" frameborder="0"></iframe>

Persamaan kedua merupakan kelipatan persamaan pertama sehingga kedua garis berimpit.

---

# **4. Eliminasi Gauss**

Eliminasi Gauss adalah metode untuk menyelesaikan sistem persamaan linear menggunakan operasi baris elementer hingga diperoleh bentuk tangga.

### Contoh

$$
\begin{cases}
x_1+2x_2-x_3=5\\
2x_1+5x_2+x_3=12\\
3x_1+8x_2+2x_3=19
\end{cases}
$$

Ditulis dalam bentuk matriks diperbesar:

$$
\left[
\begin{array}{ccc|c}
1 & 2 & -1 & 5\\
2 & 5 & 1 & 12\\
3 & 8 & 2 & 19
\end{array}
\right]
$$

### Setelah Eliminasi Gauss (Bentuk Tangga)

$$
\left[
\begin{array}{ccc|c}
1 & 2 & -1 & 5\\
0 & 1 & 3 & 2\\
0 & 0 & 1 & 1
\end{array}
\right]
$$

yang setara dengan:

$$
\begin{cases}
x_1+2x_2-x_3=5\\
x_2+3x_3=2\\
x_3=1
\end{cases}
$$

### Hasil Penyelesaian

Substitusi balik:

$$
x_3=1
$$

$$
x_2+3(1)=2
$$

$$
x_2=-1
$$

$$
x_1+2(-1)-1=5
$$

$$
x_1=8
$$

Sehingga diperoleh:

$$
(x_1,x_2,x_3)=(8,-1,1)
$$

### Eliminasi Gauss Menggunakan Python

```python
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