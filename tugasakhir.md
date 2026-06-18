# Tugas Akhir KAL (Determinan, Dekomposisi dan Invers Matriks)

## A. Soal Determinan Matriks 3×3
### Soal 1

$$
A=
\begin{bmatrix}
2 & 1 & 3\\
0 & 4 & 5\\
1 & 2 & 1
\end{bmatrix}
$$

### Ekspansi baris ke-3

$$
\det(A)=
\sum_{j=1}^{3}
(-1)^{3+j}a_{3j}\det(A_{3j})
$$

$$
=(-1)^{3+1}(1)\det
\begin{bmatrix}
1 & 3\\
4 & 5
\end{bmatrix}
+(-1)^{3+2}(2)\det
\begin{bmatrix}
2 & 3\\
0 & 5
\end{bmatrix}
+(-1)^{3+3}(1)\det
\begin{bmatrix}
2 & 1\\
0 & 4
\end{bmatrix}
$$

$$
=(1)(1)(1\cdot5-3\cdot4)
+(-1)(2)(2\cdot5-3\cdot0)
+(1)(1)(2\cdot4-1\cdot0)
$$

$$
=(5-12)-2(10)+(8)
$$

$$
=-7-20+8
$$

$$
\det(A)=-19
$$


### Soal 2

$$
B=
\begin{bmatrix}
3 & 2 & 1\\
1 & 0 & 4\\
2 & 5 & 1
\end{bmatrix}
$$

### Ekspansi baris ke-2

$$
\det(B)=
\sum_{j=1}^{3}
(-1)^{2+j}a_{2j}\det(A_{2j})
$$

$$
=(-1)^{2+1}(1)\det
\begin{bmatrix}
2 & 1\\
5 & 1
\end{bmatrix}
+(-1)^{2+2}(0)\det
\begin{bmatrix}
3 & 1\\
2 & 1
\end{bmatrix}
+(-1)^{2+3}(4)\det
\begin{bmatrix}
3 & 2\\
2 & 5
\end{bmatrix}
$$

$$
=(-1)(1)(2\cdot1-1\cdot5)
+(1)(0)(3\cdot1-1\cdot2)
+(-1)(4)(3\cdot5-2\cdot2)
$$

$$
=-1(-3)+0+(-4)(11)
$$

$$
=3-44
$$

$$
\det(B)=-41
$$


### Soal 3

$$
C=
\begin{bmatrix}
1 & 2 & 3\\
2 & 4 & 6\\
1 & 1 & 1
\end{bmatrix}
$$

### Ekspansi baris ke-3

$$
\det(C)=
\sum_{j=1}^{3}
(-1)^{3+j}a_{3j}\det(A_{3j})
$$

$$
=(-1)^{3+1}(1)\det
\begin{bmatrix}
2 & 3\\
4 & 6
\end{bmatrix}
+(-1)^{3+2}(1)\det
\begin{bmatrix}
1 & 3\\
2 & 6
\end{bmatrix}
+(-1)^{3+3}(1)\det
\begin{bmatrix}
1 & 2\\
2 & 4
\end{bmatrix}
$$

$$
=(1)(12-12)+(-1)(6-6)+(1)(4-4)
$$

$$
=0+0+0
$$

$$
\det(C)=0
$$

Karena

$$
\det(C)=0
$$

maka

$$
\text{Matriks } C \text{ singular}
$$

## B. Soal Dekomposisi Matriks (LU Decomposition)

### Soal 4

$$
A=
\begin{bmatrix}
2 & 4 & 2\\
1 & 5 & 2\\
1 & 2 & 4
\end{bmatrix}
$$

Misalkan

$$
A=LU
$$

dengan

$$
L=
\begin{bmatrix}
1 & 0 & 0\\
l_{21} & 1 & 0\\
l_{31} & l_{32} & 1
\end{bmatrix}
$$

Langkah 1

Hilangkan elemen di bawah pivot pertama $a_{11}=2$

$$
l_{21}=\frac{1}{2}
$$

$$
R_2 \leftarrow R_2-\frac12R_1
$$

$$
[1,5,2]-\frac12[2,4,2]
=
[0,3,1]
$$

Kemudian

$$
l_{31}=\frac12
$$

$$
R_3 \leftarrow R_3-\frac12R_1
$$

$$
[1,2,4]-\frac12[2,4,2]
=
[0,0,3]
$$

Sehingga diperoleh

