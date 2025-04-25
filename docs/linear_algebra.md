# Algebra Linear 

## Matrizes

### Checklist

- [  ] Capítulo 1.1 e início do 1.1 do GAAL

### Operações com Matrizes

As definições abaixo estão implementadas no diretório [matrix](/src/matrix/).

> **Definição de soma:**
A soma de matrizes de mesmo tamanho A = (a<sub>ij</sub>)<sub>m x n</sub> e B = (a<sub>ij</sub>)<sub>m x n</sub> é definida como sendo a matriz m x n
>
> <center>C = A + B</center>
>
> obtida somando-se os elementos correspondentes de A e B, ou seja, 
>
> <center>c<sub>ij</sub> = a<sub>ij</sub> + b<sub></sub>,</center>
>
> para i = 1, ..., m e j = 1, ..., n. Escrevemos também [A + B]<sub>ij</sub> = a<sub>ij</sub> + b<sub>ij</sub>.
>

> **Definição de multiplicação:** A multiplicação de uma matriz A = (a<sub>ij</sub>)<sub>m x n</sub> por um [escalar](/src/matrix/scalar.py) (número) $\alpha$ é definida pela matriz m x n
>
> <center>B = αA</center>
>
> obtida multiplicando-se cada elemento da matriz A pelo escalar α, ou seja,
>
> <center>b<sub>ij</sub> = α a<sub>ij</sub>,
>
> para i = 1, ..., m e j = 1, ..., n. Escrevemos também [αA]<sub>ij</sub> = α a<sub>ij</sub>. Dizemos que a matriz B é um múltiplo escalar da matriz A. **to-do**

> **Definição de produto:** O produto de duas matrizes, tais que o número de colunas da primeira matriz é igual ao número de linhas da segunda, A = (a<sub>ij</sub>)<sub>m x p</sub> e B = (b<sub>ij</sub>)<sub>p x n</sub> é definido pela matriz m x n
>
> <center>C = AB</center>
>  
> obtida da seguinte forma:
> 
> <center>c<sub>ij</sub> = a<sub>i1</sub>b<sub>1j</sub> + a<sub>i2</sub>b<sub>2j</sub> + ... + a<sub>ip</sub>b<sub>pj</sub>,</center>
>   
> para i = 1, ..., m e j = 1, ..., n. Escrevemos também [AB]<sub>ij</sub> = a<sub>i1</sub>b<sub>1j</sub> + a<sub>i2</sub>b<sub>2j</sub> + ... + a<sub>ip</sub>b<sub>pj</sub>.

> **Definição de transposta:** A transposta de uma matriz A = (a<sub>ij</sub>)<sub>m x n</sub> é definida pela matriz n x m
>
> <center>B = A<sup>t</sup></center>
>
> obtida trocando-se as linhas com as colunas, ou seja,
>
> b<sub>ij</sub> = a<sub>ij</sub>,
>
> para i = 1, ..., n e j = 1, ..., m. Escrevemos também [A<sup>t</sup>]<sub>ij</sub> = a<sub>ij</sub>.

### Propriedades da Álgebra Matricial

> **Teorema 1.1:** Sejam A, B e C matrizes com tamanhos apropriados,  $\alpha$ e $\beta$ escalares. São válidas as seguintes propriedades para as operações matriciais:
>
> - **(a) (comutatividade)**  A + B = B + A
>
> - **(b) (associatividade)**  A + (B + C) = (A + B) + C
>
> - **(c) (elemento neutro)**  A matriz $\overline{0}$ m x n, definida por $\mathbf{[\overline{0}]}_{ij} = 0$, para i = 1, ..., m, j = 1, ..., n, é tal que
>
> <center>$$A + \overline{0} = A$$</center>
>
> para toda matriz A, m x n. A matriz $\overline{0}$ é chamada **matriz nula** m x n.
>
> - **(d) (elemento simétrico)**  Para cada matriz A, existe uma única matriz -A, definida por [-A]<sub>ij</sub> = -a<sub>ij</sub>, tal que
>
> <center>$$ A + (-A) = \overline{0}. $$</center>
>
> - **(e) (associatividade)**  $\alpha$ ($\beta$ A) = ($\alpha$ $\beta$) A
>
> - **(f) (distributividade)**  ($\alpha$ + $\beta$) A = $\alpha$ A + $\beta$ A
>
> - **(g) (distributividade)**  $\alpha$ (A + B) = $\alpha$ A + $\alpha$ B
>
> - **(h) (associatividade)**  A(BC) = (AB)C 
>
> - **(i) (elemento neutro)**  Para cada inteiro positivo p, a matriz p x p,  
  I<sub>p</sub> = $\begin{bmatrix}
  1 & 0 & \cdots & 0 \\
  0 & 1 & \cdots & 0 \\
  \vdots & \vdots & \ddots & \vdots \\
  0 & 0 & \cdots & 1
  \end{bmatrix}$  
> chamada **matriz identidade**, é tal que A I<sub>n</sub> = I<sub>m</sub> A = A, para toda matriz A = (a<sub>ij</sub>)<sub>m x n</sub>.
>
> - **(j) (distributividade)**  A(B + C) = AB + AC e (B + C)A = BA + CA;
>
> - **(k)**  ($\alpha$ A)B = $\alpha$ (AB) = A($\alpha$ B);
> 
> - **(l)**  (A<sup>t</sup>)<sup>t</sup> = A;
>
> - **{m}**  (A + B)<sup>t</sup> = A<sup>t</sup> + B<sup>t</sup>;
> 
> - **(n)**  ($\alpha$ A)<sup>t</sup> = $\alpha$ A<sup>t</sup>;
> 
> - **(o)**  (AB)<sup>t</sup> = B<sup>t</sup>A<sup>t</sup>.

## Inversão de Matrizes e Determinantes

## Vetores no Plano e no Espaço