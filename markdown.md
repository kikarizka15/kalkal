---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---
# INVERS
## Diketahui:
$A =
\begin{bmatrix}
1 & 1 & 1 & 1 \\
2 & -1 & 1 & -1 \\
1 & 2 & -1 & 1 \\
3 & -1 & 2 & 1
\end{bmatrix}
\quad
B =
\begin{bmatrix}
10 \\
-1 \\
6 \\
11
\end{bmatrix}
$

## Mencari Invers Matriks A
### Langkah 1 Rumus Invers
$A^{-1} = \frac{1}{\det(A)} \cdot \text{adj}(A)$

### Langkah 2 Hitung Determinan
### Kita ekspansi baris pertama:
det(A)=1C11​+1C12​+1C13​+1C14​

dengan

Cij​=(−1)i+jMij​

di mana Mij​ adalah minor.

Jadi kita cari minor satu-satu dari baris pertama.

## Cari determinan dari baris pertama
det(A)=−3+9+11−4=13

## Minor

$
\text{Minor } M_{11}
$

$
M_{11}=
\begin{vmatrix}
-1 & 1 & -1\
2 & -1 & 1\
-1 & 2 & 1
\end{vmatrix}
$


# Menghitung Determinan Matriks dengan Ekspansi Baris

$$
\sum_{k=1}^{n} (-1)^{i+k} a_{ik} M_{ik}
$$

Dengan ( M_{ij} ) adalah minor dari matriks ( A ), dan:

$$
M_{ij} = \det A_{ij}
$$

( A_{ij} ) adalah submatriks yang diperoleh dengan menghapus baris ke-( i ) dan kolom ke-( j ) dari matriks ( A ).

---

## 1. Determinan Matriks 2x2

$$
A=\begin{pmatrix}-7 & -5 \ 1 & 4\end{pmatrix}
$$

**Rumus:**

$$
\det(A)=ad-bc
$$

**Perhitungan:**

$$
\det(A)=(-7)(4)-(-5)(1)
$$

$$
=-28+5=-23
$$

---

## 2. Determinan Matriks 3x3

$$
A=\begin{pmatrix}
0 & 2 & -3\
1 & -2 & -1\
0 & 0 & 1
\end{pmatrix}
$$

**Ekspansi baris pertama:**

$$
\det(A)=0 + (-1)^{1+2}(2)
\begin{vmatrix}1 & -1\0 & 1\end{vmatrix}

* (-1)^{1+3}(-3)
  \begin{vmatrix}1 & -2\0 & 0\end{vmatrix}
  $$

**Hitung minor:**

$$
= (-1)(2)(1\cdot1-(-1)\cdot0) + (1)(-3)(0)
$$

$$
=-2
$$

---

## 3. Determinan Matriks 4x4

$$
A=
\begin{pmatrix}
1 & -3 & 1 & 1\
-3 & 1 & 1 & 1\
1 & 1 & -3 & 1\
1 & 1 & 1 & -3
\end{pmatrix}
$$

Jumlah setiap baris:

$$
1-3+1+1=0
$$

Karena baris saling bergantung (linear dependent):

$$
\det(A)=0
$$

**Sifat determinan:**
Jika ada baris/kolom yang saling bergantung → determinan = 0

---

# Menggunakan Rumus Adjoin untuk Mencari Invers Matriks

$$
(\mathrm{adj}, A)*{ij} = (-1)^{i+j} M*{ji}
$$

$$
A^{-1} = \frac{1}{\det A} , \mathrm{adj}, A
$$

---

## 4. Invers Matriks 2x2

$$
A=\begin{pmatrix}-7 & -5 \ 1 & 4\end{pmatrix}
$$

**Langkah 1: Determinan**

$$
\det(A)=-23
$$

**Langkah 2: Minor**

$$
M_{11}=4,\quad M_{12}=1,\quad M_{21}=-5,\quad M_{22}=-7
$$

**Langkah 3: Kofaktor**

$$
C_{11}=4,\quad C_{12}=-1,\quad C_{21}=5,\quad C_{22}=-7
$$

**Langkah 4: Adjoin**

$$
\text{adj}(A)=\begin{pmatrix}4 & 5 \ -1 & -7\end{pmatrix}
$$

**Langkah 5: Invers**

$$
A^{-1}=\frac{1}{-23}
\begin{pmatrix}4 & 5 \ -1 & -7\end{pmatrix}
$$

**Hasil:**

$$
A^{-1} =
\begin{pmatrix}
-\frac{4}{23} & -\frac{5}{23} \
\frac{1}{23} & \frac{7}{23}
\end{pmatrix}
$$

---

## 5. Invers Matriks 3x3

$$
A = \begin{pmatrix}
0 & 2 & -3 \
1 & -2 & -1 \
0 & 0 & 1
\end{pmatrix}
$$

**Langkah 1: Determinan**

$$
\det(A) = -2
$$

**Langkah 2: Kofaktor**

$$
C = \begin{pmatrix}
-2 & -1 & 0 \
-2 & 0 & 0 \
-8 & -3 & -2
\end{pmatrix}
$$

**Langkah 3: Adjoin**

$$
\text{adj}(A) =
\begin{pmatrix}
-2 & -2 & -8 \
-1 & 0 & -3 \
0 & 0 & -2
\end{pmatrix}
$$

**Langkah 4: Invers**

$$
A^{-1} = \frac{1}{-2}
\begin{pmatrix}
-2 & -2 & -8 \
-1 & 0 & -3 \
0 & 0 & -2
\end{pmatrix}
$$

$$
A^{-1} =
\begin{pmatrix}
1 & 1 & 4 \
\frac{1}{2} & 0 & \frac{3}{2} \
0 & 0 & 1
\end{pmatrix}
$$

---

## 6. Invers Matriks 4x4

$$
A=
\begin{pmatrix}
1 & -3 & 1 & 1\
-3 & 1 & 1 & 1\
1 & 1 & -3 & 1\
1 & 1 & 1 & -3
\end{pmatrix}
$$

**Langkah 1: Determinan**

$$
\det(A)=0
$$

**Langkah 2: Kesimpulan**

$$
A^{-1} \text{ tidak ada (matriks singular)}
$$