$$
\begin{bmatrix}
2 & 4 & 2\\
0 & 3 & 1\\
0 & 0 & 3
\end{bmatrix}
$$

Langkah 2

Hilangkan elemen di bawah pivot kedua

Karena elemen $(3,2)$ sudah nol,

$$
l_{32}=0
$$

Matriks $U$

$$
U=
\begin{bmatrix}
2 & 4 & 2\\
0 & 3 & 1\\
0 & 0 & 3
\end{bmatrix}
$$

Matriks $L$

$$
L=
\begin{bmatrix}
1 & 0 & 0\\
\frac12 & 1 & 0\\
\frac12 & 0 & 1
\end{bmatrix}
$$

Hasil

$$
L=
\begin{bmatrix}
1 & 0 & 0\\
\frac12 & 1 & 0\\
\frac12 & 0 & 1
\end{bmatrix}
$$

$$
U=
\begin{bmatrix}
2 & 4 & 2\\
0 & 3 & 1\\
0 & 0 & 3
\end{bmatrix}
$$

### Soal 5

$$
B=
\begin{bmatrix}
1 & 2 & 1\\
2 & 5 & 3\\
4 & 10 & 8
\end{bmatrix}
$$

Langkah 1

Pivot pertama $=1$

$$
l_{21}=2
$$

$$
R_2 \leftarrow R_2-2R_1
$$

$$
[2,5,3]-2[1,2,1]
=
[0,1,1]
$$

$$
l_{31}=4
$$

$$
R_3 \leftarrow R_3-4R_1
$$

$$
[4,10,8]-4[1,2,1]
=
[0,2,4]
$$

Matriks menjadi

$$
\begin{bmatrix}
1 & 2 & 1\\
0 & 1 & 1\\
0 & 2 & 4
\end{bmatrix}
$$

Langkah 2

Pivot kedua $=1$

$$
l_{32}=2
$$

$$
R_3 \leftarrow R_3-2R_2
$$

$$
[0,2,4]-2[0,1,1]
=
[0,0,2]
$$

Maka

$$
U=
\begin{bmatrix}
1 & 2 & 1\\
0 & 1 & 1\\
0 & 0 & 2
\end{bmatrix}
$$

Matriks $L$

$$
L=
\begin{bmatrix}
1 & 0 & 0\\
2 & 1 & 0\\
4 & 2 & 1
\end{bmatrix}
$$

Hasil

$$
L=
\begin{bmatrix}
1 & 0 & 0\\
2 & 1 & 0\\
4 & 2 & 1
\end{bmatrix}
$$

$$
U=
\begin{bmatrix}
1 & 2 & 1\\
0 & 1 & 1\\
0 & 0 & 2
\end{bmatrix}
$$

### Soal 6

$$
C=
\begin{bmatrix}
4 & 2 & 0\\
2 & 5 & 1\\
0 & 1 & 3
\end{bmatrix}
$$

Langkah 1

Pivot pertama $=4$

$$
l_{21}=\frac24=\frac12
$$

$$
R_2 \leftarrow R_2-\frac12R_1
$$

$$
[2,5,1]-\frac12[4,2,0]
=
[0,4,1]
$$

$$
l_{31}=0
$$

$$
R_3 \leftarrow R_3-0R_1
$$

$$
[0,1,3]
$$

Maka

$$
\begin{bmatrix}
4 & 2 & 0\\
0 & 4 & 1\\
0 & 1 & 3
\end{bmatrix}
$$

Langkah 2

Pivot kedua $=4$

$$
l_{32}=\frac14
$$

$$
R_3 \leftarrow R_3-\frac14R_2
$$

$$
[0,1,3]-\frac14[0,4,1]
=
\left[0,0,\frac{11}{4}\right]
$$

Matriks $U$

$$
U=
\begin{bmatrix}
4 & 2 & 0\\
0 & 4 & 1\\
0 & 0 & \frac{11}{4}
\end{bmatrix}
$$

Matriks $L$

$$
L=
\begin{bmatrix}
1 & 0 & 0\\
\frac12 & 1 & 0\\
0 & \frac14 & 1
\end{bmatrix}
$$

Hasil

$$
L=
\begin{bmatrix}
1 & 0 & 0\\
\frac12 & 1 & 0\\
0 & \frac14 & 1
\end{bmatrix}
$$

$$
U=
\begin{bmatrix}
4 & 2 & 0\\
0 & 4 & 1\\
0 & 0 & \frac{11}{4}
\end{bmatrix}
$$

