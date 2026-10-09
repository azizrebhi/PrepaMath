# Chapitre 17 : Équations différentielles linéaires

<table>
        <tr>
            <td><b>I</b></td>
            <td><b>Équations différentielles linéaires d’ordre 1 . . . . .</b></td>
            <td><b>1012</b></td>
        </tr>
        <tr>
            <td>1</td>
            <td>Définitions et notations . . . . . . . . . . . . . . . . . . . . .</td>
            <td>1012</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Propriétés linéaires : structure de l’ensemble des solutions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .</td>
            <td>1016</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Théorème de Cauchy linéaire . . . . . . . . . . . . . . . .</td>
            <td>1017</td>
        </tr>
        <tr>
            <td>4</td>
            <td>Espace des solutions de l’équation homogène . . . .</td>
            <td>1018</td>
        </tr>
        <tr>
            <td>5</td>
            <td>Méthode de variation des constantes . . . . . . . . . .</td>
            <td>1020</td>
        </tr>
        <tr>
            <td><b>II</b></td>
            <td><b>Équations différentielles linéaires<br />à coefficients constants . . . . . . . . . . . . . . . . . . . . .</b></td>
            <td><b>1022</b></td>
        </tr>
        <tr>
            <td>1</td>
            <td>Résolution pratique de l’équation homogène . . . .</td>
            <td>1022</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Exponentielle d’un endomorphisme, d’une matrice</td>
            <td>1025</td>
        </tr>
        <tr>
            <td><b>III</b></td>
            <td><b>Équations différentielles linéaires<br />scalaires d’ordre <i>n</i> . . . . . . . . . . . . . . . . . . . . . . . . .</b></td>
            <td><b>1030</b></td>
        </tr>
        <tr>
            <td>1</td>
            <td>Définition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .</td>
            <td>1030</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Traduction sous la forme d’un système différentiel<br />linéaire d’ordre 1 . . . . . . . . . . . . . . . . . . . . . . . . . . .</td>
            <td>1031</td>
        </tr>
        <tr>
            <td><b>IV</b></td>
            <td><b>Équations différentielles linéaires<br />scalaires d’ordre 2 . . . . . . . . . . . . . . . . . . . . . . . . .</b></td>
            <td><b>1034</b></td>
        </tr>
        <tr>
            <td>1</td>
            <td>Wronskien . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .</td>
            <td>1035</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Recherche d’une solution particulière : méthode de<br />variation des constantes . . . . . . . . . . . . . . . . . . . . .</td>
            <td>1038</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Techniques classiques d’obtention d’une solution de<br />l’équation homogène . . . . . . . . . . . . . . . . . . . . . . .</td>
            <td>1041</td>
        </tr>
        <tr>
            <td><b>V</b></td>
            <td><b>Exemples de résolution d’équations non résolues</b></td>
            <td><b>1045</b></td>
        </tr>
        <tr>
            <td colspan="2"><b>Démonstration du théorème de Cauchy linéaire . . . .</b></td>
            <td><b>1047</b></td>
        </tr>
        <tr>
            <td colspan="2"><b>Démonstrations et solutions des exercices du cours . .</b></td>
            <td><b>1049</b></td>
        </tr>
        <tr>
            <td colspan="2"><b>Exercices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .</b></td>
            <td><b>1075</b></td>
        </tr>
</table>

# Équations différentielles linéaires ![icon: 17](page_2_image_1_v2.jpg)

Dans ce chapitre, $\mathbb{K}$ désigne $\mathbb{R}$ ou $\mathbb{C}$, $I$ un intervalle de $\mathbb{R}$ d'intérieur non vide, et $E$ un $\mathbb{K}$-espace vectoriel de dimension finie muni d'une norme $\|\cdot\|$. En première année ont été abordées :

* les équations différentielles linéaires d'ordre 1 de la forme :
$$y' + a(t) y = b(t) \quad \text{avec} \quad a : I \to \mathbb{K} \text{ et } b : I \to \mathbb{K} \text{ continues ;}$$

* les équations différentielles linéaires d'ordre 2 à coefficients constants de la forme :
$$y'' + ay' + by = c(t) \quad \text{avec} \quad (*a, b*) \in \mathbb{K}^2 \text{ et } c : I \to \mathbb{K} \text{ continue.}$$

Les objectifs du cours de seconde année sont, toujours en restant dans le cas linéaire :

* pour les équations d'ordre 1, étendre l'étude aux cas de fonctions à valeurs vectorielles (dans un espace de dimension finie) ;
* pour les équations d'ordre 2, étendre l'étude au cas de coefficients non constants.

# I Équations différentielles linéaires d'ordre 1

## 1 Définitions et notations

**Notation** Dans tout ce chapitre, afin d'alléger les écritures (et en particulier éviter trop de parenthèses), on convient que si $u$ est un endomorphisme de $E$ et $e$ un vecteur de $E$, alors la valeur de $u$ en $e$, notée traditionnellement $u(e)$, sera souvent notée $u \cdot e$.

Soit $a : I \to \mathcal{L}(E)$ et $b : I \to E$ deux applications continues.

Quand on cherche toutes les applications dérivables $\varphi : I \to E$ vérifiant :
$$\forall t \in I \quad \varphi'(t) = a(t) \cdot \varphi(t) + b(t),$$

on dit que l'on résout l'**équation différentielle linéaire du premier ordre** :
$$x' = a(t) \cdot x + b(t). \hfill (E)$$

I Équations différentielles linéaires d’ordre 1

**Remarque** Sans la convention « $u \cdot e$ » donnée plus haut, la relation ci-dessus s’écrit :
$$\forall t \in I \quad \varphi'(t) = a(t)(\varphi(t)) + b(t),$$
et l’équation est alors notée :
$$x' = a(t)(x) + b(t).$$

## **Définition 1**
*   On appelle **solution** sur $I$ de l’équation différentielle (E) toute application $\varphi : I \to E$ dérivable vérifiant :
$$\forall t \in I \quad \varphi'(t) = a(t) \cdot \varphi(t) + b(t).$$
*   L’application $b$ est appelée **second membre** de l’équation (E).
*   On appelle **équation homogène** (ou **sans second membre**) associée à (E) l’équation :
$$x' = a(t) \cdot x. \hfill (\text{E}_0)$$

**Remarque** On pourra noter $x'(t) = a(t) \cdot x(t) + b(t)$ l’équation (E) si l’on veut préciser le nom de la variable libre, en particulier s’il y a ambiguïté sur le nom de cette variable.

<mark>p.1049</mark> ### **Exercice 1** *Régularité des solutions*
Montrer que si les applications $a$ et $b$ sont de classe $\mathcal{C}^k$, alors toute solution de (E) est de classe $\mathcal{C}^{k+1}$.

**Remarque** Les applications $a$ et $b$ étant *a minima* supposées continues, une solution de (E) est au moins de classe $\mathcal{C}^1$.

### Exemple issu de la physique : particule chargée dans un champ électromagnétique
Dans $E = \mathbb{R}^3$, considérons une particule de charge $q$ et de vitesse $\vec{v}$ placée dans un champ électromagnétique uniforme $(\vec{E}(t), \vec{B}(t))$ (dépendant continûment du temps). Cette particule est soumise à la force de Lorentz <sup>1</sup> :
$$\vec{f} = q \vec{v} \wedge \vec{B}(t) + q \vec{E}(t),$$
et donc, en notant $\vec{a}$ son accélération et $m$ sa masse :
$$\vec{a} = \frac{q}{m} \vec{v} \wedge \vec{B}(t) + \frac{q}{m} \vec{E}(t).$$
Autrement dit, la vitesse $\vec{v}$ est solution l’équation différentielle :
$$x' = x \wedge \left( \frac{q}{m} \vec{B}(t) \right) + \frac{q}{m} \vec{E}(t).$$

---
1. Pour la définition du produit vectoriel, voir exercice 3 de la page 799.

1013

# Chapitre 17. Équations différentielles linéaires

qui s’écrit aussi :
$$x' = a(t) \cdot x + b(t)$$

avec, pour tout $t \in I$ :
$$\begin{aligned} a(t) : E & \longrightarrow E \\ x & \longmapsto x \wedge \left( \frac{q}{m} \vec{B}(t) \right) \end{aligned} \quad \text{et} \quad b(t) = \frac{q}{m} \vec{E}(t).$$

## Traduction matricielle : systèmes différentiels linéaires

**Convention** Dans la suite, on identifie $\mathcal{M}_{n,1}(\mathbb{K})$ et $\mathbb{K}^n$.

### **Définition 2**
> On appelle **système différentiel linéaire du premier ordre** toute équation différentielle linéaire du premier ordre de la forme :
> $$X' = A(t) X + B(t)$$
> avec $A : I \to \mathcal{M}_n(\mathbb{K})$ et $B : I \to \mathbb{K}^n$ des applications continues, et où la fonction inconnue $X$ va de $I$ dans $\mathbb{K}^n$.
>
> Un tel système s’écrit sous la forme :
>
> ```llamaparse
> parse(
>   mode="default",
>   box_2d=[465, 140, 580, 970],
>   preprocessing=[detect_layout],
>   prompt="Transcribe the system of differential equations using LaTeX cases environment. Include the (Sys) label on the right."
> )
> ```
>
> où les $a_{i,j}$, appelées **coefficients**, et les $b_i$, appelées **seconds membres**, sont des applications continues de $I$ dans $\mathbb{K}$.

**Interprétation** Si l’on munit l’espace vectoriel $E$ d’une base $\mathcal{B}$, alors l’équation différentielle :
$$x' = a(t) \cdot x + b(t) \hfill (E)$$
se traduit matriciellement par le système différentiel linéaire du premier ordre :
$$X' = A(t) X + B(t) \hfill (\text{Sys})$$
où, pour tout $t \in I$ :
* $A(t)$ est la matrice de $a(t)$ dans la base $\mathcal{B}$ ;
* $B(t)$ est la matrice colonne des coordonnées de $b(t)$ dans la base $\mathcal{B}$.

En effet, une application $\varphi : I \to E$ est solution de (E) si, et seulement si, :
$$\forall t \in I \quad X'(t) = A(t) X(t) + B(t)$$
où $X(t)$ est la matrice colonne des coordonnées de $\varphi(t)$ dans la base $\mathcal{B}$.

1014

# I Équations différentielles linéaires d'ordre 1

**Remarque** Si $n = 1$, alors le système différentiel (Sys) s’écrit :
$$x_1' = a_{1,1}(t) x_1 + b_1(t),$$
et n’est alors rien d’autre qu’une équation différentielle linéaire d’ordre 1.

**Exemple** Reprenons l’exemple de la présente page de la particule chargée dans un champ électromagnétique, qui nous a conduit à l’équation différentielle suivante :
$$x' = x \wedge \left( \frac{q}{m} \vec{B}(t) \right) + \frac{q}{m} \vec{E}(t). \quad \text{(Eq1)}$$

Supposons que les champs magnétique et électrique $\vec{B}(t)$ et $\vec{E}(t)$ aient une direction constante commune et plaçons-nous dans une base orthonormée $\mathcal{B}$ de $\mathbb{R}^3$ dont le premier vecteur est dirigé selon ces champs.

Les composantes de $\frac{q}{m} \vec{B}(t)$ et $\frac{q}{m} \vec{E}(t)$ dans la base $\mathcal{B}$ sont alors de la forme :

$$\text{Mat}_{\mathcal{B}} \left( \frac{q}{m} \vec{B}(t) \right) = \begin{pmatrix} \alpha(t) \\ 0 \\ 0 \end{pmatrix} \quad \text{et} \quad \text{Mat}_{\mathcal{B}} \left( \frac{q}{m} \vec{E}(t) \right) = \begin{pmatrix} \beta(t) \\ 0 \\ 0 \end{pmatrix}.$$

En notant alors $X(t) = \begin{pmatrix} x_1(t) \\ x_2(t) \\ x_3(t) \end{pmatrix}$ les composantes de $x(t)$ dans la base $\mathcal{B}$, on a :

$$\text{Mat}_{\mathcal{B}} \left( x(t) \wedge \left( \frac{q}{m} \vec{B}(t) \right) \right) = \begin{pmatrix} 0 \\ \alpha(t) x_3(t) \\ -\alpha(t) x_2(t) \end{pmatrix}$$

L’équation différentielle (Eq1) se traduit alors par le système différentiel suivant :

$$
\begin{cases}
x'_1(t) & = \beta(t) \\
x'_2(t) & = \alpha(t) x_3(t) \\
x'_3(t) & = -\alpha(t) x_2(t)
\end{cases}
\hfill (\text{Sys}_1)
$$

## Problème de Cauchy

*   On dit qu’une solution $\varphi$ de l’équation différentielle (E) vérifie la **condition initiale** $(t_0, x_0) \in I \times E$ si l’on a :
$$\varphi(t_0) = x_0.$$

*   On appelle **problème de Cauchy**, l’équation (E) munie d’une condition initiale $(t_0, x_0) \in I \times E$ :
$$(E) : x' = a(t) \cdot x + b(t) \quad \text{et} \quad x(t_0) = x_0.$$

*   Résoudre ce **problème de Cauchy**, c’est trouver toutes les solutions $\varphi$ de (E) vérifiant la condition initiale $\varphi(t_0) = x_0$.

1015

# Chapitre 17. Équations différentielles linéaires

## Mise sous forme intégrale d’un problème de Cauchy

## **Proposition 1**

Soit $(t_0, x_0) \in I \times E$. Une application $\varphi \in \mathcal{C}(I, E)$ est une solution du problème de Cauchy :

$$(E) : x' = a(t) \cdot x + b(t) \quad \text{et} \quad x(t_0) = x_0.$$

si, et seulement si, elle satisfait l'équation intégrale :

$$\forall t \in I \quad \varphi(t) = x_0 + \int_{t_0}^{t} a(s) \cdot \varphi(s) \, ds + \int_{t_0}^{t} b(s) \, ds$$


<mark>Démonstration page 1049</mark>


## 2 Propriétés linéaires : structure de l’ensemble des solutions

**Notation** Pour $a : I \to \mathcal{L}(E)$ et $x : I \to E$, notons $a \cdot x$ l’application :
$$
\begin{aligned}
a \cdot x : I & \longrightarrow E \\
t & \longmapsto a(t) \cdot x(t).
\end{aligned}
$$

Avec cette notation, l’équation différentielle (E) s’écrit :
$$x' = a \cdot x + b. \eqno(\text{E})$$

L’application :
$$
\begin{aligned}
L : \mathcal{C}^1(I, E) & \to \mathcal{C}^0(I, E) \\
x & \mapsto x' - a \cdot x
\end{aligned}
$$
est bien définie, c’est une application linéaire, et l’on constate que les équations (E) et $(\text{E}_0)$ se formulent naturellement à l’aide de $L$ :
$$(E) : L(x) = b \quad \text{et} \quad (E_0) : L(x) = 0.$$

Les propriétés générales des équations linéaires donnent alors les deux résultats suivants.

## **Proposition 2**

*   L’ensemble $\mathcal{S}_0$ des solutions de l’équation homogène $(E_0)$ est un sous-espace vectoriel de $\mathcal{C}^1(I, E)$ ; c’est le noyau de l’application linéaire $L$ introduite ci-dessus.
*   Si $\varphi_p$ est une solution particulière de $(E)$, l’ensemble $\mathcal{S}$ des solutions de l’équation $(E)$ s’écrit :

$$\mathcal{S} = \varphi_p + \mathcal{S}_0.$$

C’est donc un sous-espace affine de $\mathcal{C}^1(I, E)$ de direction $\mathcal{S}_0$.

1016

*I Équations différentielles linéaires d'ordre 1*

**Remarque** À ce stade, on peut dire que l’ensemble $\mathcal{S}$ est soit vide, soit un sous-espace affine de $\mathcal{C}^1(I, E)$ dirigé par $\mathcal{S}_0$. En fait, nous verrons (*cf.* théorème de Cauchy linéaire ci-dessous) que l’ensemble $\mathcal{S}$ n’est jamais vide.

**Proposition 3 (Principe de superposition)**
Supposons que le second membre $b$ de (E) s’écrive :
$$b = \alpha_1 b_1 + \alpha_2 b_2 \quad \text{avec} \quad (\alpha_1, \alpha_2) \in \mathbb{K}^2 \quad \text{et} \quad (b_1, b_2) \in (\mathcal{C}(I, E))^2.$$
Si $\varphi_1$ et $\varphi_2$ sont respectivement solutions des équations :
$$x' = a(t) \cdot x + b_1(t) \quad \text{et} \quad x' = a(t) \cdot x + b_2(t),$$
alors la fonction $\alpha_1 \varphi_1 + \alpha_2 \varphi_2$ est solution de (E).

## 3 Théorème de Cauchy linéaire

Dans cette sous-section, $a$ et $b$ désignent des applications continues sur $I$ à valeurs respectivement dans $\mathcal{L}(E)$ et $E$. On considère l’équation différentielle linéaire du premier ordre :
$$x' = a(t) \cdot x + b(t) \hfill \text{(E)}$$

### Théorème de Cauchy linéaire

La démonstration du théorème fondamental suivant n’est pas exigible. Elle est proposée en annexe à la fin du chapitre (page 1047).

**Théorème 4 (Théorème de Cauchy linéaire)**
Pour tout $(t_0, x_0) \in I \times E$, il existe une et une seule solution $\varphi$ de l’équation (E) vérifiant la condition initiale $\varphi(t_0) = x_0$.
Autrement dit, le problème de Cauchy :
$$\text{(E)} : x' = a(t) \cdot x + b(t) \quad \text{et} \quad x(t_0) = x_0$$
possède une unique solution.

**Remarque** La partie « existence » du théorème de Cauchy linéaire assure que l’ensemble $\mathcal{S}$ des solutions de (E) est non vide (car $I \times E$ est non vide).

p.1049 **Exercice 2** Soit $\varphi_1$ et $\varphi_2$ deux solutions distinctes de (E). Montrer que :
$$\forall t \in I \quad \varphi_1(t) \neq \varphi_2(t).$$

p.1049 **Exercice 3** Montrer qu’une solution non nulle de l’équation homogène $(\text{E}_0)$ ne s’annule en aucun point de $I$.

1017

Chapitre 17. Équations différentielles linéaires

**Remarque** La partie « unicité » du théorème de Cauchy linéaire assure :
* que les graphes de deux solutions distinctes de (E) ne se croisent pas (*cf.* exercice 2) ;
* qu’une solution non nulle de $(\text{E}_0)$ ne s’annule pas (*cf.* exercice 3).

<mark>p.1050</mark> **Exercice 4** Soit $A \in \mathcal{C}(I, \mathcal{M}_n(\mathbb{R}))$, $B \in \mathcal{C}(I, \mathbb{R}^n)$ et $t_0 \in I$.
On considère le système différentiel réel :
$$X' = A(t)X + B(t) \quad \quad \text{(Sys)}$$
Montrer qu’une solution $\varphi : I \to \mathbb{C}^n$ de (Sys) est réelle (c’est-à-dire à valeurs dans $\mathbb{R}^n$) si, et seulement si, $\varphi(t_0) \in \mathbb{R}^n$.

**Remarque** Le théorème de Cauchy linéaire a été démontré dans le cours de première année pour les équations différentielles linéaires scalaires ($E = \mathbb{K}$) du premier ordre en exhibant la forme explicite des solutions.
Pour ces équations, de la forme :
$$x' + a(t)x = b(t) \quad \text{avec} \quad a : I \to \mathbb{K} \text{ et } b : I \to \mathbb{K} \text{ continues,}$$
l’unique solution prenant la valeur $x_0$ au point $t_0 \in I$ est :
$$t \mapsto \exp(-F(t)) \left( x_0 + \int_{t_0}^t \exp(F(u)) b(u) du \right)$$
où $F$ est la primitive de $a$ sur $I$ s’annulant en $t_0$.
Cette forme explicite ne s’étend malheureusement pas au cas général où la dimension de $E$ est supérieure ou égale à 2. En effet, on ne sait pas, en général, expliciter les solutions d’une équation différentielle linéaire du premier ordre. La démonstration du théorème de Cauchy linéaire se révèle donc plus ardue. Rappelons qu’elle est proposée sous forme d’exercices à la page 1047.

## 4 Espace des solutions de l'équation homogène

### **Proposition 5**
> Soit $t_0 \in I$. Notons $\mathcal{S}_0$ l’espace vectoriel des solutions de l’équation homogène $(\text{E}_0) : x' = a(t) \cdot x$. L’application :
> $$\begin{aligned} \delta_{t_0} : \mathcal{S}_0 &\to E \\ \varphi &\mapsto \varphi(t_0) \end{aligned}$$
> est un isomorphisme d’espaces vectoriels.

**Démonstration.** L’application $\delta_{t_0}$ est évidemment linéaire, et elle est bijective puisque, pour tout $x_0 \in E$, le théorème de Cauchy linéaire assure l’existence d’un et un seul élément $\varphi \in \mathcal{S}_0$ tel que $\varphi(t_0) = x_0$. $\square$

### **Corollaire 6**
> L’espace $\mathcal{S}_0$ est de dimension finie égale à celle de $E$.

1018

*I Équations différentielles linéaires d’ordre 1*

# **Point méthode**

Le fait de connaître la dimension de $\mathcal{S}_0$ se révèle utile lors de la résolution de $(E_0)$. En effet, si l'on dispose de $n$ solutions $\varphi_1, \dots, \varphi_n$ de $(E_0)$, alors pour obtenir que la famille $(\varphi_1, \dots, \varphi_n)$ est une base de $\mathcal{S}_0$ et donc que :

$$\mathcal{S}_0 = \text{Vect } (\varphi_1, \dots, \varphi_n),$$

il suffit de montrer, au choix :

* que la famille $(\varphi_1, \dots, \varphi_n)$ est libre ;
* que la famille $(\varphi_1, \dots, \varphi_n)$ est génératrice (en montrant que toute solution de $(E_0)$ s'écrit nécessairement comme combinaison linéaire de $\varphi_1, \dots, \varphi_n$).

**Exemple** Reprenons l’exemple de la particule chargée dans un champ électromagnétique. Supposons cette fois-ci que le champ électrique $\vec{E}$ est nul et que le champ magnétique $\vec{B}$ est constant. Le système différentiel obtenu à l’exemple de la page 1015 s’écrit alors :

$$
\begin{cases}
x'_1(t) & = & 0 \\
x'_2(t) & = & \alpha x_3(t) \\
x'_3(t) & = & -\alpha x_2(t)
\end{cases}
\quad \text{avec } \alpha \text{ une constante positive.}
$$

Constatons que les trois fonctions suivantes sont solutions :

$$
\varphi_1 : t \mapsto \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} \quad \varphi_2 : t \mapsto \begin{pmatrix} 0 \\ \sin(\alpha t) \\ \cos(\alpha t) \end{pmatrix} \quad \text{et} \quad \varphi_3 : t \mapsto \begin{pmatrix} 0 \\ \cos(\alpha t) \\ -\sin(\alpha t) \end{pmatrix}.
$$

D’autre part, le système étudié étant un système différentiel linéaire homogène de taille 3, l’espace $\mathcal{S}_0$ de ses solutions est de dimension 3.

Puisque la famille $(\varphi_1(0), \varphi_2(0), \varphi_3(0))$ est libre, la famille $(\varphi_1, \varphi_2, \varphi_3)$ l’est aussi ; c’est donc une base de $\mathcal{S}_0$. On a donc :

$$
\mathcal{S}_0 = \text{Vect}(\varphi_1, \varphi_2, \varphi_3).
$$

p.1050

## **Exercice 5** On souhaite résoudre le système différentiel homogène :

$$
\begin{cases} 
x_1'(t) &= x_1(t) + 2x_2(t) \\
x_2'(t) &= 2x_1(t) + x_2(t) 
\end{cases} \tag{Sys}
$$

1. Soit $f = (f_1, f_2)$ solution de (Sys).
    (a) En sommant les deux équations, montrer qu'il existe $a \in \mathbb{K}$ tel que :
    $$\forall t \in \mathbb{R} \quad (f_1 + f_2)(t) = a e^{3t}.$$
    (b) En déduire que $f \in \text{Vect}(\varphi_1, \varphi_2)$ avec :
    $$\varphi_1 : t \mapsto (e^{-t}, -e^{-t}) \quad \text{et} \quad \varphi_2 : t \mapsto (e^{3t}, e^{3t}).$$

2. Conclure la résolution.

1019

Chapitre 17. Équations différentielles linéaires

## 5 **Méthode de variation des constantes**

Il a été vu en première année, dans le cas des équations différentielles linéaires *scalaires* d’ordre 1, la méthode de *variation de la constante* qui permet, si l’on connaît une solution non nulle de l’équation homogène $(E_0)$, de déterminer une solution particulière de $(E)$.

Cette méthode se généralise au cas des équations vectorielles en la **méthode de variation des constantes**.

Commençons par deux exercices qui faciliteront la présentation à suivre de la méthode de variation des constantes.

p.1051 **Exercice 6** Soit $\varphi_1, \dots, \varphi_n$ des solutions de l’équation homogène $(E_0)$.
Montrer que les trois assertions suivantes sont équivalentes :
(i) la famille $(\varphi_1, \dots, \varphi_n)$ est une base de $\mathcal{S}_0$ ;
(ii) il existe $t_0 \in I$ tel que la famille $(\varphi_1(t_0), \dots, \varphi_n(t_0))$ soit une base de $E$ ;
(*iii*) pour tout $t \in I$, la famille $(\varphi_1(t), \dots, \varphi_n(t))$ est une base de $E$.

Dans la suite, on suppose disposer d’une base $(\varphi_1, \dots, \varphi_n)$ de l’espace $\mathcal{S}_0$ des solutions de l’équation homogène $(E_0)$.

p.1051 **Exercice 7** Montrer que toute application $\varphi : I \to E$ de classe $\mathcal{C}^1$ s’écrit de manière unique sous la forme :
$$\varphi = \sum_{k=1}^n \lambda_k \varphi_k$$
avec $\lambda_1, \dots, \lambda_n$ des fonctions de classe $\mathcal{C}^1$ de $I$ dans $\mathbb{K}$.
*Indication : pour le caractère* $\mathcal{C}^1$*, utiliser le déterminant.*

### **Point méthode (Méthode de variation des constantes)**

