# Menghitung determinan matrik dengan menggunakan rumus expansi baris

$$
\sum_{k=1}^{n} (-1)^{i+k} a_{ik} M_{ik}
$$

dengan \( M_{ij} \) adalah minor dari matriks \( A \) dan

$$
M_{ij} = \det A_{ij}
$$

\( A_{ij} \) adalah submatrik dengan menghapus baris \( i \) dan kolom \( j \) dari matriks \( A_{m \times n} \) dengan \( 1 \le i,j \le n \).

## 1. Determinan Matriks 2x2

$$
A=
\begin{pmatrix}
-7 & -5 \\
1 & 4
\end{pmatrix}
$$

Rumus:

$$
\det(A)=ad-bc
$$

Perhitungan:

$$
\det(A)=(-7)(4)-(-5)(1)
$$

$$
=-28+5=-23
$$

## 2. Determinan Matriks 3x3

$$
A=
\begin{pmatrix}
0 & 2 & -3\\
1 & -2 & -1\\
0 & 0 & 1
\end{pmatrix}
$$

Ekspansi baris pertama:

$$
\det(A)=0 + (-1)^{1+2}(2)
\begin{vmatrix}
1 & -1\\
0 & 1
\end{vmatrix}
+ (-1)^{1+3}(-3)
\begin{vmatrix}
1 & -2\\
0 & 0
\end{vmatrix}
$$

Hitung minor:

$$
= (-1)(2)(1\cdot1-(-1)\cdot0) + (1)(-3)(0)
$$

$$
=-2
$$

## 3. Determinan Matriks 4x4

$$
A=
\begin{pmatrix}
1 & -3 & 1 & 1\\
-3 & 1 & 1 & 1\\
1 & 1 & -3 & 1\\
1 & 1 & 1 & -3
\end{pmatrix}
$$

Jumlah setiap baris:

$$
1-3+1+1=0
$$

Karena ada baris yang saling bergantung (linear dependent):

$$
\det(A)=0
$$

**Sifat Determinan: Kalau ada baris/kolom yang saling bergantung (linear dependent) → determinan = 0**

Baris 1:

$$
1-3+1+1=0
$$

Baris 2:

$$
-3+1+1+1=0
$$

Baris 3:

$$
1+1-3+1=0
$$

Baris 4:

$$
1+1+1-3=0
$$

Semua baris jumlahnya 0.

Jadi

$$
\det(A)=0
$$

# Menggunakan rumus matriks adjoin untuk menghitung invers dari matriks berikut dengan rumus

$$
(\mathrm{adj}\,A)_{ij}=(-1)^{i+j}M_{ji}
$$

$$
A^{-1}=\frac{1}{\det A}\,\mathrm{adj}\,A
$$

## 4. Invers Matriks 2x2 (Metode Adjoin)

$$
A=
\begin{pmatrix}
-7 & -5 \\
1 & 4
\end{pmatrix}
$$

Langkah 1: Determinan

$$
\det(A)=(-7)(4)-(-5)(1)=-28+5=-23
$$

Langkah 2: Minor

$$
M_{11}=4,\quad
M_{12}=1,\quad
M_{21}=-5,\quad
M_{22}=-7
$$

Langkah 3: Kofaktor

$$
C_{11}=4,\quad
C_{12}=-1,\quad
C_{21}=5,\quad
C_{22}=-7
$$

Langkah 4: Adjoin (transpose kofaktor)

$$
\operatorname{adj}(A)=
\begin{pmatrix}
4 & 5\\
-1 & -7
\end{pmatrix}
$$

Langkah 5: Invers

$$
A^{-1}
=
\frac{1}{-23}
\begin{pmatrix}
4 & 5\\
-1 & -7
\end{pmatrix}
$$

Invers:

$$
A^{-1}
=
\begin{pmatrix}
-\frac{4}{23} & -\frac{5}{23}\\
\frac{1}{23} & \frac{7}{23}
\end{pmatrix}
$$

## 5. Invers Matriks 3x3 (Metode Adjoin)

$$
A=
\begin{pmatrix}
0 & 2 & -3\\
1 & -2 & -1\\
0 & 0 & 1
\end{pmatrix}
$$

Langkah 1: Determinan

Ekspansi baris ke-3:

$$
\det(A)
=
1
\begin{vmatrix}
0 & 2\\
1 & -2
\end{vmatrix}
=
1(0-2)
=
-2
$$

Langkah 2: Matriks Kofaktor

$$
C=
\begin{pmatrix}
-2 & -1 & 0\\
-2 & 0 & 0\\
-8 & -3 & -2
\end{pmatrix}
$$

Langkah 3: Adjoin (Transpose Kofaktor)

$$
\operatorname{adj}(A)=
\begin{pmatrix}
-2 & -2 & -8\\
-1 & 0 & -3\\
0 & 0 & -2
\end{pmatrix}
$$

Langkah 4: Invers

$$
A^{-1}
=
\frac{1}{-2}
\begin{pmatrix}
-2 & -2 & -8\\
-1 & 0 & -3\\
0 & 0 & -2
\end{pmatrix}
$$

$$
A^{-1}
=
\begin{pmatrix}
1 & 1 & 4\\
\frac{1}{2} & 0 & \frac{3}{2}\\
0 & 0 & 1
\end{pmatrix}
$$

## 6. Invers Matriks 4x4

$$
A=
\begin{pmatrix}
1 & -3 & 1 & 1\\
-3 & 1 & 1 & 1\\
1 & 1 & -3 & 1\\
1 & 1 & 1 & -3
\end{pmatrix}
$$

Langkah 1: Cek determinan

$$
1-3+1+1=0
$$

Baris saling bergantung (linear dependent)

$$
\det(A)=0
$$

Langkah 2: Kesimpulan

$$
A^{-1}\ \text{tidak ada karena determinan = 0 dan disebut Matriks Singular}
$$