---
comments: true
---

# Mathematical marvels

<div class="grid" markdown>

<a href = '../hosted/KYA323_Constants_and_constants_and_formulae.pdf'>:material-math-integral:</a> Physical constants and mathematical formulae
{ .card }

<a href = '../hosted/CLEBSCH_GORDAN.pdf.pdf'>:material-table-heart:</a> Clebsch-Gordan coefficients
{ .card }

</div>

---


## Diagonalization of a \(3 \times 3\) Matrix

Given a matrix \(A\):

\[
A = \begin{pmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{pmatrix}
\]

1. **Find the eigenvalues** by solving the characteristic equation:
\[
\det(A - \lambda I) = 0
\]
2. **Find the eigenvectors** for each eigenvalue \(\lambda\) by solving:
\[
(A - \lambda I)\mathbf{v} = 0
\]
3. **Form the matrix** \(P\) using the eigenvectors as columns:
\[
P = \begin{pmatrix}
\mathbf{v}_1 & \mathbf{v}_2 & \mathbf{v}_3
\end{pmatrix}
\]
4. **Construct the diagonal matrix** \(D\) with the eigenvalues on the diagonal:
\[
D = \begin{pmatrix}
\lambda_1 & 0 & 0 \\
0 & \lambda_2 & 0 \\
0 & 0 & \lambda_3
\end{pmatrix}
\]
5. \textbf{Verify} that \(A = PDP^{-1}\).

--8<-- "includes/abbreviations.md"