Sehingga

$$
A=LU
$$

# C. Soal Invers Matriks 3×3
## Soal  7

$$
A=
\begin{bmatrix}
1 & 2 & 1\\
0 & 1 & 1\\
2 & 3 & 4
\end{bmatrix}
$$

Determinan

$$
\det(A)
=
1
\begin{vmatrix}
1 & 1\\
3 & 4
\end{vmatrix}
-2
\begin{vmatrix}
0 & 1\\
2 & 4
\end{vmatrix}
+1
\begin{vmatrix}
0 & 1\\
2 & 3
\end{vmatrix}
$$

$$
=(1)(4-3)-2(0-2)+(1)(0-2)
$$

$$
=1+4-2
$$

$$
=3
$$

Matriks Kofaktor

$$
C=
\begin{bmatrix}
1 & 2 & -2\\
-5 & 2 & 1\\
1 & -1 & 1
\end{bmatrix}
$$

Adjoin

$$
\operatorname{adj}(A)
=
C^T
=
\begin{bmatrix}
1 & -5 & 1\\
2 & 2 & -1\\
-2 & 1 & 1
\end{bmatrix}
$$

Invers

$$
A^{-1}
=
\frac{1}{\det(A)}
\operatorname{adj}(A)
$$

$$
=
\frac13
\begin{bmatrix}
1 & -5 & 1\\
2 & 2 & -1\\
-2 & 1 & 1
\end{bmatrix}
$$

$$
A^{-1}
=
\begin{bmatrix}
\frac13 & -\frac53 & \frac13\\
\frac23 & \frac23 & -\frac13\\
-\frac23 & \frac13 & \frac13
\end{bmatrix}
$$

## Soal 8

$$
B=
\begin{bmatrix}
2 & 1 & 0\\
1 & 2 & 1\\
0 & 1 & 2
\end{bmatrix}
$$

Determinan

$$
\det(B)
=
2
\begin{vmatrix}
2 & 1\\
1 & 2
\end{vmatrix}
-1
\begin{vmatrix}
1 & 1\\
0 & 2
\end{vmatrix}
+0
$$

$$
=
2(4-1)-(2)
$$

$$
=
6-2
$$

$$
=
4
$$

Matriks Kofaktor

$$
C=
\begin{bmatrix}
3 & -2 & 1\\
-2 & 4 & -2\\
1 & -2 & 3
\end{bmatrix}
$$

Adjoin

$$
\operatorname{adj}(B)
=
\begin{bmatrix}
3 & -2 & 1\\
-2 & 4 & -2\\
1 & -2 & 3
\end{bmatrix}
$$

Invers

$$
B^{-1}
=
\frac14
\begin{bmatrix}
3 & -2 & 1\\
-2 & 4 & -2\\
1 & -2 & 3
\end{bmatrix}
$$

$$
B^{-1}
=
\begin{bmatrix}
\frac34 & -\frac12 & \frac14\\
-\frac12 & 1 & -\frac12\\
\frac14 & -\frac12 & \frac34
\end{bmatrix}
$$

## Soal 9

$$
C=
\begin{bmatrix}
3 & 0 & 2\\
2 & 0 & -2\\
0 & 1 & 1
\end{bmatrix}
$$

Determinan

$$
\det(C)
=
3
\begin{vmatrix}
0 & -2\\
1 & 1
\end{vmatrix}
+
2
\begin{vmatrix}
2 & 0\\
0 & 1
\end{vmatrix}
$$

$$
=
3(0+2)+2(2)
$$

$$
=
6+4
$$

$$
=
10
$$

Matriks Kofaktor

$$
C_f=
\begin{bmatrix}
2 & -2 & 2\\
2 & 3 & -3\\
0 & 10 & 0
\end{bmatrix}
$$

Adjoin

$$
\operatorname{adj}(C)
=
\begin{bmatrix}
2 & 2 & 0\\
-2 & 3 & 10\\
2 & -3 & 0
\end{bmatrix}
$$

Invers

$$
C^{-1}
=
\frac1{10}
\begin{bmatrix}
2 & 2 & 0\\
-2 & 3 & 10\\
2 & -3 & 0
\end{bmatrix}
$$

$$
C^{-1}
=
\begin{bmatrix}
\frac15 & \frac15 & 0\\
-\frac15 & \frac3{10} & 1\\
\frac15 & -\frac3{10} & 0
\end{bmatrix}
$$