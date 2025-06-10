## Álgebra Linear 

“Algebra Linear é o estudo dos espaços vetoriais e das transformações lineares entre eles.”

– Elon Lages Lima

> **Definição de transformação linear:** Uma transformação linear é uma função entre espaços vetoriais que preserva a adição de vetores e a multiplicação por escalar.  
> $$ f(x + y) = f(x) + f(y) \space e \space f(\alpha x) = \alpha f(x) $$

> **Definição de espaço vetorial:** Um espaço vetorial (sobre $\mathbb{R}$) é um conjunto v não vazio no qual estão definidas duas operações: adição (v x v $\rightarrow$ v) e multiplicação por escalar ($\mathbb{R}$ x v $\rightarrow$ v) tais que, para u, v, w $\in$ v e $\alpha$, $\beta$ $\in$ $\mathbb{R}$ são válidas:
> - (a) u $\oplus$ v = v $\oplus$ u
> - (b) (u $\oplus$ v) $\oplus$ w = u $\oplus$ (v $\oplus$ w)
> - (c) $\exists z$ $\in$ v tal que para qualquer u $\in$ v tem-se u $\oplus$ z = u (Not.: $\overline{0}$) 
> - (d) Para cada u $\in$ v existe um z $\in$ v tal que u $\oplus$ z = $\overline{0}$ (Not.: -u)
> - (e) $\alpha \space \odot \space (\beta \space \odot \space u) = (\alpha \beta) \space \odot \space u$ 
> - (f) $(\alpha \space + \space \beta) \space \odot u = (\alpha \space \odot u) \space \oplus \space (\beta \space \odot \space u)$
> - (g) $\alpha \space \odot \space (u \space \oplus v) = (\alpha \space \odot \space u) \space \oplus \space (\alpha \space \odot \space v)$
> - (h) $1 \space \odot \space u = u$
> Neste caso, os elementos de v são chamados de vetores.

## Números Reais

> **Definição de inverso:** Todo número real a, não nulo, possui um inverso multiplicativo tal que ab = ba = 1. Denotamos este número único por a<sup>-1</sup>.

## Somatório
São válidas algumas propriedades para a notação de somatório:

- (a) O índice do somatório é uma variável muda que pode ser substituída por qualquer letra:
$$\sum_{i=1}^n f_i = \sum_{j=1}^n f_j$$

- (b) O somatório de uma soma pode ser escrito como uma soma de dois somatórios:
$$\sum_{i=1}^n (f_i + g_i) = \sum_{i=1}^n f_i + \sum_{i=1}^n g_i$$

- (c) Se no termo geral do somatório aparece um produto, em que um fator não depende do índice do somatório, então este fator pode "sair" do somatório:
$$\sum_{i=1}^n f_i g_k = g_k \sum_{i=1}^n f_i$$

- (d) Num somatório duplo, a ordem dos somatórios pode ser trocada:
$$\sum_{i=1}^n \sum_{j=1}^m f_{ij} = \sum_{j=1}^m \sum_{i=1}^n f_{ij}$$

## Matrizes

### Checklist

- [  ] Capítulo 1.1 e 2.1 do GAAL

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

