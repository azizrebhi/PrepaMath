# Chapitre 14 : Espaces préhilbertiens et euclidiens

<table>
    <tr>
      <td><b>I</b></td>
      <td><b>Rappels et compléments . . . . . . . . . . . . . . .</b></td>
      <td><b>796</b></td>
    </tr>
    <tr>
      <td><b>II</b></td>
      <td><b>Projection orthogonale . . . . . . . . . . . . . . . .</b></td>
      <td><b>799</b></td>
    </tr>
    <tr>
      <td></td>
      <td>1     Projection orthogonale sur un sous-espace vectoriel<br />de dimension finie . . . . . . . . . . . . . . . . . .</td>
      <td>799</td>
    </tr>
    <tr>
      <td></td>
      <td>2     Distance à un sous-espace vectoriel de dimension finie</td>
      <td>801</td>
    </tr>
    <tr>
      <td><b>III</b></td>
      <td><b>Suites orthonormales . . . . . . . . . . . . . . . . .</b></td>
      <td><b>802</b></td>
    </tr>
    <tr>
      <td></td>
      <td>1     Suites totales . . . . . . . . . . . . . . . . . . . . .</td>
      <td>802</td>
    </tr>
    <tr>
      <td></td>
      <td>2     Polynômes orthogonaux . . . . . . . . . . . . . . .</td>
      <td>803</td>
    </tr>
    <tr>
      <td><b>IV</b></td>
      <td><b>Endomorphismes d’un espace euclidien . . . . . .</b></td>
      <td><b>806</b></td>
    </tr>
    <tr>
      <td></td>
      <td>1     Endomorphismes symétriques . . . . . . . . . . . .</td>
      <td>806</td>
    </tr>
    <tr>
      <td></td>
      <td>2     Réduction des endomorphismes symétriques . . . .</td>
      <td>809</td>
    </tr>
    <tr>
      <td></td>
      <td>3     Isométries vectorielles d’un espace euclidien . . . .</td>
      <td>811</td>
    </tr>
    <tr>
      <td colspan="2"><b>Démonstrations et solutions des exercices du cours . .</b></td>
      <td><b>814</b></td>
    </tr>
    <tr>
      <td colspan="2"><b>Exercices . . . . . . . . . . . . . . . . . . . . . . . . . . . .</b></td>
      <td><b>827</b></td>
    </tr>
</table>

# Espaces préhilbertiens et euclidiens
![icon: 14](page_2_image_1_v2.jpg)

En première année, on a introduit la notion d’espace préhilbertien ($\mathbb{R}$-espace vectoriel muni d’un produit scalaire) et d’espace euclidien (espace préhilbertien de dimension finie). La relecture de ce cours est fortement conseillée.

Dans ce chapitre, on considère un espace préhilbertien réel $E$ dont le produit scalaire sera noté $(\ |\ )$. La norme et la distance euclidiennes associées seront respectivement notées $\|\ \|$ et $d$.

## I Rappels et compléments

**Définition 1**
On dit que deux vecteurs $x$ et $y$ de $E$ sont **orthogonaux** si $(x \mid y) = 0$.
On note alors $x \perp y$.

**Définition 2**
On appelle **orthogonal** d’une partie $A$ de $E$, l’ensemble noté $A^\perp$ défini par :
$$A^\perp = \{x \in E \mid \forall a \in A \quad (a \mid x) = 0\}.$$

**Proposition 1**
L’orthogonal d’une partie de $E$ est un sous-espace vectoriel de $E$.

**Démonstration.**
L’orthogonal de $A$ est $A^\perp = \bigcap_{a \in A} \text{Ker } \varphi_a$, où $\varphi_a$ est la forme linéaire $x \mapsto (a \mid x)$. $\square$

**Définition 3**
On dit que deux sous-espaces vectoriels de $E$, $F$ et $G$ sont orthogonaux si :
$$\forall(*x, y*) \in F \times G \quad (x \mid y) = 0,$$
autrement dit si $G \subset F^\perp$ ou, de façon équivalente, si $F \subset G^\perp$.
On note alors $F \perp G$.

*I Rappels et compléments*

## **Proposition 2**
Si $F$ et $G$ sont deux sous-espaces vectoriels de $E$ orthogonaux, alors ils sont en somme directe. On dit alors que la somme $F + G$ est directe et orthogonale et on la note $F \overset{\perp}{\oplus} G$.

**Démonstration.** Si $F$ et $G$ sont deux sous-espaces vectoriels de $E$ orthogonaux, alors tout vecteur $x \in F \cap G$ vérifie $(x \mid x) = 0$ donc $\|x\| = 0$ puis $x = 0$. $\square$