La méthode de variation des constantes consiste à rechercher une solution de $(E)$ sous la forme :
$$\varphi = \sum_{k=1}^n \lambda_k \varphi_k \quad \text{avec} \quad \lambda_1, \dots, \lambda_n \text{ des fonctions dérivables de } I \text{ dans } \mathbb{K}.$$
En reportant cette expression dans l’équation $(E)$, on obtient, puisque $\varphi_1, \dots, \varphi_n$ sont solutions de $(E_0)$ :
$$(\varphi \text{ solution de } (E)) \iff \left( \sum_{k=1}^n \lambda'_k \varphi_k = b \right). \hfill (\star)$$
Par liberté de la famille $(\varphi_1, \dots, \varphi_n)$, on peut alors identifier $\lambda'_1, \dots, \lambda'_n$.
Le problème se réduit alors à primitiver $\lambda'_1, \dots, \lambda'_n$.

1020

I Équations différentielles linéaires d'ordre 1

**Justification de l'équivalence ($\star$) ci-dessus**

Pour tout $t \in I$, on a :

$$
\begin{aligned}
\varphi'(t) &= \left( \sum_{k=1}^n \lambda_k \varphi_k \right)' (t) \\
&= \sum_{k=1}^n \lambda_k(t) \varphi_k'(t) + \sum_{k=1}^n \lambda_k'(t) \varphi_k(t).
\end{aligned}
$$

Comme $\varphi_1, \dots, \varphi_n$ sont solutions de $(E_0)$, puis par linéarité de $a(t)$, on a :

$$
\sum_{k=1}^n \lambda_k(t) \varphi_k'(t) = \sum_{k=1}^n \lambda_k(t) a(t) \cdot \varphi_k(t) = a(t) \cdot \varphi(t)
$$

et donc finalement :

$$
\varphi'(t) = a(t) \cdot \varphi(t) + \sum_{k=1}^n \lambda_k'(t) \varphi_k(t).
$$

Ainsi on obtient l'équivalence :

$$
\varphi'(t) = a(t) \cdot \varphi(t) + b(t) \iff \sum_{k=1}^n \lambda_k'(t) \varphi_k(t) = b(t).
$$

<mark>p.1052</mark> **Exercice 8** *Suite de l'exercice 5 de la page 1019*

Résoudre le système :

$$
\left\{
\begin{array}{lcl}
x_1'(t) & = & x_1(t) + 2x_2(t) + e^{-t} \\
x_2'(t) & = & 2x_1(t) + x_2(t)
\end{array}
\right. \quad \text{(Sys)}
$$

**Remarque** Supposons que le second membre de l'équation (E) s'écrive :

$$
b = \sum_{k=1}^n \alpha_k \varphi_k.
$$

La méthode de variation donne alors :

$$
\left( \sum_{k=1}^n \lambda_k \varphi_k \text{ solution de (E)} \right) \iff \left( \forall k \in \llbracket 1, n \rrbracket \quad \lambda_k' = \alpha_k \right).
$$

Cela mène à une expression explicite des solutions de (E) :

$$
\varphi(t) = \sum_{k=1}^n \left( \mu_k + \int_{t_0}^t \alpha_k(s) \, ds \right) \varphi_k(t) \quad \text{avec} \quad (\mu_1, \dots, \mu_n) \in \mathbb{K}^n.
$$

1021

Chapitre 17. *Équations différentielles linéaires*

# II Équations différentielles linéaires du premier ordre **à coefficients constants**

L’équation différentielle linéaire :
$$x' = a(t) \cdot x + b(t)$$
est dite **à coefficients constants** si la fonction $a : \begin{array}{ccc} I & \longrightarrow & \mathcal{L}(E) \\ t & \longmapsto & a(t) \end{array}$ est constante. On identifie alors $a$ à un élément de $\mathcal{L}(E)$ et l’on note l’équation :
$$x' = a \cdot x + b(t).$$
Si l’on dispose d’une base $\mathcal{B}$ de $E$ et si $A$ et $B(t)$ sont respectivement les matrices de $a$ et $b(t)$ dans la base $\mathcal{B}$, alors l’équation précédente s’écrit matriciellement :
$$X' = AX + B(t).$$

## 1 Résolution pratique de l’équation homogène
On s’intéresse dans cette partie à une équation homogène de la forme :
$$X' = AX \quad (\text{E}_0)$$
avec $A \in \mathcal{M}_n(\mathbb{K})$. L’objectif est de présenter la méthode de résolution d’un tel système différentiel. Nous traitons trois situations, de difficulté croissante :
* $A$ est diagonalisable ;
* $A$ est à coefficients réels, diagonalisable dans $\mathbb{C}$ mais pas dans $\mathbb{R}$ ;
* $A$ n’est pas diagonalisable dans $\mathbb{C}$.

D’après le corollaire 6 de la page 1018, on sait déjà que l’ensemble $\mathcal{S}_0$ des solutions sur $\mathbb{R}$ de $(\text{E}_0)$ est un $\mathbb{K}$-espace vectoriel de dimension $n$. Résoudre l’équation $(\text{E}_0)$ revient donc à déterminer une base de $\mathcal{S}_0$.

1022

II Équations différentielles linéaires du premier ordre à coefficients constants

## Cas où $A$ est diagonalizable

p.1052

### **Exercice 9**

1. Soit $V$ un vecteur propre de $A$ ; notons $\lambda$ la valeur propre associée. Montrer que la fonction $\varphi : \begin{matrix} \mathbb{R} & \longrightarrow & \mathbb{K}^n \\ t & \longmapsto & e^{\lambda t} V \end{matrix}$ est l'unique solution du problème de Cauchy :
   $$X' = AX \quad \text{et} \quad X(0) = V.$$

2. Supposons la matrice $A$ diagonalizable. Soit $(V_1, \dots, V_n)$ une base de vecteurs propres de $A$ et $(\lambda_1, \dots, \lambda_n)$ la liste des valeurs propres associées. Montrer qu'alors, en notant, pour tout $k \in \llbracket 1, n \rrbracket$ :
   $$\varphi_k : \begin{matrix} \mathbb{R} & \longrightarrow & \mathbb{K}^n \\ t & \longmapsto & e^{\lambda_k t} V_k \end{matrix}$$
   la famille $(\varphi_1, \dots, \varphi_n)$ est une base de $\mathcal{S}$.

Le cas où $A$ est diagonalizable se révèle particulièrement simple : l'ensemble $\mathcal{S}$ des solutions de $(E_0)$ s'obtient directement à partir des éléments propres de $A$.

> ### **Point méthode (Conséquence de l'exercice précédent)**
>
> Si la matrice $A$ est diagonalizable, alors en notant $(V_1, \dots, V_n)$ une base de vecteurs propres et $(\lambda_1, \dots, \lambda_n)$ la liste des valeurs propres associées, on obtient une base $(\varphi_1, \dots, \varphi_n)$ de l'espace $\mathcal{S}$ des solutions de $(E_0)$ en prenant, pour tout $k \in \llbracket 1, n \rrbracket$ :
> $$\varphi_k : \begin{matrix} \mathbb{R} & \longrightarrow & \mathbb{K} \\ t & \longmapsto & e^{\lambda_k t} V_k. \end{matrix}$$

p.1053

**Exercice 10** Résoudre le système différentiel $X' = AX$, avec $A = \begin{pmatrix} 2 & 1 & 1 \\ 1 & 2 & 1 \\ 1 & 1 & 2 \end{pmatrix}$.

### Remarques

* Dans le cas où $A$ est à coefficients réels, on peut s'intéresser aux solutions complexes ou réelles de l'équation. Lorsqu'il y a ambiguïté, on note $\mathcal{S}_{\mathbb{C}}$ et $\mathcal{S}_{\mathbb{R}}$ pour éviter toute confusion.
* Si $A$ est diagonalizable dans $\mathbb{R}$ et si $(V_1, \dots, V_n)$ est une base de vecteurs propres *réels*, alors les applications $\varphi_k : t \mapsto e^{\lambda_k t} V_k$ du point méthode précédent sont à valeurs réelles. On a :
  $$\mathcal{S}_{\mathbb{C}} = \text{Vect}_{\mathbb{C}}(\varphi_1, \dots, \varphi_n) \quad \text{et} \quad \mathcal{S}_{\mathbb{R}} = \text{Vect}_{\mathbb{R}}(\varphi_1, \dots, \varphi_n)$$
  et la seule différence entre $\mathcal{S}_{\mathbb{C}}$ et $\mathcal{S}_{\mathbb{R}}$ réside alors dans les coefficients des combinaisons linéaires (qui sont ou bien complexes ou bien réels).

1023

Chapitre 17. *Équations différentielles linéaires*

## Cas où $A$ est diagonalizable dans $\mathbb{C}$ mais pas dans $\mathbb{R}$

Si $A \in \mathcal{M}_n(\mathbb{R})$ est diagonalizable dans $\mathbb{C}$ mais pas dans $\mathbb{R}$, le paragraphe précédent nous fournit les solutions complexes, mais pas les solutions réelles.

p.1053
**Exercice 11** Considérons une application $\varphi : \mathbb{R} \to \mathbb{C}^n$.
Montrer que, dans le $\mathbb{C}$-espace vectoriel des fonctions de $\mathbb{R}$ dans $\mathbb{C}^n$, on a :
$$\text{Vect}(\varphi, \overline{\varphi}) = \text{Vect} (\text{Re}(\varphi), \text{Im}(\varphi)).$$

### **Point méthode**

Si $A \in \mathcal{M}_n(\mathbb{R})$ est diagonalizable dans $\mathbb{C}$ mais pas dans $\mathbb{R}$, on peut déterminer l'ensemble $\mathcal{S}_{\mathbb{R}}$ des solutions réelles de $(E_0)$ à partir de la diagonalisation de $A$.

1. On forme une base de vecteurs propres complexes de $A$ telle que :
    * les vecteurs propres associés à des valeurs propres réelles appartiennent à $\mathbb{R}^n$ ;
    * vis-à-vis des valeurs propres non réelles, on forme des couples de vecteurs propres conjugués (*i.e.* de la forme $(V, \overline{V})$).
2. Dans la base $(\varphi_1, \dots, \varphi_n)$ de $\mathcal{S}_{\mathbb{C}}$ évoquée par le point méthode de la page précédente, on voit alors apparaître :
    * pour les valeurs propres réelles, des applications de la forme $t \mapsto e^{\lambda t}V$, qui sont à valeurs dans $\mathbb{R}^n$ ;
    * pour les valeurs propres non réelles, des couples de la forme $(t \mapsto e^{\lambda t}V, t \mapsto e^{\overline{\lambda} t}\overline{V})$, c'est-à-dire de la forme $(\varphi, \overline{\varphi})$
3. On change les couples de la forme $(\varphi, \overline{\varphi})$ en $(\text{Re}(\varphi), \text{Im}(\varphi))$.
   Le résultat de l'exercice 11 assure que la nouvelle famille ainsi obtenue est encore une base de $\mathcal{S}_{\mathbb{C}}$. Cette base de $\mathcal{S}_{\mathbb{C}}$ :
    * est constituée de solutions de $(E_0)$ à valeurs dans $\mathbb{R}^n$, *i.e.* d'éléments de $\mathcal{S}_{\mathbb{R}}$,
    * étant libre dans le $\mathbb{C}$-espace vectoriel $\mathcal{F}(\mathbb{R}, \mathbb{C})$, elle l'est également dans le $\mathbb{R}$-espace vectoriel $\mathcal{F}(\mathbb{R}, \mathbb{R})$.
   donc, comme elle comporte $n$ éléments et que $\dim \mathcal{S}_{\mathbb{R}} = n$, c'est une base de $\mathcal{S}_{\mathbb{R}}$.

p.1054
**Exercice 12** Résoudre dans $\mathbb{C}$ puis dans $\mathbb{R}$ le système différentiel $X' = AX$ avec :
$$A = \begin{pmatrix} 1 & -1 & 2 \\ 2 & -1 & 3 \\ 0 & 0 & 1 \end{pmatrix}.$$

1024

II Équations différentielles linéaires du premier ordre à coefficients constants

## Cas où la matrice $A$ n'est pas diagonalisable dans $\mathbb{C}$

> ### **Point méthode**
>
> Dans le cas où $A$ est seulement trigonalisable :
>
> 1. on trigonalise, c'est-à-dire qu'on écrit $A = *PTP*^{-1}$ avec $T$ triangulaire supérieure ;
> 2. en posant $Y = P^{-1}X$ et en traduisant sur $Y$ le système différentiel $X' = AX$, on obtient le système différentiel $Y' = TY$ ; ce système différentiel est triangulaire et on peut le résoudre ligne par ligne, du bas vers le haut ;
> 3. on obtient alors les solutions cherchées à l'aide de la relation $X = PY$.

**Remarque** Dans la démarche précédente :
* il n'est en aucun cas nécessaire de calculer $P^{-1}$ ;
* lorsque l'on trigonalise $A$, on cherchera à obtenir la matrice triangulaire la plus simple possible afin d'obtenir le système différentiel $Y' = TY$ le plus simple possible.

> p.1055

**Exercice 13** Résoudre le système différentiel $X' = AX$, avec

$$A = \begin{pmatrix} 3 & 0 & -1 \\ -1 & 2 & 1 \\ 1 & 0 & 1 \end{pmatrix}.$$

**Remarque** La technique consistant à obtenir un système différentiel plus simple par réduction de la matrice $A$ peut aussi s'appliquer pour un système différentiel avec second membre de la forme $X' = AX + B(t)$ (*cf.* exercice 17.4 de la page 1075).

## 2 Exponentielle d'un endomorphisme, d'une matrice
### Exponentielle d'un endomorphisme

On rappelle (*cf.* exercice 22 de la page 305) qu'il existe une norme sous-multiplicative sur $\mathcal{L}(E)$, c'est-à-dire vérifiant :

$$\forall(*a, b*) \in \mathcal{L}(E)^2 \quad \|a \circ b\| \le \|a\| \ \|b\|$$

Nous utiliserons une telle norme dans la suite.

# **Proposition 7**

Soit $a \in \mathcal{L}(E)$. La série de terme général $\frac{a^k}{k!}$ est absolument convergente.

1025

# Chapitre 17. Équations différentielles linéaires

**Démonstration.** La norme $\|\cdot\|$ utilisée sur $\mathcal{L}(E)$ étant sous-multiplicative, on a :
$$\forall k \in \mathbb{N} \quad \left\| \frac{a^k}{k!} \right\| \leqslant \frac{\|a\|^k}{k!}.$$

Donc, par comparaison, la convergence de la série $\sum \frac{\|a\|^k}{k!}$ (série numérique de l'exponentielle) donne celle de la série $\sum \left\| \frac{a^k}{k!} \right\|$. $\square$

D'où la définition suivante.

## **Définition 3**
Soit $a \in \mathcal{L}(E)$. On appelle **exponentielle** de $a$ et l'on note $\exp(a)$ ou $e^a$, la somme de la série absolument convergente :
$$\exp(a) = \sum_{k=0}^{+\infty} \frac{a^k}{k!}.$$

**Remarque** Pour tout $t \in \mathbb{R}$, on a :
$$\exp(t \operatorname{Id}_E) = \sum_{k=0}^{+\infty} \frac{(t \operatorname{Id}_E^k)}{k!} = \left( \sum_{k=0}^{+\infty} \frac{t^k}{k!} \right) \operatorname{Id}_E = e^t \operatorname{Id}_E.$$
En particulier, on a $\exp(0) = \operatorname{Id}_E$.

**Exemple** Si $a \in \mathcal{L}(E)$ est nilpotente, et si $p \in \mathbb{N}$ est tel que $a^p = 0$, alors on a :
$$\forall k \geqslant p \quad a^k = 0 \quad \text{et donc} \quad \exp(a) = \sum_{k=0}^{p-1} \frac{a^k}{k!}.$$

## **Proposition 8**
L'application $\exp : \mathcal{L}(E) \longrightarrow \mathcal{L}(E)$ est continue.
$$a \longmapsto \exp(a)$$

**Principe de démonstration.** Montrer la convergence normale sur tout compact.
Démonstration page 1057


## **Proposition 9**
Soit $a \in \mathcal{L}(E)$. L'application $\varphi : \mathbb{R} \longrightarrow \mathcal{L}(E)$ est de classe $\mathcal{C}^1$ et sa dérivée est donnée par :
$$t \longmapsto \exp(ta)$$
$$\forall t \in \mathbb{R} \quad \varphi'(t) = a \circ \exp(ta) = \exp(ta) \circ a.$$

**Principe de démonstration.** Utiliser le théorème de dérivation des séries de fonctions.
Démonstration page 1057


**Remarque** On obtient par récurrence que l'application $\varphi : t \mapsto \exp(ta)$ de la proposition précédente est de classe $\mathcal{C}^\infty$ et, pour tout $p \in \mathbb{N}$, on a :
$$\forall t \in \mathbb{R} \quad \varphi^{(p)}(t) = a^p \circ \exp(ta) = \exp(ta) \circ a^p.$$

1026

II Équations différentielles linéaires du premier ordre à coefficients constants

## Exponentielle d’une matrice

**Proposition 10**
> Soit $A \in \mathcal{M}_n(\mathbb{K})$. La série de terme général $\frac{A^k}{k!}$ est absolument convergente.

**Définition 4**
> Soit $A \in \mathcal{M}_n(\mathbb{K})$. On appelle **exponentielle** de $A$ et l’on note $\exp(A)$ ou $e^A$, la somme de la série absolument convergente :
>
> $$\exp(A) = \sum_{k=0}^{+\infty} \frac{A^k}{k!}.$$

**Remarque** Pour tout $t \in \mathbb{R}$, on a :

$$\exp(t I_n) = \sum_{k=0}^{+\infty} \frac{(t I_n^k)}{k!} = \left( \sum_{k=0}^{+\infty} \frac{t^k}{k!} \right) I_n = e^t I_n.$$

En particulier, on a $\exp(0) = I_n$.

**Exemple** Si $A \in \mathcal{M}_n(\mathbb{K})$ est nilpotente, et si $p \in \mathbb{N}$ est tel que $A^p = 0$, on a :

$$\forall k \geqslant p \quad A^k = 0 \quad \text{et donc} \quad \exp(A) = \sum_{k=0}^{p-1} \frac{A^k}{k!}.$$

<mark>p.1058</mark> **Exercice 14** Montrer que si $A$ est la matrice d’un endomorphisme $a$ dans une base $\mathcal{B}$ de $E$, alors $\exp(A)$ est la matrice dans $\mathcal{B}$ de $\exp(a)$.

Les résultats suivants sont l’adaptation à l’exponentielle de matrices des propositions 8 et 9.

**Proposition 11**
> L’application $\exp : \mathcal{M}_n(\mathbb{K}) \longrightarrow \mathcal{M}_n(\mathbb{K})$ est continue.
> $$A \longmapsto \exp(A)$$

**Proposition 12**
> Soit $A \in \mathcal{M}_n(\mathbb{K})$. L’application $\varphi : \mathbb{R} \longrightarrow \mathcal{M}_n(\mathbb{K})$ est de classe $\mathcal{C}^1$ et
> $$t \longmapsto \exp(tA)$$
>
> sa dérivée est donnée par :
>
> $$\forall t \in \mathbb{R} \quad \varphi'(t) = A \exp(tA) = \exp(tA) A.$$

**Remarque** Plus généralement, l’application $\varphi : t \mapsto \exp(tA)$ de la proposition précédente est de classe $\mathcal{C}^\infty$ et, pour tout $p \in \mathbb{N}$, on a :

$$\forall t \in \mathbb{R} \quad \varphi^{(p)}(t) = A^p \exp(tA) = \exp(tA) A^p.$$

1027

# Chapitre 17. Équations différentielles linéaires

## Exemples de calculs

**Exercice 15** (p.1058)

1. Soit $A = \text{Diag}(\lambda_1, \dots, \lambda_n)$ une matrice diagonale. Déterminer $\exp(A)$.
2. Même question si $A$ est une matrice diagonalisable.

**Exercice 16** (p.1059) Soit $A \in \mathcal{M}_n(\mathbb{K})$ telle que $A^2 - 3A + 2I_n = 0$.

1. Pour $k \in \mathbb{N}$, exprimer $A^k$ en fonction de $A$ et $I_n$.
2. En déduire l'expression de $\exp(A)$ en fonction de $A$ et $I_n$.

## Lien avec les systèmes différentiels à coefficients constants

### Version vectorielle

**Proposition 13**
Soit $a \in \mathcal{L}(E)$ et $(t_0, x_0) \in \mathbb{R} \times E$. L'application :
$$\begin{aligned} \varphi : \mathbb{R} &\longrightarrow E \\ t &\longmapsto \exp((t - t_0)a) \cdot x_0 \end{aligned}$$
est l'unique solution du problème de Cauchy :
$$x' = a \cdot x \quad \text{et} \quad x(t_0) = x_0.$$

**Démonstration.** L'application $\varphi$ est solution du problème de Cauchy considéré puisque :
$$\forall t \in \mathbb{R} \quad \varphi'(t) = \left( a \circ \exp((t - t_0)a) \right) \cdot x_0 = a \cdot \varphi(t)$$
$$\varphi(t_0) = \exp((t_0 - t_0)a) \cdot x_0 = \exp(0) \cdot x_0 = \text{Id}_E \cdot x_0 = x_0.$$
D'après le théorème de Cauchy linéaire, c'est l'unique solution.

**Corollaire 14**
Soit $a \in \mathcal{L}(E)$ et $x_0 \in E$. L'application :
$$\begin{aligned} \varphi : \mathbb{R} &\longrightarrow E \\ t &\longmapsto \exp(ta) \cdot x_0 \end{aligned}$$
est l'unique solution sur $\mathbb{R}$ du problème de Cauchy :
$$x' = a \cdot x \quad \text{et} \quad x(0) = x_0.$$

### Version matricielle

**Proposition 15 (Résolution d'un problème de Cauchy)**
Soit $A \in \mathcal{M}_n(\mathbb{K})$ et $(t_0, X_0) \in \mathbb{R} \times \mathbb{K}^n$. L'application :
$$\varphi : t \mapsto \exp((t - t_0)A)X_0$$
est l'unique solution du problème de Cauchy :
$$X' = AX \quad \text{et} \quad X(t_0) = X_0.$$

1028

**Corollaire 16**

# II Équations différentielles linéaires du premier ordre à coefficients constants

## **Corollaire 16**



Soit $A \in \mathcal{M}_n(\mathbb{K})$ et $X_0 \in \mathbb{K}^n$. L'application :

$$\begin{aligned} \varphi : \mathbb{R} &\longrightarrow \mathcal{M}_n(\mathbb{K}) \\ t &\longmapsto \exp(tA) X_0 \end{aligned}$$

est l'unique solution sur $\mathbb{R}$ du problème de Cauchy :

$$X' = AX \quad \text{et} \quad X(0) = X_0.$$

## Propriétés classiques de l’exponentielle

On retrouve, par ces résultats, des propriétés classiques de « l’exponentielle ».

### Version vectorielle

## **Proposition 17**

## **Proposition 17**

Soit $a$ un endomorphisme de $E$. On a alors :

$$\forall(*s, t*) \in \mathbb{R}^2 \quad \exp(t a) \circ \exp(s a) = \exp((t + s) a).$$


Démonstration page 1059


## **Corollaire 18**

## **Corollaire 18**

Soit $a \in \mathcal{L}(E)$.

Pour tout $t \in \mathbb{R}$, l'endomorphisme $\exp(t a)$ est inversible et :

$$\forall t \in \mathbb{R} \quad \exp(-t a) = (\exp(t a))^{-1}.$$


Démonstration page 1060


## **Proposition 19**

## **Proposition 19**

Soit $a$ et $b$ des endomorphismes de $E$ qui commutent. Alors on a :

$$\exp(a) \circ \exp(b) = \exp(a + b) = \exp(b) \circ \exp(a).$$


Démonstration page 1060


### Version matricielle

## **Proposition 20**

# **Proposition 20**

Soit $A \in \mathcal{M}_n(\mathbb{K})$. On a :

$$\forall (*s, t*) \in \mathbb{R}^2 \quad \exp(t A) \exp(s A) = \exp ((t + s) A).$$

## **Corollaire 21**

# **Corollaire 21**

Soit $A \in \mathcal{M}_n(\mathbb{K})$.

Pour tout $t \in \mathbb{R}$, la matrice $\exp(t A)$ est inversible et l'on a :

$$(\exp(t A))^{-1} = \exp(-t A).$$

## **Proposition 22**

**Proposition 22**
***

Soit $A$ et $B$ des matrices de $\mathcal{M}_n(\mathbb{K})$ tels que $AB = BA$. Alors on a :

$$\exp(A) \exp(B) = \exp(A + B) = \exp(B) \exp(A).$$

1029

Chapitre 17. Équations différentielles linéaires

## Expression explicite des solutions à un problème de Cauchy

p.1060

**Exercice 17** On considère une équation différentielle à coefficients constants :
$$(E) : x' = a \cdot x + b(t) \quad \text{avec} \quad a \in \mathcal{L}(E) \quad \text{et} \quad b \in \mathcal{C}(I, E).$$
Soit $(t_0, x_0) \in I \times E$. Montrer que le problème de Cauchy :
$$x' = a \cdot x + b(t) \quad \text{et} \quad x(t_0) = x_0$$
admet comme unique solution :
$$\begin{aligned} \varphi : I & \longrightarrow E \\ t & \longmapsto \exp((t - t_0)a) \cdot x_0 + \int_{t_0}^t \exp((t - s)a) \cdot b(s) \, ds. \end{aligned}$$

**Remarque** L’expression explicite des solutions obtenue dans l’exercice précédent n’est pas d’un grand intérêt pratique, car il est souvent plus pratique de réduire la matrice associée à $a$ que de calculer son exponentielle.
En revanche, elle peut se révéler utile dans certains exercices théoriques (*cf.* exercice 17.15 de la page 1077).

# III Équations différentielles linéaires scalaires d’ordre $n$

On suppose ici que $n$ est un entier naturel non nul.
Le cas $n = 1$ a été étudié en première année, ainsi que celui des équations différentielles linéaires scalaires d’ordre 2 à coefficients constants.

## 1 Définition

**Définition 5**
Soit $(a_k)_{k \in \llbracket 0, n-1 \rrbracket}$ une famille de $n$ applications continues de $I$ dans $\mathbb{K}$ et $b$ une application continue de $I$ dans $\mathbb{K}$. On appelle **équation différentielle linéaire scalaire d’ordre** $n$ une équation de la forme :
$$x^{(n)} + \sum_{k=0}^{n-1} a_k(t) x^{(k)} = b(t). \quad (E)$$

On appelle **solution** de l’équation différentielle linéaire (E) toute application $n$ fois dérivable $\varphi : I \to \mathbb{K}$ vérifiant :
$$\forall t \in I \quad \varphi^{(n)}(t) + \sum_{k=0}^{n-1} a_k(t) \varphi^{(k)}(t) = b(t).$$

1030

# III Équations différentielles linéaires scalaires d’ordre $n$

*   L’application $b \in \mathcal{C}(I, \mathbb{K})$ s’appelle le **second membre** de (E).
*   On dit que l’équation (E) est à **coefficients constants** si toutes les fonctions $a_k$ sont constantes et qu’elle est **homogène** ou **sans second membre** si $b = 0$.
*   On appelle **équation homogène** associée à (E), l’équation :
$$x^{(n)} + \sum_{k=0}^{n-1} a_k(t)x^{(k)} = 0 \quad \quad (E_0)$$

**Remarque** L’équation (E) dans la définition 5 de la page ci-contre est écrite sous une forme dite **résolue**, ce qui signifie que le coefficient devant $x^{(n)}$ vaut 1. Si une équation différentielle linéaire scalaire d’ordre $n$ apparaît sous une forme **non résolue**, c’est-à-dire :
$$\alpha_n(t) x^{(n)} + \alpha_{n-1}(t) x^{(n-1)} + \dots + \alpha_0(t) x = b(t).$$
alors :
*   si la fonction $\alpha_n$ ne s’annule pas sur $I$, on divise par $\alpha_n$ pour se ramener à une forme résolue ;
*   sinon, le problème est plus délicat : quelques exemples de telles équations seront vus dans la partie V.

<mark>p.1061</mark> **Exercice 18** *Régularité des solutions*
Soit $p \in \mathbb{N}$. Montrer que si les applications $a_0, \dots, a_{n-1}, b$ sont de classe $\mathcal{C}^p$, alors toute solution de (E) est de classe $\mathcal{C}^{n+p}$.

**Remarque** En particulier, puisque les applications $a_0, \dots, a_{n-1}, b$ sont *a minima* supposées continues, toute solution de (E) est de classe $\mathcal{C}^n$.

## 2 Traduction sous la forme d’un système différentiel linéaire d’ordre 1

Nous reprenons ici les notations de la définition 5 de la page précédente. Considérons les applications $A : I \to \mathcal{M}_n(\mathbb{K})$ et $B : I \to \mathbb{K}^n$ définies par :

$$
A(t) = \begin{pmatrix} 
0 & 1 & & & \\
\vdots & \ddots & \ddots & & (0) \\
\vdots & & \ddots & \ddots & \\
0 & \dots & \dots & 0 & 1 \\
-a_0(t) & -a_1(t) & \dots & \dots & -a_{n-1}(t)
\end{pmatrix} \quad \text{et} \quad B(t) = \begin{pmatrix} 
0 \\
\vdots \\
0 \\
b(t)
\end{pmatrix}.
$$

1031

# Chapitre 17. Équations différentielles linéaires

**Remarque** Pour tout $t$, la matrice $A(t)$ est la transposée de la matrice compagnon (*cf.* page 81) du polynôme $X^n + a_{n-1}(t)X^{n-1} + \dots + a_0(t)$.

Les applications $A$ et $B$ ainsi définies permettent de traduire l'équation différentielle scalaire (E) sous la forme d'un système différentiel d'ordre 1.

### **Proposition 23**
Une fonction $\varphi : I \to \mathbb{K}$ est solution de l'équation différentielle (E) si, et seulement si, l'application $\Phi : t \longmapsto \begin{pmatrix} \varphi(t) \\ \vdots \\ \varphi^{(n-1)}(t) \end{pmatrix}$ est solution du système différentiel d'ordre 1 :
$$X' = A(t)X + B(t). \tag{EM}$$


Démonstration page 1061



La proposition précédente ramène ainsi l'étude des équations différentielles scalaires d'ordre $n$ à celle des systèmes différentiels du premier ordre. Les résultats qui suivent sont donc des conséquences immédiates de ceux établis dans la partie I.

## Propriétés linéaires

### **Proposition 24 (Structure de l'ensemble des solutions)**
* L'ensemble $\mathcal{S}_0$ des solutions de l'équation homogène (E$_0$) est un sous-espace vectoriel de $\mathcal{C}^n(I, \mathbb{K})$.
* Si $\varphi_P$ est une solution de (E), alors l'ensemble $\mathcal{S}$ des solutions sur $I$ de l'équation de (E) est le sous-espace affine de $\mathcal{C}^n(I, \mathbb{K})$ passant par $\varphi_P$ et de direction $\mathcal{S}_0$ :
$$\mathcal{S} = \varphi_P + \mathcal{S}_0.$$

### **Proposition 25 (Principe de superposition)**
Soit $(\alpha_1, \alpha_2) \in \mathbb{K}^2$ et $(b_1, b_2) \in \mathcal{C}^0(I, \mathbb{K})^2$ tels que $b = \alpha_1 b_1 + \alpha_2 b_2$.
Si $\varphi_1$ et $\varphi_2$ sont respectivement solutions des équations :
$$x^{(n)} + \sum_{k=0}^{n-1} a_k(t) x^{(k)} = b_1(t)$$
$$x^{(n)} + \sum_{k=0}^{n-1} a_k(t) x^{(k)} = b_2(t)$$
alors la fonction $\alpha_1 \varphi_1 + \alpha_2 \varphi_2$ est solution de (E).

1032

III Équations différentielles linéaires scalaires d'ordre $n$

## Problème de Cauchy

Reprenons les notations de la proposition 23 de la page ci-contre.
Le théorème de Cauchy linéaire pour les systèmes différentiels nous assure que pour tout couple $(t_0, X_0) \in I \times \mathbb{K}^n$, il existe une unique solution $\Phi$ au système différentiel (EM) vérifiant la condition initiale :

$$\Phi(t_0) = X_0.$$

Puisque $\Phi(t_0) = \begin{pmatrix} \varphi(t_0) \\ \vdots \\ \varphi^{(n-1)}(t_0) \end{pmatrix}$, on constate que fixer une condition initiale de la forme $\Phi(t_0) = X_0$ revient à fixer les valeurs de $\varphi(t_0), \dots, \varphi^{(n-1)}(t_0)$. Cela mène à la version suivante du théorème de Cauchy linéaire :

### **Théorème 26 (Théorème de Cauchy linéaire)**
Pour tout $(t_0, x_0, \dots, x_{n-1}) \in I \times \mathbb{K}^n$, il existe une et une seule solution $\varphi$ de (E) vérifiant :
$$\forall k \in \llbracket 0, n - 1 \rrbracket \quad \varphi^{(k)}(t_0) = x_k.$$

**Exemple** Sans calculs, le théorème de Cauchy linéaire assure l’existence et l’unicité de la solution sur $\mathbb{R}$ du problème de Cauchy suivant :
$$x'' + \sin(t) x' + \cos(t) x = t \quad \text{et} \quad (x(0), x'(0)) = (1, 0).$$

## Espace des solutions de l’équation homogène

### **Proposition 27**
Soit $t_0 \in I$. L’application :
$$\begin{aligned} \mathcal{S}_0 &\longrightarrow \mathbb{K}^n \\ \varphi &\longmapsto (\varphi(t_0), \dots, \varphi^{(n-1)}(t_0)) \end{aligned}$$
est un isomorphisme d’espaces vectoriels.

### **Corollaire 28**
L’espace $\mathcal{S}_0$ des solutions de l’équation différentielle homogène $(E_0)$ est de dimension $n$.

1033

Chapitre 17. *Équations différentielles linéaires*

p.1062 **Exercice 19** On s’intéresse à une équation différentielle linéaire scalaire homogène à coefficients constants :

$$x^{(n)} + \sum_{k=0}^{n-1} a_k x^{(k)} = 0. \tag{E$_0$}$$

1. Montrer que, pour $\lambda \in \mathbb{C}$, la fonction $f_\lambda : t \mapsto e^{\lambda t}$ est solution de (E$_0$) si, et seulement si, $\lambda$ est racine du polynôme :
   $$P = X^n + \sum_{k=0}^{n-1} a_k X^k.$$

2. En déduire que si le polynôme $P$ est scindé à racines simples $\lambda_1, \dots, \lambda_n$, alors l’ensemble $\mathcal{S}_0$ des solutions de (E$_0$) est :
   $$\mathcal{S}_0 = \text{Vect} (f_{\lambda_1}, \dots, f_{\lambda_n}).$$

# IV Équations différentielles linéaires scalaires d’ordre 2

Nous étudions dans ce qui suit une équation linéaire scalaire du second ordre de la forme :

$$x'' + a_1(t)x' + a_0(t)x = b(t) \tag{E}$$

où $a_0$, $a_1$ et $b$ sont des fonctions continues de $I$ dans $\mathbb{K}$. Cette équation étant un cas particulier des équations linéaire scalaire d’ordre $n$ évoquées dans la partie précédente, on a les propriétés suivantes :

* l’équation (E) s’interprète sous la forme du système différentiel :
  $$X' = A(t)X + B(t) \tag{EM}$$
  avec, pour tout $t \in I$ :

$$A(t) = \begin{pmatrix} 0 & 1 \\ -a_0(t) & -a_1(t) \end{pmatrix} \text{ et } B(t) = \begin{pmatrix} 0 \\ b(t) \end{pmatrix}$$

* l’espace vectoriel $\mathcal{S}_0$ des solutions de l’équation homogène (E$_0$) associée à (E) est de dimension 2 ;
* si $\varphi_P$ est une solution de (E), alors l’ensemble $\mathcal{S}$ des solutions de (E) est :
  $$\mathcal{S} = \varphi_P + \mathcal{S}_0 ;$$
* le théorème de Cauchy linéaire assure l’existence et l’unicité d’une solution $\varphi$ de (E) vérifiant une condition initiale de la forme :
  $$(\varphi(t_0), \varphi'(t_0)) = (x_0, x_1) \quad \text{avec} \quad (t_0, x_0, x_1) \in I \times \mathbb{K}^2.$$

1034

IV Équations différentielles linéaires scalaires d'ordre 2

# 1 Wronskien

## Définition et propriétés

**Définition 6**
***
Soit $\varphi_1, \varphi_2$ deux solutions de l'équation homogène $(E_0)$.
On appelle **wronskien** de la famille $(\varphi_1, \varphi_2)$ l'application :

$$
\begin{aligned}
W_{\varphi_1, \varphi_2} : I & \longrightarrow \mathbb{K} \\
t & \longmapsto \det \begin{pmatrix} \varphi_1(t) & \varphi_2(t) \\ \varphi_1'(t) & \varphi_2'(t) \end{pmatrix}.
\end{aligned}
$$
***

**Remarque** On a :
$$\forall t \in I \quad W_{\varphi_1, \varphi_2}(t) = \varphi_1(t) \varphi_2'(t) - \varphi_1'(t) \varphi_2(t).$$

Comme $\varphi_1$ et $\varphi_2$ sont solutions de $(E_0)$, elles sont deux fois dérivables, donc $W_{\varphi_1, \varphi_2}$ est dérivable. De plus, sa dérivée se simplifie ainsi :
$$W_{\varphi_1, \varphi_2}' = \varphi_1 \varphi_2'' - \varphi_1'' \varphi_2.$$

**Proposition 29**
***
Le wronskien d'un couple $(\varphi_1, \varphi_2) \in (\mathcal{S}_0)^2$ est solution sur $I$ de l'équation différentielle linéaire homogène d'ordre 1 :
$$x' + a_1(t) x = 0.$$
***

> Démonstration page 1062

**Remarque** Si l'équation différentielle considérée est de la forme :
$$(E) : x'' + q(t)x = 0 \quad \text{avec} \quad q : I \to \mathbb{K} \text{ une fonction continue,}$$
alors le wronskien $W_{\varphi_1, \varphi_2}$ d'un couple $(\varphi_1, \varphi_2) \in (\mathcal{S}_0)^2$ vérifie $W_{\varphi_1, \varphi_2}' = 0$ et donc, $I$ étant un intervalle, il est constant sur $I$.

Le wronskien de $(\varphi_1, \varphi_2) \in (\mathcal{S}_0)^2$, en tant que solution d'une équation différentielle linéaire scalaire homogène d'ordre 1 :
* ou bien est la fonction nulle ;
* ou bien ne s'annule pas sur $I$.

Plus précisément, on a le résultat suivant :

1035

Chapitre 17. Équations différentielles linéaires

## **Proposition 30**

## **Proposition 30**

Soit $\varphi_1$ et $\varphi_2$ des solutions de $(E_0)$. Notons $W$ le wronskien de $(\varphi_1, \varphi_2)$.
Les trois assertions suivantes sont équivalentes :

$(i)$ $(\varphi_1, \varphi_2)$ est une base de $\mathcal{S}_0$ ;

$(ii)$ $\exists t \in I \quad W(t) \neq 0$ ;

$(*iii*)$ $\forall t \in I \quad W(t) \neq 0$.


<mark>Démonstration page 1063</mark>


p.1063

**Exercice 20** Justifier que les fonctions $\varphi_1 : t \mapsto \cos(t)$ et $\varphi_2 : t \mapsto t$ ne sont pas solutions sur $\mathbb{R}$ d'une même équation différentielle linéaire homogène de la forme :

$$x'' + a(t)x' + b(t)x = 0 \quad \text{avec } a \text{ et } b \text{ continues sur } \mathbb{R}.$$

### Utilisation du wronskien

Connaissant une solution non nulle de l’équation homogène $(E_0)$, l’utilisation du wronskien permet en général de terminer la résolution de $(E_0)$.

### **Point méthode**

# **Point méthode**

Supposons connue une solution $\varphi_1$ de $(E_0)$. Comme $\dim(\mathcal{S}_0) = 2$, il reste à déterminer une solution non proportionnelle à $\varphi_1$.

*   Pour $\varphi \in \mathcal{S}_0$, l'équation différentielle linéaire scalaire du premier ordre vérifiée par le wronskien $W$ de $(\varphi_1, \varphi)$ permet d'en obtenir une expression, à une constante proportionnelle près.
*   Sur un intervalle où $\varphi_1$ ne s'annule pas, on peut considérer la fonction $\left( \frac{\varphi}{\varphi_1} \right)$ dont la dérivée est donnée par :

$$ \left( \frac{\varphi}{\varphi_1} \right)' = \frac{\varphi' \varphi_1 - \varphi \varphi'_1}{\varphi_1^2} = \frac{W}{\varphi_1^2} . $$

En primitivant, on obtient alors une expression de $\frac{\varphi}{\varphi_1}$ puis de $\varphi$ comme combinaison linéaire de deux fonctions.

### Mise en oeuvre sur un exemple

Supposons que l’on souhaite résoudre sur $]0, +\infty[$ l’équation différentielle :

$$(\text{E}_0) : x'' + \frac{x'}{t} - \frac{x}{t^2} = 0,$$

et que l’on a déjà constaté que la fonction $\varphi_1 : t \mapsto t$ est solution. On sait que l’espace $\mathcal{S}_0$ des solutions de $(\text{E}_0)$ est de dimension 2. Pour terminer la résolution il reste donc à obtenir une solution non proportionnelle à $\varphi_1$.

1036

# IV Équations différentielles linéaires scalaires d’ordre 2

• Soit $\varphi$ une solution de $(E_0)$. Le wronskien $W$ de la famille $(\varphi_1, \varphi)$ est solution sur $I$ de l’équation différentielle d’ordre 1 :
$$x' + \frac{1}{t} x = 0.$$

En résolvant cette équation, on obtient $W(t) = \frac{\lambda}{t}$ avec $\lambda \in \mathbb{R}$.

D’autre part, comme $\varphi_1$ ne s’annule pas sur $]0, +\infty[$, on peut considérer la fonction $\left( \frac{\varphi}{\varphi_1} \right)$ dont la dérivée vérifie :
$$\left( \frac{\varphi}{\varphi_1} \right)' = \frac{\varphi' \varphi_1 - \varphi \varphi'_1}{\varphi_1^2} = \frac{W}{\varphi_1^2}.$$

Ainsi, on a :
$$\forall t \in ]0, +\infty[ \quad \left( \frac{\varphi}{\varphi_1} \right)' = \frac{\lambda}{t^3}.$$

Il en résulte qu’il existe $\mu \in \mathbb{R}$ tel que pour tout $t \in ]0, +\infty[$ :
$$\frac{\varphi(t)}{\varphi_1(t)} = -\frac{\lambda}{2t^2} + \mu \quad \text{puis} \quad \varphi(t) = -\frac{\lambda}{2t} + \mu t.$$

On a donc $\varphi \in \text{Vect}(\varphi_1, \varphi_2)$ avec $\varphi_2 : t \mapsto \frac{1}{t}$.

• On peut alors conclure la résolution de $(E_0)$ par différents arguments.

* **Premier argument.** Il est facile de vérifier que la fonction $\varphi_2$ est solution de $(E_0)$ et que $\varphi_1$ et $\varphi_2$ sont non proportionnelles. Par suite, comme $\dim \mathcal{S}_0 = 2$, on a nécessairement $\mathcal{S}_0 = \text{Vect}(\varphi_1, \varphi_2)$.
* **Second argument.** Dans la première partie du raisonnement on a obtenu :
$$\mathcal{S}_0 \subset \text{Vect}(\varphi_1, \varphi_2).$$
Comme $\dim \mathcal{S}_0 = 2$, on a nécessairement $\mathcal{S}_0 = \text{Vect}(\varphi_1, \varphi_2)$ (et, sans avoir besoin de le vérifier, on peut affirmer que $\varphi_2$ est une solution de $(E_0)$ et qu’elle est linéairement indépendante de $\varphi_1$).

**Remarque** L’exemple précédent est favorable car la solution $\varphi_1$ dont on est parti ne s’annule pas sur l’intervalle de résolution. Il peut arriver que cette fonction $\varphi_1$ s’annule, auquel cas il faut se restreindre à un sous-intervalle $J \subset I$ sur lequel elle ne s’annule pas. La relation :
$$\forall t \in J \quad \varphi = \lambda \varphi_1(t) + \mu \varphi_2(t)$$
obtenue ne permet pas de conclure directement ; en revanche, si $\varphi_2$ est définie sur $I$ tout entier et que l’on pense qu’elle est solution, alors il est facile de le montrer (*cf.* exercice suivant).

1037

Chapitre 17. Équations différentielles linéaires

<mark>p.1064</mark> **Exercice 21** On souhaite résoudre sur $]0, +\infty[$ l’équation différentielle homogène :

$$(E_0) : x'' + \frac{2}{t}x' + x = 0.$$

1. Vérifier que la fonction $\varphi_1 : t \mapsto \frac{\sin t}{t}$ est solution.
2. En utilisant le wronskien, terminer la résolution de $(E_0)$.

**Remarque** La solution $\varphi : t \mapsto \frac{\sin t}{t}$ de $(E_0)$ peut s’obtenir par technique « recherche de solutions développables en série entière » (*cf.* exemple de la page de la page 1041).

### Méthode alternative à la méthode précédente : variation de la constante
Connaissant une solution non nulle $\varphi_1$ de l’équation homogène $(E_0)$, on dispose d’une méthode alternative à la méthode précédente, appelée *méthode de variation de la constante*.
Elle consiste à rechercher d’autres solutions de $(E_0)$ sous la forme :
$$\varphi = \lambda \varphi_1 \quad \text{avec } \lambda \text{ une fonction deux fois dérivable.}$$
On a alors :
$$\varphi' = \lambda' \varphi_1 + \lambda \varphi_1' \quad \text{et} \quad \varphi'' = \lambda'' \varphi_1 + 2 \lambda' \varphi_1' + \lambda \varphi_1'',$$
puis, lorsque l’on injecte $\varphi$ dans l’équation $(E_0)$, le fait que $\varphi_1$ soit solution nous mène à une équation différentielle linéaire d’ordre 1 en $\lambda'$. Sur un intervalle où $\varphi_1$ ne s’annule pas, on peut alors déterminer $\lambda'$ et obtenir une expression de $\varphi$.
Cette méthode de variation de la constante ne figure pas au programme.

## 2 Recherche d’une solution particulière : méthode de variation des constantes
Nous allons ici adapter la méthode (*cf.* point méthode de la page 1020) visant, pour un système différentiel d’ordre 1, à déterminer une solution particulière connaissant une base de l’espace des solutions de l’équation homogène associée. Rappelons que l’équation $(E)$ s’interprète matriciellement (*cf.* page 1034) :
$$X' = A(t)X + B(t) \quad \quad \text{(EM)}$$
Supposons connue $(\varphi_1, \varphi_2)$ une base de l’espace $\mathcal{S}_0$ des solutions de l’équation homogène $(E_0)$. Alors, les applications :
$$\Phi_1 : t \mapsto \begin{pmatrix} \varphi_1(t) \\ \varphi_1'(t) \end{pmatrix} \quad \text{et} \quad \Phi_2 : t \mapsto \begin{pmatrix} \varphi_2(t) \\ \varphi_2'(t) \end{pmatrix}$$

1038

IV Équations différentielles linéaires scalaires d'ordre 2

forment une base de l’espace des solutions du système différentiel homogène :
$$X' = A(t)X \quad (\text{EM}_0)$$

La méthode de variation des constantes consiste alors à chercher une solution particulière de (EM) sous la forme :
$$\Phi = \lambda_1 \Phi_1 + \lambda_2 \Phi_2 \quad \text{avec } \lambda_1 \text{ et } \lambda_2 \text{ dérivables de } I \text{ dans } \mathbb{K},$$
et l’on a :

$$(\Phi \text{ solution de (EM)}) \iff \lambda'_1 \Phi_1 + \lambda'_2 \Phi_2 = B$$

$$\iff \begin{cases} \lambda'_1 \varphi_1 + \lambda'_2 \varphi_2 &= 0 \\ \lambda'_1 \varphi'_1 + \lambda'_2 \varphi'_2 &= b. \end{cases}$$

Puisque la famille $(\varphi_1, \varphi_2)$ est une base de $\mathcal{S}_0$, son wronskien ne s’annule pas. Donc, pour tout $t \in I$, le système :

$$
\begin{cases}
\lambda'_1(t) \varphi_1(t) + \lambda'_2(t) \varphi_2(t) & = 0 \\
\lambda'_1(t) \varphi'_1(t) + \lambda'_2(t) \varphi'_2(t) & = b(t)
\end{cases}
$$

permet de déterminer $\lambda'_1(t)$ et $\lambda'_2(t)$. Puis, en primitivant, on obtient une solution $\Phi$ de (EM). Cela fournit une solution de (E) car la solution $\Phi$ de (EM) obtenue est de la forme $\begin{pmatrix} \varphi \\ \varphi' \end{pmatrix}$ avec $\varphi$ une solution de (E).

### **Point méthode (Méthode de variation des constantes)**

Si l’on connaît une base $(\varphi_1, \varphi_2)$ de l’espace des solutions de $(\text{E}_0)$, alors on peut rechercher une solution particulière de (E) sous la forme :
$$\varphi = \lambda_1 \varphi_1 + \lambda_2 \varphi_2 \quad \text{avec } \lambda_1 \text{ et } \lambda_2 \text{ dérivables sur } I.$$
Une telle fonction $\varphi$ est solution de (E) si, et seulement si :
$$\begin{cases} \lambda'_1 \varphi_1 + \lambda'_2 \varphi_2 &= 0 \\ \lambda'_1 \varphi'_1 + \lambda'_2 \varphi'_2 &= b \end{cases}$$
On peut alors déterminer $\lambda'_1$ et $\lambda'_2$, puis $\lambda_1$ et $\lambda_2$ par calcul de primitives.

**Exemple** Intéressons-nous sur $]0, +\infty[$ à l’équation différentielle suivante :
$$(\text{E}) : x'' + \frac{1}{t}x' - \frac{1}{t^2}x = \frac{4 \ln t}{t}.$$
L’équation homogène a été résolue précédemment (*cf.* exemple de la page 1036) :
$$\mathcal{S}_0 = \text{Vect}(\varphi_1, \varphi_2) \quad \text{avec} \quad \varphi_1 : t \mapsto t \quad \text{et} \quad \varphi_2 : t \mapsto \frac{1}{t}.$$

1039

# Chapitre 17. *Équations différentielles linéaires*

Cherchons une solution particulière sous la forme $\varphi = \lambda_1 \varphi_1 + \lambda_2 \varphi_2$.
Une telle fonction $\varphi$ est solution si, et seulement si :

$$
\begin{cases}
\lambda'_1 \varphi_1 + \lambda'_2 \varphi_2 = 0 \\
\lambda'_1 \varphi'_1 + \lambda'_2 \varphi'_2 = \left( t \mapsto \frac{4 \ln t}{t} \right)
\end{cases}
$$

ce qui se traduit par :

$$\forall t \in ]0, +\infty[ \quad \begin{cases} t \lambda'_1(t) + \frac{1}{t} \lambda'_2(t) & = \quad 0 \\ \lambda'_1(t) - \frac{1}{t^2} \lambda'_2(t) & = \quad \frac{4 \ln t}{t} \end{cases}$$

et mène à :

$$\forall t \in ]0, +\infty[ \quad \lambda'_1(t) = \frac{2 \ln t}{t} \quad \text{et} \quad \lambda'_2(t) = -2 t \ln t.$$

Après primitivation, on peut choisir :

$$\lambda_1 : t \mapsto \ln^2 t \quad \text{et} \quad \lambda_2 : t \mapsto \frac{t^2}{2} - t^2 \ln t,$$

et obtenir la solution de (E) donnée par :

$$\begin{aligned} \varphi(t) &= (\ln^2 t) t + \left( \frac{t^2}{2} - t^2 \ln t \right) \frac{1}{t} \\ &= t \ln^2 t - t \ln t + \frac{t}{2}. \end{aligned}$$

On peut alors conclure la résolution de (E). Les solutions réelles de (E) sont les fonctions de la forme :

$$\begin{aligned} ]0, +\infty[ &\longrightarrow \mathbb{R} & \text{avec } (\lambda, \mu) \in \mathbb{R}^2. \\ t &\longmapsto t \ln^2 t - t \ln t + \frac{t}{2} + \lambda t + \frac{\mu}{t} \end{aligned}$$

<mark>
**p.1065** **Exercice 22** Résoudre sur $]0, +\infty[$ l'équation différentielle :

$$(E) : x'' + \frac{2}{t} x' + x = t.$$

sachant qu'il a été obtenu à l'exercice 21 que l'espace des solutions de l'équation homogène est :

$$\mathcal{S}_0 = \text{Vect}(\varphi_1, \varphi_2) \quad \text{avec} \quad \varphi_1 : t \mapsto \frac{\sin t}{t} \quad \text{et} \quad \varphi_2 : t \mapsto \frac{\cos t}{t}.$$
</mark>

1040

IV Équations différentielles linéaires scalaires d'ordre 2

# 3 Techniques classiques d'obtention d'une solution de l'équation homogène

Lorsque l'on cherche à résoudre une équation différentielle de la forme :

$$x'' + a_1(t)x' + a_0(t)x = b(t), \tag{E}$$

ce qui a été fait précédemment nous dit que :

* à partir d'une solution non nulle de l'équation homogène $(E_0)$, la méthode du wronskien permet de terminer la résolution de $(E_0)$ ;
* à partir d'une base de $\mathcal{S}_0$, la méthode de variation des constantes permet d'obtenir une solution particulière et ainsi d'achever la résolution de $(E)$.

Par conséquent, il apparaît que l'étape manquante est l'obtention d'une solution non nulle de l'équation homogène $(E_0)$. Il n'existe pas méthode systématique pour déterminer une telle solution.

L'objet de cette partie est de présenter quelques techniques pouvant se révéler utiles. Ces techniques ne sont pas réservées aux équations d'ordre 2 et peuvent être mises en place pour des équations d'ordre supérieur.

## Recherche de solutions « simples »

Selon l'allure de l'équation, il peut être pertinent de rechercher une solution sous une forme explicite : fonctions polynomiales, exponentielles, trigonométriques, ...

<mark>p.1065</mark> ### **Exercice 23** *Recherche d'une solution polynomiale*

Considérons sur $\mathbb{R}$ l'équation homogène :

$$(t^2 + 2t - 1) x'' + (t^2 - 3) x' - (2t + 2) x = 0. \hfill (\mathrm{E}_0)$$

1. Soit $t \mapsto P(t)$ une solution polynomiale non nulle de $(E_0)$.
   Montrer que $\deg(P) = 2$.
2. Obtenir alors toutes les fonctions polynomiales solutions de $(E_0)$.

## Recherche de solutions développables en série entière

**Exemple** Considérons sur $\mathbb{R}$ l'équation homogène :

$$(E_0) : tx'' + 2x' + tx = 0.$$

Recherchons les solutions de $(E_0)$ développables en série entière.

* Dans un premier temps, supposons que $\varphi$ soit une solution de $(E_0)$ développable en série entière sur un intervalle de la forme $]-r, r[$ avec $r > 0$.
  Pour $t \in ]-*r, r*[$, on a :

$$\varphi(t) = \sum_{<sub>n=0</sub>}^{+\infty} a_n t^n \quad \varphi'(t) = \sum_{<sub>n=1</sub>}^{+\infty} n a_n t^{n-1} \quad \text{et} \quad \varphi''(t) = \sum_{<sub>n=2</sub>}^{+\infty} n(n-1) a_n t^{n-2}.$$

1041

# Chapitre 17. *Équations différentielles linéaires*

En reportant dans l’équation $(E_0)$, on a, pour tout $t \in ]-*r, r*[$ :

$$t \sum_{n=2}^{+\infty} n(n-1) a_n t^{n-2} + 2 \sum_{n=1}^{+\infty} n a_n t^{n-1} + t \sum_{n=0}^{+\infty} a_n t^n = 0.$$

puis en réindexant les sommes pour obtenir dans chacune d’entre elles des $t^n$ :

$$\sum_{n=1}^{+\infty} n(n+1)a_{n+1} t^n + 2 \sum_{n=0}^{+\infty} (n+1)a_{n+1} t^n + \sum_{n=1}^{+\infty} a_{n-1} t^n = 0,$$

ce qui donne, en regroupant les sommes :

$$2 a_1 + \sum_{n=1}^{+\infty} ((n + 1)(n + 2)a_{n+1} + a_{n-1})t^n = 0.$$

Par unicité du développement en série entière, on peut identifier les coefficients :

$$a_1 = 0 \quad \text{et} \quad \forall n \geqslant 1 \quad (n+1)(n+2)a_{n+1} + a_{n-1} = 0. \hfill (\star)$$

Il en résulte que :

$$\forall n \in \mathbb{N} \quad a_{2n+1} = 0 \quad \text{et} \quad a_{2n} = \frac{(-1)^n}{(2n+1)!} a_0.$$

Par suite, on a :

$$\varphi(t) = a_0 \sum_{n=0}^{+\infty} \frac{(-1)^n}{(2n + 1)!} t^{2n}$$

• Réciproquement :

* le rayon de convergence de la série entière $\sum \frac{(-1)^n}{(2n+1)!} t^{2n}$ vaut $+\infty$ (on le montre par exemple par le critère de d’Alembert) ;
* la fonction :

$$\varphi_1 : t \mapsto \sum_{n=0}^{+\infty} \frac{(-1)^n}{(2n + 1)!} t^{2n}$$

est telle que ses coefficients vérifient la propriété $(\star)$, et par suite, d’après les calculs effectués dans la première partie du raisonnement, $\varphi$ est solution de $(E_0)$ sur $\mathbb{R}$.

* On peut simplifier l’expression de cette solution $\varphi_1$ en remarquant que :

$$\forall t \in \mathbb{R} \quad t \varphi(t) = \sum_{n=0}^{+\infty} \frac{(-1)^n}{(2n+1)!} t^{2n+1} = \sin t,$$

et donc finalement :

$$\varphi(0) = 1 \quad \text{et} \quad \forall t \in \mathbb{R}^* \quad \varphi(t) = \frac{\sin t}{t}.$$

**Remarque** L’équation différentielle considérée dans cet exemple est la même que celle de l’exercice 21 de la page 1038, à ceci près que, dans l’exercice 21, elle n’a été considérée que sur l’intervalle $]0, +\infty[$ et a été mise sous forme résolue.

1042

# IV Équations différentielles linéaires scalaires d'ordre 2

**p.1066** **Exercice 24** Considérons, sur $\mathbb{R}$, l'équation homogène :

$$(E_0) : 4 t x'' + 2 x' - x = 0.$$

1. Déterminer une solution $\varphi_1$ de $(E_0)$ développable en série entière vérifiant $\varphi_1(0) = 1$.
2. On se place dans cette question sur l'intervalle $]0, +\infty[$.(a) Exprimer $\varphi_1$ à l'aide de la fonction $\text{ch}$.(b) À l'aide de la méthode du wronskien, conclure la résolution de $(E_0)$.
3. On se place dans cette question sur l'intervalle $]-\infty, 0[$.(a) Exprimer $\varphi_1$ à l'aide de la fonction $\cos$.(b) À l'aide de la méthode du wronskien, conclure la résolution de $(E_0)$.

**Remarque** La résolution sur $\mathbb{R}$ tout entier de l'équation $(E)$ de l'exercice précédent est faite à l'exercice 29 de la page 1046.

## Changement de variables

Dans certains cas, l'équation différentielle $(E)$ se traduit de manière plus simple sur une fonction de la forme $u \mapsto x(\theta(u))$ (idéalement, une équation à coefficients constants). La résolution de cette équation plus simple peut permettre d'en déduire les solutions de l'équation initiale.

Cette technique n'est pas réservée aux équations homogènes. Pour preuve, l'équation considérée dans l'exemple ci-dessous n'est pas homogène.

**Exemple** Considérons, sur $]0, +\infty[$, l'équation différentielle linéaire d'ordre 2 :

$$(E) : t^2 x'' + 3 t x' + 4 x = t \ln t.$$

Raisonnons par analyse-synthèse.

*   *Analyse.* Soit $f$ une solution de $(E)$.Considérons la fonction :$$g : \begin{matrix} \mathbb{R} & \longrightarrow & \mathbb{R} \\ u & \longmapsto & f(e^u). \end{matrix}$$

Comme $f$ est deux fois dérivable sur $]0, +\infty[$, $g$ est deux fois dérivable sur $\mathbb{R}$ et l'on a, pour tout $u \in \mathbb{R}$ :

$$g'(u) = e^u f'(e^u) \quad \text{et} \quad g''(u) = e^u f'(e^u) + (e^u)^2 f''(e^u).$$

On constate alors que, pour $u \in \mathbb{R}$ :

$$g''(u) + 2 g'(u) + 4 g(u) = (e^u)^2 f''(e^u) + 3 e^u f'(e^u) + 4 f(e^u).$$

La fonction $f$ étant solution de $(E)$, on obtient, pour tout $u \in \mathbb{R}$ :

$$g''(u) + 2 g'(u) + 4 g(u) = u e^u,$$

1043

# Chapitre 17. Équations différentielles linéaires

et donc la fonction $g$ est solution sur $\mathbb{R}$ de l’équation différentielle :
$$(\widetilde{E}) : x'' + 2x' + 4x = u e^u.$$

Cette équation est une équation différentielle linéaire scalaire d’ordre 2 à coefficients constants que l’on sait résoudre. Après l’avoir résolue, on en déduit qu’il existe $(*a, b*) \in \mathbb{R}^2$ tel que, pour tout $u \in \mathbb{R}$ :
$$g(u) = a e^{-u} \cos(\sqrt{3} u) + b e^{-u} \sin(\sqrt{3} u) + \frac{7u - 4}{49} e^u.$$

$\ast$ Revenons sur la fonction $f$. Pour tout $t \in ]0, +\infty[$, on a :
$$f(t) = f(e^{\ln t}) = g(\ln t).$$

Par suite, on obtient l’expression suivante de $f(t)$ pour $t \in ]0, +\infty[$ :
$$f(t) = \frac{a}{t} \cos(\sqrt{3} \ln t) + \frac{b}{t} \sin(\sqrt{3} \ln t) + \frac{7t \ln t - 4t}{49}.$$

$\bullet$ *Synthèse.* Réciproquement, on vérifie que toute fonction $f$ de la forme ci-dessus est bien solution de (E).

**Remarque** La partie « synthèse » du raisonnement précédent ne présente pas de difficulté car il suffit de vérifier que les fonctions $f$ considérées sont deux fois dérivables et qu’elles vérifient l’équation différentielle (E). Néanmoins, il est possible d’éviter cette vérification grâce à notre connaissance de la structure de l’ensemble des solutions de (E).

En effet, (E) est une équation différentielle linéaire d’ordre 2 et, puisque l’on travaille sur $]0, +\infty[$, on peut la mettre sous forme résolue. On sait donc que l’ensemble $\mathcal{S}$ de ses solutions est un sous-espace affine de dimension 2.

La partie « analyse » du raisonnement prouve que $\mathcal{S} \subset \varphi_P + \text{Vect}(\varphi_1, \varphi_2)$ avec :
$$\varphi_P : t \mapsto \frac{t \ln t}{7} - \frac{4t}{49}, \quad \varphi_1 : t \mapsto \frac{1}{t} \cos(\sqrt{3} \ln t) \quad \text{et} \quad \varphi_2 : t \mapsto \frac{1}{t} \sin(\sqrt{3} \ln t).$$

Un argument de dimension prouve alors que l’inclusion obtenue est en fait une égalité :
$$\mathcal{S} = \varphi_P + \text{Vect}(\varphi_1, \varphi_2).$$

**Remarque culturelle** On appelle **équation d’Euler** une équation différentielle linéaire de la forme :
$$a_n t^n x^{(n)} + a_{n-1} t^{n-1} x^{(n-1)} + \dots + a_0 x = h(t) \quad \text{avec} \quad a_n \neq 0.$$

Comme dans l’exemple précédent, une telle équation peut être ramenée, par un changement de variable en $t = e^u$, à une équation différentielle linéaire à coefficients constants.

<mark>p.1068</mark> **Exercice 25** Résoudre sur $\mathbb{R}$ l’équation différentielle :
$$(E) : (1 + t^2)^2 x'' + 2(t + 1)(1 + t^2) x' + x = 0.$$

*Indication : on pourra exploiter le changement de variable $t = \tan u$.*

1044

V Exemples de résolution d’équations non résolues

### Approfondissement
Devant une équation différentielle de la forme :

$$a(t) x'' + b(t) x' + c(t) x = b(t),$$

pour laquelle on pense qu’un changement de variable est pertinent, pour rechercher quelle fonction de la forme $g : u \mapsto f(\theta(u))$ considérer, on peut écrire :

$$g''(u) = \theta'(u)^2 f''(\theta(u)) + \theta''(u) f'(\theta(u))$$

et remarquer que, si $\theta'(u)^2 = a(\theta(u))$, alors le caractère solution de $f$ :

$$a(t) f''(t) + b(t) f'(t) + c(t) f(t) = d(t),$$

se traduit sur $g$ par une équation débutant par :

$$g''(u) + \dots$$

Cela n’assure en rien que les autres termes de l’équation s’arrangent correctement, mais c’est déjà un bon début...

# V Exemples de résolution d’équations non résolues

Étant donné une équation différentielle linéaire scalaire de la forme :

$$a_n(t) x^{(n)} + \dots + a_0(t) x = b(t), \hfill (\text{E})$$

si la fonction $a_n$ ne s’annule pas sur l’intervalle $I$ de résolution, alors en divisant pas $a_n(t)$, on se ramène à une équation sous forme résolue et on sait alors que l’ensemble solution est de la forme $y_P + \mathcal{S}_0$, l’espace $\mathcal{S}_0$ des solutions de l’équation homogène étant de dimension $n$ ; de telles équations ont été traitées dans la partie III.

L’objectif de cette partie est de traiter quelques exemples d’équations ne pouvant être mises sous forme résolue.

Le plan d’étude d’équations non résolues sera en général le suivant :

**Point méthode (Étude d’une équation non résolue)**

Pour résoudre une équation linéaire de la forme $a_n(t)x^{(n)} + \dots + a_0(t)x = b$ lorsque la fonction $a_n$ possède des points d’annulation :

*   on commence par résoudre l’équation sur tout intervalle sur lequel $a_n$ ne s’annule pas ;
*   on cherche ensuite, par analyse-synthèse, les solutions sur l’intervalle entier.

1045

# Chapitre 17. Équations différentielles linéaires

Pour des équations différentielles linéaires non résolues subsistent :
* le principe de superposition
* l’ensemble $\mathcal{S}_0$ des solutions de l’équation homogène est un espace vectoriel ;
* la structure de l’ensemble des solutions : $\mathcal{S} = \varphi_P + \mathcal{S}_0$, où $\varphi_P$ est une solution particulière ;

En revanche, certaines propriétés ne sont plus vérifiées :
* la dimension de $\mathcal{S}_0$ n’est pas nécessairement égale à l’ordre de l’équation ;
* l’existence et l’unicité de la solution à un problème de Cauchy n’est plus assurée : il peut ne pas y avoir de solution, ou en exister une infinité.

p.1069 **Exercice 26** Considérons sur $\mathbb{R}$ l’équation différentielle :
$$(E) : tx' - 2x = t^3.$$

1. Donner les solutions de $(E)$ sur $]-\infty, 0[$ et sur $]0, +\infty[$.
2. Si $\varphi$ est une solution de $(E)$ sur $\mathbb{R}$, prouver que $\varphi$ est de la forme :
$$\varphi(t) = \begin{cases} \lambda t^2 + t^3 & \text{si } t \le 0 \\ \mu t^2 + t^3 & \text{si } t > 0 \end{cases} \quad \text{avec } (\lambda, \mu) \in \mathbb{R}^2.$$
3. Conclure.

p.1070 **Exercice 27** Résoudre sur $\mathbb{R}$ l’équation différentielle :
$$(E) : t^2 x' - x = 0.$$

p.1070 **Exercice 28** Résoudre sur $\mathbb{R}$ l’équation différentielle :
$$(E) : (1 - t) x' - x = t$$

p.1071 **Exercice 29** *Suite de l’exercice 24 de la page 1043*
Considérons l’équation différentielle :
$$(E_0) : 4tx'' + 2x' - x = 0.$$
On a vu à l’exercice 24 que :
* sur $]-\infty, 0[$, les solutions sont données par :
$$t \mapsto \lambda_1 \cos(\sqrt{-t}) + \lambda_2 \sin(\sqrt{-t}) \quad \text{avec } (\lambda_1, \lambda_2) \in \mathbb{R}^2 ;$$
* sur $]0, +\infty[$, les solutions sont données par :
$$t \mapsto \mu_1 \text{ch}(\sqrt{t}) + \mu_2 \text{sh}(\sqrt{t}) \quad \text{avec } (\mu_1, \mu_2) \in \mathbb{R}^2.$$
Résoudre l’équation $(E_0)$ sur $\mathbb{R}$.

1046

V Exemples de résolution d'équations non résolues

# Annexe : démonstration du théorème de Cauchy linéaire

On munit $E$ et $\mathcal{L}(E)$ de normes, toutes deux notées $\|\cdot\|$

Soit $a \in \mathcal{C}(I, \mathcal{L}(E))$, $b \in \mathcal{C}(I, E)$ et $(t_0, x_0) \in I \times E$. On cherche à prouver l'existence et l'unicité de la solution du problème de Cauchy :

$$x' = a(t) \cdot x + b(t) \quad \text{et} \quad x(t_0) = x_0. \hfill (\mathcal{P})$$

**Remarque** L'espace $E$ étant de dimension finie, il en est de même pour $\mathcal{L}(E)$, si bien que l'application bilinéaire :

$$
\begin{aligned}
\mathcal{L}(E) \times E &\longrightarrow E \\
(*u, x*) &\longmapsto u \cdot x
\end{aligned}
$$

est continue. Plus précisément (*cf.* le corollaire 25 de la page 304), il existe une constante $k \geqslant 0$ telle que :

$$\forall(*u, x*) \in \mathcal{L}(E) \times E \quad \|u \cdot x\| \leqslant k \|u\| \|x\|, \hfill (\star)$$

Cette inégalité $(\star)$ sera utilisée dans la suite.

Le résultat de l'exercice suivant sera utilisé dans la preuve.

p.1072

**Exercice 30** Soit $(z_n)_{n \in \mathbb{N}}$ une suite de fonctions continues sur $I$ à valeurs dans $E$ telles que :

$$\forall n \in \mathbb{N} \quad \forall t \in I \quad z_{n+1}(t) = \int_{t_0}^t a(u) \cdot z_n(u) \, du.$$

Le but est de prouver que la série de fonctions $\sum z_n$ converge normalement sur tout segment de $I$. Soit $K$ un segment inclus dans $I$.

1. Justifier l'existence de deux constantes $M$, $\alpha$ telles que :

$$\forall u \in K \quad \|z_0(u)\| \le M \quad \text{et} \quad \|a(u)\| \le \alpha.$$

2. Montrer que :

$$\forall t \in K \quad \forall n \in \mathbb{N}^* \quad \|z_n(t)\| \leqslant M \frac{(k \alpha |t - t_0|)^n}{n!}.$$

3. En déduire que la série $\sum z_n$ converge normalement sur $K$.

1047

# Chapitre 17. Équations différentielles linéaires

## Preuve de l'unicité

p.1073

**Exercice 31**

1. Montrer que si $h : I \to E$ est une fonction continue vérifiant :
   $$\forall t \in I \quad h(t) = \int_{t_0}^t a(u) \cdot h(u) \, \mathrm{d}u,$$
   alors $h$ est l'application nulle.
2. En déduire qu'il existe au plus une solution au problème de Cauchy $(\mathcal{P})$.

## Preuve de l'existence

p.1074

**Exercice 32** Définissons $(w_n)$ une suite de fonctions sur $I$ par :
$$\forall t \in I \quad w_0(t) = x_0$$
puis, pour tout $n \in \mathbb{N}$ :
$$\forall t \in I \quad w_{n+1}(t) = x_0 + \int_{t_0}^t (a(s) \cdot w_n(s) + b(s)) \mathrm{d}s.$$

1. Montrer que la suite de fonctions $(w_n)$ converge uniformément sur tout segment de $I$.
   *Indication : on pourra considérer la série $\sum z_n$ avec $z_n = w_{n+1} - w_n$.*
2. Montrer que la limite $\varphi$ de $(w_n)$ est solution du problème de Cauchy $(\mathcal{P})$.

1048

***Démonstrations et solutions des exercices du cours***

# **Démonstrations et solutions des exercices du cours**

**Exercice 1** Supposons que $a$ et $b$ sont de classe $\mathcal{C}^k$. Soit $\varphi$ une solution de (E).
Si $\varphi$ n'est pas de classe $\mathcal{C}^k$, alors il existe $p < k$ tel que $\varphi$ soit de classe $\mathcal{C}^p$ mais pas de classe $\mathcal{C}^{p+1}$.
Comme $a$ et $\varphi$ sont de classe $\mathcal{C}^p$, et par bilinéarité de l'application :

$$
\begin{aligned}
\mathcal{L}(E) \times E &\longrightarrow E \\
(*u, e*) &\longmapsto u \cdot e,
\end{aligned}
$$

l'application $t \mapsto a(t) \cdot \varphi(t)$ est aussi de classe $\mathcal{C}^p$. Mais alors, la relation :
$$\forall t \in I \quad \varphi'(t) = a(t) \cdot \varphi(t) + b(t)$$
entraîne que $\varphi'$ est de classe $\mathcal{C}^p$, et contredit le fait que $\varphi$ n'est pas de classe $\mathcal{C}^{p+1}$.

**Proposition 1**
* Si $\varphi \in \mathcal{C}(I, E)$ est solution de (E), alors $\varphi$ est de classe $\mathcal{C}^1$ et vérifie :
$$\forall s \in I \quad \varphi'(s) = a(s) \cdot \varphi(s) + b(s) \quad \text{et} \quad \varphi(t_0) = x_0.$$
Alors, pour tout $t \in I$, on obtient, en intégrant entre $t_0$ et $t$ :
$$\varphi(t) - \varphi(t_0) = \int_{t_0}^t \varphi'(s) ds = \int_{t_0}^t a(s) \cdot \varphi(s) ds + \int_{t_0}^t b(s) ds,$$
c'est-à-dire puisque $\varphi(t_0) = x_0$ :
$$\varphi(t) = x_0 + \int_{t_0}^t a(s) \cdot \varphi(s) ds + \int_{t_0}^t b(s) ds$$

* Réciproquement, supposons que $\varphi$ vérifie :
$$\forall t \in I \quad \varphi(t) = x_0 + \int_{t_0}^t a(s) \cdot \varphi(s) ds + \int_{t_0}^t b(s) ds.$$
    * Alors, en évaluant en $t_0$, on a $\varphi(t_0) = x_0$.
    * De plus $\varphi$ est dérivable sur $I$ comme somme de fonctions dérivables, et l'on obtient en dérivant :
$$\forall t \in I \quad \varphi'(t) = a(t) \cdot \varphi(t) + b(t).$$

**Exercice 2** S'il existe $t_0 \in I$ tel que $\varphi_1(t_0) = \varphi_2(t_0)$, alors les fonctions $\varphi_1$ et $\varphi_2$ sont toutes deux solutions du problème de Cauchy :
$$x' = a(t) \cdot x + b(t) \quad \text{et} \quad x(t_0) = \varphi_1(t_0) = \varphi_2(t_0).$$
et donc, par propriété d'unicité, on a $\varphi_1 = \varphi_2$.

**Exercice 3** Soit $\varphi : I \to E$ une solution de $(\text{E}_0)$. Supposons que $\varphi$ s'annule en un point $t_0 \in I$. Alors $\varphi$ vérifie la condition initiale $\varphi(t_0) = 0$. Or, la fonction nulle est également une solution vérifiant cette condition initiale. Par unicité de la solution vérifiant une condition initiale donnée, on en déduit que $\varphi$ est la fonction nulle.

**Remarque** Le résultat de cet exercice est une conséquence immédiate de celui de l'exercice 2 : la fonction nulle étant solution de l'équation homogène $(\text{E}_0)$, elle ne croise aucune autre solution.

1049

# Chapitre 17. Équations différentielles linéaires

## **Exercice 4**

*   Si $\varphi$ est une solution réelle de (Sys) alors on a :
    $$\forall t \in I \quad \varphi(t) \in \mathbb{R}^n,$$
    et donc en particulier $\varphi(t_0) \in \mathbb{R}^n$.
*   Réciproquement, soit $\varphi$ une solution du système (Sys) telle que $\varphi(t_0) \in \mathbb{R}^n$. Alors l'application $\overline{\varphi} : t \mapsto \overline{\varphi(t)}$ est aussi une solution de (Sys) puisque, pour tout $t \in I$, en conjuguant la relation $\varphi'(t) = A(t)\varphi(t) + B(t)$, on obtient, puisque les matrices $A(t)$ et $B(t)$ sont à coefficients réels :
    $$\overline{\varphi'(t)} = \overline{A(t)\varphi(t) + B(t)} = A(t)\overline{\varphi(t)} + B(t)$$
    autrement dit :
    $$\overline{\varphi}'(t) = A(t)\overline{\varphi}(t) + B(t).$$
    Comme $\varphi(t_0) \in \mathbb{R}^n$, on a $\varphi(t_0) = \overline{\varphi(t_0)} = \overline{\varphi}(t_0)$. Les fonctions $\varphi$ et $\overline{\varphi}$ sont donc solutions de (Sys) et vérifient la même condition initiale en $t_0$. Par unicité de la solution vérifiant un problème de Cauchy, on a $\varphi = \overline{\varphi}$, ce qui signifie que $\varphi$ est à valeurs dans $\mathbb{R}^n$.

## **Exercice 5**

1.  On a, en sommant les deux équations :
    $$(f_1 + f_2)' = 3(f_1 + f_2),$$
    donc $f_1 + f_2$ est solution de l'équation différentielle linéaire du premier ordre $y' = 3y$. On en déduit qu'il existe $a \in \mathbb{K}$ tel que :
    $$\forall t \in \mathbb{R} \quad f_1(t) + f_2(t) = ae^{3t}.$$

2.  En remplaçant $f_2(t)$ par $ae^{3t} - f_1(t)$ dans la première équation du système, on trouve :
    $$f_1'(t) = -f_1(t) + 2ae^{3t},$$
    donc $f_1$ est solution de l'équation $y' + y = 2ae^{3t}$.
    Il existe donc un scalaire $b$ tel que :
    $$\forall t \in \mathbb{R} \quad f_1(t) = be^{-t} + \frac{a}{2}e^{3t};$$
    puis
    $$\forall t \in \mathbb{R} \quad f_2(t) = -be^{-t} + \frac{a}{2}e^{3t}.$$
    On a alors :
    $$\forall t \in \mathbb{R} \quad f(t) = b(e^{-t}, -e^{-t}) + \frac{a}{2}(e^{3t}, e^{3t}),$$
    donc $f$ est combinaison linéaire de $\varphi_1 : t \mapsto (e^{-t}, -e^{-t})$ and $\varphi_2 : t \mapsto (e^{3t}, e^{3t})$.

3.  Il s'agit d'un système différentiel linéaire homogène de taille 2, donc l'espace solution $\mathcal{S}_0$ est de dimension 2. D'après la question précédente, on a :
    $$\mathcal{S}_0 \subset \text{Vect}(\varphi_1, \varphi_2).$$
    La famille $(\varphi_1, \varphi_2)$ est donc nécessairement libre et forme une base de $\mathcal{S}_0$.
    Conclusion :
    $$\mathcal{S}_0 = \text{Vect}(\varphi_1, \varphi_2).$$

1050

**Démonstrations et solutions des exercices du cours**

## Exercice 6

*   L'implication $(iii) \Rightarrow (ii)$ est évidente.
*   $(ii) \Rightarrow (i)$. Supposons $(ii)$. Soit $t_0 \in I$ tel que la famille $(\varphi_1(t_0), \dots, \varphi_n(t_0))$ soit une base de $E$. En évaluant en $t_0$ une relation du type $\sum_{k=1}^n \lambda_k \varphi_k = 0$, on obtient $\sum_{k=1}^n \lambda_k \varphi_k(t_0) = 0$ et donc, par liberté de la famille $(\varphi_1(t_0), \dots, \varphi_n(t_0))$, on a $\lambda_1 = \dots = \lambda_n = 0$.
    Par suite, la famille $(\varphi_1, \dots, \varphi_n)$ est libre. Comme c'est une famille à $n$ éléments et que $\dim \mathcal{S}_0 = \dim E = n$, c'est une base de $\mathcal{S}_0$.
*   $(i) \Rightarrow (iii)$. Supposons que $(\varphi_1, \dots, \varphi_n)$ soit une base de $\mathcal{S}_0$. Fixons $t \in I$ et montrons que $(\varphi_1(t), \dots, \varphi_n(t))$ est une base de $E$. Comme $\dim \mathcal{S}_0 = n$, il suffit de prouver le caractère générateur. Soit $a \in E$. Le théorème de Cauchy linéaire assure l'existence (et l'unicité) d'une solution $\varphi$ de $(E_0)$ vérifiant la condition initiale $\varphi(t) = a$. Comme $(\varphi_1, \dots, \varphi_n)$ est une base de $\mathcal{S}_0$, cette solution $\varphi$ s'écrit $\varphi = \sum_{k=1}^n \lambda_k \varphi_k$ avec $(\lambda_1, \dots, \lambda_n) \in \mathbb{K}^n$. On a alors :
    $$a = \varphi(t) = \sum_{k=1}^n \lambda_k \varphi_k(t).$$
    D'où le caractère générateur de la famille $(\varphi_1(t), \dots, \varphi_n(t))$.

## Exercice 7

Comme $(\varphi_1, \dots, \varphi_n)$ est une base de $\mathcal{S}_0$, l'exercice 6 de la page 1020 assure que pour tout $t \in I$, la famille $(\varphi_1(t), \dots, \varphi_n(t))$ est une base de $E$ ; cela justifie l'existence de $\lambda_1(t), \dots, \lambda_n(t)$ tels que :
$$\varphi(t) = \sum_{i=1}^n \lambda_i(t) \varphi_i(t).$$
D'où l'existence des fonctions $\lambda_1, \dots, \lambda_n$. Il reste à justifier que ces applications sont de classe $\mathcal{C}^1$ sur $I$. Fixons $i \in \llbracket 1, n \rrbracket$. Plaçons-nous dans une base $\mathcal{B}$ de $E$. Pour tout $t \in I$, on a, par linéarité du déterminant par rapport à la $i$-ème variable :
$$\begin{aligned} \det_{\mathcal{B}} (\varphi_1(t), \dots, \underbrace{\varphi(t)}_{\text{place } i}, \dots, \varphi_n(t)) &= \det_{\mathcal{B}} \left(\varphi_1(t), \dots, \sum_{k=1}^n \lambda_k(t) \varphi_k(t), \dots, \varphi_n(t)\right) \\ &= \sum_{k=1}^n \lambda_k(t) \det_{\mathcal{B}} (\varphi_1(t), \dots, \varphi_k(t), \dots, \varphi_n(t)). \end{aligned}$$
En utilisant alors le caractère alterné du déterminant, on obtient :
$$\det_{\mathcal{B}} (\varphi_1(t), \dots, \varphi(t), \dots, \varphi_n(t)) = \lambda_i(t) \det_{\mathcal{B}} (\varphi_1(t), \dots, \varphi_i(t), \dots, \varphi_n(t))$$
ou encore :
$$\lambda_i(t) = \frac{\det_{\mathcal{B}} (\varphi_1(t), \dots, \varphi(t), \dots, \varphi_n(t))}{\det_{\mathcal{B}} (\varphi_1(t), \dots, \varphi_i(t), \dots, \varphi_n(t))}.$$
Ainsi, $\lambda_i$ apparaît comme un quotient de deux applications de classe $\mathcal{C}^1$, donc est de classe $\mathcal{C}^1$.

1051

# Chapitre 17. Équations différentielles linéaires

**Exercice 8** On a obtenu à l’exercice 5 de la page 1019 les solutions du système homogène associé :

$$ \mathcal{S}_0 = \text{Vect}(\varphi_1, \varphi_2) \quad \text{avec} \quad \varphi_1 : t \mapsto e^{-t} \begin{pmatrix} 1 \\ -1 \end{pmatrix} \quad \text{et} \quad \varphi_2 : t \mapsto e^{3t} \begin{pmatrix} 1 \\ 1 \end{pmatrix} . $$

Cherchons une solution particulière sous la forme :
$$ \varphi = \lambda_1 \varphi_1 + \lambda_2 \varphi_2 \quad \text{avec } \lambda_1 \text{ et } \lambda_2 \text{ dérivables sur } \mathbb{R} . $$

Une telle fonction $\varphi$ est solution de (Sys) si, et seulement si :
$$ \forall t \in \mathbb{R} \quad \lambda'_1(t) \varphi_1(t) + \lambda'_2(t) \varphi_2(t) = \begin{pmatrix} e^{-t} \\ 0 \end{pmatrix} . $$

ce qui s’écrit sous forme matricielle :
$$ \forall t \in \mathbb{R} \quad \begin{pmatrix} e^{-t} & e^{3t} \\ -e^{-t} & e^{3t} \end{pmatrix} \begin{pmatrix} \lambda'_1(t) \\ \lambda'_2(t) \end{pmatrix} = \begin{pmatrix} e^{-t} \\ 0 \end{pmatrix} $$

ce qui donne, après obtention de $\lambda'_1$ et $\lambda'_2$ puis primitivation :
$$ \lambda_1(t) = \frac{t}{2} + k_1 \quad \text{et} \quad \lambda_2(t) = -\frac{1}{8} e^{-4t} + k_2 \quad \text{avec} \quad (k_1, k_2) \in \mathbb{K}^2 . $$

En choisissant $\lambda_1 : t \mapsto \frac{t}{2}$ et $\lambda_2 : t \mapsto -\frac{1}{8} e^{-4t}$, on trouve comme solution particulière :
$$ \varphi : t \mapsto \frac{t}{2} e^{-t} \begin{pmatrix} 1 \\ -1 \end{pmatrix} - \frac{1}{8} e^{-t} \begin{pmatrix} 1 \\ 1 \end{pmatrix} . $$

On en déduit que les solutions de (Sys) sont les fonctions :
$$ t \mapsto \left( \alpha + \frac{t}{2} \right) e^{-t} \begin{pmatrix} 1 \\ -1 \end{pmatrix} + \left( \beta e^{3t} - \frac{e^{-t}}{8} \right) \begin{pmatrix} 1 \\ 1 \end{pmatrix} \quad \text{avec} \quad (\alpha, \beta) \in \mathbb{K}^2 . $$

**Exercice 9**
1. La fonction $\varphi : t \mapsto \exp(\lambda t)V$ est dérivable sur $\mathbb{R}$, de dérivée donnée par :
   $$ \varphi'(t) = \lambda e^{\lambda t} V = e^{\lambda t} \lambda V = e^{\lambda t} AV = A e^{\lambda t} V = A \varphi(t) . $$
   Comme de plus $\varphi(0) = V$, $\varphi$ est bien solution du problème de Cauchy :
   $$ X' = AX \quad \text{et} \quad X(0) = V . $$
   Par unicité de la solution à un problème de Cauchy, c’est la seule.

2. D’après la première question, les fonctions $\varphi_1, \dots, \varphi_n$ sont solutions de l’équation $(E_0)$. Comme $\dim(\mathcal{S}) = n$, pour conclure que $(\varphi_1, \dots, \varphi_n)$ est une base de $\mathcal{S}$, il suffit de prouver la liberté. Soit $(\mu_1, \dots, \mu_n) \in \mathbb{K}^n$ tel que :
   $$ \sum_{k=1}^{n} \mu_k \varphi_k = 0 . $$

1052

**_Démonstrations et solutions des exercices du cours_**

En évaluant en $t \in I$ quelconque, on obtient, par définition de $\varphi_k$ :

$$\sum_{k=1}^{n} \mu_k e^{\lambda_k t} V_k = 0.$$

Comme la famille $(V_1, \dots, V_n)$ est libre, on en déduit que pour tout $k \in \llbracket 1, n \rrbracket$ :

$$\mu_k \underbrace{e^{\lambda_k t}}_{\neq 0} = 0 \quad \text{et donc} \quad \mu_k = 0.$$

D'où la liberté de la famille $(\varphi_1, \dots, \varphi_n)$.

### **Exercice 10**

*   Justifions que $A$ est diagonalisable et obtenons ses éléments propres.

    On a $A = I + J$ avec $J = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{pmatrix}$.

    La matrice $J$ est de rang 1. Son noyau est donc de dimension 2. Plus précisément, une base de $\text{Ker } J$ est donnée par $(V_1, V_2)$ avec :

    $$V_1 = \begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix} \quad \text{et} \quad V_2 = \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix}.$$

    De plus, on a $3 \in \text{sp}(J)$, et $V_3 = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}$ est vecteur propre associé.

    La matrice $J$ est donc diagonalisable et $(V_1, V_2, V_3)$ est une base de vecteurs propres associée au triplet $(0, 0, 3)$ de valeurs propres.

*   Par suite, $A$ est diagonalisable, et $(V_1, V_2, V_3)$ est une base de vecteurs propres associée au triplet $(1, 1, 4)$ de valeurs propres. Il en résulte qu'une base de l'espace des solutions du système différentiel étudié est $(X_1, X_2, X_3)$ avec :

    $$X_1 : t \mapsto e^t \begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix}, \quad X_2 : t \mapsto e^t \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix} \quad \text{et} \quad X_3 : t \mapsto e^{4t} \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}.$$