> **TO-DO** **Definição de matriz inversa:** Nem todas as matrizes A não nulas possuem inversa, ou seja, nem sempre existe uma matriz B tal que AB = AB = I<sub>n</sub>. De início, para que os profutos AB e BA estejam definidos e sejam iguais, é que as matrizes A e B sejam quadradas. Nesni ebtre as matrizes quadradas, muitas não possuem inversa.
>  
> Uma matriz quadrada A = (a<sub>ij</sub>)<sub>m x n</sub> é **invertível** ou **não singular**, se existe uma matriz B = (b<sub>ij</sub>)<sub>n x m</sub> tal que
> $$ A B = B A = I_n , $$
> em que I<sub>n</sub> é a matriz identidade. A matriz B é chamada de **inversa** de A. Se A não tem inversa, dizemos que A é **não invertível** ou **singular**.
>  
> **Teorema:** Se uma matriz A = (a<sub>ij</sub>)<sub>n x m</sub> possui inversa, então a inversa é única.
>  
> **Propriedades da inversa:**
> - (a) Se A = (a<sub>ij</sub>)<sub>n x m</sub> é invertível, então a sua inversa, A<sup>-1</sup>, também o é e 
> $$ (A^{-1})^{-1} = A ; $$
>  
> - (b) Se A = (a<sub>ij</sub>)<sub>n x m</sub> e B = (b<sub>ij</sub>)<sub>n x m</sub> são matrizes invertíveis, então AB é invertível e
> $$ (AB)^{-1} = B^{-1} A^{-1} ; $$
>  
> - (c) Se A = (a<sub>ij</sub>)<sub>n x m</sub> é invertível, então a sua transposta, A<sup>t</sup>, também é invertível e
> $$ (A^t)^{-1} = (A^{-1})^t . $$
>  
> **Teorema:** Sejam A e B matrizes n x m.
> - (a) Se B A = I<sub>n</sub>, então A B = I<sub>n</sub>;
> - (b) Se A B = I<sub>n</sub>, então B A = I<sub>n</sub>.
>  
> **Proposição:** Toda matriz elementar é inertível e sua inversa é também uma matriz elementar.
> - (a) E<sub>i,j</sub><sup>-1</sup> = E<sub>j,i</sub> = E<sub>i,j</sub>;
> - (b) E<sub>i</sub>($\alpha$)<sup>-1</sup> = E<sub>i</sub>(1/$\alpha$), para $\alpha$ $\neq$ 0;
> - (c) E<sub>i,j</sub>($\alpha$)<sup>-1</sup> = E<sub>i,j</sub>(-$\alpha$).
>  
> **Teorema:** Seja A uma matriz n x n. As seguintes afirma;cões são equialentes:
> - (a) Existe uma matriz B, n x n, tal que B A = I<sub>n</sub>.
> - (b) A matriz A é equivalente por linhas à matriz identidade I<sub>n</sub>.
> - (c) A matriz A é invertível.
>  
> **Teorema:** Uma matriz A é invertível se, e somente se, ela é um produto de matrizes elementares.
>  
> **Teorema:** Uma matriz A, n x n, é invertível se, e somente se, A é equivalente por linhas à matriz identidade I<sub>n</sub>.
>
> **Saiba que:** É possível encontrar o conjunto solução escalonando [A | I<sub>n</sub>].
>  
> **Teorema:** Seja A uma matriz n x n.
> - (a) O sistema linear AX = B tem solução única se, e somente se, A é invertível. Neste caso a solução é X = A<sup>-1</sup> B.
> - (b) O sistema homogêneo A X = $\overline{0}$ tem solução não trivial se, e somente se, A é singular (não invertível).
>  
> **Proposição:** Se A e B são matrizes n x n, com AB invertível, então A e B são invertíveis. 
>  
> **TO-DO:** Aplicação em interpolação polinomial e criptografia.

> **Definição de operação elementar:** Uma operação elementar sobre as linhas de uma matriz é uma das seguintes operações:
> - (a) Trocar a posição de duas linhas da matriz;
> - (b) Multiplicar uma linha da matriz por um escalar diferente de zero;
> - (c) Somar a uma linha da matriz um múltiplo escalar de outra linha.

> **Definição de matriz escalonada:** Uma matriz A = (a<sub>ij</sub>)<sub>m x n</sub> está na forma **escalonada reduzida** quando satisfaz as seguintes condições:
> - (a) As linhas nulas (formadas inteiramente por zeros), se ocorrerem, estão abaixo das linhas não nulas;
> - (b) O **pivô** (1<sup>o</sup> elemento não nulo de uma linha) de cada linha não nula é igual a 1;
> - (c) O pivô de cada linha não nula ocorre à direita do pivô da linha anterior;
> - (d) Se uma coluna contém um pivô, então todos os seus outros elementos são iguais a zero.

> **TO-DO** **Definição de equivalente por linhas:** Uma matriz A = (a<sub>ij</sub>)<sub>m x n</sub> é equivalente por linhas a uma matriz B = (b<sub>ij</sub>)<sub>m x n</sub>, se B pode ser obtido de A aplicando-se uma sequência de operações elementares sobre as suas linhas.
>
> Cuidado! São equivalente por linhas, não iguais.
> - Toda matriz é equivalente por linhas a ela mesma (**reflexividade**);
> - Se A é equivalente por linhas a B, então B é equivalente por linhas a A (**simetria**);
> - Se A é equivalente por linhas a B e B é equivalente por linhas a C, então A é equivalente por linhas a C (**transitividade**).