**Remarque** En particulier, Si $F$ est un sous-espace vectoriel de $E$ alors $F$ et $F^\perp$ sont en somme directe. On pourrait se demander si leur somme est égale à $E$. La réponse est négative en général (voir l'exercice 1) mais elle est vraie si $F$ est de dimension finie.

## **Proposition 3**
Si $F$ est un sous-espace vectoriel de $E$ et si $F$ est de dimension finie, alors :
$$E = F \overset{\perp}{\oplus} F^\perp \quad \text{et} \quad (F^\perp)^\perp = F.$$

**Démonstration.**
Comme $F$ et $F^\perp$ sont en somme directe, il suffit de montrer que $F + F^\perp = E$.

Soit $x \in E$. Montrons qu'il existe un couple $(y, z) \in F \times F^\perp$ tel que $x = y + z$. Pour cela, raisonnons par analyse-synthèse.

Comme $F$ est de dimension finie, il possède une base orthonormale $\mathcal{B} = (e_1, e_2, \dots, e_p)$ que l'on fixe.

* Analyse : supposons qu'il existe $(y, z) \in F \times F^\perp$ tel que $x = y + z$. Comme $z \in F^\perp$, on a :
$$\forall i \in \llbracket 1, p \rrbracket \quad (e_i \mid z) = 0 = (e_i \mid x - y) = (e_i \mid x) - (e_i \mid y).$$
Comme la base $\mathcal{B}$ est orthonormale, on a nécessairement :
$$y = \sum_{i=1}^p (e_i \mid y) e_i = \sum_{i=1}^p (e_i \mid x) e_i \quad \text{et} \quad z = x - y = x - \sum_{i=1}^p (e_i \mid x) e_i.$$
Ainsi, si un tel couple $(y, z)$ existe, il est unique.

* Synthèse : si l'on pose $y = \sum_{i=1}^p (e_i \mid x) e_i$ et $z = x - y$, alors $x = y + z$, $y \in F$ et
$$\forall i \in \llbracket 1, p \rrbracket \quad (e_i \mid z) = (e_i \mid x - y) = (e_i \mid x) - (e_i \mid y) = 0$$
donc $z \in F^\perp$.

Par suite, les sous-espaces vectoriels $F$ et $F^\perp$ sont supplémentaires. On a même trouvé une expression de la projection du vecteur $x$ sur $F$ parallèlement à $F^\perp$ lorsque l'on dispose d'une base orthonormale de $F$. $\square$

## **Corollaire 4**
Si $E$ est euclidien, alors pour tout sous-espace vectoriel $F$ de $E$, on a :
$$\dim F^\perp + \dim F = \dim E.$$

797

Chapitre 14. *Espaces préhilbertiens et euclidiens*

**Exemple** On a vu en première année que, dans $\mathcal{M}_n(\mathbb{R})$ muni du produit scalaire canonique $(*A, B*) \mapsto \text{Tr}(^*tAB*)$, on a :

$$\mathcal{M}_n(\mathbb{R}) = \mathcal{S}_n(\mathbb{R}) \overset{\perp}{\oplus} \mathcal{A}_n(\mathbb{R}).$$

Le résultat de la proposition 3 de la page précédente ne subsiste pas sans l'hypothèse de dimension finie, comme le montre l'exercice suivant.

<mark>p.814</mark> **Exercice 1** Soit $E = \mathcal{C}^0([0, 1], \mathbb{R})$ muni du produit scalaire :

$$\varphi : (f, g) \mapsto \int_0^1 f(x)g(x)dx.$$

On considère le sous-espace vectoriel $F = \{f \in E \mid f(0) = 0\}$.

1. Déterminer $F^\perp$.
2. En déduire que $E \neq F \overset{\perp}{\oplus} F^\perp$ et que $(F^\perp)^\perp \neq F$.

## **Théorème 5 (Théorème de représentation de Riesz)**

Soit $\varphi$ une forme linéaire sur $E$ un espace euclidien.
Il existe un unique vecteur $a \in E$ tel que : $\forall x \in E \quad \varphi(x) = (a \mid x)$.

**Démonstration.**
Comme $E$ est un espace euclidien, il possède une base orthonormale $(e_1, \dots, e_n)$.
Soit $a \in E$. La forme linéaire $x \mapsto (a \mid x)$ est égale à $\varphi$ si, et seulement si, elle coïncide avec $\varphi$ sur une base. Donc le vecteur $a$ est solution si, et seulement si :
$$\forall i \in \llbracket 1, n \rrbracket \quad (a \mid e_i) = \varphi(e_i)$$
c'est-à-dire si, et seulement si, $a = \sum_{i=1}^n \varphi(e_i)e_i$ puisque la base est orthonormale. On en déduit qu'il existe un unique vecteur solution : $a = \sum_{i=1}^n \varphi(e_i)e_i$. $\square$

**Remarque** Pour tout vecteur $a$, l'application $x \mapsto (a \mid x)$ est clairement une forme linéaire sur $E$. Le théorème de Riesz permet donc de caractériser les formes linéaires sur un espace euclidien : il s'agit des applications de la forme $x \mapsto (a \mid x)$ avec $a \in E$.

<mark>p.814</mark> **Exercice 2** Soit $\varphi$ une forme linéaire sur $\mathcal{M}_n(\mathbb{R})$.
Montrer qu'il existe une unique matrice $A \in \mathcal{M}_n(\mathbb{R})$ telle que :
$$\forall M \in \mathcal{M}_n(\mathbb{R}) \quad \varphi(M) = \text{Tr}(AM).$$

798

II Projection orthogonale

**p.814** ### **Exercice 3 Produit vectoriel**

On se place dans un espace vectoriel euclidien de dimension 3.

Étant donné deux vecteurs $a$ et $b$, on note $a \wedge b$ et on appelle **produit vectoriel** des vecteurs $a$ et $b$, l'unique vecteur tel que :

$$\forall x \in E \quad [*a, b, x*] = (a \wedge b \mid x)$$

1. Justifier la définition du produit vectoriel.
2. Déterminer les coordonnées dans une base orthonormale du produit vectoriel $a \wedge b$ en fonction de celles des vecteurs $a$ et $b$.
3. Montrer la formule du double produit vectoriel :

$$a \wedge (b \wedge c) = (a \mid c)b - (a \mid b)c.$$

# II Projection orthogonale

## 1 Projection orthogonale sur un sous-espace vectoriel de dimension finie

### **Définition 4**
Soit $F$ est un sous-espace vectoriel de $E$ de dimension finie.

On appelle **projection orthogonale** sur $F$, la projection sur $F$ parallèlement à son supplémentaire orthogonal $F^\perp$.

L'image d'un vecteur $x$ par cette projection est appelée le **projeté orthogonal** de $x$ sur $F$.

Sous ces hypothèses, on a établi dans la démonstration de la proposition 3 de la page 797 l'expression de la projection orthogonale sur $F$ :

### **Proposition 6**
Soit $F$ est un sous-espace vectoriel de dimension finie de $E$.

Si $\mathcal{B} = (e_1, e_2, \dots, e_p)$ est une base orthonormale de $F$, alors le projeté orthogonal sur $F$ d'un vecteur $x$ de $E$ est :

$$\pi(x) = \sum_{<sub>i=1</sub>}^p (e_i \mid x) e_i.$$

### **Exemples**
1. Si $a$ est un vecteur **normé**, alors la projection orthogonale d'un vecteur $x$ sur la droite vectorielle engendrée par $a$ est
$$\begin{aligned} \pi : E &\longrightarrow E \\ x &\longmapsto (a \mid x)a. \end{aligned}$$

Si le vecteur $a$ n'est pas normé (mais non nul), on le norme pour obtenir :
$$\forall x \in E \quad \pi(x) = \frac{(a \mid x)}{(a \mid a)} a.$$

799

# Chapitre 14. *Espaces préhilbertiens et euclidiens*

2. Si $E$ est euclidien et si $(x_1, x_2, \dots, x_n)$ (respectivement $(a_1, a_2, \dots, a_n)$) sont les composantes de $x$ (respectivement de $a$) dans une base orthonormale $\mathcal{B}$, on a :
$$\pi(x) = \frac{\sum_{i=1}^n a_i x_i}{\sum_{i=1}^n a_i^2} a.$$

3. Si $H$ est un hyperplan d'un espace vectoriel $E$ de dimension finie, alors il existe un vecteur non nul $a$ tel que $H = (\mathbb{R}a)^\perp$. Si l'on note $p_H$ et $p_{\mathbb{R}a}$ les projections orthogonales sur $H$ et $\mathbb{R}a$, alors on a $Id_E = p_H + p_{\mathbb{R}a}$. Pour obtenir la projection orthogonale sur $H$ d'un vecteur, il suffit donc de lui retirer sa projection orthogonale sur $H^\perp$, c'est-à-dire :
$$\forall x \in E \quad p_H(x) = x - \frac{(a \mid x)}{(a \mid a)} a.$$

4. De façon général, si $F$ et $F^\perp$ sont supplémentaires alors $Id_E = p_F + p_{F^\perp}$. Ainsi, si on connaît $p_F$, alors on connaît $p_{F^\perp}$.

**Remarque** Soit $(e_1, e_2, \dots, e_n)$ une famille libre de $E$. Le procédé d'orthonormalisation de Schmidt vu en première année permet de construire une famille orthonormale $(f_1, f_2, \dots, f_n)$ de $E$ telle que :
$$\forall p \in \llbracket 1, n \rrbracket \quad \text{Vect} \{e_1, e_2, \dots, e_p\} = \text{Vect} \{f_1, f_2, \dots, f_p\}$$
de la façon suivante. Pour tout $p \in \llbracket 0, n - 1 \rrbracket$, on pose :
$$g_{p+1} = e_{p+1} - \sum_{i=1}^p (e_{p+1} \mid f_i) f_i \quad \text{et} \quad f_{p+1} = \frac{g_{p+1}}{\|g_{p+1}\|}.$$

Le vecteur $g_{p+1}$ est obtenu en retranchant à $e_{p+1}$ son projeté orthogonal sur :
$$F_p = \text{Vect} \{e_1, e_2, \dots, e_p\}.$$

Pour normer le vecteur $g_{p+1}$, il suffit alors d'appliquer le théorème de Pythagore aux vecteurs orthogonaux $\pi(e_{p+1}) = \sum_{i=1}^p (f_i \mid e_{p+1}) f_i$ et $g_{p+1}$. On obtient ainsi :

![drawing: geometric representation of the Gram-Schmidt process showing vectors e_{p+1}, g_{p+1}, and the projection onto plane F_p](page_6_image_1_v2.jpg)

$$\|g_{p+1}\|^2 = \|e_{p+1}\|^2 - \|\pi(e_{p+1})\|^2 = \|e_{p+1}\|^2 - \sum_{i=1}^p (f_i \mid e_{p+1})^2.$$

800

II Projection orthogonale

### **Proposition 7**
Soit $F$ un sous espace vectoriel de dimension finie engendrée par une famille $(e_1, e_2, \dots, e_p)$. Étant donnés deux vecteurs $x$ et $y$ de $E$, on a :
$$y = p_F(x) \iff \begin{cases} y \in F \\ \forall i \in \llbracket 1, p \rrbracket & (x - y \mid e_i) = 0. \end{cases}$$

### **Point méthode**
La proposition précédente permet de trouver le projeté orthogonal d’un vecteur $x$ sur un sous-espace vectoriel $F$ de dimension finie sans avoir à déterminer une base orthonormale de $F$. Il suffit de connaître une famille génératrice de $F$ et de résoudre le système obtenu en traduisant les égalités $(x - y \mid e_i) = 0$ sur les coordonnées de $y$.

Lorsque l’on dispose d’une base orthonormale (ou plus simplement orthogonale) ce système est plus simple puisque diagonal et sa résolution revient à utiliser la formule de la proposition 6 de la page 799 mais il ne faut pas oublier que l’obtention d’une base orthogonale peut être longue.

p.815 **Exercice 4** Pour tout entier $n$, déterminer la projection orthogonale du polynôme $X^n$ sur $\mathbb{R}_1[X]$ pour le produit scalaire de $\mathbb{R}[X]$ :
$$\varphi : (*P, Q*) \mapsto \int_0^1 P(x) Q(x) dx.$$

## 2 Distance à un sous-espace vectoriel de dimension finie
On rappelle que si $\mathcal{X}$ est une partie non vide de $E$ et $A$ un point de $E$. On appelle **distance** de $A$ à $\mathcal{X}$ la quantité :
$$d(A, \mathcal{X}) = \inf_{M \in \mathcal{X}} d(*A, M*).$$

L’existence de cette quantité $d(A, \mathcal{X})$ vient du fait que $\{d(*A, M*); M \in \mathcal{X}\}$ est une partie non vide de $\mathbb{R}$ minorée par 0.

### **Proposition 8**
Soit $F$ un sous-espace vectoriel de $E$ de dimension finie, $p_F$ la projection orthogonale sur $F$ et $x$ un vecteur de $E$. La distance du vecteur $x$ à $F$ est atteinte en un unique point de $F$, à savoir $p_F(x)$. Autrement dit :
1. $d(*x, F*) = \|x - p_F(x)\|$;
2. $\forall y \in F \quad d(*x, F*) = \|x - y\| \iff y = p_F(x)$.

Démonstration page 815

801

Chapitre 14. Espaces préhilbertiens et euclidiens
p.816

p.815 **Exercice 5** Calculer $\inf_{(*a,b*) \in \mathbb{R}^2} \int_0^1 (x^2 - ax - b)^2 \, \mathrm{d}x$.

### **Corollaire 9**
## **Corollaire 9**

Soit $\mathcal{B} = (e_1, e_2, \dots, e_p)$ une base orthonormale d'un sous-espace vectoriel $F$ de $E$. On a l'égalité :

$$d^2(*x, F*) = \|x\|^2 - \sum_{<sub>i=1</sub>}^{p} (e_i \mid x)^2.$$


Démonstration page 816


### **Corollaire 10 (Inégalité de Bessel)**
# **Corollaire 10 (Inégalité de Bessel)**

Si $(e_1, \dots, e_p)$ est une famille orthonormée de $E$, on a, pour tout $x \in E$ :

$$\sum_{<sub>i=1</sub>}^{p} (e_i \mid x)^2 \leqslant \|x\|^2.$$

**Remarque** Si $(e_n)_{n \in \mathbb{N}}$ est une famille orthonormée, alors, pour tout $x \in E$, la série $\sum_{k} (e_k | x)^2$ est convergente car elle est à termes positifs et ses sommes partielles sont majorées par $\|x\|^2$. On a alors :
$$\sum_{k=0}^{+\infty} (e_k | x)^2 \le \|x\|^2.$$

## III Suites orthonormales
### 1 Suites totales

On a vu que si $(e_k)_{1 \le k \le n}$ est une base orthonormale de $E$, alors pour tout vecteur $x \in E$, on a $x = \sum_{k=1}^{n} (e_k | x)e_k$ et donc $\|x\|^2 = \sum_{k=1}^{n} (e_k | x)^2$.

On souhaite généraliser ce résultat dans le cas où $E$ n'est pas euclidien et que l'on ne dispose pas d'une base orthonormale mais d'une suite orthonormale. L'exercice suivant donne une condition nécessaire et suffisante pour avoir l'égalité souhaitée. Cette condition explique la définition de suite totale.



## **Exercice 6**

Soit $(e_k)_{k \in \mathbb{N}}$ une suite orthonormée et $x \in E$. L'**égalité de Parseval-Bessel** :

$$\sum_{k=0}^{+\infty} (e_k \mid x)^2 = \|x\|^2$$

est satisfaite si, et seulement si, $x$ est adhérent au sous-espace vectoriel engendré par la suite $(e_k)_{k \in \mathbb{N}}$.

802

*III Suites orthonormales*

### **Définition 5**
On appelle **suite totale** de $E$ toute suite $(e_k)_{k \in \mathbb{N}}$ de $E$ telle que le sous-espace vectoriel engendré soit dense dans $E$, c'est-à-dire $E = \overline{\text{Vect}(e_k)_{k \in \mathbb{N}}}$.

### **Corollaire 11**
Si $(e_n)_{n \in \mathbb{N}}$ est une suite orthonormale totale de $E$, alors, pour tout $x \in E$, on a :

$$\sum_{k=0}^{+\infty} (e_k \mid x)^2 = \|x\|^2.$$

### **Corollaire 12**
Si $(e_n)_{n \in \mathbb{N}}$ est une suite orthonormale totale de $E$, et si, pour tout $n \in \mathbb{N}$, $p_n$ désigne le projecteur orthogonal sur $\text{Vect}(e_0, \dots, e_n)$, alors, pour tout $x \in E$, la suite $(p_n(x))_{n \in \mathbb{N}}$ converge vers $x$.

**Démonstration.** D'après le théorème de Pythagore, on a :

$$\forall n \in \mathbb{N} \quad \|x - p_n(x)\|^2 = \|x\|^2 - \|p_n(x)\|^2 = \|x\|^2 - \sum_{k=0}^{n} (e_k \mid x)^2. \hfill \square$$

## 2 Polynômes orthogonaux

Dans cette section, nous allons voir des exemples de suites totales composées de polynômes.
En pratique, le caractère normé introduit des constantes multiplicatives, ce qui explique que l'on se limite parfois à considérer des suites orthogonales totales.
Considérons l'espace vectoriel $\mathcal{C}([a, b], \mathbb{R})$ muni du produit scalaire :

$$(f, g) \mapsto \int_{[a, b]} *f g.*$$

Pour tout $f \in \mathcal{C}([a, b], \mathbb{R})$, le théorème de densité de Weierstrass nous fournit une suite de polynômes $(p_n)_{n \in \mathbb{N}}$ convergeant uniformément vers $f$ sur le segment $[a, b]$. La majoration :

$$ \| f - p_n \| = \left( \int_{[a,b]} (f - p_n)^2 \right)^{1/2} \leqslant (b - a)^{1/2} \| f - p_n \|_\infty $$

montre que cette suite converge aussi vers $f$ pour la norme euclidienne associée au produit scalaire $(f, g) \mapsto \int_a^b fg$.

Le sous-espace des fonctions polynomiales est donc dense dans l'espace préhilbertien $\mathcal{C}([a, b], \mathbb{R})$ pour cette norme. Ainsi, si $(q_n)_{n \in \mathbb{N}}$ est une base orthonormale de $\mathbb{R}[X]$, alors, $\text{Vect}(q_n)_{n \in \mathbb{N}} = \mathbb{R}[X]$ est dense dans $E$ et donc, pour

803

# Chapitre 14. Espaces préhilbertiens et euclidiens

tout $f \in \mathcal{C}([*a, b*], \mathbb{R})$, l'égalité de Parseval-Bessel donne :

$$ \|f\|^2 = \sum_{n=0}^{+\infty} \left( \int_{[*a,b*]} q_n f \right)^2 . $$

Si $(q_n)_{n \in \mathbb{N}}$ est seulement une base orthogonale de $\mathbb{R}[X]$, cette égalité devient :

$$ \|f\|^2 = \sum_{n=0}^{+\infty} \left( \int_{[*a,b*]} q_n f \right)^2 \frac{1}{\|q_n\|^2} . $$

Les trois exercices suivants proposent la construction et l'étude d'une suite totale de polynômes orthogonaux lorsque $[*a, b*] = [-1, 1]$ (ce qui rajoute des propriétés de symétrie)

p.816
## **Exercice 7** On munit $\mathbb{R}[X]$, du produit scalaire :

$$(f, g) \mapsto (f \mid g) = \int_{-1}^{1} f(t) g(t) \mathrm{d}t.$$

1. Montrer qu'il existe une unique base orthogonale $(Q_n)_{n \in \mathbb{N}}$ de $\mathbb{R}[X]$ telle que, pour tout entier $n$, on ait $\deg(Q_n) = n$ et $Q_n$ de coefficient dominant 1.
2. Déterminer $Q_0$, $Q_1$, $Q_2$ et $Q_3$.
3. Étudier la parité de $Q_n$ en fonction de $n$.
4. Montrer que, pour tout $n \in \mathbb{N}^*$, le polynôme $Q_n$ admet $n$ racines distinctes dans $]-1, 1[$.

*On pourra introduire le polynôme* $\prod_{a \in S} (X - a)$ *où $S$ est l'ensemble des racines de $Q_n$ appartenant à l'intervalle $]-1, 1[$ et d'ordre impair.*

p.818
**Exercice 8** On considère les polynômes $(Q_n)_{n \in \mathbb{N}}$ définis dans l'exercice précédent.

1. Montrer que pour tout entier $n$, $Q_{n+2} \in \text{Vect}(XQ_{n+1}, Q_n)$, c'est-à-dire qu'il existe des réels $\alpha_n$ et $\beta_n$ tels que $Q_{n+2} = \alpha_n XQ_{n+1} + \beta_n Q_n$.
2. Prouver que, pour tout entier $n$, on a $Q_n = \frac{n!}{(2n)!} R_n^{(n)}$ avec $R_n = (X^2 - 1)^n$.
3. En déduire $Q_n(1)$, puis que :
   $$Q_{n+2} = XQ_{n+1} - \frac{(n+1)^2}{(2n+1)(2n+3)} Q_n.$$

p.819
# **Exercice 9** On considère les polynômes $(Q_n)_{n \in \mathbb{N}}$ de l'exercice précédent.

Montrer que pour tout entier $n$, le polynôme $((1 - X^2) Q'_n)'$ est colinéaire à $Q_n$.
En déduire que $Q_n$ est solution de l'équation différentielle :

$$(X^2 - 1)Q''_n + 2XQ'_n - n(n + 1)Q_n = 0.$$

804

III Suites orthonormales

![icon: p.819](page_11_image_1_v2.jpg)

### **Exercice 10 Polynômes de Legendre**

La suite des polynômes de Legendre est définie par $L_0(X) = 1$, $L_1(X) = X$ et pour tout entier $n$ par la formule de Bonnet :
$$(n + 2)L_{n+2}(X) - (2n + 3)XL_{n+1}(X) + (n + 1)L_n(X) = 0.$$

1. Déterminer $L_2$ et $L_3$ puis prouver que pour tout entier $n$, on a $L_n(1) = 1$.
2. Prouver que la suite des polynômes $(Q_n)_{n \in \mathbb{N}}$ étudiée dans les trois exercices précédents est reliée aux polynôme de Legendre par la relation :
$$\forall n \in \mathbb{N} \quad Q_n(X) = \frac{2^n (n!)^2}{(2n)!} L_n(X).$$

**Remarque** Les quatre exercices précédents prouvent que la famille des **polynômes de** Legendre forme une base orthogonale de $\mathbb{R}[X]$ pour le produit scalaire $(f,g) \mapsto ( f | g ) = \int_{-1}^{1} f(t) g(t) dt$ et que pour tout entier $n$, on a :
$$(X^2 - 1)L''_n + 2XL'_n - n(n + 1)L_n = 0.$$

Plus généralement, si $w$ est une fonction continue sur $[*a, b*]$ strictement positive sauf éventuellement en un nombre fini de points, alors le sous-espace des fonctions polynomiales est dense dans l'espace préhilbertien $\mathcal{C}([*a, b*], \mathbb{R})$ pour la norme euclidienne issue du produit scalaire :
$$( f | g ) = \int_{a}^{b} w(t) f(t) g(t) dt$$
car l'on dispose de la majoration :
$$\left( \int_{<sub>[a,b]</sub>} w (f - p_n)^2 \right)^{1/2} \le \|w\|_\infty (b - a)^{1/2} \|f - p_n\|_\infty$$
La fonction $w$ est alors appelée une fonction poids.
**Exemple** Lorsque l'on choisit $[*a, b*] = [-1, 1]$ et $w : x \mapsto \sqrt{1 - x^2}$, on obtient les **polynômes de Tchebychev de seconde espèce**.

On peut généraliser le raisonnement précédent avec des fonctions poids qui ne sont pas nécessairement continues sur un segment $[*a, b*]$. Il suffit que la fonction $w$ soit telle que, pour tout entier $n$, $t \mapsto w(t) t^n$ soit intégrable sur l'intervalle considéré.
**Exemple** On peut ainsi munir $\mathcal{C}([-1, 1], \mathbb{R})$ du produit scalaire :
$$(f, g) \mapsto ( f | g ) = \int_{-1}^{1} \frac{f(t) g(t)}{\sqrt{1 - t^2}} dt.$$
et construire une suite totale de polynômes orthogonaux. C'est l'objet de l'exercice 14.8 de la page 829 qui fait notamment apparaître les **polynômes de Tchebychev**.

805

Chapitre 14. Espaces préhilbertiens et euclidiens

On peut aussi se placer sur un intervalle non borné.

**Exemple** Si l'on munit $E = \left\{ f \in \mathcal{C}(\mathbb{R}, \mathbb{R}) : \int_{-\infty}^{+\infty} f^2(t)e^{-t^2} dt < \infty \right\}$ du produit scalaire :

$$(f, g) \mapsto (f \mid g) = \int_{-\infty}^{+\infty} f(t) g(t) e^{-t^2} dt,$$

on obtient les **polynômes d'Hermite**.

Les suites de polynômes orthogonaux proposées vérifient une relation de récurrence linéaire d'ordre 2, il est donc possible d'écrire un programme informatique permettant le calcul explicite des coefficients de ces polynômes.
Prenons l'exemple des polynômes de Tchebychev qui vérifient :
$$\forall n \in \mathbb{N} \quad T_{n<sub>+2</sub>} = 2XT_{n<sub>+1</sub>} - T_n.$$

Le programme suivant prend en paramètre un entier $n \geqslant 2$ et renvoie une liste $[a_0, \dots, a_n]$ telle que $T_n = \sum_{k=0}^{n} a_k X^k$ :

```python
def Tcheby(n):
    L0=[1]
    if n == 0: return L0
    L1=[0,1]
    if n == 1: return L1
    for k in range(2,n+1) :
        L=[-L0[0]]
        for i in range(1,k-1) :
            L+=[2*L1[i-1]-L0[i]]
        L+=[0,2*L1[k-1]]
        L0=L1
        L1=L
    return(L)
```

# IV Endomorphismes d'un espace euclidien

Dans la suite $E$ est un espace euclidien de dimension $n$.

## 1 Endomorphismes symétriques

### **Définition 6**
On dit qu'un endomorphisme $u \in \mathcal{L}(E)$ est **symétrique**, si :
$$\forall (*x, y*) \in E^2 \quad (x \mid u(y)) = (u(x) \mid y).$$

### Proposition 13
L'ensemble des endomorphismes symétriques de $E$, noté $\mathcal{S}(E)$, est un sous-espace vectoriel de $\mathcal{L}(E)$.

806

IV Endomorphismes d'un espace euclidien

## **Proposition 14**
> Soit $\mathcal{B}$ une base orthonormée de $E$. Un endomorphisme $u$ est symétrique si, et seulement si, sa matrice dans $\mathcal{B}$ est symétrique.


Démonstration page 820


<mark>p.820</mark> **Exercice 11** Soit $u$ et $v$ deux endomorphismes symétriques de $E$.
Déterminer une condition nécessaire et suffisante pour que $u \circ v$ soit symétrique.

## **Corollaire 15**
> L'espace vectoriel $\mathcal{S}(E)$ est de dimension $\frac{n(n+1)}{2}$.

**Démonstration.** Soit $\mathcal{B}$ une base orthonormée de $E$.
L'application $\Phi : \mathcal{L}(E) \longrightarrow \mathcal{M}_n(\mathbb{R})$ induit un isomorphisme de $\mathcal{S}(E)$ sur $\mathcal{S}_n(\mathbb{R})$ donc :
$$u \longmapsto \text{Mat}_{\mathcal{B}}(u)$$
$$\dim \mathcal{S}(E) = \dim \mathcal{S}_n(\mathbb{R}) = \frac{n(n+1)}{2}. \hfill \square$$

## **Proposition 16**
> L'endomorphisme induit sur un sous-espace vectoriel stable par un endomorphisme symétrique est aussi symétrique.

**Démonstration.** La relation $(x \mid u(y)) = (u(x) \mid y)$ pour tout $(*x, y*) \in E^2$ montre que l'endomorphisme $v$ induit par l'endomorphisme $u$ sur le sous-espace stable $F$ vérifie :
$$\forall (*x, y*) \in F^2 \quad (x \mid v(y)) = (v(x) \mid y). \hfill \square$$

## **Proposition 17**
> Un projecteur $p$ est une projection orthogonale si, et seulement s'il est symétrique


Démonstration page 820


<mark>p.820</mark> **Exercice 12** Déterminer les symétries qui sont des endomorphismes symétriques.

<mark>p.821</mark> **Exercice 13** Soit $p \in \mathcal{L}(E)$ un projecteur. Montrer que $p$ est une projection orthogonale si, et seulement si :
$$\forall x \in E \quad \|p(x)\| \le \|x\|.$$
*On pourra pour tout couple* $(*x, y*) \in \text{Ker } p \times \text{Im } p$, *considérer les vecteurs* $y + \lambda x$.

## **Proposition 18**
> Les sous-espaces vectoriels propres d'un endomorphisme symétrique sont deux à deux orthogonaux.


Démonstration page 821

807

Chapitre 14. Espaces préhilbertiens et euclidiens

p.821

## **Exercice 14**

1. Montrer que l'application $(*P, Q*) \mapsto \int_{-\infty}^{+\infty} P(t) Q(t) e^{-t^2/2} dt$ est un produit scalaire sur $\mathbb{R}[X]$.
2. Soit $\Phi : \mathbb{R}[X] \longrightarrow \mathbb{R}[X]$
   $\quad\quad\quad\quad P \longmapsto XP' - P''$.
   Montrer que $\Phi$ est symétrique pour ce produit scalaire.
3. Soit $n \in \mathbb{N}$.
   (a) Prouver que $\mathbb{R}_n[X]$ est stable par $\Phi$ et que l'endomorphisme induit $\Phi_n$ est diagonalisable.
   (b) Montrer l'existence d'une base orthonormée de $\mathbb{R}_n[X]$ constituée de vecteurs propres de $\Phi_n$.
4. En déduire que, pour tout entier $n$, il existe un unique polynôme $H_n$ de coefficient dominant 1 tel que $\Phi(H_n) = nH_n$ et que ce polynôme est de degré $n$.

L'exercice précédent prouve l'existence d'une base orthonormée de diagonalisation pour l'endomorphisme symétrique $\Phi_n$. Le théorème spectral, que nous énoncerons plus tard, généralise ce résultat à tout endomorphisme symétrique d'un espace euclidien.

Dans le cas de l'endomorphisme $\Phi$, on peut expliciter la base orthogonale de diagonalisation $(H_n)_{n \in \mathbb{N}}$ obtenue dont les éléments sont appelés les polynômes de Hermite. C'est l'objet de l'exercice suivant.

p.822

## **Exercice 15 Polynômes de Hermite**

On considère la base orthogonale constituée de vecteurs propres de $\Phi$, $(H_n)_{n \in \mathbb{N}}$, obtenue à l'exercice précédent.

1. Calculer $H_0, H_1, H_2$ et $H_3$.
2. Soit $g : x \mapsto e^{-x^2/2}$.
   Prouver que, pour tout entier $k$, la fonction $x \mapsto e^{x^2/2}g^{(k)}(x)$ est polynomiale de degré $k$ et de coefficient dominant $(-1)^k$.
3. En déduire que pour tout entier $n$, on a :
   $$\forall x \in \mathbb{R} \quad H_n(x) = (-1)^n e^{x^2/2}g^{(n)}(x)$$
4. Montrer que, pour tout entier $n \in \mathbb{N}^*$, on a $\|H_n\|^2 = n \|H_{n-1}\|^2$.
5. En déduire une base orthonormée de vecteurs propres de $\Phi$ puis que, pour tout polynôme $P$, on a $P = \sum_{n \in \mathbb{N}} (P \mid H_n) \frac{H_n}{n! \sqrt{2\pi}}$.

*On admettra que* $\int_{-\infty}^{+\infty} e^{-t^2/2} dt = \sqrt{2\pi}$.

808

IV Endomorphismes d'un espace euclidien

**Remarque** Comme dans les autres familles de polynômes orthogonaux présentées, on aurait pu prouver que pour tout entier $n$, $H_n$ est de même parité que $n$, à racines simples et que l’on a les relations :

$$H_{n<sub>+2</sub>} = XH_{n+1} - (n + 1)H_n,$$

$$H'_{n+1} = (n + 1)H_n$$

$$H''_n - XH'_n + nH_n = 0.$$

## 2 Réduction des endomorphismes symétriques

Pour démontrer le théorème spectral, on va utiliser deux propositions. La première assure qu’un endomorphisme symétrique possède une valeur propre réelle ; la seconde concerne la stabilité de l’orthogonal d’un sous-espace stable par un endomorphisme symétrique. Le théorème spectral en découlera par récurrence.

## **Proposition 19**
---
> Soit $A \in \mathcal{S}_n(\mathbb{R})$, alors $\text{sp}(A) \subset \mathbb{R}$.

**Principe de démonstration.** Considérer une valeur propre complexe $\lambda$ ainsi qu'un vecteur propre complexe associé $X$ et calculer $^tX A \overline{X}$.
Démonstration page 823

## **Corollaire 20**
---
> Un endomorphisme symétrique d'un espace euclidien de dimension non nulle, possède une valeur propre réelle.

**Démonstration.** Soit $u$ un endomorphisme symétrique. Alors $\chi_u$ possède une racine complexe qui est réelle comme valeur propre de la matrice symétrique réelle $\text{Mat}_{\mathcal{B}}(u)$ où $\mathcal{B}$ est une base orthonormée. $\square$

## **Proposition 21**
---
> Soit $u$ un endomorphisme symétrique et $F$ un sous-espace vectoriel de $E$.
>
> Si $F$ est stable par $u$, alors $F^\perp$ est aussi stable par $u$.

Démonstration page 824

## **Théorème 22 (Théorème spectral)**
---
> Soit $u$ un endomorphisme symétrique d'un espace euclidien $E$. Alors :
>
> * $E$ possède une base orthonormée formée de vecteurs propres de $u$.
> * $E$ est la somme directe orthogonale des sous-espaces propres de $u$ ;
>
> On dit que $u$ est diagonalisable en base orthonormée.

Démonstration page 824

809

Chapitre 14. Espaces préhilbertiens et euclidiens

**Exemple** Les polynômes de Legendre forment une base orthogonale de vecteurs propres de l’endomorphisme symétrique $P \mapsto ((X^2 - 1)P')'$.

## **Corollaire 23**

> Un endomorphisme $u \in \mathcal{L}(E)$ est symétrique si, et seulement s’il existe une base orthonormée de $E$ dans laquelle sa matrice est diagonale.
>
> Une matrice $A \in \mathcal{M}_n(\mathbb{R})$ est symétrique si, et seulement s’il existe une matrice orthogonale $P$ telle que $P^{-1}AP$ soit diagonale.


Démonstration page 824


Dans ces conditions, on dira que $u$ est **orthogonalement diagonalisable** et que $A$ est **orthogonalement semblables** à une matrice diagonale.

### Remarques

*   Le corollaire précédent fournit une condition suffisante extrêmement simple de diagonalisabilité d’une matrice réelle : il suffit qu’elle soit symétrique. On aura garde de croire que ce résultat reste vrai pour les matrices complexes : 
plexes : la matrice complexe symétrique $\begin{pmatrix} i & 1 \\ 1 & -i \end{pmatrix}$ est nilpotente non nulle. Elle n'est donc pas diagonalisable.

*   On cherchera évidemment à diagonaliser un endomorphisme symétrique $u$ dans une base orthonormée. On procédera de la façon suivante.
    1. On déterminera de façon classique le spectre et les sous-espaces propres de l’endomorphisme $u$.
    2. On déterminera une base orthonormée de chaque sous-espace propre, en utilisant, par exemple, le procédé d’orthonormalisation de Schmidt. La réunion de ces bases sera une base orthonormée $\mathcal{C}$ de diagonalisation de $u$.
    3. Si $A$ est la matrice de $u$ dans une base orthonormée $\mathcal{B}$ de $E$, la matrice $P$ de $\mathcal{B}$ dans $\mathcal{C}$ est une matrice orthogonale telle que $D = P^{-1}AP$ soit diagonale. La matrice $D$ représente, rappelons-le, la matrice de $u$ dans $\mathcal{C}$. Il faut remarquer pour éviter trop de calculs que, $P$ étant orthogonale, $P^{-1}$ est égale à $^tP$.

**Exemple** En sciences industrielles, la matrice d’inertie d’un solide $S$ :

$$
\begin{pmatrix}
\int_S (y^2 + z^2) \mathrm{d}m & -\int_S xy \mathrm{d}m & -\int_S xz \mathrm{d}m \\
-\int_S xy \mathrm{d}m & \int_S (x^2 + z^2) \mathrm{d}m & -\int_S yz \mathrm{d}m \\
-\int_S xz \mathrm{d}m & -\int_S yz \mathrm{d}m & \int_S (x^2 + y^2) \mathrm{d}m
\end{pmatrix}
$$

est une matrice symétrique. Il existe donc une base orthonormée adaptée au solide dans laquelle elle est diagonale.

810

IV Endomorphismes d’un espace euclidien

**Exercice 16** *(Polytechnique 2015)*

Soit $u$ un endomorphisme symétrique d’un endomorphisme euclidien dont le spectre est inclus dans $\mathbb{R}_+$.

1. Montrer qu’il existe un endomorphisme symétrique $v$ tel que $u = v^2$.
2. Montrer que $v$ est unique si l’on impose la condition supplémentaire $\text{sp}(v) \subset \mathbb{R}_+$.

Ce résultat est souvent appelé « lemme de la racine carrée ».

**Exercice 17** *(Polytechnique 2015)*

1. Soit $M \in \mathcal{M}_n(\mathbb{R})$. Montrer que $^*tMM*$ est symétrique et de valeurs propres positives.
2. Soit $M \in \mathcal{GL}_n(\mathbb{R})$. Montrer qu’il existe un unique couple $(*O, S*) \in \mathcal{O}_n(\mathbb{R}) \times \mathcal{S}_n^+(\mathbb{R})$ tel que :
$$M = OS \quad \text{et} \quad \text{sp } S \subset \mathbb{R}_+.$$

On utilisera le lemme de la racine carrée (exercice 16).
Cette écriture est appelée décomposition polaire de la matrice $M$.

## 3 Isométries vectorielles d’un espace euclidien

**Définition 7**
Un endomorphisme $u$ est une **isométrie vectorielle**, si :
$$\forall x \in E \quad \|u(x)\| = \|x\|.$$

**Exercice 18** Quelles sont les valeurs propres possibles d’une isométrie vectorielle ?

Rappelons quelques propriétés des isométries vues en première année.

**Proposition 24**
Une isométrie vectorielle est un automorphisme et vérifie :
$$\forall (*x, y*) \in E^2 \quad (u(x) \mid u(y)) = (x \mid y).$$

**Remarque** Cette propriété explique pourquoi une isométrie vectorielle est aussi appelée un **automorphisme orthogonal**. Il s’agit en effet d’un automorphisme qui conserve l’orthogonalité, au sens où deux vecteurs orthogonaux ont des images orthogonales.

**Proposition 25**
Soit $\mathcal{B}$ une base orthonormée de $E$. Un endomorphisme $u$ est une isométrie vectorielle si, et seulement s’il transforme $\mathcal{B}$ en une base orthonormée.

811

# Chapitre 14. *Espaces préhilbertiens et euclidiens*

## **Corollaire 26**
> Soit $\mathcal{B}$ une base orthonormée de $E$. Un endomorphisme $u$ est une isométrie vectorielle si, et seulement si, sa matrice dans $\mathcal{B}$ est orthogonale.

## **Proposition 27**
> L’endomorphisme induit sur un sous-espace vectoriel stable par une isométrie vectorielle est aussi une isométrie vectorielle.

Pour démontrer le théorème de réduction des isométries vectorielles, on va prouver deux résultats intermédiaires. Le premier est propre aux isométries, le second est plus général et aurait pu être utilisé pour démontrer le théorème spectral.

## **Proposition 28**
> Soit $u$ une isométrie vectorielle et $F$ un sous-espace vectoriel de $E$.
> Si $F$ est stable par $u$, alors $F^\perp$ est aussi stable par $u$.

**Principe de démonstration.** Prouver que $u(F^\perp) \subset u(F)^\perp$ et que $u(F) = F$.


<table style="border: 1px solid black; border-radius: 10px;"><tr><td>Démonstration page 825</td></tr></table>


## **Lemme 29**
> Soit $u$ un endomorphisme d’un $\mathbb{R}$-espace vectoriel $E$ de dimension finie non nulle.
> Alors il existe une droite ou un plan stable par $u$.

**Principe de démonstration.** Utiliser un facteur irréductible d’un polynôme annulateur de $u$.


<table style="border: 1px solid black; border-radius: 10px;"><tr><td>Démonstration page 825</td></tr></table>


## **Théorème 30**
> Soit $u$ un automorphisme orthogonal. Il existe une base orthonormée $\mathcal{B}$ de $E$ dans laquelle la matrice de $u$ est égale à une diagonale par blocs :
> * de taille 1 de la forme $(\gamma)$ avec $\gamma \in \{-1, 1\}$ ;
> * de taille 2 et de la forme :
>
> ```llamaparse
> parse(
>   mode="default",
>   box_2d=[735, 268, 790, 790],
>   prompt="Transcribe the 2x2 matrix and the condition on theta in LaTeX."
> )
> ```


<table style="border: 1px solid black; border-radius: 10px;"><tr><td>Démonstration page 825</td></tr></table>


**Exemple** Si $u$ est une isométrie vectorielle d’un espace euclidien de dimension 3, alors il existe une base orthonormée dans laquelle la matrice de $u$ est :

$$
\begin{pmatrix}
\gamma & 0 & 0 \\
0 & \cos \theta & -\sin \theta \\
0 & \sin \theta & \cos \theta
\end{pmatrix}
\text{ avec } \gamma = \det(u) = \pm 1 \quad \text{ et } \quad \theta \in \mathbb{R}.
$$

812

# IV Endomorphismes d'un espace euclidien

En effet, il ne peut y avoir qu'un seul bloc de la forme $R(\theta) = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix}$ et comme une telle matrice est de déterminant 1, on a $\gamma = \det(u)$.
S'il n'y a pas de bloc de la forme $R(\theta)$, alors il existe une base orthonormale dans laquelle la matrice est diagonale $\text{Diag}(\gamma_1, \gamma_2, \gamma_3)$, avec $(\gamma_1, \gamma_2, \gamma_3) \in \{1, -1\}^3$. Quitte à permuter les vecteurs de la base, on peut supposer $\gamma_2 = \gamma_3$. Alors $\text{Diag}(\gamma_2, \gamma_3) = R(0)$ ou $\text{Diag}(\gamma_2, \gamma_3) = R(\pi)$ suivant le signe de $\gamma_2 = \gamma_3$.

On en déduit le résultat suivant.

## **Proposition 31**
Si $u$ est une isométrie vectorielle directe d'un espace euclidien de dimension 3, alors il existe une base orthonormée dans laquelle la matrice de $u$ est :
$$ \begin{pmatrix} 1 & 0 & 0 \\ 0 & \cos \theta & -\sin \theta \\ 0 & \sin \theta & \cos \theta \end{pmatrix} \quad \text{avec} \quad \theta \in \mathbb{R}. $$

## **Corollaire 32**
Si $u$ est une isométrie vectorielle directe d'un espace euclidien de dimension 3, il existe une droite $D$ telle que $u|_D = \text{Id}_D$ et $u|_P$ soit une rotation, où $P$ est le plan orthogonal à $D$.

On dit que $u$ est une **rotation d'axe $D$**.

<mark>p.826</mark> **Exercice 19** Discuter de l'unicité de l'axe.

## Remarques
* On dit qu'une telle isométrie vectorielle directe d'un espace euclidien de dimension 3 est une **rotation** d'angle $\theta$.
  L'angle $\theta$ de la rotation peut être déterminé, au signe près, en remarquant que :
  $$ \text{Tr}(u) = 1 + 2 \cos \theta. $$
* Si $u$ est une isométrie vectorielle indirecte d'un espace euclidien de dimension 3, alors il existe une base orthonormée dans laquelle la matrice de $u$ est :
  $$ \begin{pmatrix} -1 & 0 & 0 \\ 0 & \cos \theta & -\sin \theta \\ 0 & \sin \theta & \cos \theta \end{pmatrix} \quad \text{avec} \quad \theta \in \mathbb{R}. $$
  Il existe alors une droite $D$ et un plan $P$ orthogonal à $D$ tels que $u|_P$ soit une rotation et $u|_D = -\text{Id}_D$.
  Ainsi, $u$ est la composée d'une rotation autour d'une droite $D$ et d'une symétrie orthogonale par rapport au plan orthogonal à $D$.

813

Chapitre 14. Espaces préhilbertiens et euclidiens

## Démonstrations et solutions des exercices du cours

### **Exercice 1**

1. Soit $f \in F^{\perp}$. Pour tout $g \in F$, on a $\int_{0}^{1} f(x) g(x) dx = 0$. En particulier, si l'on considère $g : x \mapsto xf(x)$, alors $\int_{0}^{1} xf(x)^2 dx = 0$. Comme la fonction $x \mapsto xf(x)^2$ est continue et positive sur $[0, 1]$, on en déduit que :
   $$\forall x \in [0, 1] \quad xf(x)^2 = 0 \quad \text{puis que} \quad \forall x \in ]0, 1] \quad f(x) = 0.$$
   La fonction $f$ étant continue, cela implique qu'elle est nulle.
   Réciproquement la fonction nulle appartient à $F^{\perp}$ donc $F^{\perp} = \{0\}$.

2. Comme $F^{\perp} = \{0\}$, on a $F \overset{\perp}{\oplus} F^{\perp} = F \neq E$ et $(F^{\perp})^{\perp} = E \neq F$.

### **Exercice 2**
L'application $(M, N) \mapsto \text{Tr}(^*tMN*)$ étant un produit scalaire sur $\mathcal{M}_n(\mathbb{R})$, le théorème de Riesz prouve l'existence d'une unique matrice $B$ telle que :
$$\forall M \in \mathcal{M}_n(\mathbb{R}) \quad \varphi(M) = \text{Tr}(^*tBM*).$$
Comme $M \mapsto ^tM$ est bijective, on en déduit le résultat.

### **Exercice 3**

1. Étant donné deux vecteurs $a$ et $b$, l'existence et l'unicité d'un vecteur $a \wedge b$ tel que $\forall x \in E \quad [*a, b, x*] = (a \wedge b \mid x)$ découle du théorème de Riesz.

2. Si l'on note $(e_1, e_2, e_3)$ la base canonique de $\mathbb{R}^3$ et $(a_1, a_2, a_3)$ (respectivement $(b_1, b_2, b_3)$ les coordonnées) du vecteur $a$ (respectivement $b$) dans cette base, alors on a :
   $$a \wedge b = \sum_{<sub>k=1</sub>}^{3} (a \wedge b \mid e_k) e_k = \sum_{<sub>k=1</sub>}^{3} [a, b, e_k] e_k.$$
   On retrouve la formule bien connue en physique et en sciences industrielles :
   $$a \wedge b \begin{vmatrix} a_2b_3 - a_3b_2 \\ a_3b_1 - a_1b_3 \\ a_1b_2 - a_2b_1 \end{vmatrix}.$$
   **Attention :** cette formule n'est pas vraie si l'on ne se place pas dans une base orthonormée.

3. On peut trouver une base orthonormale $(e_1, e_2, e_3)$ de $E$ telle que $a \in \text{Vect}(e_1)$ et $b \in \text{Vect}(e_1, e_2)$ : il suffit de prendre un plan $P$ contenant $a$ et $b$ et une base orthonormale $(e_1, e_2)$ de ce plan telle que $e_1 \in \text{Vect}(a)$ si $a \neq 0$. On complète par un vecteur $e_3$ normé orthogonal à $P$. Écrivons donc (en identifiant $E$ et $\mathbb{R}^3$ au moyen de cette base) :
   $$a = \begin{pmatrix} a \\ 0 \\ 0 \end{pmatrix} \quad b = \begin{pmatrix} b_1 \\ b_2 \\ 0 \end{pmatrix} \quad \text{et} \quad c = \begin{pmatrix} c_1 \\ c_2 \\ c_3 \end{pmatrix}.$$

814

***Démonstrations et solutions des exercices du cours***

On obtient alors facilement :

$$b \wedge c = \begin{pmatrix} b_2 c_3 \\ -b_1 c_3 \\ b_1 c_2 - b_2 c_1 \end{pmatrix} \quad \text{et} \quad a \wedge (b \wedge c) = \begin{pmatrix} 0 \\ a b_2 c_1 - a b_1 c_2 \\ -a b_1 c_3 \end{pmatrix}$$

ce qui donne le résultat $a \wedge (b \wedge c) = (a \mid c)b - (a \mid b)c$ puisque $(a \mid b) = ab_1$ et $(a \mid c) = ac_1$.

**Exercice 4** On cherche le projeté orthogonal $P$ du polynôme $X^n$ sur $\mathbb{R}_1[X]$ sous la forme $P = aX + b$. Le polynôme $P$ doit vérifier
$$(X^n - P \mid 1) = (X^n - P \mid X) = 0,$$
ce qui se traduit par le système suivant :
$$
\begin{cases}
a + 2b = \frac{2}{n + 1} \\
2a + 3b = \frac{6}{n + 2}
\end{cases}
$$
ce qui donne $P = \frac{6nX + 2 - 2n}{(n+1)(n+2)}$.

**Proposition 8** Soit $x \in E$ et $y \in F$. On a :
$$y - x = y - p_F(x) + p_F(x) - x \quad \text{avec} \quad (x - p_F(x) \mid y - p_F(x)) = 0,$$
et donc, d'après le théorème de Pythagore :
$$\|x - y\|^2 = \|x - p_F(x)\|^2 + \|y - p_F(x)\|^2 \geqslant \|x - p_F(x)\|^2.$$
Par conséquent, $d(*x, F*) \geqslant \|x - p_F(x)\|$ et, comme $p_F(x) \in F$, on a aussi $d(*x, F*) \leqslant \|x - p_F(x)\|$. D'où l'égalité. De plus :
$$d(*x, F*) = \|x - y\| \iff \|x - y\|^2 = \|x - p_F(x)\|^2 \iff \|y - p_F(x)\|^2 = 0 \iff y = p_F(x).$$

**Exercice 5** On remarque que :
$$\inf_{(*a,b*) \in \mathbb{R}^2} \int_0^1 (x^2 - ax - b)^2 dx = \inf_{P \in \mathbb{R}_1[X]} \|X^2 - P\|^2$$
où $\|\cdot\|$ est la norme euclidienne associée au produit scalaire sur $\mathbb{R}[X]$ :
$$(*P, Q*) \longmapsto \int_0^1 P(x)Q(x) dx$$
Donc :
$$\inf_{(*a,b*) \in \mathbb{R}^2} \int_0^1 (x^2 - ax - b)^2 dx = \|X^2 - P\|^2$$
où $P$ est le projeté orthogonal de $X^2$ sur $\mathbb{R}_1[X]$.
D'après l'exercice précédent, on a $P = X - \frac{1}{6}$ d'où :
$$\inf_{(*a,b*) \in \mathbb{R}^2} \int_0^1 (x^2 - ax - b)^2 dx = \int_0^1 \left(x^2 - x + \frac{1}{6}\right)^2 dx = \frac{1}{180}.$$

815

# Chapitre 14. *Espaces préhilbertiens et euclidiens*

**Corollaire 9** Par projection orthogonale sur le sous-espace $F$ engendré par $(e_1, \dots, e_p)$, on a :
$$x = p_F(x) + g = \sum_{i=1}^p (e_i \mid x) e_i + g \quad \text{avec} \quad g \in F^\perp.$$
L'égalité de Pythagore fournit :
$$\|x\|^2 = \sum_{i=1}^p (e_i \mid x)^2 + \|g\|^2.$$

**Exercice 6** Notons $F$ le sous-espace engendré par $(e_k)_{k \in \mathbb{N}}$ et, pour tout entier $n$, $F_n$ le sous-espace engendré par $(e_0, \dots, e_n)$.

Supposons que l'on ait $\sum_{k=0}^{+\infty} (e_k \mid x)^2 = \|x\|^2$.

Soit $\varepsilon > 0$, montrons que $F \cap B(x, \varepsilon)$ est non vide. D'après l'inégalité de Bessel et comme $\|x\|^2 = \lim_{n \to +\infty} \sum_{k=0}^n (e_k \mid x)^2$, il existe un entier $n$ tel que :
$$0 \le \|x\|^2 - \sum_{k=0}^n (e_k \mid x)^2 \le \varepsilon^2.$$
Le vecteur $p_n(x) = \sum_{k=0}^n (e_k \mid x) e_k$ est la projection orthogonale de $x$ sur le sous-espace vectoriel engendré par $(e_k)_{0 \le k \le n}$. Il appartient à $F$ et vérifie, d'après le théorème de Pythagore, l'inégalité :
$$\|x - p_n(x)\|^2 = \|x\|^2 - \sum_{k=0}^n (e_k \mid x)^2 \le \varepsilon^2.$$
Ainsi $p_n(x) \in F \cap B(x, \varepsilon)$ ce qui prouve $x \in \overline{F}$.

Supposons réciproquement que $x$ soit adhérent à $F$. Pour tout $\varepsilon > 0$, il existe un entier $N$ et un élément $f = \sum_{k=0}^N \alpha_k e_k$ de $F_N$ tel que $\|x - f\|^2$ soit inférieur ou égal à $\varepsilon$. Pour tout $n \ge N$, $F_N \subset F_n$ donc $f \in F_n$, ce qui entraîne :
$$0 \le \|x\|^2 - \sum_{k=0}^n (e_k \mid x)^2 = d(x, F_n)^2 \le \|x - f\|^2 \le \varepsilon.$$
Ainsi, $\|x\|^2 = \lim_{n \to +\infty} \sum_{k=0}^n (e_k \mid x)^2$.

**Exercice 7**
1. En appliquant le procédé d'orthogonalisation de Schmidt à la base canonique de $\mathbb{R}[X]$, c'est-à-dire en posant $Q_0 = 1$ et :
$$\forall n \in \mathbb{N}^* \quad Q_n = X^n - \sum_{k=0}^{n-1} \frac{(X^n \mid Q_k)}{\|Q_k\|^2} Q_k$$

816

**_Démonstrations et solutions des exercices du cours_**

on obtient une base orthogonale telle que, pour tout entier $n$, on ait $\text{deg}(Q_n) = n$ et $Q_n$ de coefficient dominant 1.

Supposons qu'il en existe une autre notée $(\tilde{Q}_n)_{n \in \mathbb{N}}$. Montrons, par récurrence forte que, pour tout entier $n$, on a $\tilde{Q}_n = Q_n$.

Par hypothèse, $\tilde{Q}_0$ est constant et de coefficient dominant 1 donc $\tilde{Q}_0 = 1 = Q_0$.
Supposons que pour un certain entier $n \in \mathbb{N}$, on ait :
$$\forall k \in \llbracket 0, n - 1 \rrbracket \quad \tilde{Q}_k = Q_k.$$

Comme les polynômes $Q_n$ et $\tilde{Q}_n$ sont de degré $n$ et de coefficient dominant 1, le polynôme $\tilde{Q}_n - Q_n$ appartient à $\mathbb{R}_{n-1}[X] = \text{Vect}(Q_0, \dots, Q_{n-1})$. De plus :
$$\forall k \in \llbracket 0, n - 1 \rrbracket \quad (Q_n \mid Q_k) = 0 \quad \text{et} \quad (\tilde{Q}_n \mid Q_k) = (\tilde{Q}_n \mid \tilde{Q}_k) = 0$$
donc :
$$\forall k \in \llbracket 0, n - 1 \rrbracket \quad (\tilde{Q}_n - Q_n \mid Q_k) = 0.$$

Ainsi, $\tilde{Q}_n - Q_n \in (\mathbb{R}_{n-1}[X])^\perp$ donc le polynôme $\tilde{Q}_n - Q_n$ est nul.

2. On a $Q_0 = 1$. On cherche $Q_1$ de la forme $X + a$ de sorte que $(Q_1 \mid 1) = 0$ et l'on obtient $Q_1 = X$.
   On cherche $Q_2$ de la forme $X^2 + aX + b$ de sorte que :
   $$(Q_2 \mid 1) = (Q_2 \mid X) = 0$$
   et l'on obtient $Q_2 = X^2 - \frac{1}{3}$.
   On cherche $Q_3$ de la forme $X^3 + aX^2 + bX + c$ de sorte que :
   $$(Q_3 \mid 1) = (Q_3 \mid X) = (Q_3 \mid X^2) = 0$$
   et l'on obtient $Q_3 = X^3 - \frac{3}{5}X$.

3. Soit $n \in \mathbb{N}$. Montrons que le polynôme $Q_n$ est de même parité que $n$, c'est-à-dire que $Q_n(X) = (-1)^n Q_n(-X)$.
   Comme $Q_n$ est de degré $n$, le polynôme $\tilde{Q}_n(X) = (-1)^n Q_n(-X)$ est de degré $n$ et de coefficient dominant 1. Il suffit donc, par unicité, de montrer que $(\tilde{Q}_n)_{n \in \mathbb{N}}$ est une famille orthogonale, c'est-à-dire que $\tilde{Q}_n$ est orthogonal à $\mathbb{R}_{n-1}[X]$ pour tout $n \in \mathbb{N}^*$.
   Soit $n \in \mathbb{N}^*$ et $P \in \mathbb{R}_{n-1}[X]$. On a :
   $$\int_{-1}^1 \tilde{Q}_n(t) P(t) dt = (-1)^n \int_{-1}^1 Q_n(-t) P(t) dt = (-1)^n \int_{-1}^1 Q_n(t) P(-t) dt = 0,$$
   les deux dernières égalités provenant du changement de variable $t \mapsto -t$ et du fait que $P(-X) \in \mathbb{R}_{n-1}[X]$ est orthogonal à $Q_n$.

4. Si $Q_n$ ne possède pas $n$ racines simples dans l'intervalle $]-1, 1[$, alors le polynôme $R = \prod_{a \in S} (X - a)$ où $S$ est l'ensemble des racines de $Q_n$ appartenant à l'intervalle $]-1, 1[$ et d'ordre impair, appartient à $\mathbb{R}_{n-1}[X] = \text{Vect}(Q_0, \dots, Q_{n-1})$. En particulier, on a $(Q_n \mid R) = 0$, c'est-à-dire $\int_{-1}^1 Q_n(t) R(t) dt = 0$.

817

# Chapitre 14. Espaces préhilbertiens et euclidiens

Or, la fonction $t \mapsto Q_n(t)R(t)$ est continue et de signe constant sur $[-1, 1]$. En effet, les racines de $Q_n R$ appartenant à l'intervalle $]-1, 1[$ sont de multiplicité paire donc la fonction $t \mapsto Q_n(t)R(t)$ est de signe constant sur $]-1, 1[$ puis sur le segment $[-1, 1]$ par continuité.

Par conséquent, la fonction $t \mapsto Q_n(t)R(t)$ est nulle sur $[-1, 1]$, ce qui implique la nullité du polynôme $Q_n R$ qui est de degré au moins $n$.

On aboutit donc à une contradiction ; ce qui prouve que le polynôme $Q_n$ possède $n$ racines simples dans l'intervalle $]-1, 1[$.

## **Exercice 8**

1. Le polynôme $Q_{n+2} - XQ_{n+1}$ appartient à $\mathbb{R}_{n+1}[X] = \text{Vect}(Q_0, \dots, Q_{n+1})$. De plus :
   $$\forall k \in \llbracket 0, n-1 \rrbracket \quad (Q_{n+2} - XQ_{n+1} \mid Q_k) = -(XQ_{n+1} \mid Q_k) = -(Q_{n+1} \mid XQ_k) = 0$$
   car $Q_{n+1}$ est orthogonal à $\text{Vect}(Q_0, \dots, Q_n) = \mathbb{R}_n[X]$.

   Comme $Q_{n+2} - XQ_{n+1} = \sum_{k=0}^{n+1} \frac{(Q_{n+2} - XQ_{n+1} \mid Q_k)}{\|Q_k\|^2} Q_k$, on en déduit que $Q_{n+2} - XQ_{n+1}$ est une combinaison linéaire des polynômes $Q_{n+1}$ et $Q_n$.
   Pour des raisons de parité, il est donc colinéaire à $Q_n$, c'est-à-dire que :
   $$Q_{n+2} \in \text{Vect}(XQ_{n+1}, Q_n).$$

2. Soit $p$ et $q$ deux entiers tels que $q < p$. On a, par intégrations par parties :
   $$(R_p^{(p)} \mid R_q^{(q)}) = -(R_p^{(p-1)} \mid R_q^{(q+1)})$$
   et, de même, pour tout $k \in \llbracket 1, p \rrbracket$, $(R_p^{(p)} \mid R_q^{(q)}) = (-1)^k (R_p^{(p-k)} \mid R_q^{(q+k)})$. En particulier, pour $k = q + 1$, on obtient $(R_p^{(p)} \mid R_q^{(q)}) = 0$.

   La famille $\left(R_n^{(n)}\right)_{n \in \mathbb{N}}$ est donc orthogonale.

   De plus, pour tout entier $n$, le polynôme $R_n$ est de degré $2n$ et unitaire donc $R_n^{(n)}$ est de degré $n$ et de coefficient dominant $\frac{(2n)!}{n!}$.

   En particulier, la famille $\left(\frac{n!}{(2n)!} R_n^{(n)}\right)_{n \in \mathbb{N}}$ est échelonnée, il s'agit donc d'une base orthogonale. On conclut à l'aide de l'unicité prouvée à la première question.

3. On a $R_n = (X - 1)^n(X + 1)^n$ donc la formule de Leibniz donne :
   $$R_n^{(n)} = \sum_{k=0}^n \binom{n}{k} ((X - 1)^n)^{(k)} ((X + 1)^n)^{(n-k)}.$$

   Comme 1 est racine d'ordre $n$ de $(X - 1)^n$, pour tout $k \in \llbracket 0, n - 1 \rrbracket$, le polynôme $((X - 1)^n)^{(k)}$ s'annule en 1. On en déduit que $R_n^{(n)}(1) = n! 2^n$ puis que
   $$Q_n(1) = 2^n \frac{(n!)^2}{(2n)!}.$$

818

***Démonstrations et solutions des exercices du cours***

Pour des raisons de degré et de coefficient dominant, on a $\alpha_n = 1$.
En évaluant la relation $Q_{n+2} = \alpha_n X Q_{n+1} + \beta_n Q_n$ en 1, on obtient :

$$2^{n+2} \frac{((n+2)!)^2}{(2n+4)!} = 2^{n+1} \frac{((n+1)!)^2}{(2n+2)!} + \beta_n 2^n \frac{(n!)^2}{(2n)!}$$

soit :

$$\frac{4(n+2)^2(n+1)^2}{(2n+4)(2n+3)(2n+2)(2n+1)} = \frac{2(n+1)^2}{(2n+2)(2n+1)} + \beta_n$$

puis :

$$\beta_n = -\frac{(n+1)^2}{(2n+1)(2n+3)}.$$

**Exercice 9** Le polynôme $((1 - X^2) Q'_n)'$ appartient à $\mathbb{R}_n[X] = \text{Vect}(Q_0, \dots, Q_n)$.

Montrons que, pour tout $k \in \llbracket 0, n - 1 \rrbracket$, on a $\left( ((1 - X^2) Q'_n)' \mid Q_k \right) = 0$, ce qui permettra de conclure.

Soit $k \in \llbracket 0, n - 1 \rrbracket$, une intégration par parties donne :

$$\left( ((1 - X^2) Q'_n)' \mid Q_k \right) = -\int_{-1}^1 (1 - t^2) Q'_n(t) Q'_k(t) dt.$$

Une seconde intégration par parties conduit alors à :

$$\begin{aligned} \left( ((1 - X^2) Q'_n)' \mid Q_k \right) &= \int_{-1}^1 Q_n(t) \left( (1 - t^2) Q''_k(t) - 2t Q'_k(t) \right) dt \\ &= \left( Q_n \mid (1 - X^2) Q''_k - 2X Q'_k \right) = 0 \end{aligned}$$

car le polynôme $(1 - X^2) Q''_k - 2X Q'_k$ appartient à $\mathbb{R}_k[X] = \text{Vect}(Q_0, \dots, Q_k)$.

Il existe donc un réel $\lambda_n$ tel que $((1 - X^2) Q'_n)' = \lambda_n Q_n$. Le coefficient dominant de $((1 - X^2) Q'_n)'$ est égal à $-n(n+1)$. Par conséquent, $Q_n$ est solution de l'équation différentielle :

$$(X^2 - 1) Q''_n + 2X Q'_n - n(n+1) Q_n = 0.$$

**Exercice 10**

1. On a $L_2(X) = \frac{3X^2 - 1}{2}$ et $L_3(X) = \frac{5X^3 - 3X}{2}$.

   Montrons par récurrence double que pour tout entier $n$, on a $H(n) : \text{« } L_n(1) = 1 \text{ »}$.
   Les assertions $H(0)$ et $H(1)$ sont évidentes. Supposons que pour un certain entier $n$ on ait $H(n)$ et $H(n+1)$, alors on a :

   $$(n+2)L_{n+2}(1) - (2n+3)L_{n+1}(1) + (n+1)L_n(1) = 0 = (n+2)L_{n+2}(1) - (2n+3) + n + 1,$$

   ce qui prouve $H(n+2)$.

2. Montrons par récurrence double que pour tout entier $n$, on a :

   $$P(n) : \text{« } Q_n(X) = \frac{2^n (n!)^2}{(2n)!} L_n(X) \text{ »}.$$

819

# Chapitre 14. Espaces préhilbertiens et euclidiens

Les assertions $P(0)$ et $P(1)$ sont évidentes. Supposons que pour un certain entier $n$ on ait $P(n)$ et $P(n+1)$, alors :

$$
\begin{aligned}
Q_{n+2} &= XQ_{n+1} - \frac{(n+1)^2}{(2n+1)(2n+3)} Q_n \\
&= \frac{2^{n+1} ((n+1)!)^2}{(2<sup>n+2</sup>)!} XL_{n+1}(X) - \frac{(n+1)^2}{(2n+1)(2n+3)} \frac{2^n (n!)^2}{(2n)!} L_n(X) \\
&= \frac{2^{n+2} ((n+2)!)^2}{(2n+4)!} \left( \frac{(2n+3)(2n+4)}{2(n+2)^2} XL_{n+1}(X) - \frac{(2<sup>n+2</sup>)(2n+4)}{4(n+2)^2} L_n(X) \right) \\
&= \frac{2^{n+2} ((n+2)!)^2}{(2n+4)!} L_{n+2}(X),
\end{aligned}
$$

ce qui prouve $P(n+2)$.

ce qui prouve $P(n+2)$.

## **Proposition 14** Soit $(e_i)_{1 \le i \le n}$ une base orthonormée de $E$ et $u$ un endomorphisme de $E$. La matrice de $u$ dans $\mathcal{B}$ est $M = ((u(e_j) \mid e_i))_{1 \le i,j \le n}$.

Si $u$ est symétrique, alors, pour tout $(*i, j*) \in \llbracket 1, n \rrbracket^2$, on a $(u(e_j) \mid e_i) = (u(e_i) \mid e_j)$ donc $M$ est symétrique.

Réciproquement, supposons $M$ symétrique. Soit $x$ et $y$ dans $E$ ; notons $X$ et $Y$ les matrices colonnes les représentant dans la base $\mathcal{B}$. Comme la base est orthonormée, on a :

$$(u(x) \mid y) = {}^t(MX)Y = {}^tX {}^tMY = {}^*tXMY* = (x \mid u(y)).$$

## **Exercice 11** Considérons les matrice $A$ et $B$ de $u$ et $v$ dans une base orthonormale. Alors $u \circ v$ est symétrique si, et seulement si, $AB$ est symétrique d'après la proposition 14 de la page 807.

Or, ${}^t(AB) = {}^tB {}^tA = BA$. Donc $AB$ est symétrique si, et seulement si, $A$ et $B$ commutent, c'est-à-dire si, et seulement si, $u$ et $v$ commutent.

## **Proposition 17**

*   Si $p$ est une projection orthogonale, on a pour tout $(x, y)$ :

$$(p(x) \mid y) = (p(x) \mid p(y) + y - p(y)) = (p(x) \mid p(y))$$

    puisque $p(x)$ appartient à $\text{Im } p$ et $y - p(y)$ à $\text{Ker } p = (\text{Im } p)^\perp$.
    On obtient de même $(x \mid p(y)) = (p(x) \mid p(y))$ d'où $(p(x) \mid y) = (x \mid p(y))$ pour tout $(*x, y*)$, ce qui montre que $p$ est symétrique.

*   Si $p$ est un projecteur symétrique, alors pour tout $(x, y) \in \text{Ker } p \times \text{Im } p$, on a :

$$(x \mid y) = (x \mid p(y)) = (p(x) \mid y) = 0.$$

    Ainsi, $\text{Ker } p$ et $\text{Im } p$ sont orthogonaux, ce qui prouve que $p$ est une projection orthogonale.

## **Exercice 12** Soit $s$ une symétrie de $E$. L'endomorphisme $p = \frac{s + \text{Id}}{2}$ est alors une projection. Comme $\mathcal{S}(E)$ est un espace vectoriel contenant $\text{Id}$, $s$ est un endomorphisme symétrique si, et seulement si, $p$ l'est donc si, et seulement si, $s$ est une symétrie orthogonale.

820

**_Démonstrations et solutions des exercices du cours_**

## **Exercice 13**

*   Supposons $p$ orthogonale. Pour tout $x \in E$, on a $(x - p(x), p(x)) \in \text{Ker } p \times \text{Im } p$ donc $\|x\|^2 = \|x - p(x)\|^2 + \|p(x)\|^2$. Ainsi, $\|p(x)\| \leqslant \|x\|$.
*   Supposons que pour tout $u \in E$, on ait $\|p(u)\| \leqslant \|u\|$.
    Soit $(*x, y*) \in \text{Ker } p \times \text{Im } p$. Pour tout $\lambda \in \mathbb{R}$, on a $p(y + \lambda x) = y$ donc :
    $$\|y\|^2 \leqslant \|y + \lambda x\|^2 = \|y\|^2 + 2\lambda(y | x) + \lambda^2\|x\|^2.$$
    La fonction polynomiale $\lambda \mapsto \lambda^2\|x\|^2 + 2\lambda(x | y)$ est donc positive, ce qui implique, lorsque $\|x\|^2 \neq 0$, que son discriminant est négatif, et conduit à $(x | y) = 0$. Évidemment, $x$ et $y$ sont orthogonaux lorsque $x = 0$.
    Ainsi, $\text{Ker } p$ et $\text{Im } p$ sont orthogonaux. Par conséquent, $p$ est une projection orthogonale.

## **Proposition 18**  Soit $x$ et $y$ deux vecteurs propres d'un endomorphisme symétrique $u$ associés à des valeurs propres différentes $\lambda$ et $\mu$. On a alors :
$$\lambda(x | y) = (u(x) | y) = (x | u(y)) = \mu(x | y)$$
donc $(\lambda - \mu)(x | y) = 0$, ce qui prouve que les vecteurs $x$ et $y$ sont orthogonaux.

## **Exercice 14**

1.  Pour tout $(*P, Q*) \in \mathbb{R}[X]^2$, la fonction $t \mapsto P(t)Q(t)e^{-t^2/2}$ est continue sur $\mathbb{R}$ et $P(t)Q(t)e^{-t^2/2} \underset{\pm\infty}{=} o\left(\frac{1}{t^2}\right)$ donc, par critère de Riemann, $t \mapsto P(t)Q(t)e^{-t^2/2}$ est intégrable sur $\mathbb{R}$.
    Ainsi, l'application $(*P, Q*) \mapsto \int_{-\infty}^{+\infty} P(t)Q(t)e^{-t^2/2} dt$ est bien définie sur $\mathbb{R}[X]^2$ et elle est clairement bilinéaire symétrique. Soit $P \in \mathbb{R}[X]$.
    On a évidemment $\int_{-\infty}^{+\infty} P(t)^2 e^{-t^2/2} dt \geqslant 0$ et comme $t \mapsto P(t)^2 e^{-t^2/2}$ est continue et positive, on en déduit que son intégrale ne peut être nulle que si c'est la fonction nulle. Comme la fonction exponentielle ne s'annule pas, il en découle que $P$ est le polynôme nul.
    Par conséquent, l'application $(*P, Q*) \mapsto \int_{-\infty}^{+\infty} P(t)Q(t)e^{-t^2/2} dt$ est un produit scalaire sur $\mathbb{R}[X]$.

2.  Soit $(*P, Q*) \in \mathbb{R}[X]^2$. On a :
    $$(\Phi(P) | Q) = \int_{-\infty}^{+\infty} e^{-t^2/2} (tP'(t) - P''(t)) Q(t) dt.$$
    Comme la fonction $t \mapsto e^{-t^2/2} P'(t) Q(t)$ est de limite nulle en $\pm\infty$, une intégration par parties donne :
    $$(\Phi(P) | Q) = \int_{-\infty}^{+\infty} e^{-t^2/2} P'(t) Q'(t) dt,$$
    quantité dans laquelle $P$ et $Q$ jouent un rôle symétrique, ce qui conduit donc à :
    $$(\Phi(P) | Q) = (P | \Phi(Q)).$$
    Par conséquent, $\Phi$ est symétrique.

821

# Chapitre 14. Espaces préhilbertiens et euclidiens

3. Soit $n \in \mathbb{N}$.
    (a) Soit $P \in \mathbb{R}_n[X]$, les polynômes $XP'$ et $P''$ appartiennent aussi au sous-espace vectoriel $\mathbb{R}_n[X]$ donc $\mathbb{R}_n[X]$ est stable par $\Phi$.
    Pour tout $k \in \llbracket 0, n \rrbracket$, on a $\Phi(X^k) = kX^k - k(k-1)X^{k-2}$ donc la matrice de $\Phi_n$ dans la base canonique de $\mathbb{R}_n[X]$ est triangulaire supérieure avec $0, 1, \dots, n$ sur la diagonale. On en déduit que $\Phi_n$ possède $n+1$ valeurs propres distinctes ce qui constitue une condition suffisante pour être diagonalisable.
    (b) Soit $k \in \llbracket 0, n \rrbracket$, $k$ est valeur propre de $\Phi_n$ donc il existe un polynôme $P_k$ tel que $\Phi_n(P_k) = kP_k$.
    D'après la proposition précédente, la famille $\left( \frac{P_k}{\|P_k\|} \right)_{0 \leqslant k \leqslant n}$ est une famille orthonormée. Comme elle est de cardinal $n+1$, c'est donc une base orthonormée de $\mathbb{R}_n[X]$ constituée de vecteurs propres de $\Phi_n$.

4. Soit $n \in \mathbb{N}$ et $P \in E_n(\Phi)$ non nul. Si l'on note $d$ le degré de $P$ et $a_P$ son coefficient dominant, alors les polynômes $\Phi(P)$ et $nP$ ont pour coefficients dominants respectifs $da_P$ et $na_P$. On en déduit que $P$ est de degré $n$.
    Ainsi, $E_n(\Phi) \subset \mathbb{R}_n[X]$ donc $E_n(\Phi) = E_n(\Phi_n)$. Comme les espaces propres de $\Phi_n$ sont de dimension 1, $E_n(\Phi)$ aussi. Par conséquent, il existe un unique polynôme $H_n$ de coefficient dominant 1 tel que $\Phi(H_n) = nH_n$ et $\deg H_n = n$.

**Exercice 15**

1. On obtient $H_0 = 1$, $H_1 = X$, $H_2 = X^2 - 1$, $H_3 = X^3 - 3X$.
2. Le résultat est évident pour $k = 0$. Supposons-le vrai pour un certain entier $k$. Il existe alors un polynôme $Q$ de degré $k$ et de coefficient dominant $(-1)^k$ tel que :
$$\forall x \in \mathbb{R} \quad g^{(k)}(x) = Q(x)e^{-x^2/2}.$$
Comme $g$ est de classe $\mathcal{C}^\infty$, on en déduit que :
$$\forall x \in \mathbb{R} \quad g^{(k+1)}(x) = (Q'(x) - xQ(x))e^{-x^2/2}.$$
Le polynôme $Q'$ étant de degré $k$ et de coefficient dominant $(-1)^k$, $Q' - XQ$ est de degré $k+1$ et de coefficient dominant $(-1)^{k+1}$, ce qui prouve le résultat au rang $k+1$.
3. D'après la question précédente, il existe un polynôme $Q_n$ de degré $n$ et de coefficient dominant $(-1)^n$ tel que :
$$\forall x \in \mathbb{R} \quad g^{(n)}(x) = Q_n(x)e^{-x^2/2}.$$
Il reste à prouver que $\Phi(Q_n) = nQ_n$ pour conclure.
On a :
$$\forall x \in \mathbb{R} \quad g^{(n+1)}(x) = (Q'_n(x) - xQ_n(x))e^{-x^2/2}$$
et
$$\forall x \in \mathbb{R} \quad g^{(n+2)}(x) = (Q''_n(x) - 2xQ'_n(x) - Q_n(x) + x^2Q_n(x))e^{-x^2/2}.$$
Ainsi :
$$\forall x \in \mathbb{R} \quad xQ'_n(x) - Q''_n(x) = e^{x^2/2} \left( -g^{(n)}(x) - xg^{(n+1)}(x) - g^{(n+2)}(x) \right).$$

822

***Démonstrations et solutions des exercices du cours***

Or, $g^{(n+2)}$ est égale à la dérivée $(n+1)$-ième de $x \mapsto -xe^{-x^2/2}$ donc, en utilisant la formule de Leibniz, on obtient :
$$\forall x \in \mathbb{R} \quad g^{(n+2)}(x) = -xg^{(n+1)}(x) - (n+1)g^{(n)}(x).$$
On a donc $\Phi(Q_n) = nQ_n$ puis $(-1)^n Q_n = H_n$.
Ainsi $\forall x \in \mathbb{R} \quad H_n(x) = (-1)^n e^{x^2/2} g^{(n)}(x)$.

4. Pour tout entier $n$, la fonction $t \mapsto g^{(n)}(x)g^{(n-1)}(x)e^{x^2/2}$ est de limite nulle en $\pm\infty$ car elle est de la forme $x \mapsto Q(x)e^{-x^2/2}$ avec $Q \in \mathbb{R}[X]$.
Ainsi, une intégration par parties donne :

$$
\begin{aligned}
\|H_n\|^2 &= \int_{-\infty}^{+\infty} e^{t^2} g^{(n)}(t) g^{(n)}(t) e^{-t^2/2} \, \mathrm{d}t \\
&= -\int_{-\infty}^{+\infty} g^{(n-1)}(t) e^{t^2/2} \left( t g^{(n)}(t) + g^{(n+1)}(t) \right) \, \mathrm{d}t.
\end{aligned}
$$

Or, pour tout réel $t$, on a :
$$tg^{(n)}(t) + g^{(n+1)}(t) = -ng^{(n-1)}(t)$$
donc $\|H_n\|^2 = n \|H_{n-1}\|^2$.

5. On en déduit que pour tout entier $n$, $\|H_n\|^2 = n! \|H_0\|^2 = n!\sqrt{2\pi}$ et donc que la famille $\left( \frac{H_n}{\sqrt{n!\sqrt{2\pi}}} \right)_{n \in \mathbb{N}}$ est une base orthonormée de $\mathbb{R}[X]$.

Si $P$ est un polynôme de degré $d$, alors, la famille $\left( \frac{H_n}{\sqrt{n!\sqrt{2\pi}}} \right)_{0 \le n \le d}$ étant une base orthonormée de $\mathbb{R}_d[X]$, on a $P = \sum_{<sub>n=0</sub>}^d (P \mid H_n) \frac{H_n}{n!\sqrt{2\pi}}$.

Pour tout entier $n$, si $n > d$, alors le polynôme $H_n$ appartient à l'orthogonal de $\mathbb{R}_d[X] = \text{Vect}(H_k)_{0 \le k \le d}$ donc $(P \mid H_n) = 0$.

Par conséquent, on peut écrire $P = \sum_{n \in \mathbb{N}} (P \mid H_n) \frac{H_n}{n!\sqrt{2\pi}}$ (il s'agit d'une somme finie).

**Proposition 19** Soit $\lambda$ une valeur propre complexe de $A$ ainsi qu'un vecteur propre complexe associé $X = (x_k)_{1 \le k \le n}$.

On a donc $AX = \lambda X$ et $A\overline{X} = \overline{\lambda}\overline{X}$ car $A$ est à coefficients réels. Ainsi :

$${}^t X A \overline{X} = \overline{\lambda} {}^t X \overline{X} = \overline{\lambda} \sum_{k=1}^{n} |x_i|^2.$$

De plus, comme $^tX A \overline{X} \in \mathcal{M}_{1,1}(\mathbb{C})$, $^tX A \overline{X} = {}^t(^tX A \overline{X}) = {}^t\overline{X} {}^tA X$. La symétrie de $A$ donne alors $^tX A \overline{X} = {}^t\overline{X} A X = \lambda {}^t\overline{X} X = \lambda \sum_{k=1}^n |x_i|^2$ donc $(\lambda - \overline{\lambda}) \sum_{k=1}^n |x_i|^2 = 0$.

Par conséquent, $\lambda$ est réel.

823

Chapitre 14. *Espaces préhilbertiens et euclidiens*

**Proposition 21** Soit $F$ un sous-espace vectoriel de $E$ stable par un endomorphisme $u$ symétrique et $x \in F^\perp$. Pour tout $y \in F$, on a $u(y) \in F$ car $F$ est stable par $u$, donc :
$$(u(x) \mid y) = (x \mid u(y)) = 0.$$
Par conséquent, $u(x) \in F^\perp$ et donc $F^\perp$ est stable par $u$.

**Théorème 22** On va démontrer l’existence d’une base orthonormée de vecteurs propres. Le second point en découlera grâce à la proposition 18 de la page 807.
La somme $G$ des sous-espaces propres de $u$ est stable par $u$. Son supplémentaire orthogonal $G^\perp$ l’est aussi d’après la proposition 21 de la page 809.
L’endomorphisme $u'$ induit par $u$ sur $G^\perp$ est évidemment symétrique. Si $G^\perp$ n’est pas réduit à $\{0\}$, il possède une valeur propre ce qui contredit $G \cap G^\perp = \{0\}$ puisque tout vecteur propre de $u'$ appartient aussi à $G$. Il vient alors $G = E$.

**Corollaire 23**
*   Si $u$ est symétrique, alors il existe une base orthonormée de vecteurs propres d’après la propriété précédente. La matrice de $u$ dans cette base est alors diagonale.
    La réciproque découle de la proposition 14 de la page 807.
*   Découle de la proposition 14 de la page 807.

**Exercice 16**
1. Soit $\mathcal{B}$ une base orthonormée et $A = \text{Mat}_{\mathcal{B}}(u)$. D’après le théorème spectral, il existe $P \in \mathcal{O}_n(\mathbb{R})$ et $D \in \mathcal{M}_n(\mathbb{R})$ diagonale telles que $A = P^{-1}DP$.
   Par hypothèse, $\text{sp } A \subset \mathbb{R}_+$ donc les coefficients diagonaux de $D$, notés $d_1, \dots, d_n$ sont positifs. On considère alors la matrice diagonale $D'$ de coefficients diagonaux $\sqrt{d_1}, \dots, \sqrt{d_n}$ de sorte que $D'^2 = D$. On a ainsi $A = B^2$ avec $B = P^{-1}D'P$.
   Comme $P$ est orthogonale, $B = {}^tP D' P$ est symétrique et il suffit de considérer l’endomorphisme $v$ tel que $B = \text{Mat}_{\mathcal{B}}(v)$ pour conclure.
2. L’endomorphisme symétrique trouvé à la question précédente convient. Montrons que c’est le seul. Pour cela considérons un endomorphisme symétrique $w$ vérifiant $w^2 = u$ et $\text{sp } w \subset \mathbb{R}_+$.
   Puisque $w$ commute avec $u$, cet endomorphisme laisse stable les sous-espaces propres de $u$. On va prouver que pour tout $\lambda \in \text{sp } u$, l’endomorphisme $w_\lambda$ induit par $w$ sur $E_\lambda(u)$ est égal à $\sqrt{\lambda} \text{Id}_{E_\lambda(u)}$, ce qui prouvera que $v$ et $w$ coïncident sur chaque espace propre de $u$ et donc sur $E$.
   Comme $w_\lambda$ est symétrique et de valeurs propres positives, il existe une base de $E_\lambda(u)$ dans laquelle sa matrice $D_\lambda$ est diagonale, à coefficients positifs et vérifie $D_\lambda^2 = \lambda I_{n_\lambda}$ où $n_\lambda = \dim E_\lambda(u)$. On en déduit que $D_\lambda = \sqrt{\lambda} I_{n_\lambda}$, ce qui prouve $w_\lambda = \sqrt{\lambda} \text{Id}_{E_\lambda(u)}$ et conclut la démonstration de l’unicité.

**Exercice 17**
1. On a ${}^t({}^*tMM*) = {}^tM {}^t({}^tM) = {}^*tMM*$ donc ${}^*tMM*$ est symétrique.
   Soit $\lambda$ une valeur propre de ${}^*tMM*$ et $X$ un vecteur propre associé.
   On a ${}^tMMX = \lambda X$ donc ${}^tX {}^tMMX = \lambda {}^tXX$ c’est-à-dire $\|MX\|^2 = \lambda \|X\|^2$ donc $\lambda \geqslant 0$.

824

***Démonstrations et solutions des exercices du cours***

2. &bull; Supposons qu'un tel couple existe.
   On a alors $^tM = ^tS^tO = SO^{-1}$ donc $^tMM = S^2$. Ainsi, $S$ est unique d'après le lemme de la racine carrée. Comme $\text{Ker } S \subset \text{Ker } M$, $S$ est inversible et l'on obtient $O = MS^{-1}$. Ainsi, un tel couple est unique s'il existe.
   &bull; Vérifions que le couple obtenu par analyse convient c'est-à-dire que $O = MS^{-1}$ est orthogonale. On a :
   $$^*tOO* = ^tS^{-1}{^tMM}S^{-1} = S^{-1}S^2S^{-1} = I_n$$
   donc le couple obtenu convient.

**Exercice 18** Soit $u$ une isométrie et $x$ un vecteur propre associé à la valeur propre $\lambda$. Comme $\|u(x)\| = \|x\| = |\lambda|\|x\|$ et comme $x$ est non nul, on a $|\lambda| = 1$. Les valeurs propres possibles d'une isométrie vectorielle sont donc $\pm 1$.

**Proposition 28**
Soit $F$ un sous-espace vectoriel de $E$ stable par une isométrie $u$ et $x \in F^\perp$. Pour tout $y \in F$, on a :
$$( u(x) \mid u(y) ) = ( x \mid y ) = 0,$$
ce qui prouve que $u(x) \in u(F)^\perp$.
Comme $u$ est un automorphisme et comme $F$ est de dimension finie, on a $\dim u(F) = \dim F$. La stabilité de $F$ par $u$ implique donc $u(F) = F$.
Par conséquent, $u(x) \in F^\perp$ donc $F^\perp$ est stable par $u$.

**Lemme 29** Comme $u$ possède un polynôme annulateur, il existe des polynômes unitaires $P_1, \dots, P_r$ de degré 1 ou 2 tels que $(P_1 \dots P_r)(u) = 0 = P_1(u) \circ \dots \circ P_r(u) = 0$.
Parmi les endomorphismes $P_1(u), \dots, P_r(u)$ l'un d'entre eux est donc non injectif. Sans perdre de généralité, on suppose qu'il s'agit de $P_1$ et l'on considère $x \in \text{Ker } P_1(u)$ non nul.
Comme $P_1$ est de degré inférieur ou égal à 2, on a $u^2(x) \in \text{Vect}(*x, u*(x))$. Par conséquent, $\text{Vect}(*x, u*(x))$ est une droite ou un plan stable par $u$.

**Théorème 30** On va démontrer le résultat par récurrence sur la dimension de $E$.
Si $E$ est de dimension 1, alors le résultat est trivial.
Soit $n \in \mathbb{N}^*$, supposons le résultat vrai pour toute isométrie d'un espace euclidien de dimension inférieure ou égale à $n - 1$ et considérons $u$ une isométrie d'un espace euclidien de dimension $n$.
&bull; Supposons que $u$ possède une valeur propre réelle $\lambda$.
  Soit $e_1$ un vecteur propre associé à $\lambda$. On a alors $E = \mathbb{R}e_1 \oplus (\mathbb{R}e_1)^\perp$. Comme $\mathbb{R}e_1$ est stable par l'isométrie $u$, son orthogonal aussi.
  Par hypothèse de récurrence, comme l'endomorphisme induit par $u$ sur $(\mathbb{R}e_1)^\perp$ est une isométrie, il existe une base orthonormée de $(\mathbb{R}e_1)^\perp$ dans laquelle sa matrice est de la forme annoncée. Il suffit de la compléter avec $\frac{e_1}{\|e_1\|}$ pour obtenir une base orthonormée de $E$ dans laquelle la matrice de $u$ est de la forme annoncée. En effet, $u$ étant une isométrie, $\lambda = \pm 1$.

825

Chapitre 14. *Espaces préhilbertiens et euclidiens*

*   Supposons que $u$ ne possède pas de valeur propre réelle. Alors $u$ possède un plan stable $P$ d'après le lemme précédent. Soit $\mathcal{B}$ une base orthonormée de $P$ et $\tilde{u}$ l'endomorphisme induit par $u$ sur $P$. La matrice $\text{Mat}_{\mathcal{B}}(u)$ est alors une matrice de $\mathcal{O}_2(\mathbb{R})$ sans valeur propre réelle.

    Or, d'après les résultats de première année, les matrices de $\mathcal{O}_2(\mathbb{R})$ sont de la forme
    $$R(\theta) = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix} \text{ ou } S(\theta) = \begin{pmatrix} \cos \theta & \sin \theta \\ \sin \theta & -\cos \theta \end{pmatrix}.$$
    Comme $u$ ne possède pas de valeur propre réelle, $\tilde{u}$ non plus et ce n'est donc pas une symétrie. On en déduit que $\text{Mat}_{\mathcal{B}}(u)$ est de la forme $R(\theta)$ avec $\sin \theta \neq 0$.

    Par hypothèse de récurrence, comme l'endomorphisme induit par $u$ sur $P^\perp$ est une isométrie, il existe une base orthonormée de $P^\perp$ dans laquelle sa matrice est de la forme annoncée. Il suffit de la compléter avec une base orthonormée de $P$ pour obtenir une base orthonormée de $E$ dans laquelle la matrice de $u$ est de la forme annoncée.

**Exercice 19** Il n'y a pas nécessairement unicité. Par exemple, si $u = \text{Id}_E$, alors toute droite convient.

Soit $u$ une rotation d'axe $D$. Supposons qu'il n'y ait un autre axe $D'$. Alors $u$ induit l'identité sur le plan $D + D'$. Ce plan contient alors un vecteur non nul du plan $D^\perp$, ce qui prouve que la rotation sur $D^\perp$ est l'identité. Donc $u = \text{Id}_E$.

En conclusion il y a unicité de l'axe si, et seulement si, $u \neq \text{Id}_E$.

826

***Exercices***

# S'entraîner et approfondir

**14.1** Soit $E$ un espace euclidien orienté de dimension $n$.

Pour tout $(e_1, \dots, e_{n-1}) \in E^{n-1}$, on note $e_1 \wedge \dots \wedge e_{n-1}$, et l'on appelle **produit vectoriel** des vecteurs $e_1, \dots, e_{n-1}$, l'unique vecteur de $E$ tel que :

$$\forall x \in E \quad [e_1, \dots, e_{n-1}, x] = ( e_1 \wedge \dots \wedge e_{n-1} \mid x )$$

1. Justifier la définition du produit vectoriel.
2. Montrer que le produit vectoriel $e_1 \wedge \dots \wedge e_{n-1}$ est nul si, et seulement si, la famille $(e_1, \dots, e_{n-1})$ est liée.
3. Montrer que si la famille $(e_1, \dots, e_{n-1})$ est orthonormale, alors $(e_1, \dots, e_n)$ est une base orthonormale directe.

**14.2** Soit $E$ un espace vectoriel préhilbertien et $F$ un sous-espace vectoriel de $E$.

1. Montrer que s'il existe un sous-espace $G$ tel que $E = F \overset{\perp}{\oplus} G$, alors $G = F^\perp$.
2. Prouver que si $E = F \overset{\perp}{\oplus} G$, alors $(F^\perp)^\perp = F$.

**14.3** Soit $u$ un endomorphisme d'un espace euclidien $E$.

1. Montrer qu'il existe un unique endomorphisme $u^*$ de $E$ vérifiant :
$$\forall(*x, y*) \in E^2 \quad ( u(x) \mid y ) = ( x \mid u^*(y) ).$$
L'endomorphisme $u^*$ est appelé l'**adjoint** de $u$.
2. Déterminer $(u^*)^*$.
3. Donner une condition nécessaire et suffisante sur $u^*$ pour que $u$ soit symétrique.
4. Donner une condition nécessaire et suffisante sur $u^*$ pour que $u$ soit une isométrie.
5. Montrer que $\text{Ker } u^* = (\text{Im } u)^\perp$ et $\text{Im } u^* = (\text{Ker } u)^\perp$.
6. Soit $F$ un sous-espace vectoriel stable par $u$. Montrer que $F^\perp$ est stable par $u^*$. Retrouver la stabilité de $F^\perp$ par $u$ lorsque $u$ est symétrique (*cf.* la proposition 21 de la page 809) ou orthogonal (*cf.* la proposition 28 de la page 812).

**14.4** Soit $u$ un endomorphisme d'un espace euclidien $E$.

1. Montrer qu'il y a équivalence entre :
   (i) $\forall x \in E \quad ( x \mid u(x) ) = 0$;
   (ii) $\forall(*x, y*) \in E^2 \quad ( u(x) \mid y ) = -( x \mid u(y) )$.
2. Montrer que deux quelconques des trois propositions suivantes impliquent la troisième :
   (i) $u$ est une isométrie ;
   (ii) $u^2 = -\text{Id}$ ;
   (*iii*) $\forall x \in E \quad ( x \mid u(x) ) = 0$.

827

Chapitre 14. *Espaces préhilbertiens et euclidiens*

**14.5** Soit $u$ un endomorphisme symétrique d’un espace euclidien $E$.

1. On suppose que $\text{Tr } u = 0$.
   Montrer qu’il existe un vecteur unitaire $\varepsilon_1$ tel que $( u(\varepsilon_1) \mid \varepsilon_1 ) = 0$.
2. Montrer que les deux propositions suivantes sont équivalentes :
   (i) il existe une base orthonormée de $E$ dans laquelle la matrice de $u$ a ses éléments diagonaux nuls,
   (ii) $\text{Tr}(u) = 0$.

**14.6** Sur un espace vectoriel réel $E$ de dimension finie, on considère une norme $\|\cdot\|$ vérifiant l’égalité du parallélogramme c’est-à-dire :
$$\forall(x, y) \in E^2 \quad \|x + y\|^2 + \|x - y\|^2 = 2 \left(\|x\|^2 + \|y\|^2\right).$$
On veut montrer qu’il s’agit d’une norme euclidienne.
On définit l’application $\varphi$ :
$$\begin{aligned} E \times E &\longrightarrow \mathbb{R} \\ (x, y) &\longmapsto \frac{1}{4} \left[ \|x + y\|^2 - \|x - y\|^2 \right]. \end{aligned}$$

1. Soit $(x_1, x_2, y) \in E^3$. Montrer que $\varphi(x_1, y) + \varphi(x_2, y) = \varphi(x_1 + x_2, y)$.
   *On pourra écrire* $x_i + y = (x_i + \frac{y}{2}) + \frac{y}{2}$ *et* $x_i = (x_i + \frac{y}{2}) - \frac{y}{2}$.
2. Soit $(x, y) \in E^2$ et $f : \mathbb{R} \longrightarrow \mathbb{R}$
   $$\lambda \longmapsto \varphi(\lambda x, y) - \lambda \varphi(x, y).$$
   (a) Montrer que $\forall (\lambda_1, \lambda_2) \in \mathbb{R}^2 \quad f(\lambda_1 + \lambda_2) = f(\lambda_1) + f(\lambda_2)$.
   (b) En déduire que $\forall r \in \mathbb{Q} \quad f(r) = 0$.
   (c) Que peut-on en déduire sur la fonction $f$ ?
3. Conclure.

**14.7** 1. Soit deux familles $(x_i)_{1 \le i \le p}$ et $(y_j)_{1 \le j \le p}$ de $p$ vecteurs d’un espace euclidien $E$ de dimension $n$, vérifiant :
$$\forall(*i, j*) \in \llbracket 1, p \rrbracket^2 \quad (x_i \mid x_j) = (y_i \mid y_j).$$
   Montrer qu’il existe une isométrie $u$ de $E$ vérifiant :
$$\forall i \in \llbracket 1, p \rrbracket \quad u(x_i) = y_i.$$
2. En déduire que deux matrices $A$ et $B$ de $\mathcal{M}_{*n,p*}(\mathbb{R})$ vérifient $^*tAA* = ^*tBB*$ si, et seulement s’il existe $Q \in \mathcal{O}_n(\mathbb{R})$ telle que $B = QA$.

828

**_Exercices_**

## **14.8** 1. Montrer que l’application :

$$(f, g) \mapsto (f \mid g) = \int_{-1}^{1} \frac{f(t) g(t)}{\sqrt{1 - t^2}} \mathrm{d}t$$

est un produit scalaire sur $\mathcal{C}([-1, 1], \mathbb{R})$.

2. Montrer que $\mathbb{R}[X]$ est dense dans $\mathcal{C}([-1, 1], \mathbb{R})$ pour la norme associée.
3. Montrer qu’il existe une unique base orthogonale $(Q_n)_{n \in \mathbb{N}}$ de $\mathbb{R}[X]$ telle que, pour tout entier $n$, on ait $\deg(Q_n) = n$ et $Q_n$ de coefficient dominant 1.
4. Déterminer $Q_0$, $Q_1$, $Q_2$ et $Q_3$.
5. Étudier la parité de $Q_n$ en fonction de $n$.
6. Montrer que, pour tout $n \in \mathbb{N}^*$, $Q_n$ admet $n$ racines distinctes dans $]-1, 1[$.
7. Soit $n \in \mathbb{N}^*$.
    (a) Prouver que, pour tout $x \in [-1, 1]$, on a $Q_n(x) = \frac{1}{2^{n-1}} \cos(n \arccos(x))$.
    (b) En déduire $Q_n(1)$ puis que $Q_{n+2} = XQ_{n+1} - \frac{1}{4} Q_n$.
8. Montrer que pour tout entier $n$, le polynôme $(X^2 - 1)Q''_n + XQ'_n$ est colinéaire à $Q_n$. En déduire que $Q_n$ est solution de l’équation différentielle :

$$(X^2 - 1)Q_n'' + XQ_n' - n^2Q_n = 0.$$

9. Soit $n \in \mathbb{N}$ et $g_n : x \mapsto (1 - x^2)^{n-1/2}$.
    (a) Montrer que pour tout $k \in \llbracket 0, n \rrbracket$, il existe un polynôme $R_k$ de degré $k$ tel que :

$$\forall x \in ]-1, 1[ \quad g_n^{(k)} = (1 - x^2)^{n-k-1/2} R_k(x).$$

    (b) Prouver que, pour tout polynôme $P$, on a :

$$(R_n \mid P) = (-1)^n \int_{-1}^1 g_n(t) P^{(n)}(t) \, dt.$$

    (c) En déduire que, pour tout $x \in ]-1, 1[$ on a :

$$Q_n(x) = (-1)^n \frac{(n-1)!}{(2n-1)!} \sqrt{1-x^2} g_n^{(n)}(x).$$

## **14.9** Soit $E$ un espace euclidien. Montrer que le groupe $\mathcal{O}(E)$ des automorphismes orthogonaux est engendré par l’ensemble des réflexions, c’est-à-dire des symétries orthogonales hyperplanes.

## **14.10** *(Polytechnique 2015)*
Soit $A \in \mathcal{GL}_n(\mathbb{R})$. Montrer qu’il existe une base orthonormale $(X_1, \dots, X_n)$ de $\mathbb{R}^n$ telle que $(AX_1, \dots, AX_n)$ soit une base orthogonale.

829

# Chapitre 14. Espaces préhilbertiens et euclidiens

## **14.11** *(Polytechnique 2015)*

Soit $A \in \mathcal{S}_n(\mathbb{R})$. On note $q_A : \begin{matrix} \mathbb{R}^n & \longrightarrow & \mathbb{R} \\ X & \longmapsto & {}^tXAX \end{matrix}$.

Montrer l'équivalence entre :
(i) $\forall X \in \mathbb{R}^n \setminus \{0_{\mathbb{R}^n}\} \quad q_A(X) > 0$;
(ii) toute valeur propre de $A$ est strictement positive ;
(*iii*) $q_A^{-1}(\{1\})$ est un compact non vide.

## **14.12** *(Polytechnique 2015)*

On munit $\mathbb{R}^n$ de sa structure euclidienne usuelle.

1. Soit $X$ un vecteur unitaire de $\mathbb{R}^q$. Déterminer la matrice, dans la base canonique, de la projection orthogonale sur $\text{Vect}(X)$.
2. Soit $X = \begin{pmatrix} X_1 \\ \vdots \\ X_q \end{pmatrix} \in \mathbb{R}^{pq}$ non nul, où $X_1, \dots, X_q$ sont des vecteurs de $\mathbb{R}^p$.
   (a) Donner une écriture par blocs $M = \begin{pmatrix} M_{1,1} & \dots & M_{1,q} \\ \vdots & \ddots & \vdots \\ M_{q,1} & \dots & M_{q,q} \end{pmatrix}$ de la matrice, dans la base canonique, de la projection orthogonale sur $\text{Vect}(X)$.
   (b) Montrer que $S = \sum_{k=1}^q M_{k,k}$ est de trace 1 et que, pour tout $Y \in \mathbb{R}^p$, ${}^tYSY \geq 0$.
3. Réciproquement, soit $S \in \mathcal{S}_p(\mathbb{R})$ de trace 1 telle que, pour tout $Y \in \mathbb{R}^p$, on ait ${}^tYSY \geq 0$.
   Montrer qu'il existe une matrice $M = \begin{pmatrix} M_{1,1} & \dots & M_{1,q} \\ \vdots & \ddots & \vdots \\ M_{q,1} & \dots & M_{q,q} \end{pmatrix}$ représentant une projection orthogonale sur un espace de dimension 1 et telle que $S = \sum_{k=1}^q M_{k,k}$.

## **14.13** Soit $E$ un espace préhilbertien réel.
Une famille de vecteurs $(x_0, \dots, x_p)$ est **obtusangle** si :
$$\forall(*i, j*) \in \llbracket 0, p \rrbracket^2 \quad i \neq j \Rightarrow (x_i \mid x_j) < 0.$$

1. On suppose que la famille $(x_0, \dots, x_p)$ est obtusangle. Prouver que $(x_1, \dots, x_p)$ est libre.
2. En déduire que si $E$ est euclidien de dimension $n$, alors toute famille obtusangle a au plus $n + 1$ vecteurs.

830

*Solution des exercices*

# Solution des exercices

**14.1** 1. Pour tout $(e_1, \dots, e_{n-1}) \in E^{n-1}$, l'application $x \mapsto [e_1, \dots, e_{n-1}, x]$ est une forme linéaire sur $E$. Le théorème de représentation de Riesz implique donc l'existence d'un unique vecteur $e_1 \wedge \dots \wedge e_{n-1}$ de $E$ tel que :
$$\forall x \in E \quad [e_1, \dots, e_{n-1}, x] = (e_1 \wedge \dots \wedge e_{n-1} \mid x).$$

2. Si la famille $(e_1, \dots, e_{n-1})$ est liée, alors, pour tout $x \in E$, il en est de même de la famille $(e_1, \dots, e_{n-1}, x)$ et donc :
$$[e_1, \dots, e_{n-1}, x] = 0 = (0_E \mid x).$$
Par unicité du produit vectoriel, on en déduit que $e_1 \wedge \dots \wedge e_{n-1}$ est nul.
Si la famille $(e_1, \dots, e_{n-1})$ est libre, alors, d'après le théorème de la base incomplète, il existe $e_n \in E$ tel que $(e_1, \dots, e_n)$ soit une base. On a alors :
$$(e_1 \wedge \dots \wedge e_{n-1} \mid e_n) = [e_1, \dots, e_{n-1}, e_n] \neq 0$$
donc $e_1 \wedge \dots \wedge e_{n-1}$ est non nul.

3. Supposons la famille $(e_1, \dots, e_{n-1})$ orthonormale et posons $e_n = e_1 \wedge \dots \wedge e_{n-1}$. Comme on a :
$$\forall k \in \llbracket 1, n - 1 \rrbracket \quad (e_n \mid e_k) = [e_1, \dots, e_{n-1}, e_k] = 0,$$
la famille $(e_1, \dots, e_{n-1}, e_n)$ est orthogonale. De plus :
$$[e_1, \dots, e_{n-1}, e_n] = (e_n \mid e_n) = \|e_n\|^2 \geq 0$$
donc la famille $(e_1, \dots, e_{n-1}, e_n)$ est une base directe. Ainsi, $(e_1, \dots, e_{n-1}, \frac{e_n}{\|e_n\|})$ est une base orthonormale directe. Par conséquent :
$$1 = \left[ e_1, \dots, e_{n-1}, \frac{e_n}{\|e_n\|} \right] = \left( e_n \mid \frac{e_n}{\|e_n\|} \right) = \|e_n\|$$
donc la famille $(e_1, \dots, e_{n-1}, e_n)$ est une base orthonormale directe.

**14.2** 1. Supposons que $E = F \overset{\perp}{\oplus} G$. On a alors $G \subset F^\perp$. Réciproquement, pour tout $x \in F^\perp$, en écrivant $x = f + g$ avec $f \in F$ et $g \in G$, le vecteur $f = x - g$ appartient à $F$ et $F^\perp$ et il est donc nul, ce qui implique que $F^\perp \subset G$.

2. Puisque $E = F \overset{\perp}{\oplus} F^\perp = F^\perp \overset{\perp}{\oplus} F$, la question précédente donne $(F^\perp)^\perp = F$.

**14.3** 1. Soit $(e_1, \dots, e_n)$ une base orthonormée de $E$.
* Si un tel endomorphisme $u^*$ existe, alors :
$$\forall y \in E \quad u^*(y) = \sum_{<sub>i=1</sub>}^n (u^*(y) \mid e_i)e_i = \sum_{<sub>i=1</sub>}^n (u(e_i) \mid y)e_i.$$
Il y a donc unicité (sous réserve d'existence).

831

# Chapitre 14. *Espaces préhilbertiens et euclidiens*

*   Soit $u^* : E \longrightarrow E$
    $$y \longmapsto \sum_{i=1}^n (u(e_i) \mid y)e_i.$$
    L'application $u^*$ est alors un endomorphisme de $E$ et :

$$
\begin{aligned}
\forall(x, y) \in E^2 \quad (x \mid u^*(y)) &= \left( \sum_{i=1}^n (x \mid e_i) e_i \middle| \sum_{j=1}^n (u(e_j) \mid y) e_j \right) \\
&= \sum_{i=1}^n (x \mid e_i) (u(e_i) \mid y) = \left( \sum_{i=1}^n (x \mid e_i) u(e_i) \middle| y \right) \\
&= (u(x) \mid y).
\end{aligned}
$$

    Donc $u^*$ convient.

2. Par définition de $u^*$, on a pour tout $(x, y) \in E^2$ :
   $$(x \mid (u^*)^* (y)) = ( u^*(x) \mid y ) = (y \mid u^*(x) ) = (u(y) \mid x ) = (x \mid u(y) ).$$
   L'unicité de $(u^*)^*$ donne alors $(u^*)^* = u$.

3. Par définition, et du fait de l'unicité de l'adjoint, $u$ est symétrique si, et seulement si, $u^* = u$.

4. Si $u$ est une isométrie, alors $u$ est bijectif et :
   $$\forall(x, y) \in E^2 \quad ( u(x) \mid y ) = ( u(x) \mid u (u^{-1}(y)) ) = (x \mid u^{-1}(y) )$$
   donc $u^* = u^{-1}$. De même, si $u$ est bijectif et si $u^* = u^{-1}$, alors :
   $$\forall(x, y) \in E^2 \quad ( u(x) \mid u(y) ) = (x \mid u^* (u(y)) ) = (x \mid y )$$
   donc $u$ est une isométrie.
   Par conséquent, $u$ est une isométrie si, et seulement si, $u$ est bijectif et si $u^* = u^{-1}$.

5. • Soit $x \in E$, on a :
   $$x \in \text{Ker } u^* \iff u^*(x) = 0 \iff \forall y \in E \quad (u^*(x) \mid y ) = 0$$
   $$\iff \forall y \in E \quad (x \mid u(y) ) = 0$$
   $$\iff x \in (\text{Im } u)^\perp .$$
   Ainsi, $\text{Ker } u^* = (\text{Im } u)^\perp$.
   • Comme $(u^*)^* = u$, en appliquant le résultat précédent à $u^*$, on obtient l'égalité $\text{Ker } u = (\text{Im } u^*)^\perp$. On en déduit $\text{Im } u^* = (\text{Ker } u)^\perp$ car $E$ est de dimension finie.

6. Soit $F$ un sous-espace vectoriel stable par $u$. Soit $y \in F^\perp$. On a, pour tout $x \in F$ :
   $$(u^*(y) \mid x ) = (y \mid u(x)) = 0 \text{ puisque } u(x) \in F \text{ par stabilité de } F.$$
   Donc $u^*(y) \in F^\perp$. Cela prouve que $F^\perp$ est stable par $u^*$.
   • Si $u$ est symétrique, on en déduit directement la stabilité de $F^\perp$ par $u = u^*$.
   • Supposons $u$ orthogonal.
     Alors $F^\perp$ est stable par $u^* = u^{-1}$, donc $F^\perp \subset u(F^\perp)$. Comme $u$ est un isomorphisme, on en déduit $F^\perp = u(F^\perp)$ par égalité des dimensions, donc $F^\perp$ est stable par $u$.

832

***Solution des exercices***

**14.4** 1. Il est clair que $(ii) \Rightarrow (i)$.
Réciproquement, supposons $(i)$ et montrons $(ii)$. Soit $(*x, y*) \in E^2$, on a :
$$(x + y \mid u(x + y)) = 0 = (x \mid u(x)) + (y \mid u(y)) + (x \mid u(y)) + (y \mid u(x))$$
donc $(u(x) \mid y) = -(x \mid u(y))$.

2. • Supposons $(i)$ et $(ii)$ et montrons $(*iii*)$.
Soit $x \in E$. On a :
$$(x \mid u(x)) = (u(x) \mid u^2(x)) = (u(x) \mid -x) = -(x \mid u(x))$$
donc $(x \mid u(x)) = 0$.
• Supposons $(ii)$ et $(*iii*)$ et montrons $(i)$.
Soit $(*x, y*) \in E^2$. En utilisant la question précédente, on a :
$$(x \mid y) = (-u^2(x) \mid y) = (u(x) \mid u(y))$$
donc $u$ est une isométrie.
• Supposons $(i)$ et $(*iii*)$ et montrons $(ii)$.
Soit $(*x, y*) \in E^2$. En utilisant la question précédente, on a :
$$(u^2(x) \mid y) = -(u(x) \mid u(y)) = -(x \mid y) = (-x \mid y)$$
donc $(u^2(x) + x \mid y) = 0$. Ainsi, pour tout $x \in E$, on a $u^2(x) + x = 0$ *i.e. u*$^2 = -\text{Id}$.

**14.5** 1. Soit $A$ la matrice (symétrique) de $u$ dans une base orthonormée $(e_1, \dots, e_n)$.
On a :
$$0 = \text{Tr } u = \sum_{<sub>i=1</sub>}^n (u(e_i) \mid e_i).$$
• S’il existe $i \in [\![1, n]\!]$ tel que $(u(e_i) \mid e_i) = 0$, alors il suffit de prendre $\varepsilon_1 = e_i$.
• Sinon, il existe $(*i, j*) \in [\![1, n]\!]^2$ tel que $(u(e_i) \mid e_i) < 0 < (u(e_j) \mid e_j)$.
Pour tout réel $t$, on pose $e(t) = (1 - t)e_i + te_j$. La fonction $t \mapsto (u(e(t)) \mid e(t))$ est alors polynomiale, négative en 0 et positive en 1. Il existe donc un réel $t_0$ tel que le vecteur $e(t_0)$ vérifie $(u(e(t_0)) \mid e(t_0)) = 0$. Les vecteurs $e_i$ et $e_j$ étant non colinéaires, le vecteur $e(t_0)$ est non nul. Par conséquent, le vecteur $\varepsilon_1 = \frac{e(t_0)}{\|e(t_0)\|}$ convient.

2. L’une des implications est triviale. Montrons l’autre par récurrence sur la dimension $n$ de $E$. C’est clair pour $n = 1$. Soit $n \geqslant 2$. Supposons le résultat acquis pour $n - 1$ et démontrons-le pour $n$.
D’après la question précédente, il existe un vecteur unitaire $\varepsilon_1$ tel que $(u(\varepsilon_1) \mid \varepsilon_1) = 0$. Complétons $\varepsilon_1$ en une base orthonormée $(\varepsilon_1, \dots, \varepsilon_n)$. La matrice de $u$ dans cette base est alors :
$$A = \begin{pmatrix} 0 & * & \dots & * \\ * & & & \\ \vdots & & B & \\ * & & & \end{pmatrix} \quad \text{avec} \quad B = ((u(\varepsilon_j) \mid \varepsilon_i))_{2 \leqslant i,j \leqslant n} \in \mathcal{S}_{n-1}(\mathbb{R}).$$

833

Chapitre 14. *Espaces préhilbertiens et euclidiens*

Comme $u$ est de trace nulle, la matrice $B$ l’est également. D’après l’hypothèse de récurrence il existe donc une matrice $P \in \mathcal{O}_{n-1}(\mathbb{R})$ telle que $^*tPBP*$ ait tous ses éléments diagonaux nuls. Il suffit alors de poser

er $Q = \begin{pmatrix} 1 & 0 & \dots & 0 \\ 0 & & & \\ \vdots & & P & \\ 0 & & & \end{pmatrix}$

pour avoir :

$$Q \in \mathcal{O}_n(\mathbb{R}) \quad \text{et} \quad ^*tQAQ* \text{ de diagonale nulle.}$$

Il existe donc une base orthonormée de $E$ dans laquelle la matrice de $u$ a ses éléments diagonaux nuls.

**14.6** 1. On pose :

$$A = 4(\varphi(x_1, y) + \varphi(x_2, y)) = \|x_1 + y\|^2 - \|x_1 - y\|^2 + \|x_2 + y\|^2 - \|x_2 - y\|^2.$$

L'égalité du parallélogramme donne :

$$\|x_1 + y\|^2 + \|x_1\|^2 = 2 \left\|x_1 + \frac{y}{2}\right\|^2 + 2 \left\|\frac{y}{2}\right\|^2$$

et :

$$\|x_1 - y\|^2 + \|x_1\|^2 = 2 \left\|x_1 - \frac{y}{2}\right\|^2 + 2 \left\|\frac{y}{2}\right\|^2.$$

Le résultat est similaire pour $x_2$, et l'on obtient donc :

$$A = 2 \left\|x_1 + \frac{y}{2}\right\|^2 + 2 \left\|x_2 + \frac{y}{2}\right\|^2 - 2 \left\|x_1 - \frac{y}{2}\right\|^2 - 2 \left\|x_2 - \frac{y}{2}\right\|^2.$$

En utilisant à nouveau l’égalité du parallélogramme, cela donne alors :

$$A = \|x_1 + x_2 + y\|^2 + \|x_1 - x_2\|^2 - \left( \|x_1 + x_2 - y\|^2 + \|x_1 - x_2\|^2 \right)$$

et donc $\varphi(x_1, y) + \varphi(x_2, y) = \varphi(x_1 + x_2, y)$.

2. (a) La question précédente donne directement le résultat.
   (b) Par récurrence sur $n \in \mathbb{N}$, on montre alors facilement que pour tout $\lambda \in \mathbb{R}$, on a $f(n\lambda) = nf(\lambda)$.
       Comme $f(1) = 0$, on a donc $\forall n \in \mathbb{N} \quad f(n) = 0$.
       De plus, pour tout $n \in \mathbb{N}$, $f(n) + f(-n) = f(0) = 0$ donc $\forall n \in \mathbb{Z} \quad f(n) = 0$.
       Soit $r \in \mathbb{Q}$, il existe $(*p, q*) \in \mathbb{Z} \times \mathbb{N}^*$ tel que $r = \frac{p}{q}$, ce qui donne, d’après ce qui précède :
       $$0 = f(p) = f(qr) = qf(r) \quad \text{donc} \quad f(r) = 0.$$
   (c) La fonction $f$ est continue car la norme est continue (comme $E$ est de dimension finie, on peut choisir n’importe quelle norme, en particulier celle qui nous est donnée). Ainsi, par densité des rationnels, on en déduit que $f$ est la fonction nulle.

3. Soit $(*x, y*) \in E^2$. On a $\|x - y\| = \|y - x\|$ donc $\varphi(*y, x*) = \varphi(*x, y*)$.
   - Les questions précédentes prouvent la linéarité à gauche de $\varphi$ et donc sa bilinéarité par symétrie.

834

**_Solution des exercices_**

*   Enfin, pour tout $x \in E$, on a $\varphi(x, x) = \|x\|^2 \geqslant 0$ avec donc égalité si, et seulement si, $x = 0$.

Ainsi, $\varphi$ est un produit scalaire sur $E$ et la norme associée à $\varphi$ est $\|\ \|$; ce qui prouve que $\|\ \|$ est une norme euclidienne sur $E$.

**14.7** 1. Soit $V$ l'espace vectoriel engendré par les $(x_i)_{1 \leqslant i \leqslant p}$ et $d$ sa dimension. Quitte à réindexer, on peut supposer que la famille $(x_i)_{1 \leqslant i \leqslant d}$ est une base de $V$.

*   Montrons que $(y_i)_{1 \leqslant i \leqslant d}$ est une base de $W$, l'espace vectoriel engendré par les $(y_i)_{1 \leqslant i \leqslant p}$.
    Pour tout $(\lambda_i)_{1 \leqslant i \leqslant d} \in \mathbb{R}^d$, on a :
    $$\left\| \sum_{i=1}^d \lambda_i y_i \right\|^2 = \left( \sum_{i=1}^d \lambda_i y_i \middle| \sum_{i=1}^d \lambda_i y_i \right) = \left( \sum_{i=1}^d \lambda_i x_i \middle| \sum_{i=1}^d \lambda_i x_i \right) = \left\| \sum_{i=1}^d \lambda_i x_i \right\|^2$$
    donc la liberté de la famille $(y_i)_{1 \leqslant i \leqslant d}$ découle de celle de la famille $(x_i)_{1 \leqslant i \leqslant d}$.
    On démontre exactement de la même manière qu'une égalité de la forme $x_i - \sum_{k=1}^d \lambda_k x_k = 0$ implique $y_i - \sum_{k=1}^d \lambda_k y_k = 0$; ce qui prouve que la famille $(y_i)_{1 \leqslant i \leqslant d}$ engendre $W$. Il s'agit donc d'une base de $W$ qui est donc de dimension $d$.

*   Considérons une base orthonormée $(x'_{d+1}, \dots, x'_n)$ de $V^\perp$, une base orthonormée $(y'_{d+1}, \dots, y'_n)$ de $W^\perp$ ainsi que l'endomorphisme $u$ défini par :
    $$\forall i \in \llbracket 1, d \rrbracket \quad u(x_i) = y_i \qquad \text{et} \qquad \forall i \in \llbracket d+1, n \rrbracket \quad u(x'_i) = y'_i.$$
    On a pour tout $i \in \llbracket 1, p \rrbracket$, $u(x_i) = y_i$ car si $x_i = \sum_{k=1}^d \lambda_k x_k$ alors $y_i = \sum_{k=1}^d \lambda_k y_k$.
    On a déjà prouvé que pour tout $x \in V$, $\|u(x)\| = \|x\|$. Par définition, $u$ transforme une base orthonormée de $V^\perp$ en une base orthonormée donc, pour tout $x' \in V^\perp$, on a $\|u(x')\| = \|x'\|$.
    Pour tout $(*x, x*') \in V \times V^\perp$, on a $(u(x), u(x')) \in W \times W^\perp$ donc, en utilisant le théorème de Pythagore, on a :
    $$\|u(x + x')\|^2 = \|u(x)\|^2 + \|u(x')\|^2 = \|x\|^2 + \|x'\|^2 = \|x + x'\|^2,$$
    ce qui prouve que $u$ est une isométrie.

2. Soit $(x_i)_{1 \leqslant i \leqslant p}$ et $(y_i)_{1 \leqslant i \leqslant p}$ les vecteurs colonnes de $A$ et $B$. L'égalité $^tAA = {}^*tBB*$ donne, pour tout $(*i, j*) \in \llbracket 1, p \rrbracket^2$, $(x_i \mid x_j) = (y_i \mid y_j)$ où $(\ \mid \ )$ est le produit scalaire canonique de $\mathbb{R}^n$. On peut donc appliquer le résultat ci-dessus. La matrice $Q$ de $u$ dans la base canonique de $\mathbb{R}^n$ vérifie l'égalité $B = QA$ qui traduit les égalités $y_i = u(x_i)$. Une telle matrice est orthogonale comme matrice d'une isométrie.
Inversement, une égalité de la forme $B = QA$ avec $^*tQQ* = I_n$ donne :
$${}^*tBB* = {}^tA {}^tQQA = {}^tAA.$$

835

Chapitre 14. Espaces préhilbertiens et euclidiens

**14.8** 1. Commençons par prouver que l'application est bien définie.

Soit $(f, g) \in \mathcal{C}([-1, 1], \mathbb{R})^2$. La fonction $h : t \mapsto \frac{f(t)g(t)}{\sqrt{1-t^2}}$ est continue sur $]-1, 1[$. De plus, au voisinage de 1, on a $\frac{f(t)g(t)}{\sqrt{1-t^2}} = O\left(\frac{1}{\sqrt{1-t}}\right)$, le critère de Riemann implique donc que $h$ est intégrable sur $[0, 1[$. De même on montre qu'elle l'est sur $]-1, 0]$. Ainsi, l'intégrale $\int_{-1}^1 \frac{f(t)g(t)}{\sqrt{1-t^2}} dt$ existe.

Il est clair que l'application $(f, g) \mapsto (f \mid g)$ est bilinéaire symétrique et que $(f \mid f) \geqslant 0$ pour tout $f \in \mathcal{C}([-1, 1], \mathbb{R})$.

Soit $f \in \mathcal{C}([-1, 1], \mathbb{R})$ telle que $(f \mid f) = 0$. La fonction $h : t \mapsto \frac{f^2(t)}{\sqrt{1-t^2}}$ est continue sur $]-1, 1[$, positive et d'intégrale nulle, donc nulle sur $]-1, 1[$. Par conséquent, la fonction $f$ est nulle sur $]-1, 1[$ puis sur $[-1, 1]$ par continuité. Ainsi, l'application $(f, g) \mapsto (f \mid g)$ est un produit scalaire sur $\mathcal{C}([-1, 1], \mathbb{R})$.

2. Soit $f \in \mathcal{C}([-1, 1], \mathbb{R})$. D'après le théorème de densité de Weierstrass, il existe une suite de fonctions polynomiales $(p_n)_{n \in \mathbb{N}}$ convergeant uniformément vers $f$ sur le segment $[-1, 1]$. La majoration :

$$ \|f - p_n\| = \left( \int_{-1}^1 \frac{(f - p_n)^2}{\sqrt{1-t^2}} \right)^{1/2} \leqslant \left( \int_{-1}^1 \frac{1}{\sqrt{1-t^2}} \right)^{1/2} \|f - p_n\|_\infty $$

prouve que la suite $(p_n)_{n \in \mathbb{N}}$ converge vers $f$ au sens de la norme euclidienne associée au produit scalaire $(f, g) \mapsto (f \mid g) = \int_{-1}^1 \frac{f(t)g(t)}{\sqrt{1-t^2}} dt$.

3. En appliquant le procédé d'orthogonalisation de Schmidt à la base canonique de $\mathbb{R}[X]$, c'est-à-dire en posant $Q_0 = 1$ et :

$$ \forall n \in \mathbb{N}^* \quad Q_n = X^n - \sum_{<sub>k=0</sub>}^{n-1} \frac{(X^n \mid Q_k)}{\|Q_k\|^2} Q_k $$

on obtient une base orthogonale telle que, pour tout entier $n$, on ait $\deg(Q_n) = n$ et $Q_n$ de coefficient dominant 1.

Supposons qu'il en existe une autre notée $(\tilde{Q}_n)_{n \in \mathbb{N}}$. Montrons, par récurrence forte que, pour tout entier $n$, on a $\tilde{Q}_n = Q_n$.

Par hypothèse, $\tilde{Q}_0$ est constant et de coefficient dominant 1 donc $\tilde{Q}_0 = 1 = Q_0$. Supposons que pour un certain entier $n \in \mathbb{N}$, on ait :

$$ \forall k \in \llbracket 0, n-1 \rrbracket \quad \tilde{Q}_k = Q_k. $$

Par hypothèse, le polynôme $\tilde{Q}_n - Q_n$ appartient à $\mathbb{R}_{n-1}[X] = \text{Vect}(Q_0, \dots, Q_{n-1})$. De plus :

$$ \forall k \in \llbracket 0, n-1 \rrbracket \quad (\tilde{Q}_n - Q_n \mid Q_k) = (\tilde{Q}_n \mid Q_k) = (\tilde{Q}_n \mid \tilde{Q}_k) = 0 $$

donc le polynôme $\tilde{Q}_n - Q_n$ est nul.

836

**Solution des exercices**

4. On a $Q_0 = 1$. On cherche $Q_1$ de la forme $X + a$ de sorte que $(Q_1 \mid 1) = 0$.
   Comme :
   $$(Q_1 \mid 1) = \left[ -\sqrt{1 - t^2} - a \arccos t \right]_{-1}^1 = \pi a = 0,$$
   l'on obtient $Q_1 = X$.
   On cherche $Q_2$ de la forme $X^2 + aX + b$ de sorte que $(Q_2 \mid 1) = (Q_2 \mid X) = 0$.
   Or :
   $$(Q_2 \mid 1) = \int_{-1}^1 \frac{t^2 + at + b}{\sqrt{1 - t^2}} dt = \int_{-1}^1 \frac{t^2}{\sqrt{1 - t^2}} dt + \pi a$$
   et le changement de variable $t = \cos u$ donne :
   $$\int_{-1}^1 \frac{t^2}{\sqrt{1 - t^2}} dt = \int_0^\pi \frac{\cos^2 u}{\sqrt{1 - \cos^2 u}} \sin u \, du = \int_0^\pi \frac{1 + \cos(2u)}{2} du = \pi/2$$
   donc $a = -\frac{1}{2}$. Comme $(Q_2 \mid X) = \int_{-1}^1 \frac{t^3 + at^2 + bt}{\sqrt{1 - t^2}} dt = \int_{-1}^1 \frac{at^2}{\sqrt{1 - t^2}} dt$, l'on obtient $Q_2 = X^2 - \frac{1}{2}$.
   On cherche $Q_3$ de la forme $X^3 + aX^2 + bX + c$ de sorte que :
   $$(Q_3 \mid 1) = (Q_3 \mid X) = (Q_3 \mid X^2) = 0.$$
   Or, $(Q_3 \mid 1) = \int_{-1}^1 \frac{t^3 + at^2 + bt + c}{\sqrt{1 - t^2}} dt = \frac{\pi}{2} a + \pi c$ donc $a = -2c$.
   D'autre part, $(Q_3 \mid X) = \int_{-1}^1 \frac{t^4 + at^3 + bt^2 + ct}{\sqrt{1 - t^2}} dt = \int_{-1}^1 \frac{t^4}{\sqrt{1 - t^2}} dt + \frac{\pi}{2} b$ et le changement de variable $t = \cos u$ donne :
   $$\int_{-1}^1 \frac{t^4}{\sqrt{1 - t^2}} dt = \int_0^\pi \frac{\cos^4 u}{\sqrt{1 - \cos^2 u}} \sin u \, du = \int_0^\pi \frac{3 + 4 \cos(2u) + \cos(4u)}{8} du = \frac{3\pi}{8}$$
   donc $b = -\frac{3}{4}$.
   Enfin, $(Q_3 \mid X^2) = \int_{-1}^1 \frac{t^5 + at^4 + bt^3 + ct^2}{\sqrt{1 - t^2}} dt = \frac{3\pi}{8} a + \frac{\pi}{2} c$ donc $a = c = 0$.
   Ainsi $Q_3 = X^3 - \frac{3}{4} X$.

5. Soit $n \in \mathbb{N}$. Montrons que le polynôme $Q_n$ est de même parité que $n$, c'est-à-dire que $Q_n(X) = (-1)^n Q_n(-X)$.
   Comme $Q_n$ est de degré $n$, le polynôme $\tilde{Q}_n(X) = (-1)^n Q_n(-X)$ est de degré $n$ et de coefficient dominant 1. Il suffit donc, par unicité, de montrer que $(\tilde{Q}_n)_{n \in \mathbb{N}}$ est une famille orthogonale, c'est-à-dire que $\tilde{Q}_n$ est orthogonal à $\mathbb{R}_{n-1}[X]$ pour tout $n \in \mathbb{N}^*$.
   Soit $n \in \mathbb{N}^*$ et $P \in \mathbb{R}_{n-1}[X]$. On a :
   $$\int_{-1}^1 \frac{\tilde{Q}_n(t) P(t)}{\sqrt{1 - t^2}} dt = (-1)^n \int_{-1}^1 \frac{Q_n(-t) P(t)}{\sqrt{1 - t^2}} dt = (-1)^n \int_{-1}^1 \frac{Q_n(t) P(-t)}{\sqrt{1 - t^2}} dt = 0,$$

837

**Chapitre 14. *Espaces préhilbertiens et euclidiens***

les deux dernières égalités provenant du changement de variable $t \mapsto -t$ et du fait que $P(-X) \in \mathbb{R}_{n-1}[X]$ est orthogonal à $Q_n$.

6. Si $Q_n$ ne possède pas $n$ racines simples dans l'intervalle $]-1, 1[$, alors le polynôme $R = \prod_{a \in S} (X - a)$ où $S$ est l'ensemble des racines de $Q_n$ appartenant à l'intervalle $]-1, 1[$ et d'ordre impair, appartient à $\mathbb{R}_{n-1}[X] = \text{Vect}(Q_0, \dots, Q_{n-1})$. En particulier, on a $(Q_n \mid R) = 0$ c'est-à-dire $\int_{-1}^1 \frac{Q_n(t) R(t)}{\sqrt{1-t^2}} dt = 0$.

   Or, la fonction $t \mapsto \frac{Q_n(t) R(t)}{\sqrt{1-t^2}}$ est continue et de signe constant $]-1, 1[$. En effet, les racines de $Q_n R$ appartenant à l'intervalle $]-1, 1[$ sont de multiplicité paire donc la fonction $t \mapsto Q_n(t) R(t)$ est de signe constant sur $]-1, 1[$. Par conséquent, le polynôme $Q_n R$ possède une infinité de racines ; il est donc nul. Comme il est de degré supérieur à $n$, on aboutit à une contradiction ; ce qui prouve que le polynôme $Q_n$ possède $n$ racines simples dans l'intervalle $]-1, 1[$.

7. (a) Commençons par prouver que la fonction $f_n : x \mapsto \cos(n \text{Arccos}(x))$ est polynomiale.
   Soit $\theta \in \mathbb{R}$, on a :
   $$
   \begin{aligned}
   \cos(n\theta) &= \text{Re}\left((\cos \theta + i \sin \theta)^n\right) \\
   &= \text{Re}\left(\sum_{k=0}^n \binom{n}{k} i^k \sin^k(\theta) \cos^{n-k}(\theta)\right) \\
   &= \sum_{p=0}^{\lfloor n/2 \rfloor} \binom{n}{2p} (-1)^p \sin^{2p}(\theta) \cos^{n-2p}(\theta) \\
   &= \sum_{p=0}^{\lfloor n/2 \rfloor} \binom{n}{2p} (-1)^p (1 - \cos^2 \theta)^p \cos^{n-2p}(\theta).
   \end{aligned}
   $$

   Ainsi, pour tout $x \in [-1, 1]$, on a :
   $$f_n(x) = \sum_{p=0}^{\lfloor n/2 \rfloor} \binom{n}{2p} (-1)^p (1 - x^2)^p x^{n-2p}.$$

   Par conséquent, $f_n$ est une fonction polynomiale. Pour tout entier $p$ inférieur ou égal à $\lfloor n/2 \rfloor$, la fonction $x \mapsto \binom{n}{2p} (-1)^p (1 - x^2)^p x^{n-2p}$ est polynomiale de degré $n$ et de coefficient dominant $\binom{n}{2p}$. Montrons que $\sum_{p=0}^{\lfloor n/2 \rfloor} \binom{n}{2p} = 2^{n-1}$.

   Pour cela, on pose :
   $$S_1 = \sum_{\substack{k=0 \\ k \text{ impair}}}^n \binom{n}{k} \quad \text{et} \quad S_2 = \sum_{\substack{k=0 \\ k \text{ pair}}}^n \binom{n}{k}.$$

   On a $S_1 + S_2 = \sum_{k=0}^n \binom{n}{k} = 2^n$ et $-S_1 + S_2 = \sum_{k=0}^n \binom{n}{k} (-1)^k = (1 - 1)^n = 0$

838

**Solution des exercices**

(car $n > 0$). Par suite, $f_n$ est une fonction polynomiale de degré $n$ et de coefficient dominant $2^{n-1}$.
Il reste à montrer que les fonctions $f_k$ sont orthogonales ce qui permettra de conclure grâce à l'unicité.
Soit $(p, q) \in \mathbb{N}^2$, on a :
$$(f_p \mid f_q) = \int_{-1}^{1} \frac{\cos(p \arccos(x)) \cos(q \arccos(x))}{\sqrt{1 - x^2}} dx$$
et en effectuant le changement de variable $x = \cos u$, on obtient :
$$(f_p \mid f_q) = \int_{0}^{\pi} \frac{\cos(pu) \cos(qu)}{\sqrt{\sin^2 u}} \sin u \, du = \int_{0}^{\pi} \cos(pu) \cos(qu) \, du.$$
La formule trigonométrique :
$$2 \cos(pu) \cos(qu) = \cos((p + q)u) + \cos((p - q)u)$$
conduit alors à $(f_p \mid f_q) = 0$ si $p \neq q$.
Par suite, on a prouvé que, pour tout $x \in [-1, 1]$,
$$Q_n(x) = \frac{1}{2^{n-1}} \cos(n \arccos(x)).$$

(b) On a $Q_n(1) = \frac{1}{2^{n-1}} \cos(n \arccos(1)) = \frac{1}{2^{n-1}}$.
Le polynôme $Q_{n+2} - X Q_{n+1}$ appartient à $\mathbb{R}_{n+1}[X] = \text{Vect}(Q_0, \dots, Q_{n+1})$.
De plus :
$$\forall k \in \llbracket 0, n - 1 \rrbracket \quad (Q_{n+2} - X Q_{n+1} \mid Q_k) = -(Q_{n+1} \mid X Q_k) = 0$$
car $Q_{n+1}$ est orthogonal à $\text{Vect}(Q_0, \dots, Q_n) = \mathbb{R}_n[X]$.
On en déduit que $Q_{n+2} - X Q_{n+1}$ est une combinaison linéaire des polynômes $Q_{n+1}$ et $Q_n$. Pour des raisons de parité, il est donc colinéaire à $Q_n$. Il existe donc un réel $\lambda_n$ tel que $Q_{n+2} = X Q_{n+1} + \lambda_n Q_n$. En évaluant cette relation en 1, on obtient $\frac{1}{2^{n+1}} = \frac{1}{2^n} + \lambda_n \frac{1}{2^{n-1}}$ donc $\lambda_n = -\frac{1}{4}$.

8. Le polynôme $(X^2 - 1)Q''_n + X Q'_n$ appartient à $\mathbb{R}_n[X] = \text{Vect}(Q_0, \dots, Q_n)$.
Montrons que, pour tout $k \in \llbracket 0, n - 1 \rrbracket$, on a $((X^2 - 1)Q''_n + X Q'_n \mid Q_k) = 0$, ce qui permettra de conclure.
Pour tout polynôme $R$, la fonction $t \mapsto \frac{R(t)}{\sqrt{1 - t^2}} = \frac{R(t)}{\sqrt{1 + t}\sqrt{1 - t}}$ est intégrable sur $]-1, 1[$, ce qui justifie toutes les intégrations par parties qui suivent.
Soit $k \in \llbracket 0, n - 1 \rrbracket$, une intégration par parties donne :
$$
\begin{aligned}
((X^2 - 1)Q''_n \mid Q_k) &= - \int_{-1}^{1} \sqrt{1 - t^2} Q''_n(t) Q_k(t) \, dt \\
&= \int_{-1}^{1} Q'_n(t) \left( \sqrt{1 - t^2} Q'_k(t) - \frac{t}{\sqrt{1 - t^2}} Q_k(t) \right) dt \\
&= \int_{-1}^{1} Q'_n(t) \sqrt{1 - t^2} Q'_k(t) \, dt - (X Q'_n \mid Q_k).
\end{aligned}
$$

839

Chapitre 14. *Espaces préhilbertiens et euclidiens*

Or, une autre intégration par parties donne :

$$
\begin{aligned}
\int_{-1}^{1} Q_n'(t) \sqrt{1 - t^2} Q_k'(t) \, \mathrm{d}t &= -\int_{-1}^{1} Q_n(t) \left( \sqrt{1 - t^2} Q_k''(t) - \frac{t}{\sqrt{1 - t^2}} Q_k'(t) \right) \\
&= (Q_n \mid (X^2 - 1)Q_k'' + XQ_k') .
\end{aligned}
$$

Cette dernière quantité est nulle car le polynôme $(X^2 - 1)Q_k'' + XQ_k'$ appartient à $\mathbb{R}_k[X] = \text{Vect}(Q_0, \dots, Q_k)$.

Ainsi, pour tout $k \in [\![0, n - 1]\!]$, on a $((X^2 - 1)Q_n'' + XQ_n' \mid Q_k) = 0$.

Comme $(X^2 - 1)Q_n'' + XQ_n'$ appartient à $\mathbb{R}_n[X]$, cela assure l'existence d'un réel $\lambda_n$ tel que $(X^2 - 1)Q_n'' + XQ_n' = \lambda_n Q_n$. Le coefficient dominant de $(X^2 - 1)Q_n'' + XQ_n'$ est égal à $n^2$. Par conséquent, $Q_n$ est solution de l'équation différentielle :

$$(X^2 - 1)Q_n'' + XQ_n' - n^2 Q_n = 0.$$

9. (a) Pour tout $k \in [\![0, n]\!]$, on note $H(k)$ l'assertion :
   « il existe un polynôme $R_k \in \mathbb{R}[X]$ tel que :
   $$\deg R_k = k \quad \text{et} \quad \forall x \in ]-1, 1[, \ g_n^{(k)}(x) = (1 - x^2)^{n-k-\frac{1}{2}} R_k(x). \ »$$

   * L'assertion $H(0)$ est vraie car il suffit de prendre $R_0 = 1$.
   * Supposons $H(k)$ vraie pour un certain $k \in [\![0, n - 1]\!]$.
     Comme $g_n$ est de classe $\mathcal{C}^\infty$, pour tout $x \in ]-1, 1[$, on a :

$$g_n^{(k+1)}(x) = (1 - x^2)^{n-k-\frac{1}{2}} R'_k(x) - 2 \left( n - k - \frac{1}{2} \right) (1 - x^2)^{n-k-1-\frac{1}{2}} x R_k(x).$$

   Il suffit donc de poser $R_{k+1} = (1 - X^2)R_k' - (2n - 2k - 1)XR_k$.
   Si l'on note $a_k$ le coefficient dominant de $R_k$, alors $R_{k+1}$ est de degré inférieur ou égal à $k+1$ et le coefficient devant $X^{k+1}$ vaut $-(2n - k - 1)a_k \neq 0$.

   On a donc montré $H(k)$, pour tout $k \in [\![0, n]\!]$.

(b) Soit $P$ un polynôme. On a :
$$(R_n \mid P) = \int_{-1}^1 g_n^{(n)}(t) P(t) \, dt.$$

Pour tout $t \in ]-1, 1[$, on a $g_n^{(n-1)}(t) P(t) = (1 - t^2)^{\frac{1}{2}} R_{n-1}(t) P(t)$ donc la fonction $t \mapsto g_n^{(n-1)}(t) P(t)$ se prolonge par continuité par zéro en $1$ et $-1$. Une intégration par parties mène alors à :
$$(R_n \mid P) = - \int_{-1}^1 g_n^{(n-1)}(t) P'(t) \, dt.$$

En réitérant le raisonnement, on arrive à :
$$(R_n \mid P) = (-1)^n \int_{-1}^1 g_n(t) P^{(n)}(t) \, dt.$$

(c) Pour tout $n \in \mathbb{N}$, le polynôme $R_n$ est de degré $n$ donc, d'après ce qui précède, orthogonal à $R_0, \dots, R_{n-1}$. Cela prouve que la famille $(R_n)_{n \in \mathbb{N}}$ est orthogonale. Si l'on note $a_n$ le coefficient dominant de $R_n$, on a alors $Q_n = \frac{1}{a_n} R_n$.

840

***Solution des exercices***

Comme on a prouvé que pour tout $k$, $a_{k+1} = -(2n - k - 1)a_k$, on a :

$$a_n = (-1)^n \prod_{k=1}^n (2n - k) = (-1)^n \frac{(2n - 1)!}{(n - 1)!}.$$

Ainsi, pour tout $x \in ]-1, 1[$ on a $Q_n(x) = (-1)^n \frac{(n - 1)!}{(2n - 1)!} \sqrt{1 - x^2} g_n^{(n)}(x)$.

**14.9** Soit $u \in \mathcal{O}(E)$. D'après le théorème 30 de la page 812, il existe un base orthonormale $\mathcal{B}$ de $E$ dans laquelle la matrice $U$ de $u$ est diagonale par blocs :
* de taille 1 de la forme $(\gamma)$ avec $\gamma \in \{-1, 1\}$ ;
* de taille 2 et de la forme :
$$\begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix} \quad \text{avec} \quad \theta \in \mathbb{R}.$$

Remarquons que, pour tout $i \in \llbracket 1, n \rrbracket$, la matrice diagonale $D_i$ dont les éléments diagonaux sont tous égaux à 1 sauf celui d'indice $i$ égal à $-1$, est la matrice dans $\mathcal{B}$ d'une réflexion (réflexion par rapport à l'hyperplan orthogonal au $i$-ème vecteur). En multipliant $U$ à droite par de telles matrices $D_i$, on peut changer en son opposée la deuxième colonne de tous les blocs de taille 2, et l'on obtient ainsi une matrice $V$ diagonale par blocs :
* de taille 1 de la forme $(\gamma)$ avec $\gamma \in \{-1, 1\}$ ;
* de taille 2 et de la forme :
$$\begin{pmatrix} \cos \theta & \sin \theta \\ \sin \theta & -\cos \theta \end{pmatrix} \quad \text{avec} \quad \theta \in \mathbb{R}.$$

Cette matrice est symétrique et orthogonale, donc c'est la matrice dans $\mathcal{B}$ d'une isométrie $v$ symétrique. Il existe donc un base orthonormale $\mathcal{B}'$ dans laquelle la matrice de $v$ est une matrice diagonale ($v$ est symétrique), avec des élément diagonaux sont tous égaux à $\pm 1$ ($v$ est une isométrie). Une telle matrice est évidemment un produit de matrices $D_i$, donc $v$ est une composée de réflexions. Or, par construction, $v$ est la composée de $u$ par des réflexions de matrices $D_i$ dans la base $\mathcal{B}$, donc $u$ est la composée de $v$ par des réflexions.

Finalement, $u$ est bien une composée de réflexions.

**14.10** La matrice $^*tAA*$ est symétrique réelle donc diagonalisable en base orthonormée.

Soit $(X_1, \dots, X_n)$ une base orthonormée de diagonalisation de $^*tAA*$.

Pour tout $(*i, j*) \in \llbracket 1, n \rrbracket^2$, on a $^t(AX_i)AX_j = {}^tX_i {}^tAAX_j$. Comme il existe un réel $\lambda_j$ tel que $^tAAX_j = \lambda_j X_j$, on en déduit que si $i \neq j$, alors :

$${}^t(AX_i)AX_j = {}^tX_i (\lambda_j X_j) = \lambda_j {}^tX_i X_j = 0$$

car la famille $(X_1, \dots, X_n)$ est orthogonale.

Enfin, comme image d'une base par une matrice inversible, la famille $(AX_1, \dots, AX_n)$ est une base

841

Chapitre 14. Espaces préhilbertiens et euclidiens

**14.11** La matrice $A$ est symétrique réelle, donc diagonalisable dans un base orthonormale. Notons $\lambda_1 \leqslant \dots \leqslant \lambda_n$ ses valeurs propres et $(E_1, \dots, E_n)$ une base orthonormale telle que $\forall i \in [\![1, n]\!]$ $AE_i = \lambda_i E_i$.

Soit $X = \sum_{i=1}^n x_i E_i \in \mathbb{R}^n$. On a $AX = \sum_{i=1}^n \lambda_i x_i E_i$ et donc $q_A(X) = \sum_{i=1}^n \lambda_i x_i^2$. On en déduit :
$$\lambda_1 \sum_{i=1}^n x_i^2 \leqslant q_A(X) \leqslant \lambda_n \sum_{i=1}^n x_i^2. \tag{*}$$

En particulier, pour tout $X \in \mathbb{R}^n$, on a $q_A(X) \geqslant \lambda_1 \|X\|^2$, et il y a égalité lorsque $X = E_1 \neq 0$.

* La minoration précédente prouve l'implication $(ii) \Rightarrow (i)$ et le cas d'égalité la réciproque $(i) \Rightarrow (ii)$.
* Supposons $(ii)$ et montrons $(iii)$.
  Comme $q_A$ est continue (fonction polynomiale), $q_A^{-1}(\{1\})$ est un fermé.
  D'autre part, pour tout $X \in q_A^{-1}(\{1\})$, on a :
  $$1 = q_A(X) \geqslant \lambda_1 \|X\|^2.$$
  Puisque $\lambda_1 > 0$, on en déduit que $q_A^{-1}(\{1\})$ est borné par $\frac{1}{\sqrt{\lambda_1}}$.
  Comme $\mathbb{R}^n$ est de dimension finie, on en déduit que $q_A^{-1}(\{1\})$ est compact.
* Montrons $(iii) \Rightarrow (i)$ par contraposition. Supposons $\lambda_1 \leqslant 0$.
  * Si $\lambda_n \leqslant 0$, l'encadrement (*) montre que $q_A^{-1}(\{1\})$ est vide.
  * Sinon, considérons le vecteur $X = x_1 E_1 + x_n E_n$, avec $(x_1, x_n) \in \mathbb{R}^2$. On a $q_A(X) = \lambda_1 x_1^2 + \lambda_n x_n^2$ et donc :
    $$q_A(X) = 1 \iff x_n^2 = \frac{1 - \lambda_1 x_1^2}{\lambda_n}.$$
    Pour $k \in \mathbb{N}$, les vecteurs $k E_1 + \sqrt{\frac{1 - \lambda_1 k^2}{\lambda_n}} E_n$ (bien définis puisque l'on a supposé $\lambda_1 \leqslant 0 < \lambda_n$) constituent une suite de $q_A^{-1}(\{1\})$, non bornée car leurs composantes suivant $E_1$ forment une suite non bornée.
    Donc $q_A^{-1}(\{1\})$ est non compact.

**14.12** 1. Comme $X$ est unitaire, la projection orthogonale sur $\text{Vect}(X)$ d'un vecteur $Y$ est $(X | Y)X$. Or :
$$(X | Y)X = X((X | Y)I_1) = X((^*tXY*)I_1) = X(^*tXY*) = (X^tX)Y.$$
Donc la matrice, dans la base canonique, de la projection orthogonale sur $\text{Vect}(X)$ est $X^tX$.

842

***Solution des exercices***

2. (a) L’écriture par blocs de la matrice, dans la base canonique, de la projection orthogonale sur $\text{Vect}(X)$ est 
2. (a) L’écriture par blocs de la matrice, dans la base canonique, de la projection

$$
M = \begin{pmatrix}
M_{1,1} & \dots & M_{1,q} \\
\vdots & \ddots & \vdots \\
M_{q,1} & \dots & M_{q,q}
\end{pmatrix}
$$
où :
$$\forall(*i, j*) \in \llbracket 1, q \rrbracket^2 \quad M_{i,j} = \frac{1}{\|X\|^2} X_i {}^tX_j$$

(on applique la question précédente à $\frac{X}{\|X\|}$).

(b) On a $\text{Tr}(S) = \sum_{k=1}^q \text{Tr} M_{k,k} = \frac{1}{\|X\|^2} \sum_{k=1}^q \text{Tr}(X_k {}^tX_k) = \frac{1}{\|X\|^2} \sum_{k=1}^q \text{Tr}({}^tX_k X_k)$.

Or, pour tout $k \in \llbracket 1, q \rrbracket$, ${}^tX_k X_k$ est une matrice carrée de taille 1 dont l’unique coefficient est $\|X_k\|^2$ donc $\sum_{k=1}^q M_{k,k}$ est de trace 1.

De plus, pour tout $k \in \llbracket 1, q \rrbracket$, $M_{k,k} = \frac{1}{\|X\|^2} X_k {}^tX_k$ est symétrique et vérifie :
$$\forall Y \in \mathbb{R}^p \quad {}^tY M_{k,k} Y = \frac{1}{\|X\|^2} {}^t({}^tX_k Y) {}^tX_k Y = \frac{1}{\|X\|^2} \|{}^tX_k Y\|^2 \ge 0.$$

Par conséquent, pour tout $Y \in \mathbb{R}^p$, ${}^*tY SY* \ge 0$.

3. Comme $S$ est symétrique réelle, elle est diagonalisable en base orthonormée. Il existe donc une matrice diagonale $D = \text{Diag}(\lambda_1, \dots, \lambda_p)$ et une matrice orthogonale $P$ telles que $S = PD {}^tP$.

Notons $q$ le rang de $S$. Quitte à réordonner les valeurs propres de $S$, on peut supposer $\lambda_{q+1} = \dots = \lambda_p = 0$. Notons $Y_1, \dots, Y_q$ les $q$ premières colonnes de $P$. On a alors, en notant $(E_{i,j})$ la base canonique de $\mathcal{M}_p(\mathbb{R})$ :
$$S = \sum_{k=1}^q \lambda_k P E_{k,k} {}^tP = \sum_{k=1}^q \lambda_k Y_k {}^tY_k.$$

Pour tout $k \in \llbracket 1, q \rrbracket$, si $V_k$ est un vecteur propre de $S$ associé à la valeur propre $\lambda_k$, alors $\lambda_k \|V_k\|^2 = {}^tV_k S V_k \ge 0$ donc $\lambda_k$ est positif.

On peut donc poser $X_k = \sqrt{\lambda_k} Y_k$, de telle sorte que :
$$S = \sum_{k=1}^q X_k {}^tX_k.$$

Par propriété de la trace, pour tout $k$, on a $\text{Tr}(X_k {}^tX_k) = \text{Tr}({}^tX_k X_k) = \|X_k\|^2$, donc :
$$\sum_{k=1}^q \|X_k\|^2 = \text{Tr}(S) = 1. \tag{*}$$

Posons 
$$
X = \begin{pmatrix} X_1 \\ \vdots \\ X_q \end{pmatrix}
$$
$\in \mathbb{R}^{pq}$. L’égalité $(*)$ montre que $X$ est normé. La matrice de la projection orthogonale sur $\text{Vect}(X)$ répond donc à la question.

843

Chapitre 14. *Espaces préhilbertiens et euclidiens*

**14.13** 1. Supposons la famille $(x_1, \dots, x_p)$ liée.

Soit $(\lambda_1, \dots, \lambda_p) \in \mathbb{R}^p \setminus \{0\}$ tel que $\sum_{i=1}^p \lambda_i x_i = 0$.

Par produit scalaire avec $x_0$, on obtient :

$$\sum_{i=1}^p \lambda_i (x_0 | x_i) = 0$$

et comme tous les $(x_0 | x_i)$ sont strictement négatifs, on en déduit que les $\lambda_i$ ne peuvent pas être tout se même signe. Posons alors :

$$I = \{i \in \llbracket 1, p \rrbracket \mid \lambda_i > 0\} \quad \text{et} \quad J = \{i \in \llbracket 1, p \rrbracket \mid \lambda_i < 0\}.$$

Ce sont deux ensembles non vides et l'on a :

$$\sum_{i \in I} \lambda_i x_i = - \sum_{j \in J} \lambda_j x_j.$$

Notons $x$ ce vecteur. Alors :

$$\|x\|^2 = - \left( \sum_{i \in I} \lambda_i x_i \middle| \sum_{j \in J} \lambda_j x_j \right) = - \sum_{(*i,j*) \in I \times J} \underbrace{\lambda_i \lambda_j}_{<0} \underbrace{(x_i | x_j)}_{<0}$$

et donc $\|x\|^2 < 0$ puisque $I \times J$ est non vide. C'est contradictoire, donc la famille $(x_1, \dots, x_p)$ est libre.

2. On en déduit que pour tout famille obtusangle $(x_0, \dots, x_p)$ de l'espace vectoriel $E$ de dimension $n$, on a $p \leqslant n$, d'où le résultat.

844