### **Exercice 11**

*   On a $\text{Vect}(\varphi, \overline{\varphi}) \subset \text{Vect}(\text{Re}(\varphi), \text{Im}(\varphi))$ du fait des deux relations :

    $$\varphi = \text{Re}(\varphi) + i \text{Im}(\varphi) \quad \text{et} \quad \overline{\varphi} = \text{Re}(\varphi) - i \text{Im}(\varphi).$$

*   L'inclusion réciproque $\text{Vect}(\text{Re}(\varphi), \text{Im}(\varphi)) \subset \text{Vect}(\varphi, \overline{\varphi})$ vient des relations :

    $$\text{Re}(\varphi) = \frac{\varphi + \overline{\varphi}}{2} \quad \text{et} \quad \text{Im}(\varphi) = \frac{\varphi - \overline{\varphi}}{2i}.$$

1053

# Chapitre 17. Équations différentielles linéaires

## **Exercice 12**

*   Pour $x \in \mathbb{C}$, on a :
    
$$\chi_A(x) = \begin{vmatrix} x-1 & 1 & -2 \\ -2 & x+1 & -3 \\ 0 & 0 & x-1 \end{vmatrix}$$

et donc, en développant par rapport à la dernière ligne :

$$\chi_A(x) = (x - 1) \begin{vmatrix} x - 1 & 1 \\ -2 & x + 1 \end{vmatrix} = (x - 1)(x^2 + 1) = (x - 1)(x + i)(x - i).$$