> **TO-DO** **Teorema:** Toda matriz A = (a<sub>ij</sub>)<sub>m x n</sub> é equivalente por linhas a uma única matriz escalonada reduzida
> $$R = (r_{ij})_{m \times n}$$

> **TO-DO** **Proposição:** Sera R uma matriz n x n, na forma escalonada reduzida. Se R $\neq$ I<sub>n</sub>, então R tem uma linha nula.

> **TO-DO** **Definição de matriz elementar:** Uma matriz elementar n x n é uma matriz obtida da matriz identidade I<sub>n</sub> aplicando-se uma, e somente uma, operação elementar.

> **TO-DO** **Teorema:** Sejam E uma matriz elementar m x m e A uma matriz qualquer m x n. Então EA é igual à matriz obtida aplicando-se na matriz A a mesma operação elementar que originou E.

### Propriedades da Álgebra Matricial

> **Teorema 1.1:** Sejam A, B e C matrizes com tamanhos apropriados,  $\alpha$ e $\beta$ escalares. São válidas as seguintes propriedades para as operações matriciais:
>
> - **(a) (comutatividade)**  A + B = B + A
>
> - **(b) (associatividade)**  A + (B + C) = (A + B) + C
>
> - **(c) (elemento neutro)**  A matriz $\overline{0}$ m x n, definida por $\mathbf{[\overline{0}]}_{ij} = 0$, para i = 1, ..., m, j = 1, ..., n, é tal que
>
> $$A + \overline{0} = A$$
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

### Determinantes

### Checklist

- [  ] Capítulo 2.1 do GAAL

> **Definição de determinante:** Seja A = (a<sub>ij</sub>)<sub>n x n</sub>. O determinante de A, denotado por det(A), é definido por
> $$ det(A) = a_{11}\tilde{a}_{11} + a_{12}\tilde{a}_{12} + ... + a_{1n}\tilde{a}_{1n} = \sum_{j=1}^{n} a_{1j}\tilde{a}_{1j} ,$$
> em que $\tilde{a}_{1j} = (-1)^{1+j}det(\tilde{A}_{1j})$ é o cofator do elemento a<sub>1j</sub>. 
>  
> **Saiba que:** O determinante de uma matriz triangular inferior é o produto dos elementos da diagonal principal.

> **Teorema:** Seja A = $(a_{ij})_{n \space x \space n}$ escrita em termos das suas linhas, denotadas por A<sub>i</sub>, ou seja, A<sub>i</sub> = [ a<sub>i1</sub>, a<sub>i2</sub>, ..., a<sub>in</sub> ]. Se para algum k, a linha A<sub>k</sub> = $\alpha$ X + $\beta$ Y, em que X = [ x<sub>1</sub>, x<sub>2</sub>, ..., x<sub>n</sub> ], Y = [ y<sub>1</sub>, y<sub>2</sub>, ..., y<sub>n</sub> ] e $\alpha$ e $\beta$ são escalares, então:
> $$ det\begin{bmatrix}
  A_1 \\
  \vdots \\
  A_{k-1} \\
  \alpha X + \beta Y \\
  A_{k+1} \\
  \vdots \\
  A_{n}
  \end{bmatrix} = \alpha \space det\begin{bmatrix}
  A_{1} \\
  \vdots \\
  A_{k-1} \\
  X \\
  A_{k+1} \\
  \vdots \\
  A_n
  \end{bmatrix} + \beta \space det\begin{bmatrix} 
  A_1 \\
  \vdots \\
  A_{k-1} \\
  Y \\
  A_{k+1} \\
  \vdots \\
  A_n
  \end{bmatrix}$$
> Aqui, A<sub>k</sub> = $\alpha X + \beta Y$ = [ $\alpha x_1 + \beta y_1 \space ... \space \alpha x_n + \beta y_n $ ]

