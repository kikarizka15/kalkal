# Tugas Akhir KAL (Determinan, Dekomposisi dan Invers Matriks)
## Soal 1

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

\bigskip

## Soal 2

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

\bigskip

## Soal 3

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