La matrice $A$ est donc diagonalisable dans $\mathbb{C}$ mais pas dans $\mathbb{R}$.

*   Après calculs :

* le vecteur $V_1 = \begin{pmatrix} 1 \\ 4 \\ 2 \end{pmatrix}$ est vecteur propre associé à la valeur propre 1 ;

* le vecteur $V_2 = \begin{pmatrix} 1 + i \\ 2 \\ 0 \end{pmatrix}$ est vecteur propre associé à la valeur propre $i$ ;

par suite, comme $A$ est à coefficients réels, le vecteur $\overline{V_2}$ est vecteur propre associé à la valeur propre $-i$.

*   Ainsi, une base de $\mathcal{S}_{\mathbb{C}}$ est donnée par $(X_1, X_2, \overline{X_2})$ avec :
    $$X_1 : t \mapsto e^t V_1 \quad \text{et} \quad X_2 : t \mapsto e^{it} V_2.$$

*   Comme $\text{Vect}(X_2, \overline{X_2}) = \text{Vect}(\text{Re}(X_2), \text{Im}(X_2))$ (*cf.* exercice 11 de la page 1024), on en déduit que la famille :
    $$(X_1, \text{Re}(X_2), \text{Im}(X_2))$$
    est une base de $\mathcal{S}_{\mathbb{C}}$, et donc de $\mathcal{S}_{\mathbb{R}}$ car elle est formée d'applications à valeurs dans $\mathbb{R}^3$.
    De manière plus explicite, la base $(X_1, \text{Re}(X_2), \text{Im}(X_2))$ est donnée par :

$$X_1(t) = e^t \begin{pmatrix} 1 \\ 4 \\ 2 \end{pmatrix} \qquad \text{Re}(X_2)(t) = \begin{pmatrix} \cos t - \sin t \\ 2 \cos t \\ 0 \end{pmatrix}$$

et

$$\text{Im}(X_2)(t) = \begin{pmatrix} \cos t + \sin t \\ 2 \sin t \\ 0 \end{pmatrix}$$

1054

***Démonstrations et solutions des exercices du cours***

## **Exercice 13**

*   L’étude des éléments propres de $A$ indique que $2$ est valeur propre triple de $A$. Comme $A \neq 2I_3$, on en déduit que $A$ est trigonalisable mais pas diagonalisable. Notons $N = A - 2I_3$. On a :
$$N = \begin{pmatrix} 1 & 0 & -1 \\ -1 & 0 & 1 \\ 1 & 0 & -1 \end{pmatrix}.$$

En posant :
$$U_2 = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \quad U_1 = \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix} \quad \text{et} \quad U_3 = \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix},$$

on a :
$$NU_1 = 0, \quad NU_2 = U_1 \quad \text{et} \quad NU_3 = 0.$$

Ainsi, en notant $P = \begin{pmatrix} 1 & 1 & 1 \\ -1 & 0 & 0 \\ 1 & 0 & 1 \end{pmatrix}$ qui est inversible, on a :
$$N = P \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} P^{-1}$$

et donc :
$$A = *PTP*^{-1} \quad \text{avec} \quad T = \begin{pmatrix} 2 & 1 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 2 \end{pmatrix}.$$

*   En notant $Y = P^{-1}X$, on a $X' = AX \iff X' = PTP^{-1}X$ Résolvons le sys-
$$\iff P^{-1}X' = TP^{-1}X$$
$$\iff Y' = TY.$$

tème différentiel $Y' = TY$, qui, en notant $Y = \begin{pmatrix} y_1 \\ y_2 \\ y_3 \end{pmatrix}$, s’écrit :
$$\begin{cases} y'_1 = 2y_1 + y_2 \\ y'_2 = 2y_2 \\ y'_3 = 2y_3 \end{cases}$$

1055

# Chapitre 17. *Équations différentielles linéaires*

*   *Analyse.* Supposons que $Y = \begin{pmatrix} y_1 \\ y_2 \\ y_3 \end{pmatrix}$ soit solution.

Les deux dernières équations mènent à l'existence $(k_2, k_3) \in \mathbb{R}^2$ tel que :

$$\forall t \in \mathbb{R} \quad y_2(t) = k_2 e^{2t} \quad \text{et} \quad y_3 = k_3 e^{2t}.$$

La première équation $y_1' = 2y_1 + k_2 e^{2t}$ apparaît alors comme une équation différentielle en $y_1$ et mène à l'existence de $k_1 \in \mathbb{R}$ tel que :

$$\forall t \in \mathbb{R} \quad y_1(t) = k_1 e^{2t} + k_2 t e^{2t}.$$

On obtient alors :

$$\forall t \in \mathbb{R} \quad Y(t) = k_1 \begin{pmatrix} e^{2t} \\ 0 \\ 0 \end{pmatrix} + k_2 \begin{pmatrix} t e^{2t} \\ e^{2t} \\ 0 \end{pmatrix} + k_3 \begin{pmatrix} 0 \\ 0 \\ e^{2t} \end{pmatrix}.$$

*   *Synthèse.* De l'analyse précédente il résulte que l'ensemble $\mathcal{S}_T$ des solutions du système différentiel $Y' = TY$ vérifie $\mathcal{S}_T \subset \text{Vect}(Y_1, Y_2, Y_3)$ avec :

$$Y_1 : t \mapsto \begin{pmatrix} e^{2t} \\ 0 \\ 0 \end{pmatrix}, \quad Y_2 : t \mapsto \begin{pmatrix} t e^{2t} \\ e^{2t} \\ 0 \end{pmatrix} \quad \text{et} \quad Y_3 : t \mapsto \begin{pmatrix} 0 \\ 0 \\ e^{2t} \end{pmatrix}.$$

Or, on sait que $\dim \mathcal{S}_T = 3$ ; la famille $(Y_1, Y_2, Y_3)$ est donc libre et en forme une base.

$\bullet$ Finalement, en utilisant l'équivalence :

$$X' = AX \iff Y' = TY \quad \text{avec} \quad X = PY,$$

on obtient que l'espace des solutions du système $X' = AX$ est :

$$\text{Vect}(X_1, X_2, X_3) \quad \text{avec} \quad X_1 = PY_1, \quad X_2 = PY_2 \quad \text{et} \quad X_3 = PY_3.$$

De manière plus explicite, on a, pour tout $t \in \mathbb{R}$ :

$$X_1(t) = e^{2t} \begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix}, \quad X_2(t) = e^{2t} \begin{pmatrix} t + 1 \\ -t \\ t \end{pmatrix} \quad \text{et} \quad X_3(t) = e^{2t} \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}$$

1056

***Démonstrations et solutions des exercices du cours***

**Proposition 8** Pour tout $k \in \mathbb{N}$, l'application :

$$u_n : \begin{matrix} \mathcal{L}(E) & \longrightarrow & \mathcal{L}(E) \\ a & \longmapsto & \displaystyle\frac{a^k}{k!} \end{matrix}$$

est continue. Montrons que la série d'applications $\sum u_k$ converge normalement au voisinage de tout point de $\mathcal{L}(E)$. Il en résultera, par théorème de continuité (*cf.* le corollaire 20 de la page 511), la continuité de l'application :

$$\exp = \sum_{k=0}^{+\infty} u_k.$$

Soit $a \in \mathcal{L}(E)$ et $M = \|a\| + 1$. Comme la norme utilisée sur $\mathcal{L}(E)$ est multiplicative, il en résulte que :