> **Teorema:** Seja A uma matriz n x n. O determinante de A pode ser calculado fazendo-se o desenvolvimento em cofatores segundo qualquer linha ou qualquer coluna.
> $$ det(A) = a_{i1}\tilde{a}_{i1} + a_{i2}\tilde{a}_{i2} + \dots + a_{in}\tilde{a}_{in} = \sum_{j=1}^n a_{ij} \tilde{a}_{ij} , \space\space para \space i = 1, \dots, n,$$
> $$ det(A) = a_{1j}\tilde{a}_{1j} + a_{i2}\tilde{a}_{2j} + \dots + a_{nj}\tilde{a}_{nj} = \sum_{i=1}^n a_{ij} \tilde{a}_{ij} , \space\space para \space j = 1, \dots, n,$$
> em que $\tilde{a} = (-1)^{i+j} det(\tilde{A}_{ij})$ é cofator do elemento a<sub>ij</sub>. A primeira expressão é chamada **desenvolvimento em cofatores do determinante de A em termos da i-ésima linha** e a segunda é chamada de **desenvolvimento em cofatores do determinante de A em termos da j-ésima coluna**.

> **Corolário:** Seja A uma matriz n x n. Se A possui duas linhas iguais, então det(A) = 0.

> **Teorema:** Sejam A e B matrizes n x n.
> - (a) Se B é obtida de A multiplicando-se uma linha por um escalar $\alpha$, então det(B) = $\alpha$ det(A)
> - (b) Se B resulta de A pela troca da posição de duas linhas k $\neq$ l, então det(B) = -det(A)
> - (c) Se B é obtida de A substituindo-se a linha l por ela somada a um múltiplo escalar de uma linha k, k $\neq$ l, então det(B) = det(A).

> **Teorema:** Sejam A e B matrizes n x n.
> - (a) O determinante do produto A por B é igual ao produto dos seus determinantes,
> $$ det(AB) = det(A)det(B). $$
> - (b) Os determinantes de A e de sua transposta A<sup>t</sup> são iguais,
> $$ det(A) = det(A^t) $$

> **TO-DO: Revisar**  
> **Teorema:** Seja A uma matriz n x n.
> - (a) A matriz A é invertível se, e somente se, det(A) $\neq$ 0.
> - (b) O sistema homogêneo AX = $\overline{0}$ tem solução não trivial se, e somente se, det(A) = 0.
>  
> **Proposição:**
> - (a) Se E<sub>i,j</sub> é a matriz elementar obtida trocando-se as linhas i e j da matriz identidade, então det(E<sub>i,j</sub>) = -1.
> - (b) Se E<sub>i</sub>($\alpha$) é a matriz elementar obtida da matriz identidade, multiplicando-se a linha i por $\alpha$, então det(E<sub>i</sub>($\alpha$)) = $\alpha$.
> - (c) Se E<sub>i,j</sub> é a matriz elementar obtida da matriz identidade, somando-se à linha j, $\alpha$ vezes a linha i, então det(E<sub>i,j</sub>($\alpha$)) = 1.
>   
> **Lema:** Sejam E<sub>1</sub> = [1 0 ... 0], E<sub>2</sub> = [0 1 0 ... 0], ..., E<sub>n</sub> = [0 ... 0 1]. Se A é uma matriz n x n, cuja i-ésima linha é igual a E<sub>k</sub>, para algum k (1 $\leq$ k $\leq$ n), então det(A) = (-1)<sup>i+k</sup>det($\tilde{A}_{ik}$).

## Sistemas Lineares

### Checklist

- [  ] Capítulo 1.2 do GAAL

> **Teorema** Se a matriz A = (a<sub>ij</sub>)<sub>m x n</sub>, é tal que m < n, então o sistema homogêneo AX = $\overline{0}$ tem soluções diferentes da solução trivial, ou seja, todo sistema homogêneo com menos equações do que incógnitas tem infinitas soluções.

> **Proposição:** Seja A uma matriz n x n. O sistema linear homogêneo AX = $\overline{0}$ satisfaz as seguintes propriedades:
> - (a) Se X e Y são soluções do sistema homogêneo, AX = $\overline{0}$, então X + Y também o é.
> - (b) Se X é solução do sistema homogêneo, AX = $\overline{0}$, então $\alpha$ X também o é.

> **Teorema:** Se dois sistemas AX = B e CX = D, sãp tais que a matriz aumentada [C | D] é obtida de [A | B] aplicando-se uma operaçãp elementar, então os dois sistemas possuem as esmas soluções.

### Método de Gauss-Jordan

O objetivo do método de Gauss-Jordan é transformar o sistema de equações lineares (ou a matriz aumentada) em uma forma reduzida por linhas (forma de identidade), para encontrar as soluções diretamente.