$$\forall k \in \mathbb{N} \quad \|u_k\|_{\infty, B_F(0,M)} \leqslant \frac{M^k}{k!}.$$

Puisque la série numérique $\sum \frac{M^k}{k!}$ converge, il s'ensuit la convergence normale sur $B_F(0,M)$, et donc au voisinage de $a$, de la série $\sum u_k$.

**Proposition 9** Pour tout $t \in \mathbb{R}$, on a :

$$\varphi(t) = \sum_{k=0}^{+\infty} \frac{(ta)^k}{k!} = \sum_{k=0}^{+\infty} u_k(t) \quad \text{avec} \quad u_k : t \mapsto \frac{t^k a^k}{k!}.$$

Toutes les applications $u_k$ sont de classe $\mathcal{C}^1$ et l'on a, pour $k \geqslant 1$ :

$$\forall t \in \mathbb{R} \quad \left( u_0'(t) = 0 \quad \text{et} \quad \forall k \geqslant 1 \quad u_k'(t) = \frac{t^{k-1}}{(k-1)!} a^k \right).$$

Si $K$ est un segment de $\mathbb{R}$, alors en notant $M$ tel que $K \subset [-M, M]$, le caractère multiplicatif de la norme utilisée sur $\mathcal{L}(E)$ donne :

$$\forall k \geqslant 1 \quad \|u_k'\|_{\infty, K} \leqslant \frac{M^{k-1}}{(k-1)!} \|a\|^k.$$

La convergence de la série numérique $\sum \frac{M^{k-1}}{(k-1)!} \|a\|^k$ prouve ainsi la convergence normale sur le segment $K$ de la série d'applications $\sum u_k'$.

D'après le théorème de dérivation des séries de fonctions (*cf.* le théorème 24 de la page 513), il s'ensuit que l'application $\varphi$ est de classe $\mathcal{C}^1$, et l'on a de plus, pour $t \in \mathbb{R}$ :

$$\varphi'(t) = \sum_{k=1}^{+\infty} u_k'(t) = \sum_{k=1}^{+\infty} \frac{t^{k-1}}{(k-1)!} a^k = \sum_{k=0}^{+\infty} \frac{t^k}{k!} a^{k+1}$$

puis en factorisant par $a$ à droite ou à gauche, on obtient la formule souhaitée :

$$\varphi'(t) = a \circ \exp(ta) = \exp(ta) \circ a.$$

1057

# Chapitre 17. Équations différentielles linéaires

## Exercice 14
Notons $\varphi$ l'application qui à un endomorphisme associe sa matrice dans la base $\mathcal{B}$ :

$$
\begin{aligned}
\varphi \quad : \quad \mathcal{L}(E) & \longrightarrow \mathcal{M}_n(\mathbb{K}) \\
u & \longmapsto \text{Mat}_{\mathcal{B}}(u).
\end{aligned}
$$

Puisque $\varphi(a) = A$, on a, par propriété de morphisme d'algèbres de $\varphi$ :

$$\forall N \in \mathbb{N} \quad \varphi \left( \sum_{k=0}^{N} \frac{a^k}{k!} \right) = \sum_{k=0}^{N} \frac{A^k}{k!}. \hfill (\star)$$

L'application $\varphi$ étant linéaire, elle est continue (car son espace de départ est de dimension finie). Comme $\sum_{k=0}^{N} \frac{a^k}{k!} \to \exp(a)$, on a donc, par continuité de $\varphi$ en $\exp(a)$ :

$$\varphi \left( \sum_{k=0}^{N} \frac{a^{k}}{k!} \right) \longrightarrow \varphi(\exp(a)).$$

Comme d'autre part $\sum_{k=0}^{N} \frac{A^k}{k!} \to \exp(A)$, la relation $(\star)$ donne, par unicité de la limite :

$$\varphi(\exp(a)) = \exp(A).$$

## Exercice 15
1. Si $A = \text{Diag}(\lambda_1, \dots, \lambda_n)$, alors :

$$\forall k \in \mathbb{N} \quad A^k = \begin{pmatrix} \lambda_1^k & & (0) \\ & \ddots & \\ (0) & & \lambda_n^k \end{pmatrix}.$$

On a alors, pour $N \in \mathbb{N}$ :

$$\sum_{k=0}^{N} \frac{A^k}{k!} = \begin{pmatrix} \sum_{k=0}^{N} \frac{\lambda_1^k}{k!} & & (0) \\ & \ddots & \\ (0) & & \sum_{k=0}^{N} \frac{\lambda_n^k}{k!} \end{pmatrix}$$

Par passage à la limite, on obtient :

$$\exp(A) = \begin{pmatrix} e^{\lambda_1} & & (0) \\ & \ddots & \\ (0) & & e^{\lambda_n} \end{pmatrix}$$

1058

***Démonstrations et solutions des exercices du cours***

2. Supposons $A$ diagonalisable. On peut donc écrire :
$$A = P D P^{-1} \quad \text{avec} \quad P \in \mathcal{GL}_n(\mathbb{K}) \quad \text{et} \quad D = \text{Diag}(\lambda_1, \dots, \lambda_n)$$
On a alors :
$$\forall N \in \mathbb{N} \quad \sum_{k=0}^N \frac{A^k}{k!} = P \left( \sum_{k=0}^N \frac{D^k}{k!} \right) P^{-1}.$$
L'endomorphisme $\mathcal{M}_n(\mathbb{K}) \longrightarrow \mathcal{M}_n(\mathbb{K})$ étant continu, on obtient, en passant à la limite :
$$M \longmapsto P^{-1} M P$$
sant à la limite :
$$\exp(A) = P \exp(D) P^{-1} = P \begin{pmatrix} e^{\lambda_1} & & (0) \\ & \ddots & \\ (0) & & e^{\lambda_n} \end{pmatrix} P^{-1}.$$

### Exercice 16
1. Notons $P = X^2 - 3X + 2$. Comme $\deg(P) = 2$, le théorème de la division euclidienne assure que l'on peut écrire :
$$X^k = P Q + R \quad \text{avec} \quad \deg(R) \leqslant 1.$$
Comme $P = (X - 2)(X - 1)$, on obtient, en évaluant en 1 et en 2 la relation précédente, $R(1) = 1$ et $R(2) = 2^k$. On trouve finalement :
$$R = (2^k - 1) X + (2 - 2^k).$$
Puis, comme $P$ est annulateur de $A$, on a :
$$A^k = (2^k - 1) A + (2 - 2^k) I_n = 2^k (A - I_n) + (2I_n - A).$$

2. Pour tout $N \in \mathbb{N}$, on a, d'après la question précédente :
$$\sum_{k=0}^N \frac{A^k}{k!} = \left( \sum_{k=0}^N \frac{2^k}{k!} \right) (A - I_n) + \left( \sum_{k=0}^N \frac{1}{k!} \right) (2I_n - A),$$
et qui donne, en passant à la limite :
$$\exp(A) = e^2 (A - I_n) + e (2I_n - A) = (e^2 - e) A + (2e - e^2) I_n.$$

**Proposition 17** Soit $s \in \mathbb{R}$. Pour $x_0 \in E$, on vérifie facilement que les applications :
$$t \mapsto \exp ((t + s) a) \cdot x_0 \quad \text{et} \quad t \mapsto (\exp(t a) \circ \exp(s a)) \cdot x_0$$
sont toutes deux solutions du problème de Cauchy :
$$x' = a \cdot x \quad \text{et} \quad x(0) = \exp(s a) \cdot x_0.$$
Donc, par unicité de la solution d'un problème de Cauchy, on obtient :
$$\forall t \in \mathbb{R} \quad \exp ((t + s) a) \cdot x_0 = (\exp(t a) \circ \exp(s a)) \cdot x_0.$$
Cela étant vrai pour tout $x_0 \in E$, on en déduit :
$$\forall t \in \mathbb{R} \quad \exp ((t + s) a) = \exp(t a) \circ \exp(s a)$$
Cela étant vrai pour tout $s \in \mathbb{R}$, le résultat souhaité est démontré.

1059

# Chapitre 17. Équations différentielles linéaires

**Corollaire 18** De la proposition précédente il vient, pour tout $t \in \mathbb{R}$ :
$$\exp(t a) \circ \exp(-t a) = \exp ((t - t) a) = \exp(0) = \text{Id}_E .$$
L'endomorphisme $\exp(-t a)$ est donc l'inverse à droite de $\exp(t a)$ et donc, comme ce sont des endomorphismes en dimension finie, c'est également son inverse à gauche.

## Proposition 19

*   Justifions d'abord que, pour tout $t \in \mathbb{R}$, les endomorphismes $\exp(ta)$ et $b$ commutent. Soit $t \in \mathbb{R}$. Pour $p \in \mathbb{N}$, notons $c_p = \sum_{k=0}^{p} \frac{(ta)^k}{k!}$.
    Puisque $a$ et $b$ commutent et que $c_p$ est un polynôme en $a$, on a :
    $$\forall p \in \mathbb{N} \quad c_p \circ b = b \circ c_p. \quad (\star)$$
    Comme la suite $(c_p)$ converge vers $a$ et par continuité des applications :

$$
\begin{aligned}
\mathcal{L}(E) &\longrightarrow \mathcal{L}(E) & \text{et} & & \mathcal{L}(E) &\longrightarrow \mathcal{L}(E) , \\
u &\longmapsto u \circ b & & & u &\longmapsto b \circ u
\end{aligned}
$$

on a, en passant à la limite dans la relation $(\star)$ :

    on a, en passant à la limite dans la relation $(\star)$ :
    $$\exp(ta) \circ b = b \circ \exp(ta).$$

*   Notons $\varphi : t \mapsto \exp(ta) \circ \exp(tb)$.
    Dérivons l'application $\varphi$. Pour $t \in \mathbb{R}$, on a :
    $$\varphi'(t) = a \circ \exp(ta) \circ \exp(tb) + \exp(ta) \circ b \circ \exp(tb)$$
    $$= a \circ \exp(ta) \circ \exp(tb) + b \circ \exp(ta) \circ \exp(tb) \quad (\exp(ta) \text{ et } b \text{ commutent})$$
    $$= (a + b) \circ \varphi(t).$$

    On a de plus $\varphi(0) = \exp(0)^2 = \text{Id}_E$.
    Fixons $x_0 \in E$. L'application $t \mapsto \varphi(t) \cdot x_0$ est solution du problème de Cauchy :
    $$x' = (a + b) \cdot x \quad \text{et} \quad x(0) = x_0.$$
    Comme l'application $t \mapsto \exp (t(a + b)) \cdot x_0$ est également solution de ce problème de Cauchy, il en résulte, par unicité, que ces deux applications sont égales :
    $$\forall t \in \mathbb{R} \quad (\exp(t a) \circ \exp(t b)) \cdot x_0 = \exp (t(a + b)) \cdot x_0.$$
    En évaluant pour $t = 1$, on obtient :
    $$(\exp(a) \circ \exp(b)) \cdot x_0 = \exp (a + b) \cdot x_0.$$
    Comme $x_0$ a été fixé quelconque dans $E$, cela prouve que :
    $$\exp(a) \circ \exp(b) = \exp (a + b).$$

### Exercice 17

*   D'après la proposition 13 de la page 1028, l'application
    $$\varphi_0 : I \longrightarrow E$$
    $$t \longmapsto \exp ((t - t_0)a) \cdot x_0$$
    est l'unique solution de l'équation homogène $(E_0)$ vérifiant $\varphi_0(t_0) = x_0$.

1060

***Démonstrations et solutions des exercices du cours***

*   Montrons que l'application :
    $$
    \begin{aligned}
    \varphi_P : I & \longrightarrow E \\
    t & \longmapsto \int_{t_0}^t \exp((t-s)a) \cdot b(s) \, \mathrm{d}s
    \end{aligned}
    $$
    est une solution particulière de (E) et vérifie $\varphi_P(t_0) = 0$. Pour $t \in I$, on a :
    $$
    \varphi_P(t) = \exp(ta) \cdot \int_{t_0}^t \exp(-sa) \cdot b(s) \, \mathrm{d}s,
    $$
    puis, en dérivant :
    $$
    \begin{aligned}
    \varphi'_P(t) &= (a \circ \exp(ta)) \cdot \int_{t_0}^t \exp(-sa) \cdot b(s) \, \mathrm{d}s + (\exp(ta) \circ \exp(-ta)) \cdot b(t) \\
    &= a \cdot \varphi_P(t) + b(t).
    \end{aligned}
    $$
    Donc $\varphi_P$ est solution de (E). On a de plus $\varphi_P(t_0) = 0$.

*   L'application $\varphi = \varphi_0 + \varphi_P$ est alors solution de (E) car elle est somme d'une solution $\varphi_0$ de l'équation homogène et d'une solution $\varphi_P$ de (E), et vérifie de plus :
    $$
    \varphi(t_0) = \varphi_P(t_0) + \varphi_0(t_0) = x_0.
    $$
    L'application $\varphi$ est donc solution du problème de Cauchy :
    $$
    x' = a(t) \cdot x + b(t) \quad \text{et} \quad x(t_0) = x_0.
    $$
    Par propriété d'unicité, c'est la seule.