**Passos principais:**

Escolher um pivô (um número diferente de zero em alguma coluna) e torná-lo igual a 1, dividindo a linha toda por ele.

Zerar os outros elementos da coluna do pivô usando operações elementares nas linhas (somar ou subtrair múltiplos da linha do pivô).

Repetir o processo para as próximas colunas e linhas, até transformar a matriz dos coeficientes em uma matriz identidade.

Ler diretamente a solução da matriz resultante.

## Vetores

### Checklist

- [  ] Capítulo 3.1, 3.2 e 3.3 do GAAL

Vetores são objetos matemáticos que possuem magnitude (tamanho) e direção, usados para representar deslocamentos, forças ou posições no espaço.

Vetores não tem posição fixa, segmento de reta sim.

> **Definição de soma:** A soma, v + w, de dois vetores v e w, é definida pelo vetor obtido da seguinte forma:
> - (a) tome um segmento orientado que representa v;
> - (b) tome um segmento orientado que representa w, com origem na extremidade de v;
> - (c) o vetor v + w é representado pelo segmento orientado que vai da origem de v até a extremidade de w.

> **Definição de multiplo por escalar:** A multiplicação de um vetor v por um escalar $\alpha$, $\alpha$ v, se $\alpha \neq 0$ e $v \neq \overline{0},$ é definida pelo vetor caracterizado por:
> - (a) tem comprimento |$\alpha$| vezes o comprimento de v,
> - (b) a direção é a mesma de v (neste caso, dizemos que eles são paralelos),
> - (c) tem o mesmo sentido de v, se $\alpha$ > 0 e tem o sentido contrário ao de v, se $\alpha$ < 0.
> Se $\alpha$ = 0 ou v = $\overline{0}$, definimos a multiplicação do vetor v pelo escalar $\alpha$ como sendo o vetor nulo, $\alpha$ v = $\overline{0}$.
> Se w = $\alpha$ v, dizemos que w é um múltiplo escalar de V.
> Veja que, dois vetores não nulos são **paralelos** (ou **colineares**) se, e somente se, um é múltiplo escalar do outro.

> **Teorema:** Sejam u, v e e vetores e $\alpha$ e $\beta$ escalares. São válidas as seguintes propriedades:
> - (a) u + v = v + u;
> - (B) (u + v) + w = u + (v + w);
> - (c) u + $\overline{0}$ = u;
> - (d) u + (-u) = $\overline{0}$;
> - (e) $\alpha$($\beta$ u) = ($\alpha\beta$)u;
> - (f) $\alpha$ (u + v) = $\alpha$ u + $\alpha$ v;
> - (g) ($\alpha$ + $\beta$) u = $\alpha$ u + $\beta$ u;
> - (h) 1u = u.
>  
> O vetor nulo ($\overline{0}$): vetor representado por $\overrightarrow{AA}$
>  
> vetor oposto (simétrico) ao u = $\overrightarrow{AB}$ é o vetor -u = $\overrightarrow{BA}$
>  
> Diferenças entre vetores: u - v = u + (-v)

> **Definição de norma:** O comprimento do vetor v também é chamado de norma de v e é denotado por ||v||.

> Segue do Teorema de Pitágoras que a norma de um vetor pode ser calculada usando as suas componentes, por
> $$ ||v|| = \sqrt{v_1^2 + v_2^2}, $$
> no caso em que v = ($v_1$, $v_2$) é um vetor no plano, e por
> $$ ||v|| = \sqrt{v_1^2 + v_2^2 + v_3^2}, $$
> no caso em que v = ($v_1$, $v_2$, $v_3$) é um vetor no espaço.

> **Definição de vetor unitário:** Um vetor de norma igual a 1 é chamado vetor unitário.

> **Definição de distância entre dois pontos:** A distância entre dois pontos P = ($x_1$, $y_1$, $z_1$) e Q = ($x_2$, $y_2$, $z_2$) é igual à norma do vetor $\overrightarrow{PQ}$. Como:
> $$ \overrightarrow{PQ} = \overrightarrow{OQ} - \overrightarrow{OP} = (x_2 - x_1, y_2 - y_1, z_2 - z_1), $$
> então a distância de P e Q é dada por
> $$ dist(P, Q) = ||\overrightarrow{PQ}|| = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}. $$