**Exercice 18** Supposons que les applications $a_0, \dots, a_{n-1}, b$ sont de classe $\mathcal{C}^p$.
Soit $\varphi : I \to \mathbb{K}$ une solution de (E). Raisonnons par l'absurde en supposant que $\varphi$ n'est pas de classe $\mathcal{C}^{n+p}$. Comme $\varphi$ est $n$ fois dérivable (car c'est une solution de (E)), il existe $k \in \llbracket n-1, n+p-1 \rrbracket$ tel que $\varphi$ soit de classe $\mathcal{C}^k$ mais pas de classe $\mathcal{C}^{<sub>k+1</sub>}$.
La relation :
$$
\varphi^{(n)} = b - a_{n-1} \varphi^{(n-1)} - \dots - a_0 \varphi
$$
mène alors à une contradiction car :
*   le membre de gauche, $\varphi^{(n)}$, n'est pas de classe $\mathcal{C}^{k-n+1}$ ;
*   le membre de droite est de classe $\mathcal{C}^{k-n+1}$ car :
    *   les fonctions $a_0, \dots, a_{n-1}, b$ sont de classe $\mathcal{C}^p$, donc $\mathcal{C}^{k-n+1}$ ;
    *   pour $i \in \llbracket 0, n-1 \rrbracket$, la fonction $\varphi^{(i)}$ est de classe $\mathcal{C}^{k-i}$, donc $\mathcal{C}^{k-n+1}$.

**Proposition 23** Pour tout $t \in I$, on a :
$$
\Phi'(t) = \begin{pmatrix} \varphi'(t) \\ \vdots \\ \varphi^{(n-1)}(t) \\ \varphi^{(n)}(t) \end{pmatrix} \quad \text{et} \quad A(t)\Phi(t) = \begin{pmatrix} \varphi'(t) \\ \vdots \\ \varphi^{(n-1)}(t) \\ -a_0(t)\varphi(t) - \dots - a_{n-1}(t)\varphi^{(n-1)}(t) \end{pmatrix}.
$$

1061

# Chapitre 17. Équations différentielles linéaires

Par suite, on a $\Phi'(t) = A(t)\Phi(t) + B(t)$ si, et seulement si :
$$\varphi^{(n)}(t) = -a_0(t)\varphi(t) - \dots - a_{n-1}(t)\varphi^{(n-1)}(t) + b(t).$$

Il en résulte que $\Phi$ est solution de l'équation différentielle :
$$X' = A(t)X + B(t)$$
si, et seulement si, $\varphi$ est solution de l'équation différentielle :
$$x^{(n)} + a_{n-1}(t)x^{n-1} + \dots + a_0(t)x = b(t).$$

## **Exercice 19**

1. L'équivalence cherchée vient du fait que pour $t \in \mathbb{R}$, on a :
$$\forall k \in \llbracket 0, n \rrbracket \quad f_\lambda^{(k)}(t) = \lambda^k e^{\lambda t}$$
et donc :
$$f_{\lambda}^{(n)}(t) + \sum_{k=0}^{n-1} a_k f_{\lambda}^{(k)}(t) = \lambda^n e^{\lambda t} + \sum_{k=0}^{n-1} a_k \lambda^k e^{\lambda t} = P(\lambda) \underbrace{e^{\lambda t}}_{\neq 0}.$$

2. Supposons que $P$ possède $n$ racines simples $\lambda_1, \dots, \lambda_n$.
* Comme $(E_0)$ est une équation différentielle linéaire homogène scalaire d'ordre $n$, on sait que son ensemble solution $\mathcal{S}_0$ est un espace vectoriel de dimension $n$.
* D'après la question précédente, pour tout $k \in \llbracket 1, n \rrbracket$, la fonction $f_{\lambda_k} : t \mapsto e^{\lambda_k t}$ est solution de $(E_0)$. On a donc :
$$\text{Vect}(f_{\lambda_1}, \dots, f_{\lambda_n}) \subset \mathcal{S}_0.$$

Comme $\dim \mathcal{S}_0 = n$, pour prouver que l'inclusion précédente est une égalité, il suffit de prouver que la famille $(f_{\lambda_1}, \dots, f_{\lambda_n})$ est libre.

Si l'on considère une combinaison linéaire $\sum_{k=1}^n \alpha_k f_{\lambda_k}$ égale à l'application nulle, alors, en dérivant $p$ fois et en évaluant en 0 pour tout $p \in \llbracket 0, n-1 \rrbracket$, il vient :
$$\forall p \in \llbracket 0, n-1 \rrbracket \quad \sum_{k=1}^n \lambda_k^p \alpha_k = 0$$

Il apparaît un système homogène de Vandermonde et, puisque $\lambda_1, \dots, \lambda_n$ sont deux à deux distincts, la matrice de Vandermonde associée est inversible, ce qui assure $\alpha_1 = \dots = \alpha_n = 0$. D'où la liberté de la famille $(f_{\lambda_1}, \dots, f_{\lambda_n})$.

**Proposition 29** L'expression obtenue pour la dérivée du wronskien de $(\varphi_1, \varphi_2)$ est :
$$W'_{\varphi_1, \varphi_2} = \varphi_1 \varphi''_2 - \varphi''_1 \varphi_2,$$
et donc, puisque $\varphi_1$ et $\varphi_2$ sont solutions de $(E_0)$ :
$$
\begin{aligned}
W_{\varphi_1, \varphi_2}' &= \varphi_1 (-a_1 \varphi_2' - a_0 \varphi_2) - (-a_1 \varphi_1' - a_0 \varphi_1) \varphi_2 \\
&= -a_1 (\varphi_1 \varphi_2' - \varphi_1' \varphi_2) \\
&= -a_1 W_{\varphi_1, \varphi_2},
\end{aligned}
$$
et donc $W_{\varphi_1, \varphi_2}$ est solution de l'équation $x' + a_1(t)x = 0$.

1062

***Démonstrations et solutions des exercices du cours***

## **Proposition 30**

*   $(iii) \implies (ii)$. Évident.
*   $(ii) \implies (i)$. Par la contraposée. Supposons que $(\varphi_1, \varphi_2)$ ne soit pas une base de $\mathcal{S}_0$. Comme $\mathcal{S}_0$ est de dimension 2, cela entraîne que $\varphi_1$ et $\varphi_2$ sont proportionnelles.
    Les applications $t \mapsto \begin{pmatrix} \varphi_1(t) \\ \varphi_1'(t) \end{pmatrix}$ et $t \mapsto \begin{pmatrix} \varphi_2(t) \\ \varphi_2'(t) \end{pmatrix}$ sont alors elles aussi proportionnelles et l'on obtient la négation de l'assertion $(ii)$ :
    
    $$ \forall t \in I \quad W(t) = \begin{vmatrix} \varphi_1(t) & \varphi_2(t) \\ \varphi_1'(t) & \varphi_2'(t) \end{vmatrix} = 0. $$

*   $(i) \implies (iii)$. Supposons que $(\varphi_1, \varphi_2)$ soit une base de $\mathcal{S}_0$. Soit $t \in I$.
    Par le théorème de Cauchy linéaire, on sait que pour tout $(\alpha, \beta) \in \mathbb{K}^2$, il existe une solution $\psi$ de $(E_0)$ vérifiant :
    
    $$ \begin{pmatrix} \psi(t) \\ \psi'(t) \end{pmatrix} = \begin{pmatrix} \alpha \\ \beta \end{pmatrix}. $$
    
    Comme $(\varphi_1, \varphi_2)$ est une base de $\mathcal{S}_0$, on peut écrire $\psi = \lambda\varphi_1 + \mu\varphi_2$, ce qui donne, en évaluant en $t$ :
    
    $$ \lambda \begin{pmatrix} \varphi_1(t) \\ \varphi_1'(t) \end{pmatrix} + \mu \begin{pmatrix} \varphi_2(t) \\ \varphi_2'(t) \end{pmatrix} = \begin{pmatrix} \alpha \\ \beta \end{pmatrix}. $$
    
    Il en résulte que la famille formée par les vecteurs $\begin{pmatrix} \varphi_1(t) \\ \varphi_1'(t) \end{pmatrix}$ et $\begin{pmatrix} \varphi_2(t) \\ \varphi_2'(t) \end{pmatrix}$ forment une famille génératrice et donc une base de $\mathbb{K}^2$.
    Le déterminant de cette famille, qui n'est rien d'autre que $W(t)$, est donc non nul.

## **Exercice 20**
Si une telle équation différentielle existait, alors les fonctions $t \mapsto \cos(t)$ et $t \mapsto t$, puisqu'elles ne sont pas proportionnelles, formeraient une base de l'espace $\mathcal{S}_0$ des solutions. Et alors, d'après la proposition 30 de la page 1036, leur wronskien $W$ ne s'annulerait pas sur $\mathbb{R}$. Or ce wronskien est donné par :

$$ W(t) = \varphi_1(t) \varphi_2'(t) - \varphi_1'(t) \varphi_2(t) = \cos t + t \sin t, $$

et le théorème des valeurs intermédiaires assure que $W$ s'annule en au moins un point de l'intervalle $]\frac{\pi}{2}, \pi[$ puisque $W(\frac{\pi}{2}) = \frac{\pi}{2} > 0$ et $W(\pi) = -1 < 0$.

1063

Chapitre 17. Équations différentielles linéaires

## **Exercice 21**

1. La fonction $\varphi_1$ est définie et deux fois dérivable sur $]0, +\infty[$ et l'on a :
   $$\forall t > 0 \quad \varphi_1'(t) = \frac{t \cos t - \sin t}{t^2} \quad \text{et} \quad \varphi_1''(t) = -\frac{t^2 \sin t + 2t \cos t - 2 \sin t}{t^3}.$$
   On vérifie facilement que :
   $$\forall t \in ]0, +\infty[ \quad \varphi_1''(t) + \frac{2}{t} \varphi_1'(t) + \varphi_1(t) = 0.$$

2. $\bullet$ Soit $\varphi$ une solution sur $]0, +\infty[$ de $(E_0)$.
   $*$ Le wronskien $W$ de $(\varphi_1, \varphi)$ vérifie sur $]0, +\infty[$ l'équation différentielle :
   $$x' + \frac{2}{t} x = 0.$$
   On en déduit qu'il existe $\lambda \in \mathbb{R}$ tel que :
   $$\forall t \in ]0, +\infty[ \quad W(t) = \frac{\lambda}{t^2}.$$
   $*$ Plaçons-nous sur un intervalle $J \subset ]0, +\infty[$ où $\varphi_1$ ne s'annule pas ; prenons par exemple $J = ]0, \pi[$. Sur cet intervalle $J$, on peut considérer la fonction $\left( \frac{\varphi}{\varphi_1} \right)$ dont la dérivée vérifie :
   $$\left( \frac{\varphi}{\varphi_1} \right)' = \frac{\varphi' \varphi_1 - \varphi \varphi_1'}{\varphi_1^2} = \frac{W}{\varphi_1^2}.$$
   Ainsi, on a :
   $$\forall t \in J \quad \left( \frac{\varphi}{\varphi_1} \right)'(t) = \frac{\lambda}{\sin^2 t}.$$
   En primitivant, on obtient l'existence de $\mu \in \mathbb{R}$ tel que pour tout $t \in J$ :
   $$\frac{\varphi(t)}{\frac{\sin t}{t}} = -\lambda \frac{\cos t}{\sin t} + \mu \quad \text{et donc} \quad \varphi(t) = -\lambda \frac{\cos t}{t} + \mu \frac{\sin t}{t}.$$

   $\bullet$ Notons alors $\varphi_2$ la fonction $t \mapsto \frac{\cos t}{t}$. La fonction $\varphi_2$ est définie et deux fois dérivable sur $]0, +\infty[$, et il est facile de vérifier que $\varphi_2$ est solution de $(E_0)$. Comme $\varphi_1$ et $\varphi_2$ ne sont pas proportionnelles, on peut conclure que l'ensemble des solutions de $(E_0)$ est :
   $$\mathcal{S}_0 = \text{Vect}(\varphi_1, \varphi_2).$$

**Remarque** Dans le raisonnement précédent, la « méthode du wronskien » ne constitue pas une preuve en tant que telle : elle permet surtout de « découvrir la solution manquante ». Une fois connue cette « solution manquante », il est facile de justifier qu'elle est solution et qu'elle complète la solution déjà connue en une base de $\mathcal{S}_0$.

1064

***Démonstrations et solutions des exercices du cours***

**Exercice 22** Cherchons une solution de (E) sous la forme :
$$\varphi = \lambda_1 \varphi_1 + \lambda_2 \varphi_2 \quad \text{avec} \quad \lambda_1 \text{ et } \lambda_2 \text{ dérivables.}$$

Une telle fonction $\varphi$ est solution si, et seulement si :
$$\begin{cases} \lambda'_1 \varphi_1 + \lambda'_2 \varphi_2 & = & 0 \\ \lambda'_1 \varphi'_1 + \lambda'_2 \varphi'_2 & = & (t \mapsto t) \end{cases}$$

ce qui s'écrit, pour tout $t \in ]0, +\infty[$ :
$$\begin{cases} \displaystyle \frac{\sin t}{t} \lambda'_1(t) + \frac{\cos t}{t} \lambda'_2(t) & = & 0 \\ \displaystyle \frac{t \cos t - \sin t}{t^2} \lambda'_1(t) - \frac{t \sin t + \cos t}{t^2} \lambda'_2(t) & = & t \end{cases}$$

ou encore :
$$\begin{cases} (\sin t) \lambda'_1(t) + (\cos t) \lambda'_2(t) & = & 0 \\ (t \cos t - \sin t) \lambda'_1(t) - (t \sin t + \cos t) \lambda'_2(t) & = & t^3 \end{cases}$$

On obtient, après résolution du système précédent :
$$\forall t \in ]0, +\infty[ \quad \lambda'_1(t) = t^2 \cos t \quad \text{et} \quad \lambda'_2(t) = -t^2 \sin t.$$

Après primitivation, on peut choisir :
$$\lambda_1 : t \mapsto t^2 \sin t - 2 \sin t + 2t \cos t \quad \text{et} \quad \lambda_2 : t \mapsto t^2 \cos t - 2 \cos t - 2t \sin t,$$
et obtenir, après simplification, la solution de (E) suivante :
$$\begin{array}{rrcl} \varphi : & ]0, +\infty[ & \longrightarrow & \mathbb{R} \\ & t & \longmapsto & \displaystyle t - \frac{2}{t}. \end{array}$$

En conclusion, les solutions réelles de (E) sont les fonctions :
$$\begin{array}{rcl} ]0, +\infty[ & \longrightarrow & \mathbb{R} \\ t & \longmapsto & \displaystyle t - \frac{2}{t} + \lambda \frac{\sin t}{t} + \mu \frac{\cos t}{t} \end{array} \quad \text{avec } (\lambda, \mu) \in \mathbb{R}^2.$$

**Exercice 23**
1. Notons $n$ le degré $P$, de telle sorte que, comme $P$ est non nul, $P$ s'écrit :
$$P = \alpha_n X^n + \dots + \alpha_0 \quad \text{avec} \quad \alpha_n \neq 0.$$

En reportant dans l'équation $(E_0)$, on constate que le polynôme :
$$Q = (X^2 + 2X - 1) P'' + (X^2 - 3) P' - (2X + 2) P$$
est le polynôme nul car il vérifie :
$$\forall t \in \mathbb{R} \quad Q(t) = 0.$$

Or, le polynôme $Q$ s'écrit :
$$Q = (n - 2) \alpha_n X^{n+1} + \dots - (2\alpha_2 + 3\alpha_1 + 2\alpha_0).$$

Comme $\alpha_n \neq 0$, on a nécessairement $n = 2$.

1065

Chapitre 17. *Équations différentielles linéaires*

2. D’après la question précédente, on peut rechercher les solutions polynomiales non nulles de $(E_0)$ sous la forme $t \mapsto P(t)$ avec $P$ de la forme :
$$P = \alpha_2 X^2 + \alpha_1 X + \alpha_0 \quad \text{avec} \quad \alpha_2 \neq 0.$$
En reportant dans l’équation $(E_0)$ et, par unicité des coefficients, on obtient que $t \mapsto P(t)$ est solution de $(E_0)$ si, et seulement si :
$$\begin{cases} \alpha_1 & = & 0 \\ \alpha_0 & = & -\alpha_2. \end{cases}$$
Par suite, les solutions polynomiales de $(E_0)$ sont les fonctions :
$$t \mapsto \lambda(t^2 - 1) \quad \text{avec} \quad \lambda \in \mathbb{R}.$$

## **Exercice 24**

1. • Dans un premier temps, supposons que $\varphi$ soit une solution de $(E_0)$ développable en série entière sur un intervalle de la forme $]-*r, r*[$ avec $r > 0$. Pour $t \in ]-*r, r*[$, on a :
$$\varphi(t) = \sum_{n=0}^{+\infty} a_n t^n \quad \varphi'(t) = \sum_{n=1}^{+\infty} n a_n t^{n-1} \quad \text{et} \quad \varphi''(t) = \sum_{n=2}^{+\infty} n(n - 1) a_n t^{n-2}.$$
En injectant dans l’équation $(E_0)$, on a, pour tout $t \in ]-*r, r*[$ :
$$4t \sum_{n=2}^{+\infty} n(n - 1) a_n t^{n-2} + 2 \sum_{n=1}^{+\infty} n a_n t^{n-1} - \sum_{n=0}^{+\infty} a_n t^n = 0.$$
puis en réindexant les sommes pour obtenir dans chacune d’entre elles des termes en $t^n$ :
$$4 \sum_{n=1}^{+\infty} n(n + 1) a_{n+1} t^n + 2 \sum_{n=0}^{+\infty} (n + 1) a_{n+1} t^n - \sum_{n=0}^{+\infty} a_n t^n = 0,$$
ce qui donne, en regroupant les sommes :
$$(2 a_1 - a_0) + \sum_{n=1}^{+\infty} ((2n + 2)(2n + 1) a_{n+1} - a_n) t^n = 0.$$
Par unicité du développement en série entière, on peut identifier les coefficients :
$$\forall n \in \mathbb{N} \quad (2n + 2)(2n + 1) a_{n+1} - a_n = 0. \hfill (\star)$$
Il en résulte que :
$$\forall n \in \mathbb{N} \quad a_n = \frac{1}{(2n)!} a_0,$$
ce qui donne :
$$\varphi(t) = a_0 \sum_{n=0}^{+\infty} \frac{t^n}{(2n)!} \cdot$$

1066

**_Démonstrations et solutions des exercices du cours_**

*   Réciproquement :
    *   le rayon de convergence de la série entière $\sum \frac{t^n}{(2n)!}$ vaut $+\infty$ (on le montre par exemple par le critère de d'Alembert) ;
    *   la fonction $\varphi_1 : \mathbb{R} \longrightarrow \mathbb{R}$
        $$t \longmapsto \sum_{n=0}^{+\infty} \frac{t^n}{(2n)!}$$
        est telle que ses coefficients vérifient la propriété $(\star)$, et par suite, d'après les calculs effectués dans la première partie du raisonnement, $\varphi_1$ est solution de $(E_0)$ sur $\mathbb{R}$. Comme de plus $\varphi_1(0) = 1$, cela répond à la question.

2. (a) Pour $t > 0$, on a $\varphi_1(t) = \sum_{n=0}^{+\infty} \frac{(\sqrt{t})^{2n}}{(2n)!} = \text{ch}(\sqrt{t})$.

(b) Sur $]0, +\infty[$, l'équation $(E_0)$ s'écrit sous forme résolue :
$$(E_0) : x'' + \frac{x'}{2t} - \frac{x}{4t} = 0.$$
L'espace solution $\mathcal{S}_0$ sur cet intervalle est donc de dimension 2.
Soit $\varphi$ une solution de $(E)$ sur $]0, +\infty[$.
Le wronskien $W$ de la famille $(\varphi_1, \varphi)$ est solution sur $]0, +\infty[$ de l'équation différentielle :
$$x' + \frac{x}{2t} = 0.$$
En résolvant cette équation, on obtient $W(t) = \frac{\lambda}{\sqrt{t}}$ avec $\lambda \in \mathbb{R}$.
On a d'autre part :
$$\left( \frac{\varphi}{\varphi_1} \right)' = \frac{\varphi' \varphi_1 - \varphi \varphi'_1}{\varphi_1^2} = \frac{W}{\varphi_1^2}$$
et donc :
$$\forall t \in ]0, +\infty[ \quad \left( \frac{\varphi}{\varphi_1} \right)'(t) = \frac{\lambda}{\sqrt{t} \, \text{ch}^2(\sqrt{t})}.$$
En primitivant, on obtient qu'il existe une constante $\mu \in \mathbb{R}$ telle que :
$$\forall t \in ]0, +\infty[ \quad \frac{\varphi(t)}{\varphi_1(t)} = 2\lambda \, \text{th}(\sqrt{t}) + \mu \quad \text{puis} \quad \varphi(t) = 2\lambda \, \text{sh}(\sqrt{t}) + \mu \, \text{ch}(\sqrt{t}).$$
Comme la fonction $\varphi$ a été prise quelconque dans $\mathcal{S}_0$, il en résulte que :
$$\mathcal{S}_0 \subset \text{Vect}(t \mapsto \text{ch}(\sqrt{t}), t \mapsto \text{sh}(\sqrt{t})),$$
puis, comme $\text{dim} \, \mathcal{S}_0 = 2$, on obtient :
$$\mathcal{S}_0 = \text{Vect}(t \mapsto \text{ch}(\sqrt{t}), t \mapsto \text{sh}(\sqrt{t})).$$

**Remarque** Une fois connue la solution $\varphi_1 : t \mapsto \text{ch}(\sqrt{t})$, on peut, sans utiliser la méthode du wronskien, pressentir que la fonction $\varphi_2 : t \mapsto \text{sh}(\sqrt{t})$ l'est également. On peut alors conclure la résolution de $(E_0)$ en vérifiant simplement que cette fonction $\varphi_2$ est bien solution de $(E_0)$ et qu'elle est linéairement indépendante de $\varphi_1$.

1067

# Chapitre 17. Équations différentielles linéaires

3. (a) Pour $t < 0$, on a :

$$\varphi_1(t) = \sum_{n=0}^{+\infty} (-1)^n \frac{(\sqrt{-t})^{2n}}{(2n)!} = \cos(\sqrt{-t}).$$

(b) Sur $]-\infty, 0[$, l'équation $(E_0)$ s'écrit également sous forme résolue. Le même raisonnement qu'à la question précédente prouve que si $\varphi$ est solution de $(E_0)$ sur $]-\infty, 0[$, alors on a :

$$\varphi \in \text{Vect} (t \mapsto \cos (\sqrt{-t}), t \mapsto \sin (\sqrt{-t})).$$

On conclut alors, pour des raisons de dimensions, que :

$$ \mathcal{S}_0 = \text{Vect} \left( t \mapsto \cos \left( \sqrt{-t} \right), t \mapsto \sin \left( \sqrt{-t} \right) \right). $$

## **Exercice 25**

*   *Analyse.* Soit $f$ une solution de $(E)$.
    *   Considérons la fonction :

$$g : \left] -\frac{\pi}{2}, \frac{\pi}{2} \right[ \longrightarrow \mathbb{R}$$
$$u \longmapsto f(\tan u).$$

Comme $f$ est deux fois dérivable sur $\mathbb{R}$, $g$ est deux fois dérivable sur $]-\frac{\pi}{2}, \frac{\pi}{2}[$. Fixons $u \in ]-\frac{\pi}{2}, \frac{\pi}{2}[$. On a, en notant $t = \tan u$ :

$$g'(u) = (1 + t^2) f'(t)$$

et

$$g''(u) = (1 + t^2)^2 f''(t) + 2 t (1 + t^2) f'(t),$$

et l'on constate que :

$$g''(u) + 2 g'(u) + g(u) = (1 + t^2)^2 f''(t) + 2 (t + 1)(1 + t^2) f'(t) + f(t).$$

En utilisant le fait que $f$ est solution de $(E)$, on obtient :

$$g''(u) + 2g'(u) + g(u) = 0,$$

et donc fonction $g$ est solution sur $\mathbb{R}$ de l'équation différentielle :

$$(\widetilde{E}) : x'' + 2x' + x = 0.$$

Cette équation est une équation différentielle linéaire scalaire d'ordre 2 à coefficients constants que l'on sait résoudre. On en déduit l'existence de $(*a, b*) \in \mathbb{R}^2$ tel que, pour tout $u \in \mathbb{R}$ :

$$g(u) = (a u + b) e^{-u}.$$

*   Revenons sur la fonction $f$. Pour tout $t \in \mathbb{R}$, on a :

$$f(t) = f(\tan(\operatorname{Arctan} t)) = g(\operatorname{Arctan} t).$$

Par suite, on obtient l'expression suivante de $f(t)$ pour $t \in \mathbb{R}$ :

$$f(t) = (a \operatorname{Arctan} t + b) e^{-\operatorname{Arctan} t}.$$

1068

**_Démonstrations et solutions des exercices du cours_**

*   *Synthèse.* Réciproquement, on vérifie que toute fonction $f$ de la forme ci-dessus est bien solution de (E).

    **Remarque** Pour justifier la partie synthèse sans calculs, on peut remarquer que, d’après la partie « analyse » du raisonnement, on a :
    $$\mathcal{S}_0 \subset \text{Vect}(\varphi_1, \varphi_2) \quad \text{avec} \quad \varphi_1 = t \mapsto e^{-\arctan t} \quad \text{et} \quad \varphi_2 : t \mapsto \arctan(t)e^{-\arctan t}.$$
    Comme l’équation est d’ordre 2 et peut être mise sous forme résolue, on a $\dim \mathcal{S}_0 = 2$. L’inclusion précédente est donc une égalité.

## **Exercice 26**

1.  Sur les intervalles $]-\infty, 0[$ et $]0, +\infty[$, l’équation se met sous forme résolue.
    *   Sur $]-\infty, 0[$, les solutions sont les fonctions :
        $$t \mapsto \lambda t^2 + t^3 \quad \text{avec} \quad \lambda \in \mathbb{R}.$$
    *   Sur $]0, +\infty[$, les solutions sont les fonctions :
        $$t \mapsto \mu t^2 + t^3 \quad \text{avec} \quad \mu \in \mathbb{R}.$$

2.  Soit $\varphi$ une solution sur $\mathbb{R}$ de l’équation $(E)$.
    Elle est solution sur $]-\infty, 0[$, donc il existe $\lambda \in \mathbb{R}$ tel que :
    $$\forall t < 0 \quad \varphi(t) = \lambda t^2 + t^3.$$
    De même, $\varphi$ est solution sur $]0, +\infty[$, donc il existe $\mu \in \mathbb{R}$ tel que :
    $$\forall t > 0 \quad \varphi(t) = \mu t^2 + t^3.$$
    La continuité de $\varphi$ en 0 entraîne alors $\varphi(0) = 0$.
    On a donc la forme recherchée pour $\varphi$ :
    $$\varphi(t) = \begin{cases} \lambda t^2 + t^3 & \text{si } t \le 0 \\ \mu t^2 + t^3 & \text{si } t > 0 \end{cases}$$

    **Remarque** Pour obtenir $\varphi(0) = 0$, plutôt que d’évoquer la continuité de $\varphi$ en 0, on peut également utiliser le fait que $\varphi$ vérifie l’équation en 0, ce qui donne aussi $\varphi(0) = 0$.

3.  Réciproquement, soit $\varphi : \mathbb{R} \to \mathbb{R}$ une fonction de la forme :
    $$\varphi(t) = \begin{cases} \lambda t^2 + t^3 & \text{si } t \le 0 \\ \mu t^2 + t^3 & \text{si } t > 0 \end{cases} \quad \text{avec } (\lambda, \mu) \in \mathbb{R}^2.$$
    Montrons que $\varphi$ est solution de (E) sur $\mathbb{R}$.
    *   Cette fonction $\varphi$ est dérivable sur $\mathbb{R}^*$ et est manifestement solution de l’équation (E) sur les intervalles $]-\infty, 0[$ et $]0, +\infty[$.
    *   On voit rapidement que $\varphi$ est de plus continue en 0.
    *   Pour tout $t < 0$, on a $\varphi'(t) = 2\lambda t + 3t^2$. On a donc $\varphi'(t) \xrightarrow[t \to 0^-]{} 0$, ce qui prouve que $\varphi$ est dérivable à gauche en 0 et $\varphi'_g(0) = 0$.
        De même, on montre que $\varphi$ est dérivable à droite en 0 et que $\varphi'_d(0) = 0$.
        Comme $\varphi'_g(0) = \varphi'_d(0)$, la fonction $\varphi$ est dérivable en 0 et $\varphi'(0) = 0$.
    *   Enfin, on a $0 \cdot \varphi'(0) - 2\varphi(0) = 0$, donc $\varphi$ vérifie l’équation différentielle en 0.

    La fonction $\varphi$ est donc solution de (E) sur $\mathbb{R}$.

1069

# Chapitre 17. Équations différentielles linéaires

## **Exercice 27**

• Tout d’abord, l’équation se met sous forme résolue sur les intervalles $]-\infty, 0[$ et $]0, +\infty[$ :
* sur $]-\infty, 0[$, les solutions sont $t \mapsto \lambda e^{-1/t}$ avec $\lambda \in \mathbb{R}$ ;
* sur $]0, +\infty[$, les solutions sont $t \mapsto \mu e^{-1/t}$ avec $\mu \in \mathbb{R}$.

• Recherchons par analyse-synthèse les solutions de (E) sur $\mathbb{R}$.
* *Analyse.* Soit $\varphi$ une solution de (E) sur $\mathbb{R}$.
    $\star$ Tout d’abord, $\varphi$ est solution de (E) sur l’intervalle $]-\infty, 0[$ et sur l’intervalle $]0, +\infty[$, donc il existe $(\lambda, \mu) \in \mathbb{R}^2$ tel que :

$$\forall t \in \mathbb{R} \quad \phi(t) = \begin{cases} \lambda e^{-1/t} & \text{si } t < 0 \\ \mu e^{-1/t} & \text{si } t > 0. \end{cases}$$

    $\star$ De plus, $\varphi$ est dérivable sur $\mathbb{R}$ et donc continue. En particulier, $\varphi$ est continue en 0, et donc possède une limite finie à gauche en 0.
    Comme $\lim_{t \to 0^-} e^{-1/t} = +\infty$, on a nécessairement $\lambda = 0$.
    La fonction $\varphi$ vérifie donc :

$$\forall t \in \mathbb{R} \quad \varphi(t) = \begin{cases} 0 & \text{si } t \leqslant 0 \\ \mu e^{-1/t} & \text{si } t > 0. \end{cases}$$

* *Synthèse.* Réciproquement, supposons que $\varphi$ est de la forme ci-dessus.
    $\star$ La fonction $\varphi$ est dérivable sur $\mathbb{R}^*$ et vérifie l’équation sur $]-\infty, 0[$ et $]0, +\infty[$.
    $\star$ Puisque $\varphi(t) = 0$ pour tout $t \le 0$, la fonction $\varphi$ est dérivable à gauche en 0 et $\varphi'_g(0) = 0$.
    $\star$ Puisque $\varphi'(t) = \mu \frac{e^{-1/t}}{t^2}$ pour tout $t > 0$, on a, par croissances comparées, $\varphi'(t) \underset{t \to 0^+}{\longrightarrow} 0$. Comme $\varphi$ est continue en 0, on en déduit que $\varphi$ est dérivable à droite en 0 et $\varphi'_d(0) = 0$.
    $\star$ Comme $\varphi'_g(0) = \varphi'_d(0)$, $\varphi$ est dérivable en 0 et $\varphi'(0) = 0$.
    $\star$ Enfin, il est facile de constater que $\varphi$ vérifie l’équation en 0.
    Par suite, $\varphi$ est bien solution de (E) sur $\mathbb{R}$.

## **Exercice 28**

• Tout d’abord, on constate que l’équation se résout facilement sur les intervalles $]-\infty, 1[$ et $]1, +\infty[$ où elle se met sous forme résolue :
* sur $]-\infty, 1[$, les solutions sont :
$$t \mapsto \frac{\lambda + t^2}{2(1 - t)} \quad \text{avec} \quad \lambda \in \mathbb{R} ;$$
* sur $]1, +\infty[$, les solutions sont :
$$t \mapsto \frac{\mu + t^2}{2(1 - t)} \quad \text{avec} \quad \mu \in \mathbb{R}.$$

1070

**_Démonstrations et solutions des exercices du cours_**

• Recherchons par analyse-synthèse les solutions de (E) sur $\mathbb{R}$.

*   *Analyse.* Soit $\varphi$ une solution sur $\mathbb{R}$.
    *   Tout d'abord, $\varphi$ est solution de (E) sur l'intervalle $]-\infty, 1[$ et sur l'intervalle $]1, +\infty[$, donc il existe $(\lambda, \mu) \in \mathbb{R}^2$ tel que :

$$\varphi(t) = \begin{cases} \displaystyle \frac{\lambda + t^2}{2(1 - t)} & \text{si } t < 1 \\ \displaystyle \frac{\mu + t^2}{2(1 - t)} & \text{si } t > 1. \end{cases}$$

    *   De plus, $\varphi$ est dérivable sur $\mathbb{R}$ et donc continue. En particulier, $\varphi$ est continue en 1, et donc possède une limite finie en 1. Cela impose d'avoir $\lambda = \mu = -1$. On obtient :

$$\forall t \in \mathbb{R}^* \quad \varphi(t) = \frac{t^2 - 1}{2(1 - t)} = -\frac{t + 1}{2},$$

et donc, par continuité en 0 :

$$\forall t \in \mathbb{R} \quad \varphi(t) = -\frac{t + 1}{2}.$$

*   *Synthèse.* Réciproquement, on vérifie que la fonction :

$$\varphi : t \mapsto -\frac{t + 1}{2}$$

est solution de (E) sur $\mathbb{R}$. C'est donc l'unique solution de (E) sur $\mathbb{R}$.

### **Exercice 29**

• *Analyse.* Soit $\varphi$ une solution de $(E_0)$ sur $\mathbb{R}$.

*   Comme $\varphi$ est solution de $(E_0)$ sur les intervalles $]-\infty, 0[$ et $]0, +\infty[$, il existe $(\lambda_1, \lambda_2, \mu_1, \mu_2) \in \mathbb{R}^4$ tel que :

$$
\forall t \in \mathbb{R} \quad \varphi(t) = \begin{cases} \lambda_1 \cos(\sqrt{-t}) + \lambda_2 \sin(\sqrt{-t}) & \text{si } t < 0 \\ \mu_1 \operatorname{ch}(\sqrt{t}) + \mu_2 \operatorname{sh}(\sqrt{t}) & \text{si } t > 0. \end{cases}
$$

*   La fonction $\varphi$ est continue sur $\mathbb{R}$, donc en particulier continue en 0. On a ainsi :

$$\varphi(0) = \lim_{0^-} \varphi = \lim_{0^+} \varphi, \quad \text{et donc} \quad \varphi(0) = \lambda_1 = \mu_1.$$

*   La fonction $\varphi$ est dérivable sur $\mathbb{R}$, donc en particulier en 0.
    *   Pour tout $t > 0$, on a :

$$\varphi'(t) = \frac{\mu_1 \text{sh}(\sqrt{t})}{2\sqrt{t}} + \frac{\mu_2 \text{ch}(\sqrt{t})}{2\sqrt{t}}.$$

Si $\mu_2$ n'était pas nul, alors on aurait $\varphi'(t) \xrightarrow[t \to 0^+]{} \pm\infty$ (selon le signe de $\mu_2$), ce qui contredirait la dérivabilité à droite de $\varphi$ en 0. Donc $\mu_2 = 0$.

1071

# Chapitre 17. Équations différentielles linéaires

$\star$ Pour tout $t < 0$, on a :

$$\varphi'(t) = \frac{\lambda_1 \sin(\sqrt{-t})}{2\sqrt{-t}} - \frac{\lambda_2 \cos(\sqrt{-t})}{2\sqrt{-t}}.$$

Si $\lambda_2$ n'était pas nul, alors on aurait $\varphi'(t) \underset{t \to 0^-}{\longrightarrow} \pm \infty$ (selon le signe de $\lambda_2$), ce qui contredirait la dérivabilité à gauche de $\varphi$ en 0. Donc $\lambda_2 = 0$.

$\ast$ On obtient que :

$$\varphi(t) = \begin{cases} \lambda_1 \cos(\sqrt{-t}) & \text{si } t < 0 \\ \lambda_1 \text{ch}(\sqrt{t}) & \text{si } t \geqslant 0 \end{cases}$$

et donc finalement :

$$\forall t \in \mathbb{R} \quad \varphi(t) = \lambda_1 \sum_{n=0}^{+\infty} \frac{t^n}{(2n)!} \cdot$$

$\bullet$ *Synthèse.* Réciproquement, toutes les fonctions de la forme précédente sont solutions de $(E_0)$ : ce sont les solutions développables en série entière déjà obtenues à l'exercice 24 de la page 1043.

## **Exercice 30**

1. $\bullet$ L'application $z_0$ étant continue, sa restriction au segment $K$ est bornée, ce qui justifie l'existence de $M$.
   $\bullet$ De même, $a$ étant continue, sa restriction au segment $K$ est bornée, ce qui justifie l'existence de $\alpha$.

2. Procédons par récurrence.
   $\bullet$ *Initialisation.* D'après la question précédente, on a, en utilisant l'inégalité $(\star)$ :

$$\forall u \in K \quad \|a(u) \cdot z_0(u)\| \leqslant k \|a(u)\| \|z_0(u)\| \leqslant k \alpha M.$$

   Donc, par positivité de l'intégrale, on a, pour tout $t \in K$ :

$$\|z_1(t)\| \leqslant \left| \int_{t_0}^t \|a(u) \cdot z_0(u)\| \,\mathrm{d}u \right| \leqslant k M \alpha |t - t_0|.$$

   Cela prouve le résultat au rang 1.

   $\bullet$ *Hérédité.* Soit $n \in \mathbb{N}^*$. Supposons le résultat vrai au rang $n$.
   Soit $t \in K$. On a, en utilisant les majorations de la question précédente :

$$
\|z_{n+1}(t)\| \leqslant \left| \int_{t_0}^t \|a(s) \cdot z_n(s)\| \, \mathrm{d}s \right| \leqslant \left| \int_{t_0}^t k \|a(s)\| \|z_n(s)\| \, \mathrm{d}s \right|
$$
$$
\leqslant \left| \int_{t_0}^t k \alpha \|z_n(s)\| \, \mathrm{d}s \right|.
$$

   L'hypothèse de récurrence nous donne de plus :

$$\forall s \in K \quad \|z_n(s)\| \leqslant M \frac{(k \alpha |s - t_0|)^n}{n!}$$

1072

**_Démonstrations et solutions des exercices du cours_**

et permet donc de poursuivre la majoration :

$$
\begin{aligned}
\|z_{n+1}(t)\| & \leqslant \frac{M(k \alpha)^{n+1}}{n!} \left| \int_{t_0}^t |s - t_0|^n \, \mathrm{d}s \right| \leqslant \frac{M(k \alpha)^{n+1}}{n!} \frac{|t - t_0|^{n+1}}{n+1} \\
& = M \frac{(k \alpha |t - t_0|)^{n+1}}{(n+1)!}
\end{aligned}
$$

Cela prouve le résultat au rang $n + 1$.

3. D’après le résultat de la question précédente, on a, en notant $\ell$ la longueur du segment $K$ :

$$ \|z_n\|_{\infty,K} \le M \frac{(k \alpha \ell)^n}{n!}. $$

Il en résulte, par comparaison, que la série $\sum \|z_n\|_{\infty,K}$ converge.
Cela prouve la convergence normale sur $K$ de la série de fonctions $\sum z_n$.

## **Exercice 31**

1. Appliquons le résultat de l’exercice 30 en prenant $z_0 = h$.
    * Il a été obtenu que la série $\sum z_n$ converge normalement sur tout segment de $I$.
    * La relation vérifiée par la fonction $h$ entraîne que :
$$\forall n \in \mathbb{N} \quad z_n = h.$$
Cela n’est possible que si $h$ est l’application nulle.

2. Soit $\varphi_1$ et $\varphi_2$ deux solutions du problème de Cauchy $(\mathcal{P})$.
    On a alors, pour tout $t \in I$ :

$$\varphi_1(t) = x_0 + \int_{t_0}^{t} a(u) \cdot \varphi_1(u) \mathrm{d}u + \int_{t_0}^{t} b(u) \mathrm{d}u$$

$$\varphi_2(t) = x_0 + \int_{t_0}^{t} a(u) \cdot \varphi_2(u) \mathrm{d}u + \int_{t_0}^{t} b(u) \mathrm{d}u$$

et donc en faisant la différence :

$$\varphi_1(t) - \varphi_2(t) = \int_{t_0}^t a(u) \cdot (\varphi_1(u) - \varphi_2(u)) \mathrm{d}u.$$

Le résultat de la première question donne alors $\varphi_1 - \varphi_2 = 0$, *i.e.* $\varphi_1 = \varphi_2$.

1073

# Chapitre 17. Équations différentielles linéaires

## Exercice 32

1. Notons $z_n = w_{n+1} - w_n$. Pour $n \in \mathbb{N}$ et $t \in I$, on a :

$$
\begin{aligned}
z_{n+1}(t) &= w_{n+2}(t) - w_{n+1}(t) \\
&= \left( x_0 + \int_{t_0}^t (a(s) \cdot w_{n+1}(s) + b(s)) \mathrm{d}s \right) \\
&\quad - \left( x_0 + \int_{t_0}^t (a(s) \cdot w_n(s) + b(s)) \mathrm{d}s \right) \\
&= \int_{t_0}^t a(s) \cdot (w_{n+1}(s) - w_n(s)) \mathrm{d}s \\
&= \int_{t_0}^t a(s) \cdot z_n(s) \mathrm{d}s.
\end{aligned}
$$

La suite $(z_n)$ vérifie donc les hypothèses de l'exercice 30. Il en résulte que la série $\sum z_n$ converge normalement sur tout segment de $I$. Il en découle que cette série de fonctions $\sum z_n$, et donc la suite $(w_n)$, converge uniformément sur tout segment de $I$.

2. &bull; Prouvons que la suite de fonctions $(t \mapsto a(t) \cdot w_n(t) + b(t))$ converge uniformément sur tout segment de $I$ vers la fonction $t \mapsto a(t) \cdot \varphi(t) + b(t)$.
   Soit $K$ est un segment de $I$.
   Puisque $a$ est continue sur $K$, il existe une constante $\alpha$ telle que :
   $$\forall t \in K \quad \|a(t)\| \le \alpha.$$
   Pour tout $t \in K$, on a, en utilisant l'inégalité $(\star)$ :

$$
\begin{aligned}
\| (a(t) \cdot w_n(t) + b(t)) - (a(t) \cdot \varphi(t) + b(t)) \| &= \| a(t) \cdot (w_n(t) - \varphi(t)) \| \\
&\le k \| a(t) \| \| w_n(t) - \varphi(t) \| \\
&\le k \alpha \| w_n(t) - \varphi(t) \|.
\end{aligned}
$$

   Par suite, la convergence uniforme sur $K$ de la suite $(w_n)$ vers $\varphi$ entraîne la convergence uniforme sur $K$ de la suite $(t \mapsto a(t) \cdot w_n(t) + b(t))$ vers la fonction $t \mapsto a(t) \cdot \varphi(t) + b(t)$.

&bull; Soit $t \in I$. Par convergence uniforme sur le segment d'extrémités $t_0$ et $t$, on a :

$$\int_{t_0}^t (a(s) \cdot w_n(s) + b(s)) \mathrm{d}s \xrightarrow[n \to +\infty]{} \int_{t_0}^t (a(s) \cdot \varphi(s) + b(s)) \mathrm{d}s.$$

Ainsi, en passant à la limite quand $n \to +\infty$ dans la relation :
$$w_{n+1}(t) = x_0 + \int_{t_0}^t (a(s) \cdot w_n(s) + b(s)) \text{d}s,$$
il vient, par unicité de la limite :
$$\varphi(t) = x_0 + \int_{t_0}^t (a(s) \cdot \varphi(s) + b(s)) \text{d}s.$$

Comme on a de plus $\varphi(t_0) = x_0$, la fonction $\varphi$ est bien solution du problème de Cauchy $(\mathcal{P})$.

1074

***Exercices***

# S'entraîner et approfondir

**17.1** Soit $p : I \to \mathbb{K}$ une fonction de classe $\mathcal{C}^1$ et $q : I \to \mathbb{K}$ une fonction continue.
Montrer qu'il existe une fonction $\alpha : I \to \mathbb{K}$, deux fois dérivable et ne s'annulant pas, telle que l'équation différentielle :

$$(E) : x'' + p(t) x' + q(t) x = 0$$

se traduise, sur la fonction $z = \frac{x}{\alpha}$, en une équation du type :

$$(\widetilde{E}) : z'' + r(t) z = 0 \quad \text{avec } r : I \to \mathbb{K} \text{ continue.}$$

**17.2** Résoudre sur $I = ]-1, 1[$ l'équation réelle :

$$4(1 - t^2) x'' - 4tx' + x = 0. \hfill (E)$$

*On cherchera des solutions développables en série entière.*

**17.3** *Équation d'Airy*
On considère l'équation différentielle :

$$(E) : y'' - xy = 0$$

Montrer, sans chercher à les expliciter à l'aide des fonctions usuelles, que toutes les solutions de $(E)$ sont développables en série entière sur $\mathbb{R}$.

**17.4** Résoudre dans $\mathbb{R}$ le système différentiel :

$$
(S) : \begin{cases} x' &= x + 8y + e^t \\ y' &= 2x + y \end{cases}
$$

**17.5** Résoudre dans $\mathbb{R}$ le système différentiel (Sys) : 

**17.5** Résoudre dans $\mathbb{R}$ le système différentiel (Sys) : $\begin{cases} x' & = & y \\ y' & = & z \\ z' & = & x \end{cases}$

**17.6** Résoudre le système réel :

$$(\text{Sys}) : \begin{cases} x' &= x - ty + te^t \\ y' &= tx + y \end{cases} \hfill (1)$$

*On pourra chercher une équation différentielle vérifiée par $x + iy$.*

**17.7** Soit $g : \mathbb{R} \to \mathbb{R}$ une fonction de classe $\mathcal{C}^1$, croissante et bornée.
Montrer que toute solution sur $\mathbb{R}$ de l'équation différentielle :

$$(E) : y'' + y = g$$

est bornée.

**17.8** Soit $f : \mathbb{R}_+ \to \mathbb{R}$ de classe $\mathcal{C}^1$ telle que $f' + f$ tend vers 0 en $+\infty$.
Montrer que $f$ et $f'$ tendent vers 0 en $+\infty$.

1075

# Chapitre 17. Équations différentielles linéaires

**17.9** Soit $f : \mathbb{R}_+ \to \mathbb{R}$ de classe $\mathcal{C}^2$ telle que $f'' + 3f' + 2f$ tend vers 0 en $+\infty$.
Montrer que $f$, $f'$ et $f''$ tendent vers 0 en $+\infty$.

**17.10** Soit $q : \mathbb{R} \to \mathbb{R}$ continue. On considère l'équation différentielle :
$$(E) : y'' + q(t) y = 0.$$
Soit $u$ et $v$ deux solutions de (E) linéairement indépendantes.
1. Notons $Z_u$ l'ensemble des zéros (*i.e.* des points d'annulation) de $u$.
   Montrer que tout point de $Z_u$ est isolé, c'est-à-dire que l'on a :
$$\forall t_0 \in Z_u \quad \exists r > 0 \quad Z_u \cap [t_0 - r, t_0 + r] = \{t_0\}.$$
2. Soit $t_0$ un point d'annulation de $u$. Supposons que $u$ s'annule sur l'intervalle $]t_0, +\infty[$. Montrer qu'il est licite de considérer $t_1$ le plus petit point d'annulation de $u$ sur l'intervalle $]t_0, +\infty[$.
3. Montrer que, sur l'intervalle $]t_0, t_1[$, $v$ s'annule une et une seule fois.

**17.11** Soit $(*a, b*) \in \mathcal{C}(\mathbb{R}, \mathbb{R})^2$. On considère l'équation différentielle homogène :
$$(E) : y'' + ay' + by = 0,$$
dont on note $\mathcal{S}_0$ l'espace des solutions.
Montrer l'équivalence entre les deux assertions :
(i) il existe une base $(f, g)$ de $\mathcal{S}_0$ avec $f$ paire et $g$ impaire ;
(ii) la fonction $a$ est impaire et la fonction $b$ est paire.

**17.12** Soit $A$ une matrice symétrique réelle telle que $\text{sp}(A) \subset \mathbb{R}_+^*$ et $\varphi$ une solution réelle non nulle sur $\mathbb{R}$ du système différentiel :
$$X' = AX$$
Montrer que l'application $t \mapsto \|\varphi(t)\|$ est une bijection de $\mathbb{R}$ sur $\mathbb{R}_+^*$ (la norme $\|\cdot\|$ désignant la norme euclidienne sur $\mathbb{R}^n$).

**17.13** Soit $n \in \mathbb{N}^*$ et $A \in \mathcal{M}_n(\mathbb{C})$. Montrer que :
$$\text{sp}(\exp(A)) = \{e^\lambda ; \lambda \in \text{sp}(A)\}.$$

**17.14** Soit $n \in \mathbb{N}^*$ et $A : \mathbb{R} \to \mathcal{M}_n(\mathbb{C})$ continue et périodique de période $T > 0$.
Montrer que le système différentiel homogène
$$(\text{Sys}) : X' = A(t) X$$
admet une solution non nulle $\varphi$ pour laquelle il existe $\lambda \in \mathbb{C}$ tel que :
$$\forall t \in \mathbb{R} \quad \varphi(t + T) = \lambda \varphi(t).$$

1076

***Exercices***

**17.15** Soit $n \in \mathbb{N}^*$ et $A \in \mathcal{M}_n(\mathbb{C})$. On s'intéresse au système différentiel :
$$(Sys) : X' = *A X.*$$

1. (a) Soit $p \in \mathbb{N}^*$, $\lambda \in \mathbb{C}$ tel que $\text{Re}(\lambda) < 0$ et $N \in \mathcal{M}_p(\mathbb{C})$ une matrice nilpotente. Montrer que :
$$\exp\left(t(\lambda I_p + N)\right) \underset{t \to +\infty}{\longrightarrow} 0.$$
*Indication : on pourra commencer par exprimer $\exp\left(t(\lambda I_p + N)\right)$ comme un polynôme en $N$.*

(b) Montrer que si chaque valeur propre de $A$ est de partie réelle strictement négative, alors toute solution du système (Sys) tend vers 0 en $+\infty$.

2. Donner une condition nécessaire et suffisante pour que toutes les solutions du système (Sys) soient bornées sur $\mathbb{R}$.

**17.16** *(Polytechnique 2015)*
Donner une condition nécessaire et suffisante sur $\beta \in \mathcal{C}(\mathbb{R}, \mathbb{R}_+^*)$ pour que le système différentiel :
$$(Sys) : \begin{cases} x'' & = & -\beta(t) y' \\ y'' & = & \beta(t) x' \end{cases}$$
admette une solution périodique non constante.

**17.17** *(Polytechnique 2015)*
Soit $\varphi : \mathbb{R} \to \mathbb{C}$ une fonction continue et $2\pi$-périodique. Existe-t-il une solution $2\pi$-périodique de l'équation différentielle :
$$(E) : y^{(4)} + y = \varphi.$$

1077

Chapitre 17. Équations différentielles linéaires

# Solution des exercices

**17.1** Soit $\varphi : I \to \mathbb{K}$ une fonction deux fois dérivable. Si $\alpha : I \to \mathbb{K}$ est une fonction deux fois dérivable ne s'annulant pas, alors la fonction $\psi = \frac{\varphi}{\alpha}$ est aussi deux fois dérivable et l'on a :
$$\varphi' = \alpha' \psi + \alpha \psi' \quad \text{et} \quad \varphi'' = \alpha'' \psi + 2 \alpha' \psi' + \alpha \psi''.$$

On obtient alors que $\varphi$ est solution de (E) si, et seulement si, $\psi$ vérifie :
$$\forall t \in I \quad \alpha(t) \psi''(t) + (2 \alpha'(t) + p(t) \alpha(t)) \psi'(t) + (\alpha''(t) + p(t) \alpha'(t) + q(t) \alpha(t)) \psi(t) = 0.$$

Choisissons alors pour $\alpha$ une solution non nulle de l'équation d'ordre 1 :
$$y' + \frac{p(t)}{2} y = 0.$$

Une telle fonction $\alpha$ ne s'annule pas sur $I$ et, puisque $p$ est de classe $\mathcal{C}^1$ sur $I$, $\alpha$ est de classe $\mathcal{C}^2$ sur $I$. Alors, les solutions $\varphi$ de l'équation :
$$(E) : x'' + p(t) x' + q(t) x = 0$$
sont toutes les fonctions $\varphi : t \mapsto \alpha(t) \psi(t)$ où $\psi$ est solution de l'équation :
$$z'' + r(t) z = 0 \quad \text{avec} \quad r = \frac{\alpha'' + p \alpha' + q \alpha}{\alpha}.$$

Comme $p$ et $q$ sont continues et $\alpha$ de classe $\mathcal{C}^2$, la fonction $r$ est continue.

**17.2** $\bullet$ Commençons par chercher les solutions de (E) développables en série entière.
* *Analyse.* Soit $\varphi$ une solution de (E) sur $]-1, 1[$, somme d'une série entière $\sum a_n t^n$ de rayon de convergence $R > 0$.
Pour $t \in ]-1, 1[ \cap ]-*R, R*[$, on a :
$$4(1 - t^2) \varphi''(t) - 4t \varphi'(t) + \varphi(t) = 0,$$
ce qui donne, en remplaçant $\varphi(t)$, $\varphi'(t)$ et $\varphi''(t)$ par leurs développements en série entière et après arrangement du calcul :
$$\sum_{<sub>n=0</sub>}^{+\infty} (4(n+2)(n+1) a_{n+2} - (4n^2 - 1) a_n) t^n = 0.$$

Par unicité du développement en série entière, l'égalité précédente se traduit par le fait que pour tout $n \in \mathbb{N}$ :
$$4(n+2)(n+1) a_{n+2} = (2n - 1)(2n + 1) a_n \tag{$\star$}$$
$$= (1 - 2n)(1 - 2n - 2) a_n$$

c'est-à-dire
$$(n+2)(n+1) a_{n+2} = \left(\frac{1}{2} - n\right) \left(\frac{1}{2} - n - 1\right) a_n$$

ou encore, en notant $\alpha = \frac{1}{2}$ :
$$a_{n+2} = \frac{(\alpha - n)(\alpha - n - 1)}{(n+2)(n+1)} a_n.$$

1078

**_Solution des exercices_**

On obtient ainsi, en distinguant les valeurs paires et impaires (et en utilisant les coefficients binomiaux généralisés) :

$$a_{2n} = \frac{(\alpha)(\alpha - 1) \cdots (\alpha - 2n + 2)(\alpha - 2n + 1)}{(2n)!} a_0 = \binom{\alpha}{2n} a_0$$

et

$$a_{2n+1} = \frac{(\alpha - 1)(\alpha - 2) \cdots (\alpha - 2n + 1)(\alpha - 2n)}{(2n + 1)!} a_1 = \frac{1}{\alpha} \binom{\alpha}{2n + 1} a_1.$$

Il en résulte que pour tout $t \in ]-1, 1[ \cap ]-*R, R*[$ :

$$\varphi(t) = a_0 \varphi_1(t) + \frac{a_1}{\alpha} \varphi_2(t)$$

avec :

$$\varphi_1 : t \mapsto \sum_{n=0}^{+\infty} \binom{\alpha}{2n} t^{2n} \quad \text{et} \quad \varphi_2 : t \mapsto \sum_{n=0}^{+\infty} \binom{\alpha}{2n + 1} t^{2n+1}$$

*   *Synthèse.* Réciproquement, les fonctions $\varphi_1$ et $\varphi_2$ sont bien définies et développables en série entière sur $]-1, 1[$ (le rayon de convergence des séries entières considérées valant 1), et leurs coefficients vérifient la relation de récurrence $(\star)$. Ainsi, $\varphi_1$ et $\varphi_2$ sont bien solutions de (E) sur $]-1, 1[$.

• De ce qui précède on a, en notant $\mathcal{S}$ l'espace vectoriel des solutions de (E) :

$$\text{Vect}(\varphi_1, \varphi_2) \subset \mathcal{S}.$$

Puisque $(\varphi_1(0), \varphi_1'(0)) = (1, 0)$ et $(\varphi_2(0), \varphi_2'(0)) = (0, 1/2)$, les fonctions $\varphi_1$ et $\varphi_2$ sont linéairement indépendantes.
Comme de plus l'équation (E) est d'ordre 2, à coefficients continus, et se met sous forme résolue sur l'intervalle $]-1, 1[$, on a $\dim \mathcal{S} = 2$.
Ainsi, l'inclusion précédente est une égalité, ce qui conclut la résolution de (E) :

$$\mathcal{S} = \text{Vect}(\varphi_1, \varphi_2).$$

**Remarque** On peut simplifier le résultat en remarquant que pour $t \in ]-1, 1[$ :

$$(\varphi_1 + \varphi_2)(t) = \sum_{n=0}^{+\infty} \binom{\alpha}{n} t^n \quad \text{et} \quad (\varphi_1 - \varphi_2)(t) = \sum_{n=0}^{+\infty} (-1)^n \binom{\alpha}{n} t^n$$

autrement dit :

$$(\varphi_1 + \varphi_2)(t) = \sqrt{1+t} \quad \text{et} \quad (\varphi_1 - \varphi_2)(t) = \sqrt{1-t}$$

Les fonctions $t \mapsto \sqrt{1+t}$ et $t \mapsto \sqrt{1-t}$ étant linéairement indépendantes, on a :

$$\mathcal{S} = \text{Vect} \left( t \mapsto \sqrt{1+t}, t \mapsto \sqrt{1-t} \right).$$

1079

# Chapitre 17. Équations différentielles linéaires

**17.3** • Remarquons tout d’abord que l’équation (E) est une équation linéaire scalaire homogène d’ordre 2, à coefficients continus, et écrite sous forme résolue, donc son ensemble $\mathcal{S}$ de solutions est un espace vectoriel de dimension 2. Ainsi, pour prouver que toutes les solutions sont développables en série entière sur $\mathbb{R}$, il suffit de prouver qu’il en existe deux linéairement indépendantes.

• Soit $f : \mathbb{R} \to \mathbb{R}$ développable en série entière sur $\mathbb{R}$ s’écrivant, pour tout $x \in \mathbb{R}$ :
$$f(x) = \sum_{n=0}^{+\infty} a_n x^n.$$

Pour tout $x \in \mathbb{R}$, on a, après simplification :
$$f''(x) - xf(x) = 2a_2 + \sum_{n=0}^{+\infty} ((n + 3)(n + 2)a_{n+3} - a_n)x^{n+1}.$$

Par unicité du développement en série entière, une telle fonction $f$ est donc solution de l’équation (E) si, et seulement si, la suite $(a_n)$ vérifie :
$$a_2 = 0 \quad \text{et} \quad \forall n \in \mathbb{N} \quad (n + 3)(n + 2)a_{n+3} - a_n = 0. \hfill (\star)$$

On peut constater qu’une telle suite $(a_n)$ est entièrement caractérisée par ses deux premiers termes $a_0$ et $a_1$ et que tous les termes de la forme $a_{3n+2}$ sont nuls.

• Nous sommes alors en mesure d’expliciter deux solutions linéairement indépendantes $\varphi_1$ et $\varphi_2$ développables en série entière sur $\mathbb{R}$.

  $*$ Considérons la suite $(\alpha_n)$ définie par :
  $$(\alpha_0, \alpha_1, \alpha_2) = (1, 0, 0) \quad \text{et} \quad \forall n \in \mathbb{N} \quad \alpha_{n+3} = \frac{\alpha_n}{(n + 3)(n + 2)}.$$

  On a alors :
  $$\forall n \in \mathbb{N} \quad \alpha_{3n+1} = \alpha_{3n+2} = 0.$$

  Posons, lorsque c’est possible :
  $$\varphi_1(x) = \sum_{n=0}^{+\infty} \alpha_n x^n = \sum_{n=0}^{+\infty} \alpha_{3n} x^{3n}.$$

  La relation de récurrence vérifiée par la suite $(\alpha_n)$ donne, pour tout $x \in \mathbb{R}$ :
  $$\left| \frac{\alpha_{3n+3} \, x^{3n+3}}{\alpha_{3n} \, x^{3n}} \right| = \frac{|x|^3}{(3n + 3)(3n + 2)} \xrightarrow[n \to +\infty]{} 0.$$

  La règle de d’Alembert assure alors que la série entière $\sum \alpha_{3n} t^{3n}$ a un rayon de convergence valant $+\infty$. La fonction $\varphi_1$ est donc bien définie sur $\mathbb{R}$, et est donc une solution de (E) développable en série entière sur $\mathbb{R}$.

  $*$ De la même manière, si l’on pose :
  $$(\beta_0, \beta_1, \beta_2) = (0, 1, 0) \quad \text{et} \quad \forall n \in \mathbb{N} \quad \beta_{n+3} = \frac{\beta_n}{(n + 3)(n + 2)},$$

  alors la fonction $\varphi_2$ :
  $$\begin{aligned} \varphi_2 : \mathbb{R} &\longrightarrow \mathbb{R} \\ x &\longmapsto \sum_{n=0}^{+\infty} \beta_{3n+1} x^{3n+1} \end{aligned}$$
  est une solution de (E) développable en série entière sur $\mathbb{R}$.

  $*$ Comme $(\varphi_1(0), \varphi_1'(0)) = (1, 0)$ et $(\varphi_2(0), \varphi_2'(0)) = (0, 1)$, les fonctions $\varphi_1$ et $\varphi_2$ sont linéairement indépendantes, ce qui termine l’exercice.

1080

***Solution des exercices***

**17.4** Le système différentiel $(S)$ s'écrit matriciellement, en notant $X = \begin{pmatrix} x \\ y \end{pmatrix}$ :

$$X' = AX + B(t) \quad \text{avec} \quad A = \begin{pmatrix} 1 & 8 \\ 2 & 1 \end{pmatrix} \quad \text{et} \quad B(t) = \begin{pmatrix} e^t \\ 0 \end{pmatrix}.$$

L'étude des éléments propres de $A$ prouve que $A$ est diagonalisable et que :

$$A = *PDP*^{-1} \quad \text{avec} \quad P = \begin{pmatrix} 2 & -2 \\ 1 & 1 \end{pmatrix} \quad \text{et} \quad D = \begin{pmatrix} 5 & 0 \\ 0 & -3 \end{pmatrix}.$$

En notant $Y = P^{-1}X$, on a alors :

$$\begin{aligned} X' = AX + B(t) &\iff X' = *PDP*^{-1}X + B(t) \\ &\iff P^{-1}X' = DP^{-1}X + P^{-1}B(t) \\ &\iff Y' = DY + P^{-1}B(t). \end{aligned}$$

Si l'on trouve les solutions $Y$ du dernier système différentiel ci-dessus, alors, via la relation $X = PY$, on en déduira les solutions du système initial. On a :

$$P^{-1} = \frac{1}{4} \begin{pmatrix} 1 & 2 \\ -1 & 2 \end{pmatrix} \quad \text{et} \quad P^{-1}B(t) = \begin{pmatrix} \frac{e^t}{4} \\ -\frac{e^t}{4} \end{pmatrix}.$$

En notant $Y = \begin{pmatrix} y_1 \\ y_2 \end{pmatrix}$, le système différentiel $Y' = DY + P^{-1}B(t)$ s'écrit :

$$\begin{cases} y'_1 = 5y_1 + \frac{e^t}{4} \\ y'_2 = -3y_2 - \frac{e^t}{4} \end{cases}$$

Ce système est constitué de deux équations linéaires d'ordre 1 que l'on sait résoudre. Les solutions obtenues sont :

$$Y : t \mapsto -\frac{e^t}{16} \begin{pmatrix} 1 \\ 1 \end{pmatrix} + k_1 e^{5t} \begin{pmatrix} 1 \\ 0 \end{pmatrix} + k_2 e^{-3t} \begin{pmatrix} 0 \\ 1 \end{pmatrix} \quad \text{avec} \quad (k_1, k_2) \in \mathbb{R}^2,$$

ce qui donne les solutions du système initial :

$$X : t \mapsto -\frac{e^t}{8} \begin{pmatrix} 0 \\ 1 \end{pmatrix} + k_1 e^{5t} \begin{pmatrix} 2 \\ 1 \end{pmatrix} + k_2 e^{-3t} \begin{pmatrix} -2 \\ 1 \end{pmatrix} \quad \text{avec} \quad (k_1, k_2) \in \mathbb{R}^2.$$

1081

Chapitre 17. Équations différentielles linéaires

**17.5** • **Première méthode.** Le système différentiel (Sys) se traduit matriciellement :

$$X' = AX \quad \text{avec} \quad X = \begin{pmatrix} x \\ y \\ z \end{pmatrix} \quad \text{et} \quad A = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{pmatrix}.$$

L'étude des éléments propres de $A$ montre que :
* $\text{sp}(A) = \{1, j, \bar{j}\}$ (avec $j = e^{\frac{2i\pi}{3}}$);
* une base de vecteurs propres associée à $(1, j, \bar{j})$ est $(V_1, V_2, \overline{V_2})$ avec :

$$V_1 = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} \text{ et } V_2 = \begin{pmatrix} 1 \\ j \\ \bar{j} \end{pmatrix}.$$

Ainsi, une base de l'espace $\mathcal{S}_{\mathbb{C}}$ des solutions complexes de (Sys) est $(X_1, X_2, \overline{X_2})$ avec :

$$X_1 : t \mapsto e^t V_1 \quad \text{et} \quad X_2 : t \mapsto e^{jt} V_2$$

et une base de l'espace $\mathcal{S}_{\mathbb{R}}$ des solutions réelles est $(X_1, \text{Re}(X_2), \text{Im}(X_2))$.
Explicitons $\text{Re}(X_2)$ et $\text{Im}(X_2)$. Pour $t \in \mathbb{R}$, on a :

$$X_2(t) = e^{-\frac{t}{2}} e^{it \frac{\sqrt{3}}{2}} \begin{pmatrix} 1 \\ e^{\frac{2i\pi}{3}} \\ e^{\frac{-2i\pi}{3}} \end{pmatrix} = e^{-\frac{t}{2}} \begin{pmatrix} e^{it \frac{\sqrt{3}}{2}} \\ e^{i \left( t \frac{\sqrt{3}}{2} + \frac{2\pi}{3} \right)} \\ e^{i \left( t \frac{\sqrt{3}}{2} - \frac{2\pi}{3} \right)} \end{pmatrix}$$

ce qui donne :

$$ \text{Re}(X_2)(t) = e^{-\frac{t}{2}} \begin{pmatrix} \cos \left( \frac{t\sqrt{3}}{2} \right) \\ \cos \left( \frac{t\sqrt{3}}{2} + \frac{2\pi}{3} \right) \\ \cos \left( \frac{t\sqrt{3}}{2} - \frac{2\pi}{3} \right) \end{pmatrix} \quad \text{et} \quad \text{Im}(X_2)(t) = e^{-\frac{t}{2}} \begin{pmatrix} \sin \left( \frac{t\sqrt{3}}{2} \right) \\ \sin \left( \frac{t\sqrt{3}}{2} + \frac{2\pi}{3} \right) \\ \sin \left( \frac{t\sqrt{3}}{2} - \frac{2\pi}{3} \right) \end{pmatrix} $$

• **Deuxième méthode.** Sans traduire matriciellement le système (Sys), on peut remarquer que $\begin{pmatrix} x \\ y \\ z \end{pmatrix}$ est solution de (Sys) si, et seulement si :

$$x''' = x \text{ ; } y = x' \quad \text{et} \quad z = x''.$$

Autrement dit, les solutions sont de la forme $\begin{pmatrix} x \\ x' \\ x'' \end{pmatrix}$ avec $x$ vérifiant $x''' = x$.

Reste alors à résoudre l'équation $x''' = x$. Commençons par la résoudre dans $\mathbb{C}$ (il restera alors à prendre les parties réelles des solutions complexes pour obtenir les solutions réelles).
Comme il s'agit d'une équation différentielle linéaire scalaire d'ordre 3 homogène, on sait que ses solutions forment un espace vectoriel de dimension 3.
Remarquons que les trois applications :

$$\varphi_1 : t \mapsto e^t \text{ ; } \quad \varphi_2 : t \mapsto e^{jt} \quad \text{et} \quad \varphi_3 : t \mapsto e^{\bar{j}t}$$

1082

**_Solution des exercices_**

sont solutions. Il suffit alors de prouver la liberté de la famille $(\varphi_1, \varphi_2, \varphi_3)$ pour pouvoir affirmer que c'est une base de l'espace des solutions complexes.
**Liberté de** $(\varphi_1, \varphi_2, \varphi_3)$. Remarquons que $\varphi_1, \varphi_2, \varphi_3$ sont de classe $\mathcal{C}^\infty$ et sont des vecteurs propres pour l'application dérivation :
$$
\begin{aligned}
\mathcal{C}^\infty(\mathbb{R}, \mathbb{C}) & \longrightarrow \mathcal{C}^\infty(\mathbb{R}, \mathbb{C}) \\
f & \longmapsto f'
\end{aligned}
$$
associés respectivement aux trois valeurs propres deux à deux distinctes $1, j$ et $\bar{j}$. La famille $(\varphi_1, \varphi_2, \varphi_3)$ est donc libre.

**17.6** • *Analyse.* Soit $\varphi = (\varphi_1, \varphi_2)$ une solution de (Sys).
On constate que la fonction $\psi = \varphi_1 + i\varphi_2$ vérifie :
$$\forall t \in \mathbb{R} \quad \psi'(t) = (1 + it) \psi(t) + t e^t.$$
En résolvant l'équation scalaire d'ordre 1 (résolution de l'équation homogène puis recherche d'une solution particulière par la méthode de variation de la constante) :
$$z' = (1 + it) z + t e^t,$$
on obtient l'existence d'une constante $\alpha \in \mathbb{C}$ telle que :
$$\forall t \in \mathbb{R} \quad \psi(t) = \alpha \exp \left( t + i \frac{t^2}{2} \right) + i e^t.$$
Puisque $\varphi_1 = \text{Re}(\psi)$ et $\varphi_2 = \text{Im}(\psi)$, on obtient (en écrivant $\alpha$ sous forme algébrique $\alpha = a + ib$) :
$$\forall t \in \mathbb{R} \quad \begin{pmatrix} \varphi_1(t) \\ \varphi_2(t) \end{pmatrix} = \begin{pmatrix} 0 \\ e^t \end{pmatrix} + a e^t \begin{pmatrix} \cos \left( \frac{t^2}{2} \right) \\ \sin \left( \frac{t^2}{2} \right) \end{pmatrix} + b e^t \begin{pmatrix} -\sin \left( \frac{t^2}{2} \right) \\ \cos \left( \frac{t^2}{2} \right) \end{pmatrix}$$
• *Synthèse.* De la partie « analyse » du raisonnement il résulte que :
$$\mathcal{S} \subset \varphi_P + \text{Vect}(\varphi_1, \varphi_2)$$
avec
$$\varphi_P(t) = \begin{pmatrix} 0 \\ e^t \end{pmatrix}, \varphi_1(t) = e^t \begin{pmatrix} \cos \left( \frac{t^2}{2} \right) \\ \sin \left( \frac{t^2}{2} \right) \end{pmatrix} \text{ et } \varphi_2(t) = e^t \begin{pmatrix} -\sin \left( \frac{t^2}{2} \right) \\ \cos \left( \frac{t^2}{2} \right) \end{pmatrix}.$$
Comme on sait que $\mathcal{S}$ est un sous-espace affine de dimension 2, il en résulte que l'inclusion précédente est une égalité.

**17.7** • L'espace des solutions de l'équation homogène $(E_0) : y'' + y = 0$ est :
$$\mathcal{S}_0 = \text{Vect}(\varphi_1, \varphi_2) \quad \text{avec} \quad \varphi_1 : t \mapsto \cos t \quad \text{et} \quad \varphi_2 : t \mapsto \sin t.$$
Il est donc clair que toute solution de l'équation homogène est bornée sur $\mathbb{R}$. Il suffit donc, pour conclure, de prouver qu'il existe une solution bornée de (E).

1083

# Chapitre 17. Équations différentielles linéaires

* Recherchons une solution de (E) sous la forme $\varphi_P = \lambda_1 \varphi_1 + \lambda_2 \varphi_2$ avec $\lambda_1$ et $\lambda_2$ deux fonctions dérivables sur $\mathbb{R}$. Une telle fonction $\varphi_P$ est solution de (E) si, et seulement si :
$$\begin{cases} \lambda'_1 \varphi_1 + \lambda'_2 \varphi_2 &= 0 \\ \lambda'_1 \varphi'_1 + \lambda'_2 \varphi'_2 &= g \end{cases}$$

c'est-à-dire :
$$\forall t \in \mathbb{R} \quad \begin{cases} \lambda'_1(t) \cos(t) + \lambda'_2(t) \sin(t) &= 0 \\ -\lambda'_1(t) \sin(t) + \lambda'_2(t) \cos(t) &= g(t) \end{cases}$$

ce qui donne, pour tout $t \in \mathbb{R}$ :
$$\lambda'_1(t) = -\sin(t) g(t) \quad \text{et} \quad \lambda'_2(t) = \cos(t) g(t).$$

En prenant :
$$\lambda_1 : t \mapsto -\int_0^t \sin(u) g(u) \, du \quad \text{et} \quad \lambda_2 : t \mapsto \int_0^t \cos(u) g(u) \, du$$

on obtient la solution de (E) suivante :
$$\varphi_P : t \mapsto -\cos(t) \int_0^t \sin(u) g(u) \, du + \sin(t) \int_0^t \cos(u) g(u) \, du.$$

* Pour tout $t \in \mathbb{R}$, on a :
$$|\varphi_P(t)| \leqslant \left| \int_0^t \sin(u) g(u) \, du \right| + \left| \int_0^t \cos(u) g(u) \, du \right|.$$

Pour conclure que $\varphi_P$ est bornée, il suffit donc de prouver que les fonctions :
$$\alpha : t \mapsto \int_0^t \sin(u) g(u) \, du \quad \text{et} \quad \beta : t \mapsto \int_0^t \cos(u) g(u) \, du$$

le sont.

* Pour $t \in \mathbb{R}$, on a, en intégrant par parties :
$$\begin{aligned} \alpha(t) &= [-\cos(u) g(u)]_0^t + \int_0^t \cos(u) g'(u) \, du \\ &= g(0) - \cos(t) g(t) + \int_0^t \cos(u) g'(u) \, du. \end{aligned}$$

Comme $g$ est croissante, sa dérivée $g'$ est à valeurs positives. Comme $g$ est bornée, la fonction $g'$ est intégrable sur $\mathbb{R}$. Par comparaison, la fonction $t \mapsto \cos(t) g'(t)$ est aussi intégrable sur $\mathbb{R}$, et donc la fonction :
$$t \mapsto \int_0^t \cos(u) g'(u) \, du$$

est bornée. Ainsi, l'expression obtenue précédemment pour $\alpha(t)$ prouve que la fonction $\alpha$ est bornée.

* On obtient de même que la fonction $\beta$ est bornée.

1084

**Solution des exercices**

**17.8** Comme $f + f' \xrightarrow[+\infty]{} 0$, pour obtenir les deux limites $f \xrightarrow[+\infty]{} 0$ et $f' \xrightarrow[+\infty]{} 0$, il suffit d'en prouver une seule. Montrons que $f \xrightarrow[+\infty]{} 0$.

Notons $g = f + f'$. La fonction $f$ est alors solution de l'équation différentielle :
$$(E) : y' + y = g.$$
En résolvant l'équation (E), on obtient l'existence d'une constante $\alpha \in \mathbb{R}$ telle que :
$$\forall t \in \mathbb{R}_+ \quad f(t) = \alpha e^{-t} + e^{-t} \int_0^t e^u g(u) \, du.$$
Comme $\alpha e^{-t} \xrightarrow[t \to +\infty]{} 0$, il reste à prouver que $e^{-t} \int_0^t e^u g(u) \, du \xrightarrow[t \to +\infty]{} 0$.
On a, lorsque $u \to +\infty$ :
$$e^u g(u) = \text{o}(e^u),$$
donc, la fonction $u \mapsto e^u$ étant positive et non intégrable, on a par intégration des relations de comparaison lorsque $t \to +\infty$ :
$$\int_0^t e^u g(u) \, du = \text{o}\left(\int_0^t e^u \, du\right).$$
Comme $\int_0^t e^u \, du = e^t - 1 \sim e^t$, on en déduit, lorsque $t \to +\infty$ :
$$e^{-t} \int_0^t e^u g(u) \, du = \text{o}(1).$$

**17.9** $\bullet$ Montrons d'abord que $f \xrightarrow[+\infty]{} 0$. Notons $g = f'' + 3f' + 2f$.
La fonction $f$ est alors solution de l'équation différentielle :
$$(E) : y'' + 3y' + 2y = g.$$
$*$ Une base de l'espace $\mathcal{S}_0$ de l'équation homogène associée est formée par :
$$\varphi_1 : t \mapsto e^{-t} \quad \text{et} \quad \varphi_2 : t \mapsto e^{-2t}.$$
$*$ Cherchons une solution particulière par la méthode de variation des constantes sous la forme $\varphi_P = \lambda_1 \varphi_1 + \lambda_2 \varphi_2$ avec $\lambda_1$ et $\lambda_2$ dérivables.
Une telle fonction est solution si, et seulement si :
$$\forall t \in \mathbb{R}_+ \quad \begin{cases} e^{-t} \lambda'_1(t) &+& e^{-2t} \lambda'_2(t) &=& 0 \\ -e^{-t} \lambda'_1(t) &-& 2e^{-2t} \lambda'_2(t) &=& g(t) \end{cases}$$
c'est-à-dire :
$$\forall t \in \mathbb{R}_+ \quad \lambda'_1(t) = e^t g(t) \quad \text{et} \quad \lambda'_2(t) = -e^{2t} g(t).$$
En prenant :
$$\lambda_1 : t \mapsto \int_0^t e^u g(u) \, du \quad \text{et} \quad \lambda_2 : t \mapsto -\int_0^t e^{2u} g(u) \, du,$$
on obtient la solution suivante :
$$\varphi_P(t) = e^{-t} \int_0^t e^u g(u) \, du - e^{-2t} \int_0^t e^{2u} g(u) \, du.$$

1085

# Chapitre 17. Équations différentielles linéaires

* On peut conclure la résolution de (E) et en déduire, comme $f$ est solution de (E), qu'il existe $(\alpha, \beta) \in \mathbb{R}^2$ tel que :
$$\forall t \in \mathbb{R}_+ \quad f(t) = e^{-t} \left( \alpha + \int_0^t e^*u g*(u) \, du \right) + e^{-2t} \left( \beta - \int_0^t e^{2u} g(u) \, du \right).$$

* Comme $g$ tend vers 0 en $+\infty$, on a, par intégration des relations de comparaison lorsque $t \to +\infty$ :
$$\int_0^t e^*u g*(u) \, du = o \left( \int_0^t e^u \, du \right) \quad \text{et} \quad \int_0^t e^{2u} g(u) \, du = o \left( \int_0^t e^{2u} \, du \right)$$
c'est-à-dire :
$$\int_0^t e^*u g*(u) \, du = o(e^t) \quad \text{et} \quad \int_0^t e^{2u} g(u) \, du = o(e^{2t}).$$
L'expression obtenue pour $f(t)$ donne alors $f \xrightarrow[+\infty]{} 0$.

• Pour conclure, il reste à prouver que $f'$ et $f''$ tendent vers 0 en $+\infty$.
* **Première méthode.** En repartant de l'expression de $f(t)$, on peut dériver pour obtenir une expression de $f'(t)$ et $f''(t)$, et montrer alors que $f' \xrightarrow[+\infty]{} 0$ et $f'' \xrightarrow[+\infty]{} 0$.
* **Deuxième méthode.** Puisque $f'' + 3f' + 2f \xrightarrow[+\infty]{} 0$ et $f \xrightarrow[+\infty]{} 0$, on a :
$$f'' + 3f' \xrightarrow[+\infty]{} 0.$$
Cette dernière propriété nous permet de prouver que $f'$ et $f''$ tendent vers 0 en $+\infty$ (*cf.* exercice 17.8).

**17.10** 1. Soit $t_0 \in Z_u$. Comme $u(t_0) = 0$ et que $u$ n'est pas l'application nulle (car sinon la famille $(*u, v*)$ serait liée), on a $u'(t_0) \neq 0$. En effet, si $u'(t_0)$ était nul, alors $u$ et l'application nulle seraient solutions du même problème de Cauchy :
$$y'' + q(t) y = 0 \quad \text{et} \quad (y(t_0), y'(t_0)) = (0, 0)$$
et alors la partie « unicité » du théorème de Cauchy linéaire donnerait $u = 0$. Comme $u$ est dérivable sur $\mathbb{R}$, elle l'est en particulier au point $t_0$, d'où :
$$\frac{u(t) - u(t_0)}{t - t_0} \xrightarrow[\substack{t \to t_0 \\ t \neq t_0}]{} u'(t_0)$$
autrement dit, comme $u(t_0) = 0$ :
$$\frac{u(t)}{t - t_0} \xrightarrow[\substack{t \to t_0 \\ t \neq t_0}]{} u'(t_0).$$
Comme $u'(t_0) \neq 0$, la limite précédente assure qu'il existe $r > 0$ tel que :
$$\forall t \in \mathbb{R} \cap [t_0 - r, t_0 + r] \setminus \{t_0\} \quad u(t) \neq 0.$$
Cela prouve le résultat souhaité car un tel $r > 0$ vérifie :
$$Z_u \cap [t_0 - r, t_0 + r] = \{t_0\}.$$

1086

**_Solution des exercices_**

2. Notons $A$ l'ensemble des points d'annulation de $u$ sur $]t_0, +\infty[$ :
$$A = Z_u \cap ]t_0, +\infty[.$$
Montrons que $A$ admet un plus petit élément. L'ensemble $A$ est une partie non vide (car $u$ s'annule sur $]t_0, +\infty[$) et minorée (par $t_0$) de $\mathbb{R}$, donc possède une borne inférieure.
Notons $t_1 = \inf(A)$ et montrons que $t_1 \in A$.

* Prouvons que $u(t_1) = 0$. Par caractérisation séquentielle de la borne inférieure, il existe une suite $(\alpha_n)$ d'éléments de $A$ tendant vers $t_1$. Le fait que $(\alpha_n)$ soit à valeurs dans $A$ et la continuité de $u$ donnent :
$$(\forall n \in \mathbb{N} \quad u(\alpha_n) = 0) \quad \text{et} \quad u(\alpha_n) \to u(t_1).$$
On a donc $u(t_1) = 0$.
* Prouvons alors que $t_1 \in ]t_0, +\infty[$. Sachant que l'on a déjà $t_1 \geqslant t_0$, il suffit de justifier que $t_1 \neq t_0$. D'après la première question, $t_0$ est un point isolé de $A$, donc il existe $r > 0$ tel que :
$$Z_u \cap [t_0 - r, t_0 + r] = \{t_0\}.$$
Pour un tel $r > 0$, on a $A \cap [t_0 - r, t_0 + r] = \varnothing$. Donc $t_0 + r$ minore $A$, ce qui assure $t_0 + r \leqslant t_1$. Par suite, on a $t_1 \neq t_0$.

3. Montrons que la fonction $v$ possède un et un seul point d'annulation dans $]t_0, t_1[$.

* **Existence** Le wronskien $W = uv' - u'v$ de $(u, v)$ vérifie l'équation différentielle $W' = 0$, donc est constant. Comme il est non nul (car $u$ et $v$ sont linéairement indépendantes), il existe $k \in \mathbb{R}^*$ tel que :
$$\forall t \in \mathbb{R} \quad u(t) v'(t) - u'(t) v(t) = k. \tag{$\star$}$$
Comme $u(t_0) = 0$, et $u$ n'étant pas la fonction nulle, on a $u'(t_0) \neq 0$.
De même, comme $u(t_1) = 0$, on a $u'(t_1) \neq 0$. D'autre part, $u$ ne s'annulant pas sur l'intervalle $]t_0, t_1[$, elle y garde un signe constant d'après le théorème des valeurs intermédiaires.
On est donc dans l'une des deux situations suivantes :
    * *Premier cas :* $\forall t \in ]t_0, t_1[ \quad u(t) > 0$. On a alors :
$$\forall t \in ]t_0, t_1[ \quad \frac{u(t)}{t - t_0} > 0$$
puis, comme $u'(t_0) = \lim_{\substack{t \to t_0 \\ t > t_0}} \frac{u(t)}{t - t_0}$, on a $u'(t_0) \geqslant 0$ et donc $u'(t_0) > 0$.
De la même manière, on obtient $u'(t_1) < 0$.
    * *Deuxième cas :* $\forall t \in ]t_0, t_1[ \quad u(t) < 0$. Alors, de même que précédemment, on obtient $u'(t_0) < 0$ et $u'(t_1) > 0$.

Dans les deux cas, la relation $(\star)$, évaluée en $t_0$ et en $t_1$, impose d'avoir :
$$v(t_0) v(t_1) < 0.$$
Le théorème des valeurs intermédiaires assure alors que la fonction $v$ s'annule au moins une fois sur l'intervalle $]t_0, t_1[$.

1087

Chapitre 17. Équations différentielles linéaires

*   **Unicité.** À ce stade de l’exercice, on peut affirmer qu’entre deux zéros consécutifs de $u$ la fonction $v$ s’annule au moins une fois. Les rôles de $u$ et $v$ étant symétriques, on en déduit qu’entre deux zéros consécutifs de $v$ la fonction $u$ s’annule au moins une fois. Donc, si $v$ possédait plusieurs points d’annulation sur l’intervalle $]t_0, t_1[$, alors la fonction $u$ devrait aussi s’y annuler, ce qui est contradictoire avec la définition de $t_1$.

**17.11** • Supposons $(ii)$ et montrons qu’il existe une base $(f, g)$ de $\mathcal{S}_0$ avec $f$ paire et $g$ impaire.
*   Remarquons que pour tout $\varphi \in \mathcal{S}_0$, la fonction $\tilde{\varphi} : t \mapsto \varphi(-t)$ est également solution de (E). En effet, pour tout $t \in \mathbb{R}$, on a :
    $$\tilde{\varphi}'(t) = -\varphi'(-t) \quad \text{et} \quad \tilde{\varphi}''(t) = \varphi''(-t),$$
    donc, en utilisant l’imparité de $a$ et la parité de $b$ :
$$
\begin{align*}
\tilde{\varphi}''(t) + a(t) \tilde{\varphi}'(t) + b(t) \tilde{\varphi}(t) &= \varphi''(-t) - a(t) \varphi'(-t) + b(t) \varphi(-t) \\
&= \varphi''(-t) + a(-t) \varphi'(-t) + b(-t) \varphi(-t) \\
&= 0.
\end{align*}
$$
*   Par suite, pour tout $\varphi \in \mathcal{S}_0$, les fonctions :
    $$\varphi_P : t \mapsto \varphi(t) + \varphi(-t) \quad \text{et} \quad \varphi_I : t \mapsto \varphi(t) - \varphi(-t)$$
    sont des solutions de (E) respectivement paire et impaire. S’il existe une solution $\varphi \in \mathcal{S}_0$ qui n’est ni paire ni impaire, alors, les deux fonctions $\varphi_P$ et $\varphi_I$ ci-dessus sont toutes deux non nulles donc linéairement indépendantes et forment une base de $\mathcal{S}_0$.
*   Il reste donc à démontrer qu’il existe une solution de (E) qui ne soit ni paire ni impaire. Pour cela, il suffit de constater que, d’après le théorème de Cauchy linéaire, il existe une solution $\varphi$ de (E) vérifiant la condition initiale $(\varphi(0), \varphi'(0)) = (1, 1)$. Une telle solution n’est ni paire (car $\varphi'(0) \neq 0$) ni impaire (car $\varphi(0) \neq 0$).

• Réciproquement, supposons qu’il existe une base $(f, g)$ de $\mathcal{S}_0$ avec $f$ paire et $g$ impaire.
*   Tout d’abord, le wronskien $W$ de $(f, g)$ :
    $$W = fg' - f'g,$$
    est une fonction paire et vérifie $W' + aW = 0$, ou encore, puisque $W$ ne s’annule pas : $\frac{W'}{W} = -a$. Il en résulte que la fonction $a$ est impaire.
*   Il reste à montrer que $b$ est paire.
    Fixons $t_0 \in \mathbb{R}$ et montrons que $b(-t_0) = b(t_0)$. Soit $\varphi : \mathbb{R} \to \mathbb{R}$ l’unique solution de (E) vérifiant $\varphi(t_0) = 1$ et $\varphi'(t_0) = 0$.
    $\star$ Justifions d’abord que la fonction $\tilde{\varphi} : t \mapsto \varphi(-t)$ est également solution de (E).
    Comme $\varphi$ est solution de (E) et $\mathcal{S}_0 = \text{Vect}(f, g)$, $\varphi$ s’écrit :
    $$\varphi = \lambda f + \mu g \quad \text{avec} \quad (\lambda, \mu) \in \mathbb{R}^2.$$

1088

**_Solution des exercices_**

Comme $f$ et $g$ sont respectivement paire et impaire, on montre que :
$$\tilde{\varphi} = \lambda f - \mu g.$$
On a donc $\tilde{\varphi} \in \text{Vect}(f, g)$, *i.e.* $\tilde{\varphi}$ est solution de (E).
$\star$ En dérivant $\tilde{\varphi}$, on a :
$$\forall t \in \mathbb{R} \quad \tilde{\varphi}'(t) = -\varphi'(-t) \quad \text{et} \quad \tilde{\varphi}''(t) = \varphi''(-t)$$
donc en particulier :
$$\tilde{\varphi}'(-t_0) = -\varphi'(t_0) \quad \text{et} \quad \tilde{\varphi}''(-t_0) = \varphi''(t_0).$$
Comme $\tilde{\varphi}$ vérifie l’équation (E) en $-t_0$, on obtient :
$$\varphi''(t_0) - a(-t_0) \varphi'(t_0) + b(-t_0) \varphi(t_0) = 0$$
autrement dit, étant donné la condition initiale vérifiée par $\varphi$ :
$$\varphi''(t_0) + b(-t_0) = 0.$$
D’autre part, en écrivant que $\varphi$ vérifie l’équation en $t_0$ et étant donné la condition initiale vérifiée par $\varphi$, on a :
$$\varphi''(t_0) + b(t_0) = 0.$$
Il en résulte que $b(-t_0) = b(t_0)$. D’où le résultat.

**17.12** Comme $A$ est symétrique réelle, il existe une base orthonormée $(V_1, \dots, V_n)$ de vecteurs propres de $A$. Comme $\text{sp}(A) \subset \mathbb{R}_+^*$, les valeurs propres associées $\lambda_1, \dots, \lambda_n$ sont toutes strictement positives.
Pour tout $k \in \llbracket 1, n \rrbracket$, notons :
$$\begin{aligned} X_k : \mathbb{R} &\longrightarrow \mathbb{R}^n \\ t &\longmapsto e^{\lambda_k t} V_k. \end{aligned}$$
La famille $(X_1, \dots, X_n)$ est alors une base de l’espace $\mathcal{S}_0$ des solutions de $X' = AX$. Il existe donc $(\alpha_1, \dots, \alpha_n) \in \mathbb{R}^n \setminus \{(0, \dots, 0)\}$ tel que :
$$\varphi = \sum_{k=1}^n \alpha_k X_k.$$
Pour $t \in \mathbb{R}$, on a, puisque $(V_1, \dots, V_n)$ est une base orthonormée :
$$\|\varphi(t)\|^2 = \left\| \sum_{k=1}^n \alpha_k e^{\lambda_k t} V_k \right\|^2 = \sum_{k=1}^n \alpha_k^2 e^{2\lambda_k t}.$$
Comme les $\alpha_k$ ne sont pas tous nuls et que les $\lambda_k$ sont tous strictement positifs, la fonction $t \mapsto \|\varphi(t)\|^2$ est strictement croissante et tend vers $+\infty$ en $+\infty$ et vers $0$ en $-\infty$.
Comme la fonction $t \mapsto \|\varphi(t)\|^2$ est de plus continue, elle réalise une bijection strictement croissante de $\mathbb{R}$ sur $\mathbb{R}_+^*$. En composant par la fonction $u \mapsto \sqrt{u}$, bijection strictement croissante de $\mathbb{R}_+^*$ vers $\mathbb{R}_+^*$, on obtient le résultat souhaité.

1089

# Chapitre 17. Équations différentielles linéaires

**17.13** On sait que $A$ est trigonalisable dans $\mathcal{M}_n(\mathbb{C})$ : en notant $\lambda_1, \dots, \lambda_n$ les valeurs propres de $A$ comptées avec leur ordre de multiplicité, la matrice $A$ s’écrit :

$$A = P T P^{-1} \quad \text{avec} \quad P \in \mathcal{G}\mathcal{L}_n(\mathbb{C}) \quad \text{et} \quad T = \begin{pmatrix} \lambda_1 & & (\star) \\ & \ddots & \\ (0) & & \lambda_n \end{pmatrix}.$$

Pour tout $k \in \mathbb{N}$, la matrice $T^k$ est triangulaire supérieure avec une diagonale constituée de $\lambda_1^k, \dots, \lambda_n^k$. Par suite, la matrice $\exp(T)$ est aussi triangulaire supérieure, de la forme :

$$\exp(T) = \begin{pmatrix} e^{\lambda_1} & & (\star) \\ & \ddots & \\ (0) & & e^{\lambda_n} \end{pmatrix}.$$

Le spectre de $\exp(T)$ vaut donc $\text{sp}(\exp(T)) = \{e^{\lambda_k} \ ; \ k \in \llbracket 1, n \rrbracket\}$.

Cela prouve le résultat souhaité car, comme $\exp(A) = P \exp(T) P^{-1}$, les matrices $\exp(A)$ et $\exp(T)$ sont semblables donc ont même spectre.

**17.14** Considérons l’application $\Psi$ qui à une fonction $X : \mathbb{R} \to \mathbb{C}^n$ associe la fonction :

$$\begin{aligned} \Psi(X) : \mathbb{R} &\longrightarrow \mathbb{C}^n \\ t &\longmapsto X(t + T) \end{aligned}$$

Comme $A$ est $T$-périodique, si $X$ est solution de (Sys), alors $\Psi(X)$ l’est aussi car pour tout $t \in \mathbb{R}$ :

$$\begin{aligned} \Psi(X)'(t) = X'(t + T) &= A(t + T) X(t + T) \\ &= A(t) X(t + T) && (T\text{-périodicité de } A) \\ &= A(t) \Psi(X)(t) && (\text{par définition de } \Psi) \end{aligned}$$

Ainsi, l’application $\Psi$ induit un endomorphisme de l’espace $\mathcal{S}$ des solutions de (Sys). Comme $\mathcal{S}$ est un $\mathbb{C}$-espace vectoriel non nul de dimension finie (il est de dimension $n$), cet endomorphisme induit admet au moins une valeur propre $\lambda \in \mathbb{C}$. Un vecteur propre associé à cette valeur propre $\lambda$ est une solution non nulle $\varphi$ de (Sys) vérifiant :

$$\Psi(\varphi) = \lambda \varphi, \quad \text{c’est-à-dire} \quad \forall t \in \mathbb{R} \quad \varphi(t + T) = \lambda \varphi(t).$$

**17.15** 1. (a) Soit $t \in \mathbb{R}$. Puisque les matrices $t\lambda I_p$ et $tN$ commutent, on a :

$$\exp(t(\lambda I_p + N)) = \exp(t\lambda I_p + tN) = \exp(\lambda t I_p) \exp(tN) = e^{\lambda t} \exp(tN).$$

Puisque $N$ est nilpotente et appartient à $\mathcal{M}_p(\mathbb{C})$, on a :

$$\forall k \geqslant p \quad N^k = 0 \quad \text{et donc} \quad \exp(tN) = \sum_{k=0}^{p-1} \frac{(tN)^k}{k!}.$$

1090

**_Solution des exercices_**

Par suite :
$$\exp (t(\lambda I_p + N)) = \sum_{k=0}^{p-1} \frac{e^{\lambda t} t^k}{k!} N^k.$$

Pour tout $k \in \llbracket 0, p - 1 \rrbracket$, on a $|e^{\lambda t} t^k| = e^{\text{Re}(\lambda) t} |t|^k$, et donc comme $\text{Re}(\lambda) < 0$, les croissances comparées donnent $e^{\lambda t} t^k \xrightarrow[t \to +\infty]{} 0$. On en déduit :
$$\forall k \in \llbracket 0, p - 1 \rrbracket \quad \frac{e^{\lambda t} t^k}{k!} N^k \xrightarrow[t \to +\infty]{} 0,$$
puis :
$$\exp (t(\lambda I_p + N)) \xrightarrow[t \to +\infty]{} 0.$$

(b) $\bullet$ Si l'on note $u$ l'endomorphisme de $\mathbb{C}^n$ canoniquement associé à $A$, on sait que $\mathbb{C}^n$ s'écrit comme somme directe de sous-espaces stables par $u$ sur chacun desquels $u$ induit la somme d'une homothétie et d'un endomorphisme nilpotent. Matriciellement, cela signifie que $A$ s'écrit :
$$A = P \tilde{A} P^{-1} \quad \text{avec} \quad \tilde{A} = \begin{pmatrix} A_1 & & \\ & \ddots & \\ & & A_m \end{pmatrix} \tag{$\star$}$$
où, pour tout $k \in \llbracket 1, m \rrbracket$, $A_k$ est un bloc diagonal de la forme :
$$A_k = \lambda_k I_{p_k} + N_k \quad \text{avec} \quad \lambda_k \in \text{sp}(A) \quad \text{et} \quad N_k \text{ nilpotente.}$$

$\bullet$ Pour $t \in \mathbb{R}$, en écrivant $t\tilde{A} = \begin{pmatrix} tA_1 & & \\ & \ddots & \\ & & tA_m \end{pmatrix}$ et en effectuant des produits par blocs, on constate que :
$$\exp(t\tilde{A}) = \begin{pmatrix} \exp(tA_1) & & \\ & \ddots & \\ & & \exp(tA_m) \end{pmatrix}.$$
Or, pour tout $k \in \llbracket 1, m \rrbracket$, comme $\text{Re}(\lambda_k) < 0$, le résultat de la première question donne $\exp(tA_k) \xrightarrow[t \to +\infty]{} 0$. On a donc $\exp(t\tilde{A}) \xrightarrow[t \to +\infty]{} 0$.

$\bullet$ Comme $A = P \tilde{A} P^{-1}$, on a :
$$(\forall k \in \mathbb{N} \quad (tA)^k = P (t\tilde{A})^*k P*^{-1}) \quad \text{puis} \quad \exp(tA) = P \exp(t\tilde{A}) P^{-1}.$$
Donc, par continuité de l'application $M \mapsto P M P^{-1}$, on obtient :
$$\exp(tA) \xrightarrow[t \to +\infty]{} 0.$$

1091

# Chapitre 17. *Équations différentielles linéaires*

Cela répond à la question puisque les solutions du système différentiel :
$$(Sys) : X' = AX$$
sont les applications de la forme :
$$t \mapsto \exp(tA) X_0 \quad \text{avec} \quad X_0 \in \mathbb{C}^n.$$

2. $\bullet$ Supposons que toutes les solutions de (Sys) soient bornées.
   $*$ Soit $\lambda$ une valeur propre de $A$. En prenant $V$ un vecteur propre de $A$ associé à $\lambda$, l'application
   $$X : t \mapsto e^{\lambda t}V$$
   est solution de (Sys). Pour $t \in \mathbb{R}$, on a $\|X(t)\| = e^{\text{Re}(\lambda)t} \|V\|$ et donc :
   $\star$ si $\text{Re}(\lambda) > 0$, alors $\|X(t)\| \underset{t \to +\infty}{\longrightarrow} +\infty$;
   $\star$ si $\text{Re}(\lambda) < 0$, alors $\|X(t)\| \underset{t \to -\infty}{\longrightarrow} +\infty$.
   Par suite, toutes les solutions de (Sys) étant bornées, on a $\text{sp}(A) \subset i\mathbb{R}$.
   $*$ Montrons maintenant que $A$ est diagonalisable. Par l'absurde : supposons que cela ne soit pas le cas. Reprenons la relation $(\star)$ utilisée à la question 1b. Comme $A$ n'est pas diagonalisable, au moins un des blocs diagonaux $A_k$ n'est pas une matrice d'homothétie, donc est de taille au moins 2 avec une matrice nilpotente $N_k$ non nulle. Fixons une telle valeur de $k$, et notons :
   $$r = \max\{i \in \mathbb{N} \mid N^i \neq 0\}.$$
   On a, pour $t \in \mathbb{R}$ :
   $$\exp(tA_k) = e^{\lambda_k t} \sum_{k=0}^r \frac{t^k}{k!} N^k \quad \text{avec} \quad N^r \neq 0$$
   puis, comme $\lambda_k \in i\mathbb{R}$ :
   $$\|\exp(tA_k)\| = \left\| \sum_{k=0}^r \frac{t^k}{k!} N^k \right\| = \frac{|t|^r}{r!} \underbrace{\left\| \sum_{k=0}^r \frac{r! \, t^{k-r}}{k!} N^k \right\|}_{\underset{t \to +\infty}{\longrightarrow} \|N^r\| \neq 0},$$
   Comme $r \geqslant 1$, il en résulte que $\|\exp(tA_k)\| \underset{t \to +\infty}{\longrightarrow} +\infty$, et donc :
   $$\|\exp(tA)\| \underset{t \to +\infty}{\longrightarrow} +\infty.$$
   Si $(E_1, \dots, E_n)$ est une base de $\mathbb{C}^n$, alors l'application :
   $$\begin{aligned} \mathcal{M}_n(\mathbb{C}) & \longrightarrow \mathbb{R} \\ M & \longmapsto \max \left( \|ME_1\|, \dots, \|ME_n\| \right) \end{aligned}$$
   est une norme sur $\mathcal{M}_n(\mathbb{C})$. La propriété :
   $$\|\exp(tA)\| \underset{t \to +\infty}{\longrightarrow} +\infty$$
   appliquée avec cette norme donne que, parmi les fonctions :
   $$t \mapsto \exp(tA) E_k \quad \text{pour} \quad k \in \llbracket 1, n \rrbracket$$

1092

**_Solution des exercices_**

au moins une n’est pas bornée. Ceci est en contradiction avec l’hypothèse initiale car les fonctions précédentes sont solutions de (Sys).

* Réciproquement, supposons $A$ diagonalisable et $\text{sp}(A) \subset i\mathbb{R}$.
  Il existe $(V_1, \dots, V_n)$ une base de vecteurs propres de $A$. En notant $(\lambda_1, \dots, \lambda_n)$ la liste des valeurs propres associées, on a :
  $$\mathcal{S} = \text{Vect}(X_1, \dots, X_n) \quad \text{avec} \quad \forall k \in \llbracket 1, n \rrbracket \quad X_k : t \mapsto e^{\lambda_k t} V_k.$$
  Pour tout $k \in \llbracket 1, n \rrbracket$, le fait que $\lambda_k$ soit imaginaire pure donne :
  $$\forall t \in \mathbb{R} \quad |e^{\lambda_k t}| = 1 \quad \text{et donc} \quad \|X_k(t)\| = \|V_k\|.$$
  Ainsi, les applications $X_1, \dots, X_n$ sont bornées, ainsi que tous les éléments de $\mathcal{S}$ car elles en sont des combinaisons linéaires.

## **17.16**

* En notant $z = x + iy$, on constate que, pour tout $t \in \mathbb{R}$ :

$$
\begin{cases}
x''(t) & = & -\beta(t) y'(t) \\
y''(t) & = & \beta(t) x'(t)
\end{cases} \iff z''(t) = i\beta(t) z'(t).
$$

Par suite, le système différentiel (Sys) se traduit sur $z$ par l’équation suivante :
$$(E) : z'' - i\beta(t)z' = 0$$
et l’existence d’une solution périodique non constante au système (Sys) équivaut à l’existence d’une solution périodique non constante à l’équation (E).

* _Résolution de_ (E).
  Notons $\theta : \mathbb{R} \to \mathbb{R}$ la primitive de $\beta$ s’annulant en 0 :
  $$\theta : t \mapsto \int_0^t \beta(u) du.$$
  Les solutions de l’équation (E) sont les fonctions dont la dérivée est de la forme :

$$
\begin{aligned}
\mathbb{R} &\longrightarrow \mathbb{C} \quad \text{avec } \lambda \in \mathbb{C}, \\
t &\longmapsto \lambda e^{i\theta(t)}
\end{aligned}
$$

ce qui mène à des solutions de la forme :

$$\mathbb{R} \longrightarrow \mathbb{C}$$
$$t \longmapsto \lambda \int_{0}^{t} e^{i\theta(u)} \mathrm{d}u + \mu \quad \text{avec } (\lambda, \mu) \in \mathbb{C}^2.$$

* Il reste à savoir s’il existe des solutions de (E) périodiques non constantes.
  Étant donné la forme des solutions de (E), de telles solutions existent si, et seulement si, la fonction :

$$
\begin{aligned}
\varphi : \mathbb{R} &\longrightarrow \mathbb{C} \\
t &\longmapsto \int_{0}^{t} e^{i\theta(u)} \mathrm{d}u
\end{aligned}
$$

1093

# Chapitre 17. Équations différentielles linéaires

est périodique non constante.

* Supposons qu'il existe $T > 0$ tel que $\varphi$ soit $T$-périodique.
  Les fonctions $\varphi'$ et $\varphi''$ données par :
  $$\forall t \in \mathbb{R} \quad \varphi'(t) = e^{i\theta(t)} \quad \text{et} \quad \varphi''(t) = i \beta(t) \varphi'(t),$$
  sont également $T$-périodiques. Donc :
  (i) la relation $\beta = -i \frac{\varphi''}{\varphi'}$ assure que la fonction $\beta$ est $T$-périodique ;
  (ii) comme $e^{i\theta(T)} = \varphi'(T) = \varphi'(0) = e^{i\theta(0)} = 1$, on en déduit que :
  $$\exists k \in \mathbb{Z} \quad \theta(T) = \int_0^T \beta(u) \mathrm{d}u = 2k\pi ;$$
  (iii) comme $\varphi(T) = \varphi(0) = 0$, on a :
  $$\int_0^T e^{i\theta(u)} \mathrm{d}u = 0.$$

* Réciproquement, supposons les trois conditions précédentes vérifiées et montrons que la fonction $\varphi$ est $T$-périodique.
  Pour cela, montrons que l'application :
  $$\psi : t \mapsto \varphi(t + T) - \varphi(t) = \int_t^{t+T} e^{i\theta(u)} \mathrm{d}u$$
  est nulle.
  $\star$ Considérons :
  $$\gamma : t \mapsto \int_t^{t+T} \beta(u) \mathrm{d}u.$$
  La fonction $\gamma$ est dérivable et la $T$-périodicité de $\beta$ donne :
  $$\forall t \in \mathbb{R} \quad \gamma'(t) = \beta(t + T) - \beta(t) = 0$$
  L'application $\gamma$ est donc constante et l'on a :
  $$\forall t \in \mathbb{R} \quad \gamma(t) = \gamma(0) = \int_0^T \beta(u) \mathrm{d}u = 2k\pi.$$
  Pour tout $t \in \mathbb{R}$, on a alors :
  $$\theta(t + T) = \int_0^{t+T} \beta(u) \mathrm{d}u = \psi(t + T) + \theta(t) = 2k\pi + \theta(t)$$
  et donc :
  $$e^{i\theta(t+T)} = e^{i\theta(t)}.$$
  $\star$ Pour tout $t \in \mathbb{R}$, on a :
  $$\psi'(t) = e^{i\theta(t+T)} - e^{i\theta(t)} = 0,$$
  donc l'application $\psi$ est constante.
  $\star$ Enfin, on a, d'après (iii) :
  $$\psi(0) = \int_0^T e^{i\theta(u)} \mathrm{d}u = 0,$$
  donc $\psi$ est l'application nulle.

1094

***Solution des exercices***

**17.17** En notant :

$$X = \begin{pmatrix} y \\ y' \\ y'' \\ y''' \end{pmatrix} \quad A = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ -1 & 0 & 0 & 0 \end{pmatrix} \quad \text{et} \quad B(t) = \begin{pmatrix} 0 \\ 0 \\ 0 \\ \varphi(t) \end{pmatrix},$$

L’équation (E) se traduit matriciellement par (EM) : $X' = AX + B(t)$.
L’existence d’une solution $2\pi$-périodique à (E) équivaut à l’existence d’une solution $2\pi$-périodique à (EM).

• Justifions qu’une solution $X : \mathbb{R} \to \mathbb{C}$ de (EM) est $2\pi$-périodique si, et seulement si, $X(2\pi) = X(0)$.
  * Un sens est évident : si $X$ est $2\pi$-périodique, alors on a $X(2\pi) = X(0)$.
  * Réciproquement, si $X(2\pi) = X(0)$, alors la fonction $\widetilde{X} : t \mapsto X(t+2\pi)$ vérifie :
    $$\forall t \in \mathbb{R} \quad \widetilde{X}'(t) = X'(t + 2\pi)$$
    $$= AX(t + 2\pi) + B(t + 2\pi)$$
    $$= A\widetilde{X}(t) + B(t) \quad \text{(car } B \text{ est } 2\pi\text{-périodique)}$$
    donc $\widetilde{X}$ est solution de (EM). Comme de plus $\widetilde{X}(0) = X(2\pi) = X(0)$, on peut conclure que les fonctions $X$ et $\widetilde{X}$ sont égales car elles sont solutions d’un même problème de Cauchy. Donc $X$ est $2\pi$-périodique.

• On sait exprimer les solutions de (EM) :
  $$X : t \mapsto \exp(tA) \left( X_0 + \int_0^t \exp(-sA)B(s)ds \right) \quad \text{avec} \quad X_0 \in \mathbb{C}^4.$$

D’après le point précédent, une telle solution $X$ est $2\pi$-périodique si, et seulement si, $X(2\pi) = X(0)$, ce qui s’écrit :
$$\exp(2\pi A) \left( X_0 + \int_0^{2\pi} \exp(-sA)B(s)ds \right) = X_0,$$
ou encore :
$$(\exp(2\pi A) - I_4) X_0 = -\exp(2\pi A) \int_0^{2\pi} \exp(-sA)B(s)ds.$$

• Justifions que la matrice $\exp(2\pi A) - I_4$ est inversible ; cela prouvera l’existence (et l’unicité) de $X_0 \in \mathbb{C}^4$ vérifiant la condition ci-dessus, et donc l’existence (et l’unicité) d’une solution $2\pi$-périodique.
Pour justifier que $\exp(2\pi A) - I_4$ est inversible, il suffit de constater que, comme :
$$\text{sp}(A) = \{ \lambda \in \mathbb{C} \mid \lambda^4 + 1 = 0 \},$$
on a :
$$i\mathbb{Z} \cap \text{sp}(A) = \emptyset, \quad \text{donc} \quad 2i\pi\mathbb{Z} \cap \text{sp}(2\pi A) = \emptyset,$$
donc 1 n’est pas valeur propre de $\exp(2\pi A)$ (*cf.* exercice 17.13 de la page 1076).

1095