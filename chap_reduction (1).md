## BVCWCPD4CXD8D6CT BE BM CA AJ CTCSD9CRD8CXD3D2 CSCTD7 CTD2CSD3D1D3D6D4CWCXD7D1CTD7

| I  Sous-espaces stables et endomorphismes induits .  64  II  Éléments propres  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  67  1  Définition des éléments propres d'un endomorphisme  67  2  Rappels sur les matrices semblables  .  .  .  .  .  .  .  .  70  3  Éléments propres d'une matrice carrée  .  .  .  .  .  .  .  72  4  Polynômes annulateurs  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  74  5  Polynôme caractéristique  .  .  .  .  .  .  .  .  .  .  .  .  .  .  78  III  Endomorphismes et matrices diagonalisables . . .  86  IV  Endomorphismes et matrices trigonalisables  .  .  .  92  V  Utilisations des polynômes annulateurs  .  .  .  .  .  .  96  1  Polynôme minimal  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  96  2  Théorème de Cayley-Hamilton  .  .  .  .  .  .  .  .  .  .  .  98  3  Lemme de décomposition des noyaux .  .  .  .  .  .  .  .  99  4  Polynômes annulateurs et diagonalisabilité  .  .  .  .  103  5  Endomorphismes nilpotents, matrices nilpotentes  .  104  Démonstrations et solutions des exercices du cours  .  .  107  Exercices .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  130   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## CA AJ CTCSD9CRD8CXD3D2 CSCTD7 CTD2CSD3D1D3D6D4CWCXD7D1CTD7

<!-- image -->

Dans ce chapitre, E est un espace vectoriel non réduit à { 0 } sur un souscorps I K de C (on se limite en pratique au cas où I K est égal à I R ou C ) et u est un endomorphisme de E .

##  CBD3D9D7B9CTD7D4CPCRCTD7 D7D8CPCQD0CTD7 CTD8 CTD2CSD3D1D3D6D4CWCXD7D1CTD7 CXD2CSD9CXD8D7

## Définition 1

Un sous-espace vectoriel F de E est dit stable par u si u ( F ) ⊂ F . On dit aussi que u stabilise F .

## BXDCCTD1D4D0CTD7

1. Les sous-espaces vectoriels { 0 } et E sont stables par tout endomorphisme. Il existe des endomorphismes pour lesquels il n'y en a pas d'autres. Par exemple, une rotation vectorielle r d'angle θ / ∈ π Z Z du plan euclidien.
2. En effet, pour tout vecteur x non nul, la droite I R x n'est pas stable car, comme θ n'est pas multiple entier de π , r ( x ) / ∈ Vect ( x ). Ainsi r ne stabilise aucune droite.
2. À l'opposé, une homothétie stabilise tous les sous-espaces vectoriels de E. Il est évident qu'un endomorphisme stabilise tous les sous-espaces vectoriels de E si, et seulement s'ilstabilise toutes les droites de E .

L'exercice qui suit montre que, réciproquement, cette propriété caractérise les homothéties. Pour cela, on utilise un résultat classique sur les homothéties qui a déjà été vu en première année.

3. Tout sous-espace vectoriel inclus dans le noyau de u ou contenant l'image de u est stable par u .
4. L'intersection et la somme de sous-espaces vectoriels stables par u sont stables par u .

✞

✝

<!-- image -->

✞

✝

☎

✆

☎

✆

<!-- image -->

## Exercice 1

1. On suppose que pour tout x ∈ E , la famille ( x, u ( x )) est liée. Montrer que u est une homothétie.
2. En déduire que les seuls endomorphismes stabilisant tous les sous-espaces vectoriels de E sont les homothéties.

Exercice 2 Soit D la dérivation de I K [ X ].

1. Soit F un sous-espace vectoriel de I K [ X ] stable par D et contenant un polynôme P non nul de degré d . Montrer que I K d [ X ] ⊂ F .
2. Déterminer tous les sous-espaces vectoriels de I K [ X ] stables par D .

D2CSCXCRCPD8CXD3D2 Si F est stable par D , on pourra distinguer deux cas, selon que l'ensemble des degrés des polynômes de F est majoré ou non.

## Proposition 1

Si les endomorphismes u et v commutent, c'est-à-dire si u ◦ v = v ◦ u , alors Ker v et Im v sont stables par u .

✞

✝

☎

✆

## Proposition 2

Si F est un sous-espace vectoriel de E engendré par une famille ( e i ) i ∈ I , alors F est stable par u si, et seulement si :

$$\forall i \in I \ \ u ( e _ { i } ) \in F .$$

Démonstration page 108

## BXDCCTD1D4D0CTD7

✝

☎

✆

1. Soit x un vecteur non nul de E . La droite I K x est donc stable par u si, et seulement s'il existe λ ∈ I K tel que u ( x ) = λx .
2. Soit x un vecteur de E. Le sous-espace vectoriel :

Dans ce cas, si λ = 0, c'est-à-dire si x ̸∈ Ker u , alors u ( I K x ) = I K x .

̸

est le plus petit sous-espace vectoriel de E contenant x et stable par u.

$$\begin{array} { c } \text {e sous-espace vectoriel } \colon \\ \\ \text {Vect } \{ u ^ { k } ( x ) \, | \, k \in \mathbb { N } \} \\ \\ \text {ce vectoriel de } E \text { contenant } \\ \\ \text {contenant } x \end{array}$$

En effet, ce sous-espace vectoriel contient x (car x = u 0 ( x )) et est stable par u (car pour tout entier k , u ( u k ( x ) ) = u k +1 ( x )). De plus, il est évidemment inclus dans tout sous-espace vectoriel contenant x et stable par u .

## Définition 2

Soit F un sous-espace vectoriel stable par u . On appelle endomorphisme induit par u sur F l'endomorphisme u F ∈ L ( F ) défini par :

$$\forall x \in F \ \ u _ { F } \left ( x \right ) = u \left ( x \right ) ,$$

✞ Démonstration page 108

BH

✞

✝

✞

✝

<!-- image -->

## BVCWCPD4CXD8D6CT BE BA CA AJ CTCSD9CRD8CXD3D2 CSCTD7 CTD2CSD3D1D3D6D4CWCXD7D1CTD7

BTD8D8CTD2D8CXD3D2 On ne peut parler d'endomorphisme induit par u sur un sousespace vectoriel F que dans la mesure où F est stable par u.

Dans ce cas, on distinguera soigneusement l'endomorphisme induit u F , qui est une application linéaire de F vers F, de la restriction u | F qui est une application linéaire de F vers E.

CACTD1CPD6D5D9CT L'image de u F est égale à u ( F ) et son noyau à F ∩ Ker u.

<!-- image -->

☎

✆

## Exercice 3

Soit F un sous-espace vectoriel de E . Montrer que l'ensemble L F ( E ) des endomorphismes stabilisant F est une sous-algèbre de L ( E ).

## Corollaire 3 (Traduction matricielle de la stabilité)

Soit F un sous-espace vectoriel de E de dimension p et B = ( e 1 , . . . , e n ) une base de E adaptée à F , c'est-à-dire telle que B ′ = ( e 1 , . . . , e p ) soit une base de F .

L'endomorphisme u stabilise F si, et seulement si, sa matrice dans la base B

$$\begin{array} { l } L ^ { \prime } \text {endomorphism} \ u \text { stabilise } F \text { si, et semplementi} \text { si, sa} \, m \\ \\ \text { est de la form } \left ( \begin{array} { c c } A & C \\ 0 & B \end{array} \right ) , \, a v e c \ A \in \mathcal { M } _ { p } ( \mathbb { K } ) . \\ \\ D _ { \ } a r \, \underset { \ } a r = A _ { \ } a r t \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } h e r \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w r t i s \, \underset { \ } a r t \, \underset { \ } w$$

Dans ce cas, A est la matrice dans la base B ′ de l'endomorphisme induit u F .

Démonstration page 108

✞

✝

## CACTD1CPD6D5D9CTD7 · Une matrice de la forme ( A C 0 B ) est dite triangulaire par blocs .

☎

✆

- . On

rappelle que son déterminant est égal au produit det A × det B

- ∗ Le sous-espace vectoriel G est stable par u si, et seulement si, C = 0. Dans ce cas B s'interprète comme la matrice de l'endomorphisme induit par u sur G dans la base ( e p +1 , . . . , e n ).
- Avec les notations précédentes, notons G = Vect ( e p +1 , . . . , e n ).

☎

- ∗ Lorsque G n'est pas stable par u , l'interprétation de B est plus délicate. Notons q ∈ L ( E ) la projection sur G parallèlement à F ; on peut interpréter B comme la matrice dans la base ( e p +1 , . . . , e n ) de l'endomorphisme induit par q ◦ u sur G .

✆

Exercice 4 Soit E un espace vectoriel de dimension finie et B = ( e 1 , . . . , e n ) une base de E .

1. Pour tout i ∈ [ [1 , n ] ] , posons E i = Vect( e i ). Caractériser par leur matrice dans la base B , les endomorphismes de E qui stabilisent chaque E i .
2. Pour tout i ∈ [ [1 , n ] ] , posons F i = Vect ( e 1 , . . . , e i ). Caractériser, par leur matrice dans la base B , les endomorphismes de E qui stabilisent chaque F i .

BIBI

## Proposition 4

L'endomorphisme u stabilise chaque E i si, et seulement si, sa matrice dans la base B est diagonale par blocs, c'est-à-dire de la forme :

Soit B = ( B 1 , . . . , B p ) une base adaptée à une décomposition E = ⊕ 1 ⩽ i ⩽ p E i .

$$\begin{array} { r l } & { l e p a r b l o c s , c ' e s t - \hat { a } - d i r e } & { d e l a f o r } \\ & { \quad \left ( \begin{array} { c c c c } A _ { 1 } & 0 & \cdots & 0 \\ & 0 & \ddots & \ddots & \vdots \\ & \vdots & \ddots & \ddots & 0 \\ 0 & \cdots & 0 & A _ { p } \end{array} \right ) } \\ & { \quad \left ( \begin{array} { c c c c } A _ { 1 } & 0 & \cdots & \vdots \\ & \ddots & \ddots & \ddots & \vdots \\ 0 & \cdots & 0 & A _ { p } \end{array} \right ) } \\ & { p ] , l a m a t r i c e A _ { i } e s t c a r r e e d ' o r o r } \\ & { u t , i \in \mathbb { I } [ 1 , n ] , \ A _ { i } \colon e s t l a m a t r i c e } \end{array}$$

où, pour tout i ∈ [ [1 , p ] ] , la matrice A i est carrée d'ordre dim E i .

Dans ce cas, pour tout i ∈ [ [1 , p ] ] , A i est la matrice dans la base B i de l'endomorphisme induit par u sur E i .

✞ Démonstration page 108

☎

✆

##  AJ BXD0 AJ CTD1CTD2D8D7 D4D6D3D4D6CTD7

✝

## BD BWAJ CTACD2CXD8CXD3D2 CSCTD7 AJ CTD0 AJ CTD1CTD2D8D7 D4D6D3D4D6CTD7 CSB3D9D2 CTD2CSD3D1D3D6D4CWCXD7D1CT

## Définition 3

1. On dit que λ ∈ I K est valeur propre de u s'il existe un vecteur non nul x ∈ E tel que u ( x ) = λx , c'est-à-dire si l'endomorphisme u -λ Id E est non injectif.
2. On dit que x ∈ E est vecteur propre de u associé à la valeur propre λ ∈ I K s'il est non nul et vérifie u ( x ) = λx .
3. Si λ ∈ I K est valeur propre de u , le sous-espace propre de u associé à la valeur propre λ est :

$$E _ { \lambda } \left ( u \right ) = K e r \left ( u - \lambda \, I d _ { E } \right ) = \left \{ x \in E \, | \, u \left ( x \right ) = \lambda x \right \}$$

CACTD1CPD6D5D9CT Si un vecteur x non nul vérifie λx = μx , alors λ = μ ; ce qui explique que l'on parle de la valeur propre associée à un vecteur propre.

## Définition 4

Le spectre d'un endomorphisme d'un espace de dimension finie est l'ensemble de ses valeurs propres.

## CACTD1CPD6D5D9CTD7

- L'endomorphisme u admet 0 pour valeur propre si, et seulement s'il n'est pas injectif. Dans ce cas E 0 ( u ) = Ker u .
- Une droite vectorielle est stable par u si, et seulement si, elle est engendrée par un vecteur propre de u .
- Si λ ∈ I K est valeur propre de u , les vecteurs propres associés à la valeur propre λ sont les vecteurs non nuls de E λ ( u ).

BJ

✞

✝

## BVCWCPD4CXD8D6CT BE BA CA AJ CTCSD9CRD8CXD3D2 CSCTD7 CTD2CSD3D1D3D6D4CWCXD7D1CTD7

- Soit x un vecteur propre de u ∈ L ( E ) associé à une valeur propre λ non nulle . On a alors x = u ( x λ ) ∈ Im u . Par suite, tout espace propre associé à une valeur propre non nulle est inclus dans Im u .

Par suite, toute somme finie de sous-espaces propres associés à des valeurs propres non nulles est incluse dans Im u .

## Point méthode

On recherche les éléments propres d'un endomorphisme (valeurs et sousespaces associés) en étudiant l'équation u ( x ) = λx.

## BXDCCTD1D4D0CTD7

1. Homothétie. Tout vecteur non nul est vecteur propre de l'homothétie λ Id E pour la valeur propre λ . Par suite cette homothétie admet λ pour unique valeur propre et l'espace propre associé est E .
2. Rotation. Soit E un plan vectoriel euclidien orienté et u une rotation dont l'angle a pour mesure θ / ∈ π Z Z (si θ ∈ π Z Z , alors u est une homothétie).

Pour tout vecteur x non nul, l'angle ( ̂ x, u ( x ) ) n'est pas multiple entier de π ; par suite, u ( x ) / ∈ Vect ( x ). Ainsi u n'a ni valeur propre, ni vecteur propre.

̸

3. Projection. Soit p ∈ L ( E ) un projecteur avec p = 0 et p = Id E (sinon, p est une homothétie).

̸

Soit λ une valeur propre de p et x un vecteur propre associé. On a p ( x ) = λx puis p ( p ( x )) = λp ( x ) donc p ( x ) = λp ( x ). Ainsi, soit p ( x ) = 0 soit λ = 1. Les seules valeurs propres possibles de p sont donc 0 et 1.

̸

Or Im p = Ker( p -Id E ) et Ker p sont deux sous-espaces supplémentaires. L'hypothèse p = 0 et p = Id E implique qu'ils ne sont pas réduits à { 0 } .

̸

En conclusion, 0 et 1 sont les deux valeurs propres de p avec pour sous-espaces propres associés Ker p et Ker( p -Id E ) = Im p .

4. Symétries. Soit F et G supplémentaires dans E et s la symétrie par rapport à F parallèlement à G .

Rappelons que, si p est le projecteur d'image F et de noyau G , on a s = 2 p -Id E .

$$\ A i n s i \, l a \, l a \, r e l a t u \, \hat { a } \ p ( x ) = \frac { \lambda + 1 } { 2 } \, x .$$

̸

On déduit de ce qui a été prouvé sur les projections que, si s = ± Id E (ce qui correspond à F = E et F = { 0 } ), alors s admet pour valeurs propres 1 et -1 et que les sous-espaces propres associés sont respectivement F et G .

̸

Exercice 5 Soit E = C ∞ ( I R , I R ) et D ∈ L ( E ) la dérivation.

Déterminer les valeurs propres et les sous-espaces propres de D .

BK

̸

☎

✆

<!-- image -->

✞

✝

<!-- image -->

✞

✝

☎

✆

☎

✆

<!-- image -->

✞

✝

☎

✆

Exercice 6 Soit E = C I N , l'espace des suites complexes.

On définit Δ ∈ L ( E ) par Δ ( ( u n ) n ∈ I N ) = ( v n ) n ∈ I N avec ∀ n ∈ I N v n = u n +1 . Déterminer les valeurs propres et les sous-espaces propres de Δ.

Exercice 7

Déterminer les valeurs propres de

Soit E = C [ X ] et u ∈ L ( E ) défini par u ( P ) = XP . u .

<!-- image -->

Exercice 8 Soit ϕ un isomorphisme de E dans F et u un endomorphisme de E . Déterminer les éléments propres de -1 en fonction de ceux de .

## Proposition 5

Si les endomorphismes u et v commutent, c'est-à-dire si u ◦ v = v ◦ u , alors les sous-espaces propres de l'un sont stables par l'autre.

Démonstration. Soit λ une valeur propre de u ; comme u et v commutent, il en est de même de ( u -λ Id E ) et v . D'après la proposition 1 de la page 65, E λ ( u ) = Ker( u -λ Id E ) est stable par v .

## Proposition 6

- Si λ 1 , . . . , λ p sont des valeurs propres deux à deux distinctes de u , alors les sous-espaces propres associés E λ 1 ( u ) , . . . , E λ p ( u ) sont en somme directe.
- Toute famille de vecteurs propres associés à des valeurs propres deux à deux distinctes est libre.

## Principe de démonstration.

- On procède par récurrence sur l'entier p .
- On utilise le premier point.

## BXDCCTD1D4D0CTD7

1. En reprenant l'exercice 5 de la page précédente, on voit que, si λ 1 , . . . , λ n sont des réels deux à deux distincts, la famille de fonctions ( e λ 1 , . . . , e λ n ) est une famille libre de C ∞ ( I R , I R ) (on a noté e λ la fonction définie par e λ : t ↦→ e λt ).

Ainsi, la famille ( e λ ) λ ∈ I R est libre.

2. En reprenant l'exercice 6, on voit que, si λ 1 , . . . , λ p sont des complexes deux à deux distincts, la famille de suites ( ( λ n 1 ) n ∈ I N , . . . , ( λ n p ) n ∈ I N ) est libre dans C I N . Ainsi, la famille ( ( λ n ) n ∈ I N ) λ ∈ C est libre.

BL

✞

✝

Démonstration page 109

☎

✆

ϕ ◦ u ◦ ϕ u

✞

✝

BVCWCPD4CXD8D6CT BE BA CA AJ CTCSD9CRD8CXD3D2 CSCTD7 CTD2CSD3D1D3D6D4CWCXD7D1CTD7

☎

✆

<!-- image -->

Exercice 9 Soit E = C ∞ ( I R ∗ + , I R ) et u ∈ L ( E ) défini par :

$$u \left ( f \right ) = g \quad o \hat { u } \quad \forall t > 0 \ \ g \left ( t \right ) = t f ^ { \prime } \left ( t \right ) .$$

Pour tout α ∈ I R , notons f α la fonction définie par f α ( t ) = t α .

Montrer que la famille ( f α ) α ∈ I R est libre.

## Corollaire 7

Si E est de dimension finie et si λ 1 , . . . , λ p sont des valeurs propres deux à deux distinctes de u , alors :

$$\sum _ { i = 1 } ^ { p } \dim E _ { \lambda _ { i } } \left ( u \right ) \leqslant \dim E$$

## Corollaire 8

Un endomorphisme d'un espace vectoriel de dimension n a au plus n valeurs propres distinctes.

✞ Démonstration page 110

☎

✆

## Proposition 9

Si F est un sous-espace vectoriel de E stable par u, les valeurs propres de l'endomorphisme u F induit par u sur F sont les valeurs propres λ de u telles que E λ ( u ) ∩ F = { 0 } . On a alors :

$$E _ { \lambda } ( u _ { F } ) = E _ { \lambda } ( u ) \cap F .$$

Démonstration. Par définition E λ ( u F ) = { x ∈ F | u F ( x ) = λx } donc :

$$E _ { \lambda } ( u _ { F } ) = \{ x \in F \, | \, u ( x ) = \lambda x \} = F \cap E _ { \lambda } ( u ) .$$

## BE CACPD4D4CTD0D7 D7D9D6 D0CTD7 D1CPD8D6CXCRCTD7 D7CTD1CQD0CPCQD0CTD7

Dans cette partie, E est supposé de dimension finie n .

Les résultats rappelés ont été vus en première année ; leurs démonstrations ne seront donc pas redonnées.

## Proposition 10

Si f est un endomorphisme de E et si B et B ′ sont deux bases de E , alors les matrices M et M ′ de f respectivement dans les bases B et B ′ sont reliées par :

$$M ^ { \prime } = P ^ { - 1 } M P ,$$

où P est la matrice de passage de B à B ′ .

BC

̸

✝

✞

✝

## Définition 5

Deux matrices A et B de M n ( I K ) sont semblables s'il existe P ∈ GL n ( I K ) telle que B = P -1 AP .

## Proposition 11

Deux matrices M et M ′ de M n ( I K ) sont semblables si, et seulement si, elles représentent le même endomorphisme de I K n c'est-à-dire s'il existe B et B ′ deux bases de I K n et f ∈ L ( I K n ) telles que :

## Proposition 12

Deux matrices semblables ont même trace et même déterminant

☎

✆

Montrer que M et M ′ sont semblables dans M n ( I R ) c'est-à-dire qu'il existe une matrice Q ∈ GL n ( I R ) tel que M ′ = Q -1 MQ .

Exercice 10 Soit M et M ′ deux matrices de M n ( I R ) semblables dans M n ( C ), c'est-à-dire telles qu'il existe P ∈ GL n ( C ) tel que M ′ = P -1 MP .

## CACTD1CPD6D5D9CTD7

- Soit A la matrice représentant l'endomorphisme u dans une base B .

Un vecteur x de E , dont X ∈ M n, 1 ( I K ) est la matrice colonne des coordonnées dans B , est un vecteur propre de u associé à la valeur propre λ si, et seulement si, X est non nulle et vérifie AX = λX .

- Soit A ∈ M n ( I K ) et u ∈ L ( I K n ) l'endomorphisme canoniquement associé à A , c'est-à-dire :

$$u \colon \, \mathbb { K } ^ { n } \, \longrightarrow \, \mathbb { K } ^ { n } \, \\ X \, \longmapsto \, A X$$

(on identifie I K n et M n, 1 ( I K )).

$$X \, \longmapsto \, A X$$

Un vecteur X ∈ I K n est un vecteur propre de u associé à la valeur propre λ si, et seulement si, X est non nul et vérifie AX = λX .

Cela justifie les définitions qui suivent.

<!-- image -->

$$M = M a t _ { B } ( f ) \quad e t \quad M ^ { \prime } = M a t _ { B ^ { \prime } } ( f ) .$$

BD

✞

✝

## BF AJ BXD0 AJ CTD1CTD2D8D7 D4D6D3D4D6CTD7 CSB3D9D2CT D1CPD8D6CXCRCT CRCPD6D6 AJ CTCT

## Définition 6

Soit A ∈ M n ( I K )

1. On dit que λ ∈ I K est valeur propre de A s'il existe une matrice colonne X ∈ M n, 1 ( I K ) non nulle telle que AX = λX .
2. On dit que la matrice colonne X ∈ M n, 1 ( I K ) est vecteur propre de A associé à la valeur propre λ ∈ I K si elle est non nulle et vérifie AX = λX .
3. Si λ ∈ I K est valeur propre de A , le sous-espace propre de A associé à la valeur propre λ est :

$$E _ { \lambda } \left ( A \right ) = \text {Ker} \left ( A - \lambda I _ { n } \right ) = \left \{ X \in \mathcal { M } _ { n , 1 } ( \mathbb { K } ) \, | \, A X = \lambda X \right \}$$

4. L'ensemble des valeurs propres de A est appelé le spectre de A et noté sp ( A ).

CACTD1CPD6D5D9CT Le scalaire λ est valeur propre de A ∈ M n ( I K ) si, et seulement si, A -λI n est non inversible. De plus, d'après le théorème du rang :

$$\dim E _ { \lambda } ( A ) = n - r g ( A - \lambda I _ { n } ) .$$

☎

✆

<!-- image -->

## Exercice 11

1. Déterminer les éléments propres propres de la matrice
2. Soit ( α, β ) ∈ I K 2 .

$$\ J = \begin{pmatrix} 1 & \cdots & 1 \\ \vdots & & \vdots \\ 1 & \cdots & 1 \end{pmatrix} \in \mathcal { M } _ { n } ( \mathbb { K } ) .$$

Déterminer les éléments propres propres de la matrice A = αJ + βI n .


 En sciences industrielles, on utilise des matrices d'inductance qui relient flux magnétique et intensité.

précédents, deux valeurs propres L -M et L +2 M

Lorsque celle-ci est de la forme ⎛ ⎜ ⎝ L M M M L M M M L ⎞ ⎟ ⎠ , elle admet, d'après l'exercice .

BE

## Point méthode

On peut rechercher les éléments propres d'une matrice en étudiant l'équation AX = λX.

On verra, à l'aide du polynôme caractéristique, une méthode qui permet d'obtenir les valeurs propres d'une matrice sans résolution de systèmes.

CACTD1CPD6D5D9CT Les éléments propres d'une matrice A sont ceux de l'endomorphisme de M n, 1 ( I K ) qui à une matrice colonne X associe AX .

## Proposition 13

Soit A une matrice représentant l'endomorphisme u dans une base ( e 1 , . . . , e n ). On a alors sp( A ) = sp( u ) et, pour tout λ ∈ sp( u ) :

$$e _ { 1 } , \dots , e _ { n } ) . \text { On a alors sp(A) } & = \text {sp} ( u ) \text { et, } \text {pour tout} \ \lambda \in \text {sp} ( u ) \ \colon \\ & \\ x = \sum _ { i = 1 } ^ { n } x _ { i } e _ { i } \in E _ { \lambda } ( u ) \Longleftrightarrow X = \begin{pmatrix} x _ { 1 } \\ \vdots \\ x _ { n } \end{pmatrix} \in E _ { \lambda } ( A ) .$$

Démonstration. On utilise l'exercice 8 de la page 69 avec :

## Corollaire 14

$$\varphi \colon & \quad E \ \longrightarrow \ \mathcal { M } _ { n , 1 } ( \mathbb { K } ) \\ x = \sum _ { i = 1 } ^ { n } x _ { i } e _ { i } \ & \longmapsto \ X = \begin{pmatrix} x _ { 1 } \\ \vdots \\ x _ { n } \end{pmatrix} \\$$

Deux matrices semblables ont le même spectre et les sous-espaces propres associés sont de même dimension.

CACTD1CPD6D5D9CT Plus précisément, si A = P -1 BP , alors pour tout λ ∈ sp( A ) :

$$E _ { \lambda } ( A ) = \{ P ^ { - 1 } X \, ; \, X \in E _ { \lambda } ( B ) \} .$$

BTD8D8CTD2D8CXD3D2 Lorsque A est une matrice à coefficients réels, on peut considérer que A appartient à M n ( I R ) ou à M n ( C ) .

- On obtient dans le premier cas, les éléments propres réels, dans le second, les éléments propres complexes de A.
- On distinguera donc le spectre réel de A, noté sp I R ( A ) et formé des λ ∈ I R tels que A -λI n ne soit pas inversible, du spectre complexe, sp C ( A ) , de cette matrice. Une matrice de M n ( I R ) étant inversible dans cette algèbre si, et seulement si, elle l'est dans M n ( C ) (grâce aux déterminants), on a :

$$s p _ { \mathbb { R } } ( A ) = s p _ { \mathbb { C } } ( A ) \cap \mathbb { R } .$$

BF

## BVCWCPD4CXD8D6CT BE BA CA AJ CTCSD9CRD8CXD3D2 CSCTD7 CTD2CSD3D1D3D6D4CWCXD7D1CTD7

BXDCCTD1D4D0CT La matrice A = ( 0 -1 1 0 ) n'a pas de valeurs propres dans I R mais on a :

$$^ { s p _ { \mathbf C } \left ( A \right ) = \{ - i , i \} . }$$

Plus généralement, on a le résultat suivant :

## Proposition 15

Soit I K ′ un sous-corps du corps I K et A ∈ M n ( I K ′ ). Alors le spectre de A dans I K ′ est inclus dans le spectre de A dans I K .

✞ Démonstration page 111

☎

✆

## Proposition 16

Soit A ∈ M n ( I R ). Si λ ∈ sp C ( A ), alors λ est valeur propre de A et :

$$X \in E _ { \lambda } ( A ) \Leftrightarrow \overline { X } \in E _ { \overline { \lambda } } ( A )$$

Plus précisément, si ( X 1 , . . . , X k ) est une base de E λ ( A ) alors ( X 1 , . . . , X k ) est une base de E λ ( A ) donc dim E λ ( A ) = dim E λ ( A ).

☎

✆

Principe de démonstration. On prouve que, si ( X 1 , . . . , X k ) est une base de E λ ( A ) , alors la famille ( X 1 , . . . , X k ) est libre et composée de vecteurs propres de A pour la valeur propre λ . On en déduit dim E λ ( A ) ⩽ dim E λ ( A ) puis l'égalité. ✞ ✝ Démonstration page 111

## CACTD1CPD6D5D9CT

Soit A ∈ M n ( I R ) et λ ∈ sp I R ( A ).

X ↦→ A -λI n X

Si l'on considère A comme une matrice réelle, alors le sous-espace propre associé est le I R -espace vectoriel E I R λ ( A ) = { X ∈ M n, 1 ( I R ) | AX = λX } . Si l'on considère A comme une matrice complexe, alors le sous-espace propre associé est le C -espace vectoriel E C λ ( A ) = { X ∈ M n, 1 ( C ) | AX = λX } . Dans les deux cas, le sous-espace propre est le noyau de l'application linéaire ( ) .

Le théorème du rang donne donc dim I K E I K λ ( A ) = n -rg I K ( A -λI n ). Comme le rang d'une matrice réelle est le même qu'on la considère dans M n ( I R ) ou dans M n ( C ) (il est caractérisé par la plus grande taille des matrices carrées extraites de déterminant non nul), on en déduit que la dimension du sousespace propre ne change pas suivant que l'on considère A comme une matrice réelle ou comme une matrice complexe.

## BG D3D0DDD2 CM D3D1CTD7 CPD2D2D9D0CPD8CTD9D6D7

Dans le chapitre précédent, consacré en particulier à la structure d'algèbres, nous avons étudié la substitution polynomiale et les polynômes annulateurs (voir à partir de la page 31). Dans un souci d'unification des deux cas qui se

BG

✝

présentent ici, nous avons défini la substitution polynomiale et les polynômes annulateurs dans le cadre plus général d'une I K -algèbre. Étant donnée l'importance de ces notions dans le cas de ce chapitre consacré à la réduction, nous reprenons ici, intégralement, ces notions pour les endomorphismes et des matrices carrées.

On définit les itérés de u ∈ L ( E ) par récurrence sur k ∈ I N de la façon suivante : u 0 = Id E , puis, pour k ⩾ 1, u k = u k -1 ◦ u , c'est-à-dire :

$$u ^ { k } = \underbrace { u \circ \cdots \circ u } _ { k \text { f o i s } } . \\ \intertext { a r r e c u r r e n c e ) \colon }$$

On en déduit facilement (par récurrence) :

$$\forall \, ( k , \ell ) \in \mathbb { N } ^ { 2 } \ \ u ^ { k } \circ u ^ { \ell } = u ^ { \ell } \circ u ^ { k } = u ^ { k + \ell } .$$

Pour A ∈ M n ( I K ), on définit de même les puissances de A par récurrence sur k ∈ I N : A 0 = I n , puis, pour k ⩾ 1, A k = A k -1 × A , c'est-à-dire :

On a également :

## Définition 7

$$\text {Sentinel} \, \overline { \, } & \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar { \ } \, \underbar {$$

On note P ( u ) l'endomorphisme de E défini par :

$$P \left ( u \right ) = a _ { 0 } \, I d _ { E } + a _ { 1 } u + \cdots + a _ { p } u ^ { p } = \sum _ { k = 0 } ^ { p } a _ { k } u ^ { k } . \\ \subset \Lambda _ { 4 } \left ( \left | K \right | _ { 0 } \, o n d \hat { \phi } \text {fit} \, d o \, m \hat { a } _ { 0 } \, m o t \, n i j o \, R \left ( \, A \right ) \subset \Lambda _ { 4 } \left ( \left | K \right | _ { 0 } \, n o r d o t i o n \right ) .$$

Pour A ∈ M n ( I K ), on définit de même la matrice P ( A ) ∈ M n ( I K ) par :

$$P \left ( A \right ) = a _ { 0 } I _ { n } + a _ { 1 } A + \cdots + a _ { p } A ^ { p } = \sum _ { k = 0 } ^ { p } a _ { k } A ^ { k } .$$

On appelle polynôme en u (respectivement en A ) tout endomorphisme (respectivement toute matrice) de la forme P ( u ) (respectivement P ( A )) avec P ∈ I K [ X ]

D3D8CPD8CXD3D2 L'ensemble des polynômes en u ∈ L ( E ) est noté I K [ u ] . L'ensemble des polynômes en A ( I K ) est noté I K [ A ] .

BH

∈ M n

$$A ^ { k } = \underbrace { A \times \cdots \times A } _ { k \text { f o i s } } .$$

$$\forall \left ( k , \ell \right ) \in \mathbb { N } ^ { 2 } \ A ^ { k } A ^ { \ell } = A ^ { \ell } A ^ { k } = A ^ { k + \ell } .$$

BVCWCPD4CXD8D6CT BE BA CA AJ CTCSD9CRD8CXD3D2 CSCTD7 CTD2CSD3D1D3D6D4CWCXD7D1CTD7

## Proposition 17

Pour tout ( P, Q ) ∈ I K [ X ] 2 , les endomorphismes P ( u ) et Q ( u ) commutent.

En particulier, pour tout P ∈ I K [ X ] , Im P ( u ) et Ker P ( u ) sont des sousespaces stables par u .

Démonstration. Le fait que pour tout couple d'entiers ( k, ℓ ) , les endomorphismes u k et u ℓ commutent, permet d'obtenir l'égalité P ( u ) ◦ Q ( u ) = Q ( u ) ◦ P ( u ) .

Il suffit alors d'appliquer la proposition 1 de la page 65 à v = P ( u ) qui commute avec u .

## Proposition 18

1. Si x ∈ E λ ( u ) et si P ∈ I K [ X ] alors P ( u )( x ) = P ( λ ) x .
2. En particulier, si λ est valeur propre de u , alors P ( λ ) est valeur propre de P ( u ) et tout vecteur propre de u associé à la valeur propre λ est vecteur propre de P ( u ) associé à la valeur propre P ( λ ).

✞

✝

Démonstration page 112

☎

✆

## Corollaire 19

Soit A ∈ M n ( I K ).

1. Si X ∈ E λ ( A ) et si P ∈ I K [ X ] alors P ( A ) X = P ( λ ) X .
2. En particulier, si λ est valeur propre de A , alors P ( λ ) est valeur propre de P ( A ) et tout vecteur propre de A associé à la valeur propre λ est vecteur propre de P ( A ) associé à la valeur propre P ( λ ).

## Définition 8

On dit que P ∈ I K [ X ] est un polynôme annulateur de u , s'il vérifie P ( u ) = 0.

On dit que P ∈ I K [ X ] est un polynôme annulateur de A ∈ M n ( I K ) s'il vérifie P ( A ) = 0.

## BXDCCTD1D4D0CTD7

1. Si p est un projecteur, alors p 2 = p donc le polynôme X 2 -X annule p .
2. Si s est une symétrie, alors s 2 = Id donc le polynôme X 2 -1 annule s .

## Proposition 20

Si P est un polynôme annulateur de u ∈ L ( E ), alors toute valeur propre de u est racine de P .

Démonstration. D'après la proposition 18, si λ est valeur propre de u , alors P ( λ ) est valeur propre de l'endomorphisme nul P ( u ) donc P ( λ ) = 0 .

BI

## BXDCCTD1D4D0CT

On retrouve le fait que si p est un projecteur alors sp( p ) ⊂ { 0 , 1 } et si s est un symétrie alors sp( s ) ⊂ {-1 , 1 } .

BTD8D8CTD2D8CXD3D2 Lorsqu'on dispose d'un polynôme annulateur P de u ∈ L ( E ), on peut dire que toutes les valeurs propres de u sont racines de P , mais certaines racines de P peuvent ne pas être valeurs propres de u .

Ainsi, le polynôme X 2 -X = X ( X -1) est un polynôme annulateur de Id E , alors que 0 n'est pas valeur propre de Id E .

## Corollaire 21

Si P est un polynôme annulateur de A ∈ M n ( I K ), alors toute valeur propre de A est racine de P .

## Corollaire 22

Si P est un polynôme annulateur de u tel que P (0) = 0 et si E est de dimension finie, alors u est bijectif.

̸

Démonstration. D'après la proposition précédente, 0 n'est pas valeur propre de u . L'endomorphisme u est donc injectif. Comme E est de dimension finie, on en déduit que u est bijectif.

## Corollaire 23

Si P est un polynôme annulateur de A et si P (0) = 0, alors A est inversible.

̸

BXDCCTD1D4D0CT Si u vérifie u 4 + u +Id = 0, alors u est inversible. Plus précisément, on a u -1 = -u 3 -Id car u ◦ ( -u 3 -Id ) = Id.

Ainsi, si P (0) = 0, alors u -1 = -1 P (0) Q ( u ).

Plus généralement, soit P est un polynôme annulateur de u . Il existe un polynôme Q tel que P -P (0) = XQ . On a donc u ◦ Q ( u ) = Q ( u ) ◦ u = -P (0) Id.

̸

## Point méthode

La connaissance d'un polynôme annulateur de u permet aussi le calcul rapide des puissances de u .

En effet, si P annule u et si R est le reste de la division euclidienne de X p par P , alors u p = R ( u ).

L'utilisation de cette remarque nécessite de connaître un polynôme annulateur de u suffisamment « simple » pour pouvoir déterminer R .

BJBJ

✞

✝

☎

✆

<!-- image -->

$$\begin{array} { c } \text {Exercise 12} \text { Soft } A = \left ( \begin{array} { c c c } 1 & 2 & - 1 \\ - 4 & 1 0 & - 4 \\ - 8 & 1 6 & - 6 \end{array} \right ) . \\ \\ 1 . \text { Trouver un polynome P unitaire de degré 2 tel} \end{array}$$

1. Trouver un polynôme P unitaire de degré 2 tel que P ( A ) = 0.
2. En déduire que A est inversible.
3. Pour tout entier n déterminer le reste de la division euclidienne de X n par P .
4. En déduire A n , pour tout entier naturel n .

## BH D3D0DDD2 CM D3D1CT CRCPD6CPCRD8 AJ CTD6CXD7D8CXD5D9CT

## D3D0DDD2 CM D3D1CT CRCPD6CPCRD8 AJ CTD6CXD7D8CXD5D9CT CSB3D9D2CT D1CPD8D6CXCRCT

Par définition, λ ∈ I K est valeur propre de A ∈ M n ( I K ) si, et seulement si, la matrice A -λI n est non inversible donc si, et seulement si, det ( λI n -A ) = 0. L'expression det ( λI n -A ) étant polynomiale en λ , on introduit le polynôme associé.

## Définition 9

Soit A ∈ M n ( I K ). On appelle polynôme caractéristique de A et on note χ A ( X ) l'unique polynôme tel que :

$$\forall \lambda \in \mathbb { C } \ \chi _ { \lambda } ( \lambda ) = \det \left ( \lambda I _ { n } - A \right ) . \\$$

Par abus, on note χ A ( X ) = det ( XI n -A )

## CACTD1CPD6D5D9CTD7

- Il s'agit d'un léger abus. En effet, on a défini uniquement le déterminant d'une matrice à coefficients dans le corps des complexes. Pour pouvoir parler du polynôme det ( XI n -A ), il faudrait avoir défini le déterminant d'une matrice à coefficients dans le corps des fractions rationnelles (ce qui ne pose pas plus de difficultés).
- Le polynôme caractéristique d'une matrice A ∈ M n ( I R ) est identique que l'on considère A comme une matrice réelle ou comme une matrice complexe.

## Théorème 24

Un scalaire λ ∈ I K est une valeur propre de A si, et seulement s'il est une racine du polynôme caractéristique de A.

Démonstration. Un scalaire λ est valeur propre de A si, et seulement si, A -λI n ̸∈ GL n ( I K ) c'est-à-dire si, et seulement si, det ( A -λI n ) = 0 .

$$C o m m e \ d e t \left ( A - \lambda I _ { n } \right ) = ( - 1 ) ^ { n } \chi _ { A } ( \lambda ) , \, \text {on} \, \text {in} \, \partial \hat { d } \, \text {duit} \, \text {le} \, \text {resultat.}$$

BK

✞ p.112

✝

✞

✝

Proposition 25

Si A ∈ M n ( I K ) est triangulaire de diagonale ( α 1 , . . . , α n ), alors son polynôme caractéristique est égal à n ∏ k =1 ( X -α k ) et sp( A ) = { α 1 , . . . , α n } .

## Point méthode

Le théorème précédent montre l'importance pratique d'obtenir le polynôme caractéristique sous forme factorisée. On réalise dans les cas concrets cet objectif en calculant le déterminant det ( XI n -A ) par opérations élémentaires afin de faire apparaître des facteurs communs dans les lignes ou les colonnes.

BXDCCTD1D4D0CT Soit A = ⎛ ⎝ 3 5 -6 4 7 -9 3 6 -7 ⎞ ⎠ . Le polynôme caractéristique de A est donné par :

∣ ∣ La somme des coefficients des colonnes du déterminant ci-dessus étant 2 -X, l'opération C 1 ← C 1 + C 2 + C 3 montre qu'on a :

$$\chi _ { A } ( X ) = ( - 1 ) ^ { 3 } \left | \begin{array} { c c c c } 3 - X & 5 & - 6 \\ & 4 & 7 - X \\ & 3 & 6 & - 7 - X \end{array} \right | . \\ \text {dues coefficients des colonnes du déterminant ci-dessus } \hat { \text {ant} } \, 2 \\ - \, C _ { 1 } + C _ { 2 } + C _ { 3 } \, \text {montre qu'on a } \colon$$

$$r a t i n \, C _ { 1 } \leftarrow & \, C _ { 1 } + C _ { 2 } + C _ { 3 } \, \text {montre que} \, a \, \colon \\ & \, \chi _ { A } ( X ) = - \, \left | \begin{array} { c c c c } 2 - X & 5 & - 6 \\ 2 - X & 7 - X & - 9 \\ 2 - X & 6 & - 7 - X \end{array} \right | \, = ( X - 2 ) \, \left | \begin{array} { c c c c } 1 & 5 & - 6 \\ 1 & 7 - X & - 9 \\ 7 - X & 2 & 1 \end{array} \right | . \\ \text {Les operations} \, L _ { 2 } \leftarrow & L _ { 2 } - L _ { 1 } \, \text { et } \, L _ { 3 } \leftarrow L _ { 3 } - L _ { 1 } \, \text { consistent alors} \, \hat { a } \colon \\ & \, \left | \begin{array} { c c c c } 1 & 5 & - 6 \\ 1 & 5 & - 6 \\ \end{array} \right |$$

Le spectre de A est donc { 2 , -j, -j 2 } dans C et seulement { 2 } dans I R .

☎

✆

Calculer le polynôme caractéristique de A . Déterminer son spectre dans I R et C .

$$\text {Les operations } L _ { 2 } & \leftarrow L _ { 2 } - L _ { 1 } \text { et } L _ { 3 } \leftarrow L _ { 3 } - L _ { 1 } \text { conduisent alors } \hat { a } \colon \\ & \quad \chi _ { A } ( X ) = ( X - 2 ) \left | \begin{array} { c c c } 1 & 5 & - 6 \\ 0 & 2 - X & - 3 \\ 0 & 1 & - X - 1 \end{array} \right | = ( X - 2 ) \left ( X ^ { 2 } - X + 1 \right ) . \\ \text {Le spectre de } A & \text { est donc } \{ 2 , - j , - j ^ { 2 } \} \text { dans } \mathbb { C } \text { et selement } \{ 2 \} \text { dans } \text { IR} .$$

$$\begin{pmatrix} \underline { p } . 1 2 \\ \underline { p } . 1 1 \end{pmatrix} \, \text {Exercise 13} \, \text { Soft } \theta \in \mathbb { I } \, \text { et } \, A = \begin{pmatrix} 1 & 0 & 0 \\ 0 & \cos \theta & - \sin \theta \\ 0 & \sin \theta & \cos \theta \end{pmatrix} . \\ \, \text {Calculator } \, \text {le polyomé caractéristique de } A . \, \text {Déterminer son spectre}$$

CACTD1CPD6D5D9CT Si A ∈ M n ( C ), alors χ A = χ A donc on retrouve le résultat de la proposition 16 :

☎

✆

<!-- image -->

$$\lambda \in s p \left ( \overline { A } \right ) \Longleftrightarrow \overline { \lambda } \in s p \left ( A \right ) \\$$

Exercice 14 Soit A ∈ M n ( I K ). Montrer que A et t A ont le même polynôme caractéristique.

BL

## BVCWCPD4CXD8D6CT BE BA CA AJ CTCSD9CRD8CXD3D2 CSCTD7 CTD2CSD3D1D3D6D4CWCXD7D1CTD7

## Corollaire 26

Soit A ∈ M n ( I K ).

- Si I K = C , alors A a au moins une valeur propre.
- Si I K = I R et si n est impair, alors A a au moins une valeur propre.

Démonstration. On utilise le résultat précédent et le fait :

- qu'un polynôme non constant à coefficients complexes possède au mois une racine complexe (théorème de d'Alembert-Gauss),
- qu'un polynôme à coefficient réel de degré impair possède au moins une racine (théorème des valeurs intermédiaires).

BTD8D8CTD2D8CXD3D2 Comme le montre l'exemple de la page 74, une matrice réelle n'admet pas nécessairement de valeur propre réelle.

## Proposition 27

Soit A ∈ M n ( I K ). Son polynôme caractéristique χ A est un polynôme unitaire de degré n et l'on a :

$$\chi _ { A } ( X ) = X ^ { n } - ( \text {Tr} \, A ) \ X ^ { n - 1 } + \dots + ( - 1 ) ^ { n } \det A .$$

Principe de démonstration. On utilise le développement complet d'un déterminant.

Rappelons que, si A = ( a i,j ) 1 ⩽ i,j ⩽ n ∈ M n ( I K ) , on a :

$$\det A = \sum _ { \sigma \in S _ { n } } \varepsilon \left ( \sigma \right ) a _ { \sigma ( 1 ) , 1 } \dots a _ { \sigma ( n ) , n } .$$

CACTD1CPD6D5D9CT On retrouve le fait qu'une matrice carrée de taille n a au plus n valeurs propres distinctes.

## BXDCCTD1D4D0CTD7

$$X ^ { 2 } - ( \text {Tr} \, A ) \, X + \det A = X ^ { 2 } - ( \alpha + \delta ) \, X + ( \alpha \delta - \beta \gamma ) \, .$$

1. Le polynôme caractéristique de A = ( α β γ δ ) ∈ M 2 ( I K ) est :
2. Le polynôme caractéristique de A = ⎛ ⎝ α β γ α ′ β ′ γ ′ α ′′ β ′′ γ ′′ ⎞ ⎠ de M 3 ( I K ) est :
3. Si M est matrice triangulaire supérieure par blocs de la forme ( A C 0 D ) , alors son polynôme caractéristique est donné par :

X 3 -Tr( A ) X 2 + ( ( αβ ′ -α ′ β ) + ( αγ ′′ -α ′′ γ ) + ( β ′ γ ′′ -β ′′ γ ′ ) ) X -det A. On remarquera que le coefficient de X est la trace de la comatrice de A.

Ce résultat se généralise à toute matrice triangulaire par blocs.

$$\text {polyne} \arcter \hat { \text {riestique est donné par} } \colon \\ \chi _ { M } ( X ) = \left | \begin{array} { c c c } X I _ { p } - A & - C \\ 0 & X I _ { q } - D \end{array} \right | = \chi _ { A } ( X ) \chi _ { D } ( X ) . \\ \text {sultat se genéralise àoute matrice triangulaire par blocs.}$$

BC

✞

✝

Démonstration page 113

☎

✆

✞

✝

<!-- image -->

✞

✝

☎

✆

☎

✆

<!-- image -->

✞

✝

☎

✆

<!-- image -->

Exercice 15 Soit A ∈ M n ( I K ). Calculer le polynôme caractéristique de la matrice par blocs B = ( 0 A A 0 ) en fonction de celui de A .

Exercice 16 Soit A et B deux matrices de M n ( C ).

Montrer que le polynôme caractéristique de la matrice C de M 2 n ( C ) définie par :

$$C = \left ( \begin{array} { c c } A & B \\ B & A \end{array} \right )$$

est le produit des polynômes caractéristiques de A + B et A -B.

## Exercice 17 Polynôme caractéristique d'une matrice compagnon

$$\begin{pmatrix} \underline { p } . 1 3 \\ \underline { p } . 1 3 \end{pmatrix} & \text {Exercise 17} \, \text {Poly\hat{m}e caracteristique d'une matrice compar pagination} \\ & \left ( \begin{array} { c c c c c c } 0 & 0 & \dots & \dots & 0 & - a _ { 0 } \\ 1 & 0 & \dots & \dots & 0 & - a _ { 1 } \\ 0 & 1 & \ddots & \ddots & \vdots & \vdots \\ \vdots & \vdots & \ddots & \ddots & \vdots & \vdots \\ 0 & 0 & \dots & 1 & 0 & - a _ { p - 2 } \\ 0 & 0 & \dots & 0 & 1 & - a _ { p - 1 } \end{array} \right ) \\ & \text {Monterre que } \chi _ { A } ( X ) = X ^ { p } + a _ { p - 1 } X ^ { p - 1 } + \dots + a _ { 1 } X + a _ { 0 } . \\ & \text {Indicates } \varGamma _ { 1 } \varGamma _ { 2 } \varGamma _ { 3 } \varGamma _ { 4 } \varGamma _ { 5 } \varGamma _ { 6 } \varGamma _ { 7 } \varGamma _ { 8 } \varGamma _ { 9 } \varGamma _ { 1 } \varGamma _ { 2 } \varGamma _ { 3 } \varGamma _ { 4 } \varGamma _ { 5 } \varGamma _ { 6 } \varGamma _ { 7 } \varGamma _ { 8 } \varGamma _ { 9 } \varGamma _ { 1 } \varGamma _ { 2 } \varGamma _ { 3 } \varGamma _ { 4 } \varGamma _ { 5 } \varGamma _ { 6 } \varGamma _ { 7 } \varGamma _ { 8 } \varGamma _ { 9 } \varGamma _ { 1 } \varGamma _ { 2 } \varGamma _ { 3 } \varGamma _ { 5 } \varGamma _ { 6 } \varGamma _ { 7 } \varGamma _ { 8 } \varGamma _ { 9 } \varGamma _ { 1 } \varGamma _ { 2 } \varGamma _ { 3 } \varGamma _ { 6 } \varGamma _ { 7 } \varGamma _ { 8 } \varGamma _ { 9 } \varGamma _ { 1 } \varGamma _ { 2 } \varGamma _ { 3 } \varGamma _ { 6 } \varGamma _ { 7 } \varGamma _ { 8 } \varGamma _ { 9 } \varGamma _ { 1 } \varGamma _ { 2 } \varGamma _ { 3 } \varGamma _ { 6 } \varGamma _ { 7 } \varGamma _ { 8 } \varGamma _ { 9 } \varGamma _ { 1 } \varGamma _ { 2 } \varGamma _ { 3 } \varGamma _ { 6 } \varGamma _ { 7 } \varGamma _ { 8 } \varGamma _ { 9 } \varGamma _ { 1 } \varGamma _ { 2 } \varGamma _ { 3 } \varGamma _ { 6 } \varGamma _ { 7 } \varGamma _ { 8 } \varGamma _ { 9 } \varGamma _ { 1 } \varGamma _ { 2 } \varGamma _ { 3 } \varGamma _ { 6 } \varGamma _ { 7 } \varGamma _ { 8 } \varGamma _ { 9 } \varGamma _ { 1 } \varGamma _ { 2 } \varGamma _ { 3 } \varGamma _ { 6 } \varGamma _ { 7 } \varGamma _ { 8 } \varGamma _ { 9 } \varGamma _ { 1 } \varGamma _ { 2 } \varGamma _ { 3 } \varGamma _ { 6 } \varGamma _ { 7 } \varGamma _ { 8 } \varGamma _ { 9 } \varGamma _ { 1 } \varGamma _ { 2 } \varGamma _ { 3 } \varGamma _ { 6 } \varGamma _ { 7 } \varGamma _ { 8 } \varGamma _ { 9 } \varGamma _ { 1 } \varGamma _ { 2 } \varGamma _ { 3 } \varGamma _ { 6 } \varGamma _ { 7 } \varGamma _ { 8 } \varGamma _ { 9 } \varGamma _ { 1 } \varGamma _ { 2 } \varGamma _ { 3 } \varGamma _ { 6 } \varGamma _ { 7 } \varGamma _ { 8 } \varGamma _ { 9 } \varGamma _ { 1 } \varGamma _ { 2 } \varGamma _ { 3 } \varGamma _ { 6 } \varGamma _ { 7 } \varGamma _ { 8 } \varGamma _ { 9 } \varGamma _ { 1 } \varGamma _ { 2 } \varGamma _ { 3 } \varGamma _ { 6 } \varGamma _ { 7 } \varGamma _ { 8 } \varGamma _ { 9 } \varGamma _ { 1 } \varGamma _ { 2 } \varGamma _ { 3 } \varGamma _ { 6 } \varGamma _ { 7 } \varGamma _ { 8 } \varGamma _ { 9 } \varGamma _ { 1 } \varGamma _ { 2 } \varGamma _ { 3 } \varGamma _ { 6 } \varGamma _ { 7 } \varGamma _ { 8 } \varGamma _ { 9 } \varGamma _ { 1 } \varGamma _ { 2 } \varGamma _ { 3 } \varGamma _ { 6 } \varGamma _ { 7 } \varGamma _ { 8 } \varGamma _ { 9 } \varGamma _ { 1 } \varGamma _ { 2 } \varGamma _ { 3 } \varGamma _ { 6 } \varGamma _ { 7 } \varGamma _ { 8 } \varGamma _ { 9 } \varGamma _ { 1 } \varGamma _ { 2 } \varGamma _ { 3 } \varGamma _ { 6 } \varGamma _ { 7 } \varGamma _ { 8 } \varGamma _ { 9 } \varGamma _ { 1 } \varGamma _ { 2 } \varGamma _ { 3 } \varGamma _ { 6 } \varGamma _ { 7 } \varGamma _ { 8 } \varGamma _ { 9 } \varGamma _ { 1 } \varGamma _ { 2 } \varGamma _ { 3 } \varGamma _ { 6 } \varGamma _ { 7 } \varGamma _ { 8 } \varGamma _ { 9 } \varGamma _ { 1 } \varGamma _ { 2 } \varGamma _ { 3 } \varGamma _ { 6 } \varGamma _ { 7 } \varGamma _ { 8 } \varGamma _ { 9 } \varGamma _ { 1 } \varGamma _ { 2 } \varGamma _ { 3 } \varGamma _ { 6 } \varGamma _ { 7 } \varGamma _ { 8 } \varGamma _ { 9 } \varGamma _ { 1 } \varGamma _ { 2 } \varGamma _ { 3 } \varGamma _ { 6 } \varGamma _ { 7 } \varGamma _ { 8 } \varGamma _ { 9 } \varGamma _ { 1 } \varGamma _ { 2 } \varGamma _ { 3 } \varGamma _ { 6 } \varGamma _ { 7 } \varGamma _ { 8 } \varGamma _ { 9 } \varGamma _ { 1 } \varGamma _ { 2 } \varGamma _ { 3 } \varGamma _ { 6 } \varGamma _ { 7 } \varGamma _ { 8 } \varGamma _ { 9 } \varGamma _ { 1 } \varGamma _ { 2 } \varGamma _ { 3 } \varGamma _ { 6 } \varGamma _ { 7 } \varGamma _ { 8 } \varGamma _ { $$

Montrer que χ A ( X ) = X p + a p -1 X p -1 + · · · + a 1 X + a 0 .

D2CSCXCRCPD8CXD3D2 En notant L 0 , . . . , L p -1 les lignes de la matrice XI p -A , on pourra effectuer l'opération L 0 ← L 0 + XL 1 + · · · + X p -1 L p -1 .

## CACTD1CPD6D5D9CTD7

- On peut également prouver ce résultat par récurrence en développant par rapport à la première ligne.
- La matrice A de l'exercice précédent est appelée matrice compagnon du polynôme P . Elle intervient souvent dans les exercices et problèmes. Nous la retrouverons dans l'exercice 33 de la page 98.

## D3D0DDD2 CM D3D1CT CRCPD6CPCRD8 AJ CTD6CXD7D8CXD5D9CT CSB3D9D2 CTD2CSD3D1D3D6D4CWCXD7D1CT

On suppose dans ce paragraphe que E est un espace vectoriel de dimension finie n non nulle.

## Lemme 28

Deux matrices semblables ont même polynôme caractéristique.

Démonstration. Soit A ∈ M n ( I K ) et P ∈ GL n ( I K ) . En utilisant les propriétés des déterminants, on a pour tout scalaire λ :

BD

$$\ n a n s , \, \text {on a tour scalaire } \lambda \, \colon \\ \chi _ { P A ^ { - 1 } } ( \lambda ) = \det \left ( \lambda I _ { n } - P A ^ { - 1 } \right ) = \det \left ( P \left ( \lambda I _ { n } - A \right ) P ^ { - 1 } \right ) = \det \left ( \lambda I _ { n } - A \right ) = \chi _ { A } ( \lambda ) . \ \square$$

✞

✝

## BVCWCPD4CXD8D6CT BE BA CA AJ CTCSD9CRD8CXD3D2 CSCTD7 CTD2CSD3D1D3D6D4CWCXD7D1CTD7

Le fait que deux matrices semblables aient le même polynôme caractéristique, c'est-à-dire que deux matrices représentant le même endomorphisme aient le même polynôme caractéristique, justifie la définition suivante.

## Définition 10

On appelle polynôme caractéristique de l'endomorphisme u et l'on note χ u , le polynôme caractéristique de toute matrice représentant u .

On a donc, pour tout scalaire λ , χ u ( λ ) = det( λ Id E -u ).

## CACTD1CPD6D5D9CTD7

- La notion de polynôme caractéristique d'un endomorphisme n'a donc aucun sens si E n'est pas de dimension finie.
- Si u est l'endomorphisme canoniquement associé à A , alors χ u = χ A .

## Proposition 29

Le polynôme χ u est unitaire, de degré n et l'on a :

$$\chi _ { u } ( X ) = X ^ { n } - ( \text {Tr} \, u ) \ X ^ { n - 1 } + \dots + ( - 1 ) ^ { n } \det u .$$

Exercice 18 Soit u ∈ L ( E ) de rang 1. Exprimer χ u à l'aide de Tr u .

☎

✆

<!-- image -->

D2CSCXCRCPD8CXD3D2 On pourra utiliser une base adaptée au sous-espace vectoriel Im u .

## Théorème 30

Un scalaire λ ∈ I K est une valeur propre de u si, et seulement si, c'est une racine du polynôme caractéristique de u.

Démonstration. Un scalaire λ ∈ I K est une valeur propre si, et seulement si, u -λ Id E n'est pas inversible c'est-à-dire :

$$\chi _ { u } \left ( \lambda \right ) = d e t ( \lambda \, I d _ { E } - u ) = 0 .$$

CACTD1CPD6D5D9CT On retrouve le fait qu'un endomorphisme d'un espace vectoriel de dimension n a au plus n valeurs propres distinctes.

## Corollaire 31

- Si I K = C , alors u a au moins une valeur propre.
- Si I K = I R et si dim E est impair, alors u a au moins une valeur propre.

BTD8D8CTD2D8CXD3D2 Comme le montre l'exercice 7 de la page 69, en dimension infinie, un endomorphisme d'un C -espace vectoriel n'admet pas nécessairement de valeur propre.

BE

## Proposition 32

Si F est un sous-espace vectoriel de E stable par u , alors le polynôme caractéristique, χ u F , de l'endomorphisme induit par u sur F divise χ u .

☎

✆

<!-- image -->

Principe de démonstration. Calculer le polynôme caractéristique de la matrice de u dans une base adaptée à F (base de F complétée en une base de E ). ✞ ✝ Démonstration page 114

## CACTD1CPD6D5D9CTD7

- En particulier, on a l'inclusion sp ( u F ) ⊂ sp u .
- Le polynôme caractéristique d'un endomorphisme u stabilisant les sousespaces vectoriels d'une décomposition E = E 1 ⊕··· ⊕ E p est :

$$\chi _ { u } ( X ) = \chi _ { u _ { 1 } } ( X ) \cdots \chi _ { u _ { p } } ( X ) , \\ \tau _ { u } = \tau _ { 1 }$$

où, pour tout i ∈ [ [1 , p ] ] , u i est l'endomorphisme induit par u sur E i .

En effet, si ( B 1 , . . . , B p ) est une base adaptée à la somme directe considérée, la matrice de u dans cette base est une matrice diagonale par blocs dont le i -ème bloc diagonal est la matrice de u i dans la base B i de E i .

## Proposition 33

Si le polynôme caractéristique de u est scindé (respectivement scindé à racines simples), alors celui de l'endomorphisme induit par u sur tout sousespace vectoriel de E stable par u l'est aussi.

✞ Démonstration page 114

☎

✆

## D6CSD6CT CSCT D1D9D0D8CXD4D0CXCRCXD8 AJ CT CSB3D9D2CT DACPD0CTD9D6 D4D6D3D4D6CT

## Définition 11

On appelle ordre de multiplicité d'une valeur propre λ de u (respectivement de A ), son ordre de multiplicité en tant que racine du polynôme caractéristique de u (respectivement de A ).

CACTD1CPD6D5D9CT En particulier, une valeur propre de u est dite simple, double, triple, . . . si c'est une racine simple, double, triple, . . . du polynôme caractéristique de u .

D3D8CPD8CXD3D2 L'ordre de multiplicité d'une valeur propre λ sera noté m ( λ ).

BTD8D8CTD2D8CXD3D2 La notion d'ordre de multiplicité, tout comme celle de polynôme caractéristique, n'a pas de sens en dimension infinie.

CACTD1CPD6D5D9CT D'après la remarque de la page 74, la multiplicité d'une valeur propre réelle d'une matrice réelle ne change pas si l'on considère A comme une matrice réelle ou comme une matrice complexe.

BF

✝

## BVCWCPD4CXD8D6CT BE BA CA AJ CTCSD9CRD8CXD3D2 CSCTD7 CTD2CSD3D1D3D6D4CWCXD7D1CTD7

## Proposition 34

Pour tout λ ∈ sp ( u ), on a :

$$1 \leqslant \dim E _ { \lambda } ( u ) \leqslant m \left ( \lambda \right ) .$$

Principe de démonstration. On utilise la stabilité par u de E λ ( u ) et la proposition 32 de la page précédente. ✞ ✝ Démonstration page 114

## BXDCCTD1D4D0CTD7

1. Si u est de rang r , le polynôme χ u ( X ) est divisible par X n -r , puisque le noyau Ker u = E 0 ( u ) est de dimension n -r .

$$\left [ \begin{matrix} \text {on considere la matrice } \colon \\ & & 0 & \dots & 0 & \alpha _ { n - 1 } \\ & & \vdots & & \vdots & \vdots \\ A = \left [ \begin{matrix} 0 & \dots & 0 & \alpha _ { n - 1 } \\ & & \vdots & & \vdots \\ 0 & \dots & 0 & \alpha _ { 1 } \\ \alpha _ { n - 1 } & \dots & \alpha _ { 1 } & 0 \end{matrix} \right ] , \\ \text {erieur ou égal à 2, il existe des scalaires a et} \\ \text {erieur ou égal à 2, il existe des scalaires a et} \\$$

2. En particulier, si l'on considère la matrice :

qui est de rang inférieur ou égal à 2, il existe des scalaires a et b tels que :

Le coefficient a , égal à l'opposé de la trace de A , est nul.

$$\text {erieur ou égal à } 2 , \text { il existe des scalaires a } \ e \\ \chi _ { A } ( X ) = X ^ { n - 2 } \left ( X ^ { 2 } + a X + b \right ) . \\ \text {al à l'opposé de la trace de } A , \text { est null.} \\ \text {efficient} \ h \text { on peut précéder par } \vec { r } c u r r e n c e$$

Pour obtenir le coefficient b , on peut procéder par récurrence.

$$\text {Pou obtensor le coefficient} \, b , \, & \text {on} \, \text {pe} \text {ceder par} \, \text {recurrence} . \\ \text {Pou n} = 2 , \, & \text {on} \, \text {obtient} \, b = - \alpha _ { 1 } ^ { 2 } . \\ & \quad \left | \begin{array} { c c c c } X & \dots & 0 & - \alpha _ { n - 1 } \\ & & \dots & \vdots \\ & & \vdots & \vdots \\ & & & 0 \\ & & \dots & X & - \alpha _ { 1 } \\ & & & X & 0 \\ & & & & \vdots \\ & & & & \vdots \\ & & & & 0 \\ & & & \dots & X & - \alpha _ { 1 } \\ & & & & - \alpha _ { n } & \dots & - \alpha _ { 1 } \\ & & & & & & \end{array} \right | = X ^ { n - 2 } \left ( X ^ { 2 } + b _ { n } \right ) \, \text {et} \, \colon \\ \text {En développant par rapport à la première colonne, on a} .$$

En développant par rapport à la première colonne, on a :

$$| \, - \alpha _ { n - 1 } \, \dots \, - \alpha _ { 1 } \, \quad X \quad & \dots \quad 0 \quad - \alpha _ { n } \, \Big | \\ \det \left | \, & \quad \colon \quad \vdots \quad \vdots \quad \colon \quad \colon \quad = X ^ { n - 1 } \left ( X ^ { 2 } + b _ { n + 1 } \right ) \\ \Big | \, & \quad 0 \quad \dots \quad X \quad - \alpha _ { 1 } \quad X \quad \Big | \\ \text {evolppant par rapport à la première colonne, on a :} \\ \Big | \, & \quad X \quad \dots \quad 0 \quad - \alpha _ { n } \, \Big |$$

donc b n +1 = b n -α 2 n .

$$\text {En developpant par r aport à la premier colonne, on a :} \\ \quad \left | \begin{array} { c c c } X & \dots & 0 & - \alpha _ { n } \\ & \vdots & & \vdots \\ & \vdots & & \vdots \\ 0 & \dots & X & - \alpha _ { 1 } \\ - \alpha _ { n } & \dots & - \alpha _ { 1 } & X \end{array} \right | \\ \text {dond b_{n+1} = b_{n} - \alpha^{2} .} \\ \text {On en déduit que pour tout entier n b_{n} = - \sum _ { n } ^ { n - 1 } \alpha _ { n } ^ { 2 } .}$$

On peut également obtenir ce résultat en utilisant le développement complet du déterminant :

On en déduit que pour tout entier n b n = -n -1 ∑ j =1 α 2 j .

$$\chi _ { A } \left ( X \right ) = \sum _ { \sigma \in S _ { n } } P _ { \sigma } \ a v e c { \ P _ { \sigma } } = \varepsilon \left ( \sigma \right ) \prod _ { i = 1 } ^ { n } \left ( X \delta _ { \sigma ( i ) , i } - a _ { \sigma ( i ) , i } \right ) .$$

BK

BG

☎

✆

- Si σ laisse invariants au plus n -3 entiers de [ [1 , n ] ] , alors on a deg ( P σ ) ⩽ n -3.
- Si σ laisse invariants au moins n -1 entiers de [ [1 , n ] ] , alors, comme c'est une bijection, on a σ = Id et P σ = X n .
- Si σ laisse invariants exactement n -2 entiers de [ [1 , n ] ] , alors σ est une transposition τ i,j ( i = j ) et P σ = -a j,i a i,j X n -2 .

̸

Pour i = n et j ⩽ n -1, on obtient P σ = -α 2 j X n -2 .

Pour 1 ⩽ i, j ⩽ n -1, on a a j,i = a i,j = 0, donc P σ = 0.

$$\text {il vient alors } b = - \sum _ { j = 1 } ^ { n - 1 } \alpha _ { j } ^ { 2 } . \text {En conclusion } \chi _ { A } ( X ) = X ^ { n } - X ^ { n - 2 } \sum _ { j = 1 } ^ { n - 1 } \alpha _ { j } ^ { 2 } . \\ \\ \text {Corollaire 35}$$

## Corollaire 35

Si λ est valeur propre simple de u , alors dim E λ ( u ) = 1.

Démonstration. C'est une conséquence immédiate de la proposition 34 de la page ci-contre

CACTD1CPD6D5D9CT Le spectre de u est, par définition, l'ensemble des racines de χ u dans I K . Comme dans le cas des polynômes, on distinguera soigneusement les notions d'ensemble et de liste des valeurs propres de u .

- L'ensemble des valeurs propres est le spectre de u . S'il est égal à { λ 1 , . . . , λ p } , avec λ 1 , . . . , λ p distincts deux à deux, alors on a :

où Q ∈ I K [ X ] n'a pas de racine dans I K .

$$\chi _ { u } ( X ) = Q ( X ) \prod _ { i = 1 } ^ { p } ( X - \lambda _ { i } ) ^ { m ( \lambda _ { i } ) } \\ \intertext { a n d a p a s d e r a c i n e d a n s } \intertext { a n d a p a s d e r a c i n e d a n s } K .$$

- Une liste des valeurs propres est une famille de scalaires répétant les valeurs propres avec leurs multiplicités. Une telle liste est unique à l'ordre près et si ( μ 1 , . . . , μ s ) est en est une, alors on a :

$$\chi _ { u } ( X ) & = Q ( X ) \prod _ { i = 1 } ^ { s } \left ( X - \mu _ { i } \right ) \\ \text {pass the race dans} \, \mathbb { K } ,$$

- Bien sûr, la liste ( μ 1 , . . . , μ s ) est à l'ordre près formée des λ 1 , . . . , λ p répétés autant de fois que leur multiplicité, c'est-à-dire :

où Q ∈ I K [ X ] n'a pas de racine dans I K .

On a donc :

$$( \mu _ { 1 } , \dots , \mu _ { s } ) = & \underbrace { ( \lambda _ { 1 } , \dots , \lambda _ { 1 } , \dots , \underbrace { \lambda _ { p } , \dots , \lambda _ { p } } } _ { m ( \lambda _ { 1 } ) \text { fois} } ) . \\ \intertext { n c \colon } & \alpha = m ( \lambda ) \, , \, | \, + \, , \, + \, | \, + \, m ( \lambda ) \, , \, )$$

$$s = m ( \lambda _ { 1 } ) + \dots + m ( \lambda _ { p } ) .$$

- Si χ u est scindé, alors on a s = n et :

$$\chi _ { u } \left ( X \right ) = \prod _ { k = 1 } ^ { p } \left ( X - \lambda _ { k } \right ) ^ { m \left ( \lambda _ { k } \right ) } = \prod _ { i = 1 } ^ { n } \left ( X - \mu _ { i } \right ) .$$

BH

## BVCWCPD4CXD8D6CT BE BA CA AJ CTCSD9CRD8CXD3D2 CSCTD7 CTD2CSD3D1D3D6D4CWCXD7D1CTD7

## Proposition 36

Soit u ∈ L ( E ), avec dim E = n , tel que χ u soit scindé.

- Si ( μ 1 , . . . , μ n ) est une liste de valeurs propres de u , alors :

$$\text {Tr} \, u = \sum _ { i = 1 } ^ { n } \mu _ { i } \, \ e t \, \det u = \prod _ { i = 1 } ^ { n } \mu _ { i } . \\$$

- Si sp ( u ) = { λ 1 , . . . , λ p } , avec λ 1 , . . . , λ p distincts deux à deux, alors :

$$\text {Tr} \, u = \sum _ { i = 1 } ^ { p } m \left ( \lambda _ { i } \right ) \lambda _ { i } \ \det \ d e t \, u = \prod _ { i = 1 } ^ { p } \lambda _ { i } ^ { m ( \lambda _ { i } ) } .$$

✞ ✝ Démonstration page 114

## BXDCCTD1D4D0CTD7

1. Tout endomorphisme d'un espace vectoriel complexe de dimension finie a un polynôme caractéristique scindé puisque tout polynôme de C [ X ] l'est.
2. Il existe des endomorphismes d'espace vectoriel réel de dimension finie dont le polynôme caractéristique n'est pas scindé.

̸

$$R ( \theta ) = \left ( \begin{array} { c c } \cos \theta & - \sin \theta \\ \sin \theta & \cos \theta \end{array} \right ) \\ o r t h o n r o m e \, d i c e t e t a p o u p l o w$$

Par exemple, la rotation d'angle θ = 0 mod π du plan vectoriel euclidien orienté a pour matrice :

dans une (toute) base orthonormée directe et a pour polynôme caractéristique :

$$X ^ { 2 } - 2 X \cos \theta + 1 ,$$

BI

qui n'est pas scindé.

##  BXD2CSD3D1D3D6D4CWCXD7D1CTD7 CTD8 D1CPD8D6CXCRCTD7 CSCXCPCVD3D2CPD0CXD7CPCQD0CTD7

On rappelle que E est un espace vectoriel de dimension finie n non nulle.

## Définition 12

- Un endomorphisme u est dit diagonalisable s'il existe une base de E dans laquelle sa matrice est diagonale.
- Une matrice A de M n ( I K ) est dite diagonalisable si elle est semblable à une matrice diagonale, c'est-à-dire s'il existe une matrice D ∈ M n ( I K ) diagonale et une matrice P ∈ GL n ( I K ) telles que A = PDP -1 .

## Proposition 37

Un endomorphisme u de E est diagonalisable si, et seulement s'il existe une base de E constituée de vecteurs propres de u .

✞ Démonstration page 115

☎

✆

✝

☎

✆

✞

✝

## CACTD1CPD6D5D9CTD7

- Une base dans laquelle la matrice de u est diagonale s'appelle une base de diagonalisation de u.
- Une base de diagonalisation de u ∈ L ( E ) est donc une base de E constituée de vecteurs propres de u .

☎

✆

<!-- image -->

✞

✝

☎

✆

Exercice 19 Soit D n ∈ L ( I K n [ X ]) avec n ⩾ 1, défini par D n ( P ) = P ′ .

L'endomorphisme D est-il diagonalisable?

<!-- image -->

Exercice 20 Soit f ∈ L ( M n ( I K ) ) défini par f ( A ) = A +Tr( A ) I n . L'endomorphisme f est-il diagonalisable ?

## Proposition 38

Les projecteurs et les symétries de E sont diagonalisables.

✞ Démonstration page 115

✝

☎

✆

CACTD1CPD6D5D9CT On verra plus tard qu'il y a plus rapide. En effet, d'après le théorème 60 de la page 103, un endomorphisme annulant un polynôme scindé à racines simples est diagonalisable.

## Proposition 39

Soit A ∈ M n ( I K ) une matrice représentant un endomorphisme u .

La matrice A est alors diagonalisable si, et seulement si, u est diagonalisable.

Démonstration. C'est une conséquence directe de la définition 12 de la page ci-contre.

## Corollaire 40

Une matrice A ∈ M n ( I K ) est diagonalisable si, et seulement si, son endomorphisme canoniquement associé est diagonalisable.

CACTD1CPD6D5D9CT Soit A ∈ M n ( I K ) diagonalisable et P ∈ GL n ( I K ) la matrice de passage de la base canonique à une base B de vecteurs propres de A . D'après l'effet d'un changement de base sur la matrice d'un endomorphisme, la matrice de l'endomorphisme canoniquement associé à A dans la base B est égale à P -1 AP . Cette dernière matrice est donc diagonale.

BJ

<!-- image -->

✞

✝

☎

✆

Si c'est le cas, fournir une matrice P ∈ GL 3 ( I K ) telle que P -1 AP soit diagonale.

## Point méthode

Soit A ∈ M n ( I K ) diagonalisable et ( E 1 , . . . , E n ) une base de I K n constituée de vecteurs propres de A associés aux valeurs propres λ 1 , . . . , λ n .

Si on pose P = ( E 1 , . . . , E n ), alors :

$$P ^ { - 1 } A P = D i a g \left ( \lambda _ { 1 } , \dots , \lambda _ { n } \right ) .$$

$$( \underline { p } . 1 5 ) \, \ E x c i e { 2 1 } \, \ L a \, \matrice \, A = \left ( \begin{array} { c c c } 0 & 3 & 2 \\ - 2 & 5 & 2 \\ & 2 & - 3 \end{array} \right ) \, \ e s t { \text {ell} } \, \text {diagonalisable} ? \\ \, \text {Si} \, \text {c'est le cas, fournir une matrice } \, P \in \mathcal { G L } _ { 3 } ( \text {IK} ) \, \text {telle que } P ^ { - 1 } \, A \, P \, \text {soft diagonalale.}$$

La proposition suivante permet de déterminer si un endomorphisme est diagonalisable sans déterminer explicitement ses espaces propres mais en en connaissant simplement la dimension.

## Proposition 41

Si sp( u ) = { λ 1 , . . . , λ p } , avec λ 1 , . . . , λ p distincts deux à deux, alors les propriétés suivantes sont équivalentes :

- ( i ) l'endomorphisme u est diagonalisable,
- ( iii ) p ∑ i =1 dim E λ i ( u ) = dim E .
- ( ii ) p ⊕ i =1 E λ i ( u ) = E ,

## Corollaire 42

Soit A ∈ M n ( I K ) de spectre { λ 1 , . . . , λ p } , avec λ 1 , . . . , λ p distincts deux à deux. Il y a équivalence entre :

- ( i ) la matrice A est diagonalisable,
- ( ii ) p ⊕ i =1 E λ i ( A ) = M n, 1 ( I K ), ( iii ) p ∑ i =1 dim E λ i ( A ) = n .

## BXDCCTD1D4D0CTD7

1. Si u ∈ L ( E ) admet λ pour unique valeur propre, u est diagonalisable si, et seulement si, le sous-espace propre associé est égal à E , c'est-à-dire si, et seulement si, u = λ Id E .

De même, si A ∈ M n ( I K ) admet λ pour unique valeur propre, elle est diagonalisable si, et seulement si, son endomorphisme canoniquement associé est égal à λ Id I K n , c'est-à-dire si, et seulement si, A = λI n .

BKBK

<!-- image -->

✞ Démonstration page 116

✝

☎

✆

2. En particulier un endomorphisme u vérifiant u p = 0 n'est diagonalisable que s'il est nul. En effet, d'après la proposition 20 de la page 76, il est annulé par le polynôme X p donc il admet au plus une valeur propre : 0. Un tel endomorphisme est dit nilpotent .

L'étude de ces endomorphismes sera détaillée plus tard.

3. De même, si A ∈ M n ( I K ) est triangulaire de termes diagonaux tous égaux à λ , alors son polynôme caractéristique est égal à ( X -λ ) n , d'après la proposition 25 de la page 79. La matrice A admet donc λ pour valeur propre d'ordre n ; elle n'est donc diagonalisable que si A = λI n .

## CACTD1CPD6D5D9CTD7

- Si { λ 1 , . . . , λ p } ⊂ sp( u ) et si p ∑ i =1 dim E λ i ( u ) = dim E , alors

$$\{ \lambda _ { 1 } , \dots , \lambda _ { p } \} = \text {sp} ( u ) \quad \text {et} \quad E = \bigoplus _ { i = 1 } ^ { p } E _ { \lambda _ { i } } .$$

- Supposons que u soit diagonalisable de spectre { λ 1 , . . . , λ r } . Nous avons alors la décomposition en somme directe :

$$E = E _ { \lambda _ { 1 } } ( u ) \oplus \cdots \oplus E _ { \lambda _ { r } } ( u ) .$$

Si l'on note ( p λ 1 , . . . , p λ r ) la famille des projecteurs associés ; alors les endomorphismes u et λ 1 p λ 1 + · · · + λ r p λ r coïncident sur chaque E λ i donc :

$$u = \lambda _ { 1 } p _ { \lambda _ { 1 } } + \dots + \lambda _ { r } p _ { \lambda _ { r } } .$$

Ainsi, dans toute base B adaptée à la somme directe précédente, la matrice de u est diagonale par blocs de la forme :

$$D i a g \left ( D _ { 1 } , \dots , D _ { r } \right )$$

où D k est la matrice scalaire de dimension dim E λ k ( u ) de rapport λ k .

BXDCCTD1D4D0CT Soit la matrice complexe :

$$\begin{array} { c } \text {complex} \colon \\ A = \left ( \begin{array} { c c c c } 0 & 1 & 0 & 0 \\ 1 & k & 1 & 1 \\ 0 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 \end{array} \right ) . \\ \end{array}$$

On voit aisément que son polynôme caractéristique vaut X 2 ( X 2 -kX -3) . Comme A est de rang 2, le sous espace-propre associé à 0 est de dimension 2. Si k vérifie k 2 +12 = 0 , le trinôme X 2 -kX -3 à deux racines λ 1 et λ 2 distinctes non nulles. Les sous-espaces vectoriels propres associés étant de dimension supérieure ou égale à 1 , la matrice A est diagonalisable.

BL

̸

✞

✝

## BVCWCPD4CXD8D6CT BE BA CA AJ CTCSD9CRD8CXD3D2 CSCTD7 CTD2CSD3D1D3D6D4CWCXD7D1CTD7

Si k est égal à ± 2 i √ 3 , le trinôme X 2 -kX -3 à une seule racine λ = k 2 · Le sous-espace propre associé est obtenu en résolvant :

⎩ Il est donc de dimension 1 engendré par ⎛ ⎜ ⎜ ⎝ 1 λ 1 1 ⎞ ⎟ ⎟ ⎠ . La dimension de la somme des sous-espaces vectoriels propres valant 3 , la matrice A n'est pas diagonalisable.

## Corollaire 43

Si u est un endomorphisme d'un espace vectoriel de dimension n et possède n valeurs propres distinctes c'est-à-dire si χ u est est scindé à racines simples, alors u est diagonalisable et chaque sous-espace propre est de dimension 1.

De même, si A ∈ M n ( I K ) possède n valeurs propres distinctes alors A est diagonalisable et chaque sous-espace propre est de dimension 1 .

✞ Démonstration page 117

☎

$$( \underline { p } . 1 7 ) \, \text { Exercise 22 } \, \L a \, \text { matrice } \, A = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 4 & 5 \\ 0 & 0 & 6 \end{pmatrix} \, \text {est-ellé diagonalisable?}$$

☎

✆

<!-- image -->

BTD8D8CTD2D8CXD3D2 Il faut bien noter que le résultat précédent ne fournit qu'une condition suffisante pour que u soit diagonalisable comme le montre l'exercice 20 de la page 87.

Le théorème qui suit donne une condition nécessaire et suffisante.

## Théorème 44

Pour que u ∈ L ( E ) soit diagonalisable, il faut et il suffit qu'il vérifie les deux conditions suivantes :

- son polynôme caractéristique χ u est scindé sur I K ;
- pour toute valeur propre de u , la dimension du sous-espace propre associé est égale à l'ordre de cette valeur propre, c'est-à-dire :

$$\forall \lambda \in \text {sp} ( u ) \ \dim E _ { \lambda } ( u ) = m ( \lambda ) .$$

Principe de démonstration. Utiliser les propositions 41 de la page 88 et 34 de la page 84. ✞

✝

☎

✆

Démonstration page 117

✆

$$\begin{array} { r l } & { s o c i \hat { e } e s t o b t e n u e n r \hat { e } s o l v a n t \colon } \\ & { \quad \left \{ \begin{array} { l l l } { - \lambda x + y } & { = } & { 0 } \\ { x + \lambda y + z + t } & { = } & { 0 } \\ { y - \lambda z } & { = } & { 0 } \\ { y - \lambda t } & { = } & { 0 } \end{array} } \end{array}$$

BC

✝

✞

✝

## CACTD1CPD6D5D9CT

Pour toute valeur propre simple λ , on a toujours dim E λ ( u ) = m ( λ ) car :

$$E _ { \lambda } ( u ) \neq \{ 0 \} \quad e t \quad \dim E _ { \lambda } ( u ) \leqslant m ( \lambda ) = 1 .$$

## Corollaire 45

Pour que A ∈ M n ( I K ) soit diagonalisable, il faut et il suffit qu'elle vérifie les deux conditions suivantes :

- son polynôme caractéristique χ A est scindé sur I K ;
- pour toute valeur propre de A , la dimension du sous-espace propre associé est égale à l'ordre de cette valeur propre, c'est-à-dire :

$$\forall \lambda \in \text {sp} ( A ) \ \dim E _ { \lambda } ( A ) = m ( \lambda ) .$$

̸

☎

✆

et suffisante portant sur ( a, b, c ) ∈ I K 3 pour que la matrice A soit diagonalisable.

## Point méthode

Pour que u ∈ L ( E ) soit diagonalisable, il faut et il suffit qu'il vérifie les deux conditions suivantes :

- son polynôme caractéristique χ u est scindé sur I K ;
- pour toute valeur propre multiple de u , la dimension du sous-espace propre associé est égale à l'ordre de cette valeur propre.

On a un résultat similaire pour les matrices.

$$\begin{array} { c c c } ( p . 1 7 ) & \text {Exercise 23} & \text {Soit A} = \left ( \begin{array} { c c c } 1 & a & b \\ 0 & 1 & c \\ 0 & 0 & - 1 \end{array} \right ) \in \mathcal { M } _ { 3 } ( I K ) . \text { Donner une conditionnée necessaire} \\ & & \\ & \text {et suffisante portant sur } ( a , b , c ) \in I K ^ { 3 } \text { pour que la matrice } A \text { doit diagonalisable.} \end{array}$$

CACTD1CPD6D5D9CT Il n'est pas toujours nécessaire de calculer le polynôme caractéristique d'un endomorphisme pour savoir s'il est diagonalisable comme le montre l'exercice 20 de la page 87 ou l'exemple suivant.

BXDCCTD1D4D0CT Soit n un entier.

On considère l'endomorphisme de I R [ X ] , v : P ↦→ ( 1 -X 2 ) P ′ + nXP . Il stabilise le sous-espace vectoriel I R n [ X ] . En effet, v (1) = nX , v ( X n ) = nX n -1 et, pour tout k de [ [1 , n -1] ] , on a :

$$v ( X ^ { k } ) = ( n - k ) \, X ^ { k + 1 } + k X ^ { k - 1 } \in \mathbb { R } _ { n } [ X ] .$$

Considérons alors l'endomorphisme u induit par v sur I R n [ X ].

<!-- image -->

BD

## BVCWCPD4CXD8D6CT BE BA CA AJ CTCSD9CRD8CXD3D2 CSCTD7 CTD2CSD3D1D3D6D4CWCXD7D1CTD7

La matrice de u dans la base canonique (1 , X, . . . , X n ) est :

$$\begin{pmatrix} \ n a b a n o n i q u e \ ( 1 , X , \dots , X ^ { n } ) \ e s t \colon \\ \left ( \begin{array} { c c c } 0 & 1 & & ( 0 ) \\ n & 0 & 2 & \\ & n - 1 & \ddots & \ddots \\ & & \ddots & \ddots \\ ( 0 ) & & 1 & 0 \end{array} \right ) \\ \ e t r i s t i q u e \ n a r a s i s a n t \ p a s \ f a c l e \ a \ c l u c ler , \\ \ e d u \ d i r e c t e m e n t . \end{pmatrix}$$

Son polynôme caractéristique ne paraissant pas facile à calculer, on peut rechercher les valeurs propres de u directement.

Un polynôme P non nul de I R n [ X ] est un vecteur propre de u s'il existe λ ∈ I R tel que :

soit :

$$\left ( 1 - X ^ { 2 } \right ) P ^ { \prime } + n X P & = \lambda P , \\ n X - \lambda & = n - \lambda \quad n + \lambda$$

dans I R ( X ) . Si la factorisation de P sur C est C r ∏ k =1 ( X -α k ) n k , on a :

$$\frac { P ^ { \prime } } { P } = \frac { n X - \lambda } { X ^ { 2 } - 1 } = \frac { n - \lambda } { 2 \left ( X - 1 \right ) } + \frac { n + \lambda } { 2 \left ( X + 1 \right ) } \\$$

$$\frac { P ^ { \prime } } { P } = \sum _ { k = 1 } ^ { r } \frac { n _ { k } } { X - \alpha _ { k } } .$$

Ainsi, si P est un vecteur propre associé à un réel λ , alors, par unicité de la décomposition en éléments simples, n -λ 2 et n + λ 2 sont des entiers naturels et :

$$P = C ( X - 1 ) ^ { \frac { n - \lambda } { 2 } } ( X + 1 ) ^ { \frac { n + \lambda } { 2 } } . \\$$

Pour tout k ∈ [ [0 , n ] ] , on pose donc P k = ( X -1) k ( X +1) n -k . On vérifie alors que :

$$\forall k \in [ 0 , n ] \ \ u ( P _ { k } ) = ( n - 2 k ) \, P _ { k } . \\ \zeta _ { k } ( 0 , n ) = \Omega ( P _ { k } ) = 1 \quad \zeta _ { k } ( \mu _ { k } ) \colon \Omega ( \mu _ { k } ) .$$

Comme les nombres réels ( n -2 k ) k ∈ [ [0 ,n ] ] sont deux à deux distincts, u possède n +1 valeurs propres distinctes ; il est donc diagonalisable et la famille ( P k ) k ∈ [ [0 ,n ] ] est une base de vecteurs propres de u .

## CE BXD2CSD3D1D3D6D4CWCXD7D1CTD7 CTD8 D1CPD8D6CXCRCTD7 D8D6CXCVD3D2CPD0CXD7CPCQD0CTD7

On suppose dans ce paragraphe que E est un espace vectoriel de dimension finie n non nulle.

## Définition 13

- L'endomorphisme u est dit trigonalisable s'il existe une base de E dans laquelle la matrice de u est triangulaire supérieure.
- Une matrice A ∈ M n ( I K ) est dite trigonalisable si elle est semblable à une matrice triangulaire supérieure.

BE

✞

✝

✞

✝

CACTD1CPD6D5D9CT Soit B = ( e 1 , . . . , e n ) une base de E . La matrice de u dans la base B est triangulaire supérieure si, et seulement si :

## Proposition 46

Soit A ∈ M n ( I K ) une matrice représentant un endomorphisme u .

La matrice A est alors trigonalisable si, et seulement si, u est trigonalisable.

Démonstration. C'est une conséquence directe de la définition 13.

## Corollaire 47

Une matrice A ∈ M n ( I K ) est trigonalisable si, et seulement si, son endomorphisme canoniquement associé est trigonalisable.

CACTD1CPD6D5D9CT On aurait pu aussi choisir la forme triangulaire inférieure. En effet, il est facile de vérifier que, si la matrice d'un endomorphisme u dans une base ( e 1 , e 2 , . . . , e n ) est triangulaire supérieure, alors sa matrice dans la base ( e n , e n -1 , . . . , e 1 ) est triangulaire inférieure.

☎

✆

<!-- image -->

Exercice 24 Soit A la matrice de u dans une base ( e 1 , e 2 , . . . , e n ) et B celle de u dans la base ( e n , e n -1 , . . . , e 1 ). Quelle est la relation entre A et B ?

## Théorème 48

Un endomorphisme u ∈ L ( E ) est trigonalisable si, et seulement si, son polynôme caractéristique est scindé sur I K .

Démonstration page 118

Principe de démonstration. Le sens direct découle de la proposition 25 de la page 79. La réciproque se prouve par récurrence. ✞ ✝

## Corollaire 49

Un matrice est trigonalisable si, et seulement si, son polynôme caractéristique est scindé sur I K .

☎

✆

<!-- image -->

Exercice 25 Soit u trigonalisable et F un sous-espace vectoriel stable par u . Montrer que l'endomorphisme induit u F est aussi trigonalisable.

## Corollaire 50

Si E est un C -espace vectoriel, alors tout endomorphisme de E est trigonalisable.

Toute matrice carrée à coefficients dans C est trigonalisable.

Démonstration.

<!-- image -->

BL

BF

☎

✆

$$\forall i \in \mathbb { I } , n - 1 \Big ] \ e _ { i } \in V e c t \left ( e _ { 1 } , \dots , e _ { i } \right ) .$$

✞

✝

<!-- image -->

✞

✝

☎

✆

☎

✆

<!-- image -->

BL

## BVCWCPD4CXD8D6CT BE BA CA AJ CTCSD9CRD8CXD3D2 CSCTD7 CTD2CSD3D1D3D6D4CWCXD7D1CTD7

CACTD1CPD6D5D9CT Il existe des endomorphismes d'espace vectoriel réel de dimension finie non trigonalisable.

̸

Par exemple, une rotation du plan euclidien d'angle θ = 0 mod π a un polynôme caractéristique non scindé donc n'est pas trigonalisable.

## BXDCCTD1D4D0CTD7

1. Soit A ∈ M 2 ( I K ) ayant une valeur propre double λ . Deux cas se présentent :
2. (a) A est diagonalisable et, d'après l'exemple 1 de la page 88, on a A = λI 2 .
3. (b) A n'est pas diagonalisable et le sous-espace propre pour la valeur propre λ est alors de dimension 1.

̸

Soit u un vecteur propre associé à cette valeur propre qu'on complète en une base ( u, v ) de I K 2 . Si P est la matrice de passage de la base canonique de I K 2 à cette base, on a P -1 AP = ( λ α 0 β ) , avec α = 0, car A n'est pas diagonalisable. Comme λ est la seule valeur propre de A , on a β = λ .

En prenant comme base (

αu, v

)

à la place de

(

u, v

), on remarque que

A

est

2. Soit A ∈ M 3 ( I K ) ayant une valeur propre simple λ et une valeur propre double μ . Supposons A non diagonalisable, c'est-à-dire dim E μ ( A ) = 1.

$$\text {En prenant comme base (alpha)} \\ \text {sembble à } \left ( \begin{array} { c c } \lambda & 1 \\ 0 & \lambda \end{array} \right ) . \\ \text {Soit A en } \mathcal { M } _ { 3 } ( \| K ) \text { avant une valeur}$$

Soit u un vecteur propre de A pour la valeur propre λ et v un vecteur propre de A pour la valeur propre μ . Complétons ( u, v ) en une base ( u, v, w ) de I K 3 et notons P la matrice de passage de la base canonique de I K 3 à cette base.

On peut encore faire mieux comme le montre l'exercice suivant.

$$\text {notons } P \ a \ m a t r i c e \, d \text { passage de la base canonique de } & \, I K ^ { 3 } \ \hat { a } \, \text { cette base.} \\ & \text {On a } P ^ { - 1 } A P = \left ( \begin{array} { c c c } \lambda & 0 & \alpha \\ 0 & \mu & \beta \\ 0 & 0 & \gamma \end{array} \right ) \, \text {et} \, \text {Tr} \, ( A ) = \lambda + 2 \mu \, \text {domne } \gamma = \mu . \\ \text {On peut encore faire mieux comme le montre l'exercice suivant.}$$

Exercice 26 Soit A ∈ M 3 ( I K ) ayant une valeur propre simple λ et une valeur propre double μ . On suppose A non diagonalisable, c'est-à-dire que dim E μ ( A ) = 1.

$$d o b l u & \quad . \text {On suppose } A \text { non diagonalisable, } c ^ { \text {est-a-dire que dim } E _ { \mu } ( A ) = 1 } . \\ & \text {Montrer qu'il existe } P \in \mathcal { G } _ { 3 } ( \mathbb { K } ) \text { tel que } P ^ { - 1 } A P = \left ( \begin{array} { c c c } \lambda & 0 & 0 \\ 0 & \mu & 1 \\ 0 & 0 & \mu \end{array} \right ) . \\ & \text {Indication } \quad \text {on pourra modifier le trioisème vecteur d'une base de trigonalisation}$$

D2CSCXCRCPD8CXD3D2 BM on pourra modifier le troisième vecteur d'une base de trigonalisation.

$$\underline { p } . 1 1 9 \, \text { } \, \text {Exercise 27. Sort } A = \left ( \begin{array} { c c c c } 0 & 3 & 3 \\ - 1 & 8 & 6 \\ 2 & - 1 4 & - 1 0 \end{array} \right ) . \\ 1 . \, \text {La matrice } A \, \text {est-elle diagonalisable?}$$

1. La matrice A est-elle diagonalisable?
2. Montrer que A est trigonalisable et déterminer P ∈ GL 3 ( I K ) et T triangulaire supérieure telles que A = PTP -1 .

BG

✞

✝

☎

✆

<!-- image -->

## Exercice 28

1. La matrice A = ⎛ ⎝ 14 18 18 -6 -7 -9 -2 -3 -1 ⎞ ⎠ est-elle diagonalisable ? trigonalisable ?
2. Montrer que la matrice A est semblable à la matrice ⎛ ⎝ 2 0 0 0 2 1 0 0 2 ⎞ ⎠

## Corollaire 51

Soit u est un endomorphisme trigonalisable.

- Si ( μ 1 , . . . , μ n ) est une liste de valeurs propres de u , on a :

$$\text {Tr} \, u = \sum _ { i = 1 } ^ { n } \mu _ { i } \, \ e t \, \det u = \prod _ { i = 1 } ^ { n } \mu _ { i } . \\$$

- Si sp ( u ) = { λ 1 , . . . , λ p } , on a alors :

$$T r \, u = \sum _ { i = 1 } ^ { p } m \left ( \lambda _ { i } \right ) \lambda _ { i } \ \det \ d e t \, u = \prod _ { i = 1 } ^ { p } \lambda _ { i } ^ { m ( \lambda _ { i } ) } .$$

## Démonstration.

C'est une conséquence immédiate de la proposition 36 et du théorème 48 de la page 93.

CACTD1CPD6D5D9CT Recherche de la valeur propre de plus grand module.

Soit A ∈ M n ( C ) dont les valeurs propres λ 1 , . . . , λ p , de multiplicités respectives m ( λ 1 ) , . . . , m ( λ p ), vérifient :

$$| \lambda _ { 1 } | > | \lambda _ { 2 } | \geqslant \cdots \geqslant | \lambda _ { p } | .$$

Ainsi λ 1 est l'unique valeur propre de module maximal.

$$\lambda _ { 1 } = \lim _ { k \to + \infty } \frac { \text {Tr} \left ( A ^ { k + 1 } \right ) } { \text {Tr} \left ( A ^ { k } \right ) } .$$

Pour tout entier k , on a Tr ( A k ) = p ∑ i =1 m ( λ i ) λ k i ∼ k → + ∞ m ( λ 1 ) λ k 1 donc :

On a déjà prouvé qu'un endomorphisme (respectivement une matrice) est trigonalisable si, et seulement si, son polynôme caractéristique est scindé.

L'exercice suivant prouve qu'un endomorphisme (respectivement une matrice) est trigonalisable si, et seulement s'il possède un polynôme annulateur scindé.

BH

✞

✝

✞

✝

☎

✆

<!-- image -->

Exercice 29 (Approfondissement)

On veut montrer qu'un endomorphisme est trigonalisable si, et seulement s'il est annulé par un polynôme scindé.

1. Montrer par récurrence sur la dimension de E que si un endomorphisme u de E est annulé par un polynôme scindé, alors il est trigonalisable.
2. Montrer que si u est un endomorphisme trigonalisable de E , alors χ u annule u .
3. Conclure.

CACTD1CPD6D5D9CT En fait, pour tout endomorphisme u , on a χ u ( u ) = 0. Il s'agit du théorème de Cayley-Hamilton qui sera démontré dans la section suivante.

## CE CDD8CXD0CXD7CPD8CXD3D2D7 CSCTD7 D4D3D0DDD2 CM D3D1CTD7 CPD2D2D9D0CPD8CTD9D6D7 BD D3D0DDD2 CM D3D1CT D1CXD2CXD1CPD0

## Proposition 52

Soit u ∈ L ( E ). L'ensemble des polynômes P tels que P ( u ) = 0 est un idéal appelé idéal annulateur de u .

## Corollaire 53

Soit A ∈ M n ( I K ). L'ensemble des polynômes P tels que P ( A ) = 0 est un idéal appelé idéal annulateur de A .

CACTD1CPD6D5D9CT Comme le montre l'exercice suivant, il peut arriver, en dimension infinie, que l'idéal annulateur soit réduit au polynôme nul.

Nous verrons dans la section suivante que c'est impossible en dimension finie.

☎

✆

<!-- image -->

1. Soit λ ∈ I R et P ∈ I R [ X ] . Calculer P ( D ) ( e λ ). 2. En déduire l'idéal annulateur de D .

Exercice 30 On note D la dérivation de C ∞ ( I R ) et, pour tout λ ∈ I R , e λ la fonction définie sur I R par : ∀ t ∈ I R e λ ( t ) = exp ( λt ).

## Proposition 54

1. Si E de dimension finie, alors l'idéal annulateur de tout endomorphisme de E est non réduit à { 0 } .
2. L'idéal annulateur de A ∈ M n ( I K ) n'est pas réduit à { 0 } .

✞ Démonstration page 122

☎

✆

BI

✝

✞

✝

<!-- image -->

✞

✝

☎

✆

☎

✆

CACTD1CPD6D5D9CT D'après le théorème 21 de la page 16, si I est un idéal de I K [ X ] non réduit au polynôme nul, alors il existe un unique polynôme unitaire P , appelé générateur unitaire de I , tel que I = P I K [ X ].

## Définition 14

Soit E de dimension finie et u ∈ L ( E ). Le générateur unitaire de l'idéal annulateur de u est appelé polynôme minimal de u ; on le note π u .

On a la même définition pour A ∈ M n ( I K ).

Dans la suite on supposera E de dimension finie non nulle, ce qui assure l'existence d'un polynôme minimal pour tout u ∈ L ( E ) .

## CACTD1CPD6D5D9CTD7

- Comme dim E = 0, on a deg ( π u ) ⩾ 1, car si P = λ , avec λ ∈ I K ∗ , on a P ( u ) = λ Id E = 0.

̸

̸

- Le polynôme minimal π u est de degré 1 si, et seulement si, u est une homothétie.

En effet, si u = λ Id alors π u divise X -λ . Comme π u est unitaire et de degré supérieur ou égal à 1, on en déduit que π u = X -λ .

Réciproquement, si π u = X -λ , alors 0 = π ( u ) = u -λ Id donc u = λ Id.

## Exercice 31

1. Déterminer le polynôme minimal d'un projecteur p de E .
2. Déterminer le polynôme minimal d'une symétrie s de E .

<!-- image -->

Exercice 32 Montrer que l'ensemble des racines du polynôme minimal π u est égal au spectre de u .

## Proposition 55

On a le même résultat pour A ∈ M n ( I K

```
Si d = deg( π u ), alors la famille ( u k ) 0 ⩽ k ⩽ d -1 est une base de I K [ u ] et l'on a donc dim ( I K [ u ] ) = deg ( π u ). ).
```

## Principe de démonstration.

On utilise la division euclidienne par le polynôme minimal π u .

✞

✝

Démonstration page 123

☎

✆

BJ

✞

✝

## Point méthode

La démonstration de la proposition précédente fournit une méthode pratique de décomposition de v ∈ I K [ u ] dans la base ( u k ) k ∈ [ [0 ,d -1] ] de I K [ u ] :

si v = P ( u ), avec P ∈ I K [ X ] , on détermine le reste de la division euclidienne de P par le polynôme minimal de u .

Ainsi, pour calculer les puissances successives de u , on détermine le reste de la division euclidienne de X p , avec p ∈ I N , par le polynôme minimal de u .

## BE CCCW AJ CTD3D6 AI CTD1CT CSCT BVCPDDD0CTDDB9 CPD1CXD0D8D3D2

On a vu l'intérêt d'obtenir des polynômes annulateurs dans la recherche de valeurs propres d'un endomorphisme et l'on a prouvé leur existence en dimension finie.

Le théorème de Cayley-Hamilton affirme que le polynôme caractéristique d'un endomorphisme u est un polynôme annulateur de u .

La démonstration de ce théorème n'est pas exigible.

Nous proposons ici une démonstration en plusieurs étapes s'appuyant sur les matrices compagnons, notion hors-programme mais qui fait l'objet de nombreux sujets de concours.

☎

✆

<!-- image -->

## Exercice 33 Polynôme minimal d'une matrice compagnon

$$S o i t \ ( a _ { 0 } , \dots , a _ { p - 1 } ) \in \mathbb { K } ^ { p } \ e t$$

On note ( E 0 , . . . , E p -1 ) la base canonique de M p, 1 ( I K ) et l'on pose :

$$\_ - 1 ) \in \mathbb { K } ^ { p } \ e t \\ A = \begin{pmatrix} 0 & 0 & \dots & \dots & 0 & - a _ { 0 } \\ 1 & 0 & \dots & \dots & 0 & - a _ { 1 } \\ 0 & 1 & \ddots & & & \\ \vdots & \vdots & \ddots & \ddots & \vdots & \vdots \\ 0 & 0 & \dots & 1 & 0 & - a _ { p - 2 } \\ 0 & 0 & \dots & 0 & 1 & - a _ { p - 1 } \end{pmatrix} .$$

$$P ( X ) = X ^ { p } + a _ { p - 1 } X ^ { p - 1 } + \cdots a _ { 1 } X + a _ { 0 } . \\$$

1. Calculer A k E 0 , pour k ∈ [ [0 , p -1] ] . En déduire que deg ( π A ) ⩾ p .
2. Calculer AE p -1 , puis P ( A ) E 0 . En déduire que π A = P .

CACTD1CPD6D5D9CT Combiné avec l'exercice 17 de la page 81, ce résultat prouve que si A est une matrice compagnon, alors π A = χ A .

BL

BK

✞

✝

✞ p.124

✝

<!-- image -->

☎

✆

<!-- image -->

Exercice 34 Soit u ∈ L ( E ) et x un vecteur non nul de E .

1. Montrer qu'il existe un plus petit sous-espace vectoriel de E , noté F x , stable par u et contenant x .
2. Prouver que, si F x est de dimension p , alors ( x, u ( x ) , . . . , u p -1 ( x ) ) est une base de F x .

## Théorème 56 (Théorème de Cayley-Hamilton)

Soit u ∈ L ( E ) avec E de dimension finie.

Le polynôme caractéristique de u ∈ annule u , c'est-à-dire χ u ( u ) = 0.

Principe de démonstration. On utilise le lemme précédent, puis les exercices 17 de la page 81 et 33 de la page précédente sur les matrices compagnons. ✞

✝

☎

✆

Démonstration (non exigible) page 124

BTD8D8CTD2D8CXD3D2 Comme il fait intervenir le polynôme caractéristique de u ∈ L ( E ), le théorème de Cayley-Hamilton n'a de sens que si E est de dimension fi nie .

## Corollaire 57 (Théorème de Cayley-Hamilton)

Si A ∈ M n ( I K ), alors χ A ( A ) = 0.

$$( \underline { p } . 1 2 4 ) \, \ E x c i e { 3 } { 5 } \, \ On \, \text {repend la matrice } A = \left ( \begin{array} { c c c } 3 & 5 & - 6 \\ 4 & 7 & - 9 \\ 3 & 6 & - 7 \end{array} \right ) \, \, d \, \text {le} \, \text {example} \, \, p g e 7 . \\ \, \ \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \, \,$$

☎

✆

Montrer que A est inversible et calculer A -1 en fonction de I 3 , A et A 2 .

## BF CTD1D1CT CSCT CS AJ CTCRD3D1D4D3D7CXD8CXD3D2 CSCTD7 D2D3DDCPD9DC

Théorème 58 (Lemme de décomposition des noyaux)

Soit u ∈ L ( E ), ( P 1 , . . . , P r ) ∈ I K [ X ] r une famille finie de polynômes deux à deux premiers entre eux et P = P 1 . . . P r leur produit.

On a alors la décomposition en somme directe :

$$K e r \, P \left ( u \right ) = \bigoplus _ { k = 1 } ^ { r } K e r \, P _ { k } \left ( u \right ) .$$

Principe de démonstration. On utilise la relation de Bézout pour n = 2 puis on procède par récurrence sur r . ✞ ✝ Démonstration page 125

☎

✆

BLBL

✞

✝

BVCWCPD4CXD8D6CT BE BA CA AJ CTCSD9CRD8CXD3D2 CSCTD7 CTD2CSD3D1D3D6D4CWCXD7D1CTD7

Corollaire 59

Soit ( P 1 , . . . , P r ) ∈ I K [ X ] r une famille finie de polynômes deux à deux premiers entre eux, P leur produit et u ∈ L ( E ).

Si P est un polynôme annulateur de u , on a alors :

$$E = \bigoplus _ { k = 1 } ^ { r } K e r \, P _ { k } \left ( u \right ) .$$

## CACTD1CPD6D5D9CT

On retrouve le fait que si p est un projecteur alors Ker p et Ker( p -Id) sont supplémentaires et que, si p est une symétrie alors Ker( s -Id) et Ker( s +Id) sont supplémentaires.

☎

✆

<!-- image -->

Exercice 36 Soit ( P 1 , . . . , P r ) ∈ I K [ X ] r une famille de polynômes deux à deux premiers entre eux et P leur produit. On suppose que P ( u ) = 0.

Montrer que les projecteurs associés à la décomposition en somme directe :

$$E = \bigoplus _ { k = 1 } ^ { r } K e r \, P _ { k } ( u ) .$$

sont des polynômes en u .

## BXDCCTD1D4D0CTD7

1. Soit ( a, b ) ∈ I K 2 . L'ensemble S des suites u telles que :

$$\forall n \in \mathbb { N } \ \ u _ { n + 2 } = a u _ { n + 1 } + b u _ { n }$$

est le noyau de l'endomorphisme Q ( T ), avec :

$$Q = X ^ { 2 } - a X - b \ \ e t \ \ T \ \colon \ \mathbb { K } ^ { \mathbb { N } } \ \longrightarrow \ \mathbb { K } ^ { \mathbb { N } } \\ u \ \longmapsto \ ( u _ { n + 1 } ) _ { n \in \mathbb { N } } . \\$$

Si le polynôme Q a deux racines distinctes λ 1 et λ 2 , alors le lemme des noyaux donne :

$$& \text {dome} \colon \\ & \quad S = \text {Ker} ( T - \lambda _ { 1 } \text {Id} ) \oplus \text {Ker} ( T - \lambda _ { 2 } \text {Id} ) = \{ ( A \lambda _ { 1 } ^ { n } + B \lambda _ { 2 } ^ { n } ) _ { n \in \mathbb { N } } \, , \, ( A , B ) \in \mathbb { K } ^ { 2 } \} \, . \\ & \text {On retrove ainsi le résultat obtenu en premieri année} .$$

2. Soit ( a, b ) ∈ I K 2 . Considérons l'ensemble S des fonctions f deux fois dérivables sur I R telles que f ′′ = af ′ + bf . Il est aisé de montrer que tout élément de S est de classe C ∞ sur I R . Ainsi, S est le noyau de l'endomorphisme Q ( D ), avec :

$$Q = X ^ { 2 } - a X - b \ e t \ D \ \colon \ \mathcal { C } ^ { \infty } ( \mathbb { R } , \mathbb { K } ) \ \longrightarrow \ \mathcal { C } ^ { \infty } ( \mathbb { R } , \mathbb { K } ) \ .$$

BCBC

✞

✝

Démonstration page 125

☎

✆

Si le polynôme Q a deux racines distinctes λ 1 et λ 2 , alors le lemme des noyaux donne :

$$\mathcal { S } & = K e r ( D - \lambda _ { 1 } \text {Id} ) \oplus K e r ( D - \lambda _ { 2 } \text {Id} ) \\ & = \{ x \mapsto A e ^ { \lambda _ { 1 } x } + B e ^ { \lambda _ { 2 } x } \colon ( A , B ) \in \mathbb { K } ^ { 2 } \} . \\ \text {done le résultat obtenu en premier année.}$$

On retrouve donc le résultat obtenu en première année.

Nous allons généraliser ces deux résultats.

## BTD4D4D0CXCRCPD8CXD3D2 CPD9DC AJ CTD5D9CPD8CXD3D2D7 CSCXAB AJ CTD6CTD2D8CXCTD0D0CTD7 D0CXD2 AJ CTCPCXD6CTD7 AI CP CRD3CTÆCRCXCTD2D8D7 CRD3D2D7D8CPD2D8D7

Soit l'équation différentielle linéaire à coefficients constants d'ordre p :

$$f ^ { ( p ) } + \alpha _ { p - 1 } f ^ { ( p - 1 ) } + \dots + \alpha _ { 1 } f ^ { \prime } + \alpha _ { 0 } f = 0 \\ \alpha _ { 0 } \, \cdot \, \underset { \infty } { \subset } \P P ^ { p } \, d i v o n p n u _ { 0 } \, f \subset \mathcal { C } ^ { \infty } \left ( \mathbb { R } \, \P \, \Gamma \right )$$

On appelle polynôme caractéristique de (ED) le polynôme :

où ( α 0 , . . . , α p -1 ) ∈ C p d'inconnue f ∈ C ∞ ( I R , C ) .

$$C ( X ) = X ^ { p } + \sum _ { k = 0 } ^ { p - 1 } \alpha _ { k } X ^ { k } . \\$$

deux à deux distincts et les p k &gt; 0).

Sa factorisation dans C [ X ] sera notée C ( X ) = r ∏ k =1 ( X -λ k ) p k (les λ k sont

Si D désigne l'endomorphisme de dérivation de E = C ∞ ( I R , C ), l'ensemble S des solutions de (ED) est le noyau de l'endomorphisme C ( D ) . Le lemme des noyaux nous fournit alors la décomposition en somme directe :

$$\mathcal { S } = \bigoplus _ { k = 1 } ^ { r } K e r \left ( D - \lambda _ { k } \, I d _ { E } \right ) ^ { p _ { k } } . \\ \lambda _ { \ } o n n o t e _ { \ } e _ { \ } l a f o n c t i o n _ { \ } r } \mapsto e _ { \ } l a x$$

On prouve alors par récurrence sur p la relation suivante :

Pour tout complexe λ , on note e λ , la fonction x ↦→ e λx .

$$( D - \lambda _ { k } \, I d _ { E } ) ^ { p } \left ( f \times e _ { \lambda _ { k } } \right ) & = e _ { \lambda _ { k } } \times D ^ { p } ( f ) \\ f ) \in \mathbb { [ } 1 _ { \ } r ] \times \mathcal { \circ } ^ { \infty } \left ( \mathbb { R } \ \P \right ) \ O n \ o n \ d \mathring { o } d u i t \ \cdot$$

$$\text {tour} \ ( k , f ) \in [ 1 , r ] \times \mathcal { C } ^ { \infty } \left ( \mathbb { R } , \mathbb { C } \right ) . \ \text {On en deduit } \colon \\ \text {Ker} \left ( D - \lambda _ { k } \, \text {Id} _ { E } \right ) ^ { p _ { k } } = \left \{ x \mapsto P ( x ) e ^ { \lambda _ { k } x } \, ; \, P \in \mathbb { C } _ { p _ { k } - 1 } [ X ] \right \} . \\ \text {Ainsi, tout équipe} \ f \, \text {de } \mathcal { S } \ s ^ { \prime } \text {crit sous la forme} \colon$$

pour tout ( k, f ) ∈ [ [1 , r ] ] ×C ∞ ( I R , C ) . On en déduit :

Ainsi, tout élément f de S s'écrit sous la forme :

pour une unique famille ( P k ) ∈ r ∏ k =1 C p k -1 [ X ] et l'espace S est de dimension p.

$$f ( x ) = \sum _ { k = 1 } ^ { r } P _ { k } ( x ) e ^ { \lambda _ { k } x } \\ ( D _ { 0 } ) _ { 0 } = \sum _ { k = 1 } ^ { r } P _ { k } ( x ) e ^ { \lambda _ { k } x }$$

Lorsque p = 1 ou 2, ce dernier point est également une conséquence du théorème de Cauchy sur les équations linéaires à coefficients constants d'ordre 1 ou 2.

BCBD

## BTD4D4D0CXCRCPD8CXD3D2 CPD9DC D7D9CXD8CTD7 D6 AJ CTCRD9D6D6CTD2D8CTD7 D0CXD2 AJ CTCPCXD6CTD7 AI CP CRD3CTÆCRCXCTD2D8D7 CRD3D2D7D8CPD2D8D7

Soit l'équation récurrente linéaire à coefficients constants d'ordre p :

$$\forall n \in \mathbb { N } \ \ u _ { n + p } + \alpha _ { p - 1 } u _ { n + p - 1 } + \cdots + \alpha _ { 1 } u _ { n + 1 } + \alpha _ { 0 } u _ { n } = 0 \\ \\$$

avec ( ) C p , avec = 0, d'inconnue = C I N .

α 0 , . . . , α p -1 ∈ α 0 u ∈ E On appelle polynôme caractéristique de (ER) le polynôme :

̸

$$C ( X ) = X ^ { p } + \sum _ { k = 0 } ^ { p - 1 } \alpha _ { k } X ^ { k } . \\$$

Sa factorisation dans C sera notée :

$$C ( X ) = \prod _ { k = 1 } ^ { r } \left ( X - \lambda _ { k } \right ) ^ { p _ { k } } \\ \text {div} \text {ints} \ e t \, \lfloor e s \ p _ { k } \ f r a t h s c r { D } \rfloor$$

(les λ k sont deux à deux distincts et les p k &gt; 0) .

Désignons alors par T l'endomorphisme de translation de L ( C I N ) défini par :

L'ensemble S des solutions de (ER) est le noyau de l'endomorphisme C ( T ). Comme une suite de S est déterminée par ses p premiers termes, l'application :

$$T \left ( ( u _ { n } ) _ { n \in \mathbb { N } } \right ) & = ( u _ { n + 1 } ) _ { n \in \mathbb { N } } \, . \\ \intertext { l u t i o n s d e ( E R ) e s t l e n o y a u d l e n } \mathcal { C } _ { n } + 1 \prec _ { n } \cdot \hat { \cdot } _ { n } & = 0 .$$

$$\begin{array} { r l r } { \mathcal { S } } & { \longrightarrow } & { \mathbb { K } ^ { p } } \\ { u } & { \longmapsto } & { ( u _ { 0 } , \dots , u _ { p - 1 } ) } \\ { t } & { l o d i m o n s i o n d o s t \, \mathcal { G } a s t o } \end{array}$$

est un isomorphisme et la dimension de S est égale à p. De plus, le lemme des noyaux nous fournit la décomposition en somme directe :

$$\mathcal { S } & = \bigoplus _ { k = 1 } ^ { r } K e r \left ( T - \lambda _ { k } \, I d _ { E } \right ) ^ { p _ { k } } . \\ \intertext { d e d t e r m i n e r p o u r t o u t k l e n o w a u }$$

- Si λ k = 0 , il s'agit du noyau de T p k . C'est évidemment l'espace vectoriel de suites u telle que u n = 0 pour tout n ⩾ p k . On retrouve le fait qu'il est de dimension p k .

Il s'agit maintenant de déterminer pour tout k, le noyau de ( T -λ k Id E ) p k . Nous venons de voir que cet espace est de dimension p k puisque l'équation ( T -λ k Id E ) p k ( u ) = 0 est une relation de récurrence linéaire d'ordre p k .

̸

- Supposons λ k = 0 . Pour tout polynôme P ∈ I K [ X ] , un simple calcul montre que la suite image de ( λ n k P ( n ) ) n ∈ I N par T -λ k Id E est :

où Q ( X ) est le polynôme P ( X +1) -P ( X ) . Le degré de Q étant inférieur ou égal à deg P -1 , on voit par itération que Ker ( T -λ k Id E ) p k contient l'ensemble :

BCBE

$$Q ( x _ { k } ^ { n + 1 } Q ( n ) ) _ { n \in \mathbb { N } } \\ P ( X + 1 ) - P ( X ) . \ L e$$

$$\left \{ ( \lambda _ { k } ^ { n } P ( n ) ) _ { n \in \mathbb { N } } \, ; \, P \in \mathbb { K } _ { p _ { k } - 1 } [ X ] \right \} .$$

Comme d'un autre côté, c'est un sous-espace vectoriel de dimension p k puisqu'il est l'image de I K p k -1 [ X ] par l'application linéaire injective P ↦→ ( λ n k P ( n ) ) n ∈ I N (l'injectivité découlant du fait qu'un polynôme ayant une infinité de racines est nul), il vient :

puisque le noyau de ( T -λ k Id E ) p k est aussi de dimension p k .

$$\text {une infinite de raccines est null} , \, \text {il vient} \colon \\ \text {Ker} \left ( T - \lambda _ { k } \, \text {Id} _ { E } \right ) ^ { p _ { k } } & = \left \{ ( \lambda _ { k } ^ { n } P ( n ) ) _ { n \in \mathbb { N } } \, ; \, P \in \mathbb { K } _ { p _ { k } - 1 } [ X ] \right \} \\ \text {puisque le noyau de } \left ( T - \lambda _ { k } \, \text {Id} _ { E } \right ) ^ { p _ { k } } \, \text {est aussi de dimension } p _ { k } .$$

̸

Comme α 0 = 0 , tous les λ k sont non nuls donc toute solution u de (ER) s'écrit :

pour une unique famille ( Q k ) ∈ r ∏ k =1 I K p k -1 [ X ].

$$\forall n \in \mathbb { N } \ \ u _ { n } = \sum _ { k = 1 } ^ { r } \lambda _ { k } ^ { n } Q _ { k } ( n ) \\ \intertext { \forall n \in \mathbb { N } \ \ u _ { n } = \sum _ { k = 1 } ^ { r } \lambda _ { k } ^ { n } Q _ { k } ( n ) }$$

On retrouve le fait que l'espace S est de dimension p.

## BG D3D0DDD2 CM D3D1CTD7 CPD2D2D9D0CPD8CTD9D6D7 CTD8 CSCXCPCVD3D2CPD0CXD7CPCQCXD0CXD8 AJ CT

On a déjà prouvé que si le polynôme caractéristique d'un endomorphisme (respectivement d'une matrice) est scindé à racines simples, alors l'endomorphisme (respectivement la matrice) est diagonalisable mais qu'il ne s'agit que d'une condition suffisante .

Le théorème suivant prolonge ce résultat et donne une condition nécessaire et suffisante pour être diagonalisable.

## Théorème 60

Les propriétés suivantes sont équivalentes :

- ( i ) u est diagonalisable ;
- ( ii ) u possède un polynôme annulateur scindé à racines simples ;
- ( iii ) le polynôme minimal de u est scindé à racines simples.

On a le même résultat pour A ∈ M n ( I K ).

## Principe de démonstration.

✞ Démonstration page 126

☎

✆

✝

- Pour prouver ( iii ) = ⇒ ( i ) , on utilise le lemme de décomposition des noyaux.
- Pour prouver ( i ) = ⇒ ( ii ) , on utilise la décomposition en somme directe E = p ⊕ i =1 E λ i ( u ) , où sp ( u ) = { λ 1 , . . . , λ p } , puis la proposition 18 de la page 76.

CACTD1CPD6D5D9CT L'exercice 29 de la page 96 permet d'énoncer un résultat similaire pour les endomorphismes trigonalisables.

Les propriétés suivantes sont équivalentes :

- ( i ) u est trigonalisable ;
- ( ii ) u possède un polynôme annulateur scindé ;
- ( iii ) le polynôme minimal de u est scindé.

BCBF

✞

✝

## Corollaire 61

Soit u ∈ L ( E ) diagonalisable et F un sous-espace vectoriel de E stable par u . L'endomorphisme induit par u sur F est alors diagonalisable.

✞ Démonstration page 127

☎

✝ ✆ On dit qu'une famille ( u i ) i ∈ I d'endomorphismes de E est simultanément diagonalisable s'il existe une base B de E dans laquelle les matrices des u i sont diagonales.

Une telle base s'appelle alors une base de diagonalisation simultanée.

☎

✆

<!-- image -->

Exercice 37 Montrer qu'une famille d'endomorphismes de E est simultanément diagonalisable si, et seulement si, elle est composée d'endomorphismes diagonalisables commutant deux à deux.

CACTD1CPD6D5D9CT En adaptant cet exercice et en utilisant l'exercice 25 de la page 93, on obtient qu'une famille d'endomorphismes de E trigonalisables commutant deux à deux est simultanément trigonalisable.

## BH BXD2CSD3D1D3D6D4CWCXD7D1CTD7 D2CXD0D4D3D8CTD2D8D7B8 D1CPD8D6CXCRCTD7 D2CXD0D4D3D8CTD2D8CTD7

On s'intéresse dans cette section aux endomorphismes annulés par un monôme c'est-à-dire par un polynôme de la forme X k .

## Définition 15

On dit que u ∈ L ( E ) est nilpotent s'il existe un entier k tel que u k = 0 .

Le plus petit entier r tel que u r = 0 s'appelle l' indice de nilpotence de u .

## CACTD1CPD6D5D9CTD7

- L'indice de nilpotence d'un endomorphisme u nilpotent est bien défini car l'ensemble des entiers k tels que u k = 0 est une partie de I N non vide, elle admet donc un plus petit élément.
- Comme u 0 = Id, l'indice de nilpotence est un entier non nul.
- L'endomorphisme de nilpotence est égal à 1 si, et seulement si, l'endomorphisme est nul.

̸

- Un endomorphisme nilpotent est non injectif. En effet, si u est nilpotent d'indice r , alors u r -1 = 0 donc il existe un vecteur x tel que u r -1 ( x ) soit un vecteur non nul de Ker u .
- La seule valeur propre d'un endomorphisme nilpotent est nulle. En effet, d'après le point précédent, 0 est valeur propre et, grâce à la proposition 20 de la page 76, c'est la seule.

## Définition 16

Ondit que A ∈ M n ( I K ) est nilpotente s'il existe un entier k tel que A k = 0 . Le plus petit entier r tel que A r = 0 s'appelle l' indice de nilpotence de A .

BCBG

## CACTD1CPD6D5D9CTD7

- Une matrice A est nilpotente si, et seulement si, son endomorphisme canoniquement associé est nilpotent.

De même, si une matrice représente un endomorphisme, alors elle est nilpotente si, et seulement si, cet endomorphisme l'est.

Les propriétés énoncées sur les endomorphismes nilpotents sont donc transposables aux matrices nilpotentes.

- Toute matrice semblable à une matrice nilpotente est donc nilpotente.

On suppose désormais que E est un espace vectoriel de dimension finie n (non nulle car E = { 0 } .)

## Proposition 62

Les trois points suivants sont équivalents :

- ( i ) u est nilpotent,
- ( ii ) le polynôme caractéristique de u est X n ,
- ( iii ) il existe une base de E dans laquelle la matrice de u est triangulaire supérieure stricte.

✞

✝

Démonstration page 127

☎

✆

̸

## Corollaire 63

Soit A ∈ M n ( I K ). Les trois points suivants sont équivalents :

- ( i ) A est nilpotente,
- ( ii ) le polynôme caractéristique de A est X n ,
- ( iii ) A est semblable à une matrice triangulaire supérieure stricte.

## Corollaire 64

Soit A ∈ M n ( I K ). Il y a équivalence entre :

- ( i ) A est nilpotente,
- ( ii ) A est trigonalisable avec pour seule valeur propre 0.

## Corollaire 65

Soit u un endomorphisme de E . Il y a équivalence entre :

- ( i ) u est nilpotent,
- ( ii ) u est trigonalisable avec pour seule valeur propre 0.

✞

✝

<!-- image -->

✞

✝

☎

✆

☎

✆

<!-- image -->

✞

✝

☎

✆

## BVCWCPD4CXD8D6CT BE BA CA AJ CTCSD9CRD8CXD3D2 CSCTD7 CTD2CSD3D1D3D6D4CWCXD7D1CTD7

## Corollaire 66

Soit u un endomorphisme nilpotent.

Son indice de nilpotence est majoré par la dimension de E .

Démonstration. En effet, son polynôme caractéristique est X n et il est annulateur d'après le théorème de Cayley-Hamilton.

## Corollaire 67

Soit A ∈ M n ( I K ). Si A est nilpotente, alors A n = 0.

Exercice 38 Soit u un endomorphisme nilpotent d'indice r et x 0 ̸∈ Ker u r -1 . Montrer que la famille ( x 0 , u ( x 0 ) , . . . , u r -1 ( x 0 )) est libre.

Exercice 39 Soit u un endomorphisme d'un espace vectoriel E de dimension finie n nilpotent et d'indice n .

̸

1. Soit x 0 tel que u n -1 ( x 0 ) = 0 . Montrer que ( u k ( x 0 ) ) 0 ⩽ k&lt;n est une base de E. 2. Montrer que, pour tout k de [ [0 , n ] ] , le sous-espace Ker u k est de dimension k.
3. Montrer que, pour tout k de [ [0 , n ] ] , Ker u k est le seul sous-espace stable de dimension k stable par u.

<!-- image -->

## Théorème 68

Lorsqu'il existe un polynôme scindé annulant u , c'est-à-dire lorsque le polynôme minimal de u est scindé, alors E peut se décomposer en une somme directe de sous-espaces stables par u sur chacun desquels u induit la somme d'une homothétie et d'un endomorphisme nilpotent.

✞ Démonstration page 129

☎

✆

✝ CACTD1CPD6D5D9CT Matriciellement, si l'on prend une base adaptée à une telle décomposition, on obtient une matrice de la forme :

$$\begin{matrix} \text {composition, on obtient une matrice de la forme} \colon \\ \left ( \begin{array} { c c c } \lambda _ { 1 } I _ { n _ { 1 } } + N _ { 1 } & ( 0 ) \\ & \ddots & \\ ( 0 ) & \lambda _ { p } I _ { n _ { p } } + N _ { p } \\ \end{array} \right ) & o u \ N _ { 1 } , \dots , N _ { p } \ s o n \ n i l p o tentes . \\ \text {On peut même trigonoidal chaque matrice nilpotente } N _ { k } \, d e f acon \, \hat { a } \, c e \, \text {que}$$

On peut même trigonaliser chaque matrice nilpotente N k de façon à ce que chaque bloc diagonal soit triangulaire supérieur.

On obtient ainsi une forme triangulaire particulière que l'on a, par exemple, obtenue dans l'exercice 26 de la page 94.

BCBI

Exercice 40 Montrer que pour toute famille ( u 1 , . . . , u n ) de n endomorphismes nilpotents, commutant deux à deux, d'un espace vectoriel E de dimension n, on a :

$$u _ { 1 } \circ \dots \circ u _ { n } = 0 .$$

## BWAJ CTD1D3D2D7D8D6CPD8CXD3D2D7 CTD8 D7D3D0D9D8CXD3D2D7 CSCTD7 CTDCCTD6CRCXCRCTD7 CSD9 CRD3D9D6D7

## Exercice 1

1. Par hypothèse, pour tout x ∈ E , il existe un scalaire λ x tel que u ( x ) = λ x x . Si le vecteur x est non nul, alors le scalaire λ x est unique, sinon tous les scalaires λ conviennent.

Soit x et y deux vecteurs non nuls de E . Montrons que λ x = λ y .

- Si x est proportionnel à y , alors il existe un scalaire μ tel que x = μy . Ainsi :

$$u ( x ) = \lambda _ { x } x = \lambda _ { x } \mu y = u \left ( \mu y \right ) = \mu \lambda _ { y } y$$

Comme le vecteur y est non nul, on en déduit que λ x μ = λ y μ . Le scalaire μ étant non nul (car x = 0), on en déduit que λ x = λ y .

- Si la famille ( x, y ) est libre, alors l'égalité :

̸

$$u ( x + y ) = \lambda _ { x + y } ( x + y ) = u ( x ) + u ( y ) = \lambda _ { x } x + \lambda _ { y } y .$$

$$\text {implicit queue } \lambda _ { x } = \lambda _ { x + y } = \lambda _ { y } .$$

Ainsi, il existe λ ∈ I K tel que pour tout x ∈ E non nul, u ( x ) = λx . Cette égalité étant trivialement vraie pour x = 0, cela prouve que u est une homothétie.

2. Il est clair qu'une homothétie stabilise tous les sous-espaces vectoriels de E .

Réciproquement, soit u un endomorphisme stabilisant toutes les sous-espaces vectoriels de E . Pour tout vecteur x non nul, I K x est stable par u donc u ( x ) ∈ I K x , ce qui implique que la famille ( x, u ( x )) est liée. On en déduit, grâce à la question précédente, que u est une homothétie.

Ainsi, les seuls endomorphismes stabilisant tous les sous-espaces vectoriels de E sont les homothéties.

## Exercice 2

1. Comme P ∈ F , avec F stable par D , on a :

$$\forall k \in [ 0 , d ] \ \ P ^ { ( k ) } = D ^ { k } \left ( P \right ) \in F .$$

2. Soit F = { 0 } un sous-espace vectoriel de I K [ X ] stable par D ; notons A l'ensemble des degrés des polynômes non nuls de F . Il s'agit donc d'une partie de I N non vide.

La famille ( P ( k ) ) 0 ⩽ k ⩽ d est libre, car échelonnée en degré ; comme c'est une famille de polynômes de I K d [ X ] comportant d +1 = dim I K d [ X ], c'en est une base. On a montré que I K d [ X ] ⊂ F .

̸

- Si A est majoré, alors A admet un plus grand élément, que l'on note d . Par suite, F ⊂ I K d [ X ] et il existe P ∈ F de degré d donc, d'après la première question, on a I K d [ X ] ⊂ F puis F = I K d [ X ].

Réciproquement, pour tout d ∈ I N , I K d [ X ] est stable par D .

- Sinon, pour tout n ∈ I N , il existe P ∈ A tel que d := deg P ⩾ n . D'après la première question, on a I K n [ X ] ⊂ I K d [ X ] ⊂ F . Comme cette inclusion est vraie pour tout n ∈ I N , on a F = I K [ X ] .

En conclusion, les sous-espaces vectoriels de I K [ X ] stables par D sont { 0 } , I K [ X ] et les I K d [ X ] , avec d ∈ I N .

BCBJ

## BVCWCPD4CXD8D6CT BE BA CA AJ CTCSD9CRD8CXD3D2 CSCTD7 CTD2CSD3D1D3D6D4CWCXD7D1CTD7

## Proposition 1

- Soit x ∈ Ker v ; on a v ( u ( x ) ) = v ◦ u ( x ) = u ◦ v ( x ) = u (0) = 0 donc u ( x ) appartient à Ker v . Ainsi, Ker v est stable par u .
- Soit y ∈ Im v ; il existe x ∈ E tel que y = v ( x ) . Par suite u ( y ) = u ◦ v ( x ) = v ◦ u ( x ) = v ( u ( x )) ∈ Im v ; donc Im v est stable par u .

## Proposition 2

- Supposons F stable par u . Pour tout i ∈ I , comme e i ∈ F et F est stable par u , on a u ( e i ) ∈ F .
- Réciproquement, supposons que, pour tout i ∈ I , u ( e i ) ∈ F et montrons que F est stable par u . Soit x ∈ F , il existe une famille de scalaires presque nulle, ( λ i ) i ∈ I , telle que x = ∑ i ∈ I λ i e i . Par linéarité de u , on a u ( x ) = ∑ i ∈ I λ i u ( e i ) donc u ( x ) ∈ F . Par suite, F est stable par u .

Exercice 3 Il est évident que L F ( E ) est inclus dans l'algèbre L ( E ) et contient Id E .

De plus, pour tout x ∈ F , on a ( u ◦ v ) ( x ) = u ( v ( x ) ︸︷︷︸ ∈ F ) ∈ F et, par conséquent l'application u ◦ v appartient à L F ( E ).

Soit ( u, v ) ∈ L F ( E ) 2 et ( α, β ) ∈ I K 2 . Pour tout x ∈ F, on a u ( x ) ∈ F, v ( x ) ∈ F et par suite ( αu + βv ) ( x ) ∈ F . L'application αu + βv appartient donc à L F ( E ).

Ainsi, L F ( E ) est une sous-algèbre de L ( E ).

Corollaire 3 Comme ( e 1 , . . . , e p ) est une base de F , l'espace vectoriel F est stable par u ∈ L ( E ) si, et seulement si, ∀ j ∈ [ [1 , p ] ] u ( e j ) ∈ F c'est-à-dire si, et seulement si, les p premières colonnes de la matrice de u dans la base B ont leurs n -p derniers coefficients nuls, c'est-à-dire si, et seulement si, cette matrice est de la forme :

$$\begin{array} { r l } { \ h u i s , c e s t - a - d i r e s i , e t s e u i m e n t s i , cette t h e m a t r i c h } \\ { \left ( \begin{array} { c c } { A } & { C } \\ { 0 } & { B } \end{array} \right ) } & { a v e c \ A \in \mathcal { M } _ { p } ( I K ) . } \\ { \end{array}$$

L'interprétation de A est alors claire.

## Exercice 4

1. Pour tout i ∈ [ [1 , n ] ] , le sous-espace E i est stable par u ∈ L ( E ) si, et seulement s'il existe λ i ∈ I K tel que u ( e i ) = λ i e i . Les endomorphismes cherchés sont donc ceux dont la matrice dans la base B est diagonale.
2. Les espaces F i sont stables par u si, et seulement si, pour tout i ∈ [ [1 , n ] ] , u ( e i ) ∈ F i . Les endomorphismes cherchés sont donc ceux dont la matrice dans la base B est triangulaire supérieure.

Proposition 4 Le sous-espace E i est stable par u si, et seulement si, les vecteurs de B i ont pour image par u un vecteur de E i , c'est-à-dire une combinaison linéaire de vecteurs de B i . On en déduit facilement l'équivalence annoncée et l'interprétation des matrices A i .

BCBK

- Exercice 5 Un réel λ est valeur propre de D si, et seulement si, l'équation f ′ = λf a une solution non nulle dans E . Or les solutions de cette équation différentielle sont les multiples de la fonction non nulle e λ : t ↦→ exp( λt ).

En conclusion, tout réel λ est valeur propre de D et E λ ( D ) = Vect ( e λ ).

- Exercice 6 Un complexe λ est valeur propre de Δ si, et seulement si, l'équation Δ( u ) = λu a une solution non nulle dans E . Or Δ( u ) = λu équivaut à :

$$\forall n \in \mathbb { N } \ \ u _ { n + 1 } = \lambda u _ { n } , \\$$

ou encore, par une récurrence évidente, à :

$$\forall n \in \mathbb { N } \ \ u _ { n } = u _ { 0 } \lambda ^ { n } . \\$$

En conclusion, tout complexe λ est valeur propre de Δ, le sous-espace propre associé étant la droite vectorielle engendrée par la suite géométrique ( λ n ) n ∈ I N de raison λ .

Rappelons que pour λ = 0, on a ( λ n ) n ∈ I N = ( δ 0 ,n ) n ∈ I N = (1 , 0 , 0 , . . . ).

## Exercice 7

Un complexe λ est valeur propre de u si, et seulement si, l'équation XP = λP a une solution non nulle dans E .

Or, pour P = 0, on a :

$$O ( 1 , \text {pour } 1 \neq 0 , \text { on } a \, . \\ \deg ( X P ) = 1 + \deg ( P ) \in \mathbb { N } \ \ e t \ \deg ( \lambda P ) = \begin{cases} \deg ( P ) & \text {si } \ \lambda \neq 0 \\ - \infty & \text {si } \ \lambda = 0 , \end{cases} \\ \intertext { s i n g } \ e q u i n d \colon \hat { \varphi } e x i l i t s \ Y P - \mathcal { D } \text { isometrically unique } \deg ( \mathcal { D } ) \, . \, < \deg ( Y P ) \\$$

̸

ce qui rend l'égalité XP = λP impossible puisque deg( λP ) &lt; deg( XP ).

En conclusion, u n'a pas de valeur propre.

- Exercice 8 Comme ϕ est un isomorphisme, pour tout vecteur x de E et pour tout scalaire λ , on a :

c'est-à-dire :

$$\text {scale} \, \lambda , \, \text {on} \, a \, . \\ u ( x ) = \lambda x \Longleftrightarrow u \circ \varphi ^ { - 1 } ( \varphi ( x ) ) = \lambda x \Longleftrightarrow \varphi \circ u \circ \varphi ^ { - 1 } ( \varphi ( x ) ) = \lambda \varphi ( x ) , \\ c ^ { \prime } \text {est} \, \hat { a } \text {dire} \, \colon \\$$

$$x \in E _ { \lambda } ( u ) \Longleftrightarrow \varphi ( x ) \in E _ { \lambda } ( \varphi \circ u \circ \varphi ^ { - 1 } ) . \\$$

Comme ϕ est un isomorphisme, on en déduit que les endomorphismes u et ϕ ◦ u ◦ ϕ -1 ont les mêmes valeurs propres et leurs sous-espaces propres sont reliés par :

## Proposition 6

$$E _ { \lambda } ( \varphi \circ u \circ \varphi ^ { - 1 } ) = \varphi ( E _ { \lambda } ( u ) ) .$$

- Pour tout p ∈ I N ∗ , on pose H ( p ) : « Si u admet p valeurs propres distinctes, alors les espaces propres associés sont en somme directe. » Pour p = 1 , il n'y a rien à prouver.

Supposons la proposition vraie pour un certain rang p ∈ I N ∗ . Soit λ 1 , . . . , λ p +1 des valeurs propres distinctes de u et ( x 1 , . . . , x p +1 ) ∈ p +1 ∏ i =1 E λ i ( u ) vérifiant p +1 ∑ i =1 x i = 0 .

̸

## BVCWCPD4CXD8D6CT BE BA CA AJ CTCSD9CRD8CXD3D2 CSCTD7 CTD2CSD3D1D3D6D4CWCXD7D1CTD7

On a donc u p +1 x i = 0 = p +1 λ i x i

$$\left ( \frac { p + 1 } { i = 1 } \right ) & - \lambda _ { p + 1 } \sum _ { i = 1 } ^ { p + 1 } x _ { i } = \sum _ { i = 1 } ^ { p + 1 } \lambda _ { i } x _ { i } - \sum _ { i = 1 } ^ { p + 1 } \lambda _ { p + 1 } x _ { i } \\ & = \sum _ { i = 1 } ^ { p + 1 } ( \lambda _ { i } - \lambda _ { p + 1 } ) x _ { i } = \sum _ { i = 1 } ^ { p } ( \underbrace { \lambda _ { i } - \lambda _ { p + 1 } } _ { \in E _ { \lambda _ { i } } ( u ) } ) x _ { i } . \\ \intertext { \text {En applicquant $I$ hyperhede of recurrence, on obtient } \colon } & \forall i \in \mathbb { I } _ { 1 } , \eta _ { i } \ ( \lambda _ { i } - \lambda _ { p + 1 } ) x _ { i } = 0 ,$$

$$& \text {dondc u} \left ( \sum _ { i = 1 } ^ { p + 1 } x _ { i } \right ) = 0 = \sum _ { i = 1 } ^ { p + 1 } \lambda _ { i } x _ { i } \ p u i s \, \cdot \\ & 0 = u \left ( \sum _ { i = 1 } ^ { p + 1 } x _ { i } \right ) - \lambda _ { p + 1 } \sum _ { i = 1 } ^ { p + 1 } x _ { i } = \sum _ { i = 1 } ^ { p + 1 } \lambda _ { i } x _ { i } - \sum _ { i = 1 } ^ { p } \lambda _ { i } x _ { i } - \sum _ { i = 1 } ^ { p + 1 }$$

En appliquant l'hypothèse de récurrence, on obtient :

$$\forall i \in [ 1 , p ] \ \ ( \lambda _ { i } - \lambda _ { p + 1 } ) \, x _ { i } = 0 . \\$$

Or, les valeurs propres étant deux à deux distinctes, pour tout i ∈ [ [1 , p ] ] , λ i = λ p +1

̸

- Soit ( x 1 , . . . , x p ) une famille de vecteurs propres de u associés aux valeurs propres deux à deux distinctes λ 1 , . . . , λ p et ( α 1 , . . . , α p ) ∈ I K p tel que p ∑ i =1 α i x i = 0 .

$$& \text {dconc } x _ { i } = 0 . \, L ^ { \prime } \tilde { e } g a l i \stackrel { p + 1 } { \sum } _ { i = 1 } \\ \bullet & \quad \text {So } ( x _ { 1 } , \dots , x _ { p } ) \text {  une familie de vecteurs propres de } u \text { assocés aux valeurs propres}$$

Comme ( α 1 x 1 , . . . , α p x p ) ∈ p ∏ i =1 E λ i ( u ) , l'on déduit de la première partie de la proposition que, pour tout i [ [1 , p ] ] , α x = 0 .

Comme chaque x i est non nul, car vecteur propre de u , on peut conclure que :

∈ i i

$$\forall i \in [ 1 , p ] \ \alpha _ { i } = 0 . \\$$

Par suite, la famille ( x 1 , . . . , x p ) est libre.

- Exercice 9 Soit α ∈ I R . Pour tout t &gt; 0, on a u ( f α ) ( t ) = t ( αt α -1 ) = αt α donc u ( f α ) = αf α et la fonction non nulle f α est vecteur propre de u pour la valeur propre α .

Par suite, si α 1 , . . . , α n sont des réels deux à deux distincts, la famille de fonctions ( f α 1 , . . . , f α n ) est une famille libre de C ∞ ( I R ∗ + , I R ) .

Ainsi, la famille ( f α ) α ∈ I R est libre.

- Corollaire 8 D'après la proposition 6 de la page 69, à toute famille de p valeurs propres deux à deux distinctes on peut associer une famille libre de p vecteurs propres, donc p ⩽ n .

Exercice 10 Soit P 1 et P 2 deux matrices réelles telles que P = P 1 + iP 2 .

$$O n \, a \, ( P _ { 1 } + i P _ { 2 } ) \, M ^ { \prime } = M \, ( P _ { 1 } + i P _ { 2 } ) \, , \, c ^ { \prime } \text {est} \, \tilde { a } \text {-dirine} \, P _ { 1 } M ^ { \prime } = M P _ { 1 } \, \ e t \, \ P _ { 2 } M ^ { \prime } = M P _ { 2 } \, .$$

Ainsi, pour tout réel λ , on a ( P 1 + λP 2 ) M ′ = M ( P 1 + λP 2 ). Il reste à prouver l'existence d'un réel λ tel que P 1 + λP 2 ∈ GL n ( I R ) pour conclure.

̸

Or, la fonction λ ↦→ det ( P 1 + λP 2 ) est polynomiale et non nulle car P ( i ) = 0.

Elle admet donc un nombre fini de racines, ce qui assure l'existence d'un réel λ tel que P 1 + λP 2 ∈ GL n ( I R ).

BC

## Exercice 11

1. Soit λ ∈ I K . Un vecteur X = ( x i ) 1 ⩽ i ⩽ n vérifie AX = λX si, et seulement si :

̸

$$\lfloor & u n i q u e \ v a l e u r \ p r o p r e \ n \\ \ e n g e n d r e \ \bar { \ } p a r \ \left ( \begin{array} { c } 1 \\ \vdots \\ 1 \end{array} \right ) \cdot \\ \intertext { s i } S i \ \lambda = 0 \, , \, a l o r s \, \leq s y s t e r$$

Si λ = 0, on en déduit que x 1 = · · · = x n puis que λx 1 = nx 1 . Ainsi, n est l'unique valeur propre non nulle de J et le sous-espace propre associé est la droite

## D´ emonstrations et solutions des exercices du cours

$$\begin{array} { r l } & { t e u r \ X = ( x _ { i } ) _ { 1 \leqslant i \leqslant n } \ v e r i f i e \ A X = \lambda X \ s i , } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad } \\ & { \quad }$$

Si λ = 0, alors le système devient n ∑ i =1 x i = 0. Ainsi, 0 est valeur propre de J et

2. Soit λ ∈ I K . On a AX = λX si, et seulement si, αJX = ( λ -β ) X .

le sous-espace propre associé est l'hyperplan d'équation n ∑ i =1 x i = 0.

Si α = 0, alors A = βI n donc la seule valeur propre de A est β et le sous-espace propre associé est ( I K ).

M n, 1 Sinon, λ est valeur propre de A si, et seulement si, λ -β α ∈ sp( J ) = { 0 , n } . Ainsi, sp( A ) = { β, αn + β } et les sous-espaces propres associés sont respectivement E 0 ( J ) et E n ( J ).

- Proposition 15 Soit λ ∈ I K ′ une valeur propre de A et X ∈ M n, 1 ( I K ′ ) un vecteur propre associé. Comme M n, 1 ( I K ′ ) ⊂ M n, 1 ( I K ) , λ est aussi valeur propre de A ∈ M n ( I K ) , d'où l'inclusion annoncée.

## Proposition 16

- Soit X un vecteur propre de A pour la valeur propre λ . On a donc AX = λX et, en utilisant les propriétés de la conjugaison, on en déduit facilement :

$$\overline { A } \, \overline { X } = \overline { A X } = \overline { \lambda } \, \overline { X } ,$$

soit AX = λX , puisque A est à coefficients réels. D'où λ ∈ sp C ( A ) car X = 0 .

̸

- Soit ( X 1 , . . . , X k ) une base de E λ ( A ) .

D'après le point précédent, les vecteurs X 1 , . . . , X k appartiennent à E λ ( A ) .

Soit ( α 1 , . . . , α k ) une famille de scalaires telle que k ∑ j =1 α j X j = 0 .

$$0 \, a \, \text {ors} \, \sum _ { j = 1 } ^ { k } \overline { \alpha _ { j } } X _ { j } & = 0 \, \text {puis} \, \sum _ { j = 1 } ^ { k } \overline { \alpha _ { j } } X _ { j } = 0 . \, \text {La famille} \, ( X _ { 1 } , \dots , X _ { k } ) \, \text {ant libre, on} \\ \text {en déduit que} \, \overline { \alpha _ { 1 } } & = \dots = \overline { \alpha _ { k } } = 0 , \, d ' o u \ \alpha _ { 1 } = \dots = \alpha _ { k } = 0 .$$

BDBDBD

## BVCWCPD4CXD8D6CT BE BA CA AJ CTCSD9CRD8CXD3D2 CSCTD7 CTD2CSD3D1D3D6D4CWCXD7D1CTD7

Par suite la famille ( X 1 , . . . , X k ) est libre et la dimension du sous-espace propre de A pour la valeur propre λ est supérieure ou égale à k ; d'où dim E λ ( A ) ⩽ dim E λ ( A ) . Comme λ est aussi une valeur propre de A , on en déduit que :

$$\dim E _ { \overline { \lambda } } ( A ) \leqslant \dim E _ { \overline { \lambda } } ( A ) = \dim E _ { \lambda } ( A )$$

puis que dim E λ ( A ) = dim E λ ( A ) .

Proposition 18 Si u ( x ) = λx , on établit, par une récurrence immédiate :

$$\forall k \in \mathbb { N } \ \ u ^ { k } \left ( x \right ) = \lambda ^ { k } x .$$

$$& \text {Si } \ P = \sum _ { k = 0 } ^ { p } a _ { k } X ^ { k } , \text { on } \text { en dédukit } \ P ( u ) ( x ) = \sum _ { k = 0 } ^ { p } a _ { k } u ^ { k } ( x ) = \sum _ { k = 0 } ^ { p } a _ { k } \lambda ^ { k } x = P ( \lambda ) \, x . \\ & \text {Ainsi, si } \, \text {x est vecteur propre de } u \, \text { associé à la valeur propre } \lambda , \, \text { alors } x \, \text { est vecteur propre}$$

Ainsi, si x est vecteur propre de u associé à la valeur propre λ , alors x est vecteur propre de P ( u ) pour la valeur propre P ( λ ) .

## Exercice 12

1. On vérifie que A 2 = 3 A -2 I 3 . Le polynôme P = X 2 -3 X +2 convient donc.

$$O n \, e n \, d \hat { e } d u i t \, q e \ A \, e s t \, i n v e r s i b l e \, e t \, q e \ A ^ { - 1 } = \frac { 1 } { 2 } \, ( 3 I _ { 3 } - A ) . \\$$

2. On a A (3 I 3 -A ) = 2 I 3 .
3. Soit n un entier. D'après le théorème de la division euclidienne, il existe deux réels a et b , ainsi qu'un polynôme Q tels que :

$$X ^ { n } = P Q + a X + b = ( X - 1 ) ( X - 2 ) Q + a X + b .$$

Par conséquent, le reste de la division Euclidienne de X n par P est (2 n -1) X +2 -2 n .

Les réels a et b vérifient le système { 1 n = a + b 2 n = 2 a + b .

4. Soit n un entier. D'après la question précédent, il existe un polynôme Q tel que :

$$A ^ { n } = P ( A ) Q ( A ) + ( 2 ^ { n } - 1 ) \, A + ( 2 - 2 ^ { n } ) \, I _ { n } = ( 2 ^ { n } - 1 ) \, A + ( 2 - 2 ^ { n } ) \, I _ { n } ; \\$$

donc :

$$A ^ { n } = \left ( \begin{array} { c c c c } 3 & 2 \left ( 2 ^ { n } - 1 \right ) & 1 - 2 ^ { n } \\ 4 \left ( 1 - 2 ^ { n } \right ) & 9 \cdot 2 ^ { n } - 8 & 4 \left ( 1 - 2 ^ { n } \right ) \\ 8 \left ( 1 - 2 ^ { n } \right ) & 1 6 \left ( 2 ^ { n } - 1 \right ) & - 7 \cdot 2 ^ { n } + 8 \end{array} \right ) .$$

## Exercice 13

En développant det ( XI 3 -A ) par rapport à la première colonne, on obtient :

$$\lambda ( A ( X ) ^ { 2 } ) = ( X ^ { 2 } - ( X ^ { 2 } - 2 \cos ^ { 2 } | X ^ { 2 } - 2 \cos ^ { 2 } | \, X ) ^ { 1 } ) . \\ \text {Ainsi, spc} ( A ) = \{ 1 , e ^ { i \theta } , e ^ { - i \theta } \} \, \text {et} \, \text {sp} _ { \mathbb { R } } ( A ) = \{ 1 \} \, \text {ou} \, \text {sp} _ { \mathbb { R } } ( A ) = \{ - 1 , 1 \} \, \text {(si} \, \theta \equiv \pi [ 2 \pi ] ) . \\ \\ \text {Fexercice} \, 1 4 \, \text { on } A \, y _ { 4 } = \det \left ( X \, I _ { n } - \mathcal { ^ { 1 } } A \right ) \equiv \det \left ( T ( X I _ { n } - A ) \right ) = y _ { 4 } .$$

$$\text {Lindeoverpapt} \, \det ( X | _ { 3 } - A ) \, \text {paplopr} \, \alpha \, \text {premere conomme, on $\beta$ obcient} \, . \\ \chi _ { A } \left ( X \right ) = \left ( X - 1 \right ) \left ( \left ( X - \cos \theta \right ) ^ { 2 } + \sin \theta ^ { 2 } \right ) = \left ( X - 1 \right ) \left ( X ^ { 2 } - 2 \cos \theta X + 1 \right ) . \\ \text {Ainsi, spc} \left ( A \right ) = \left \{ 1 , e ^ { i \theta } , e ^ { - i \theta } \right \} \, \text {et spr} _ { \mathbb { R } } \left ( A \right ) = \left \{ 1 \right \} \, \text {ou spr} _ { \mathbb { R } } \left ( A \right ) = \left \{ - 1 , 1 \right \} \, \text {si $\theta\equiv\pi[2\pi]$.}$$

$$E x c r e c i 1 4 \ O n a \ \chi _ { A } = \det \left ( X I _ { n } - ^ { t } A \right ) = \det \left ( ^ { t } ( X I _ { n } - A ) \right ) = \chi _ { A } . \\$$

BE

Proposition 27 Soit A = ( a i,j ) 1 ⩽ i,j ⩽ n et λ ∈ I K . La matrice ( XI n -A ) est une matrice à coefficients dans I K . Son déterminant, donné par :

$$\sum _ { \sigma \in S _ { n } } \varepsilon \left ( \sigma \right ) \left ( \lambda \delta _ { \sigma ( 1 ) , 1 } - a _ { \sigma ( 1 ) , 1 } \right ) \dots \left ( \lambda \delta _ { \sigma ( n ) , n } - a _ { \sigma ( n ) , n } \right ) \\ \text {expression polynomial} \, \in \partial _ { n } \, \vartheta \, \deg \, \inf _ { \sigma \in \mathcal { A } } \, \vartheta \, \colon$$

est une expression polynomiale en λ de degré inférieur ou égal à n .

Soit σ ∈ S n différente de l'identité. il existe alors au moins deux éléments distincts i et j de [ [1 , n ] ] tels que δ σ ( i ) ,i et δ σ ( j ) ,j soient nuls et le terme :

ε ( σ ) ( λδ σ (1) , 1 -α σ (1) , 1 ) . . . ( λδ σ ( n ) ,n -α σ ( n ) ,n ) est de degré inférieur ou égal à n -2 . Les termes de degré n et n -1 de χ A ( λ ) sont donc ceux du produit :

$$( \lambda - \alpha _ { 1 , 1 } ) \dots ( \lambda - \alpha _ { n , n } ) \, , \\ ) _ { n } \, , n = 1 , \dots , n$$

soit λ n et -( α 1 , 1 + · · · + α n,n ) λ n -1 respectivement.

On obtient finalement le terme constant de χ A en évaluant en 0 .

̸

$$C _ { 2 } \leftarrow C _ { 2 } + \lambda ^ { - 1 } A C _ { 1 } \text { donne :} \\ \chi _ { B } ( \lambda ) = \left | \begin{array} { c c } \lambda I _ { n } & - A \\ - A & \lambda I _ { n } \end{array} \right | \right | \begin{array} { c c } I _ { n } & \lambda ^ { - 1 } A \\ 0 & I _ { n } \end{array} \right | = \left | \begin{array} { c c } \lambda I _ { n } & 0 \\ - A & \lambda I _ { n } - \lambda ^ { - 1 } A ^ { 2 } \end{array} \right | \\ \det , \, \text {par conséquot} \, \colon \\ \gamma _ { B } ( \lambda ) = \det \left ( \lambda ^ { 2 } I _ { n } - A ^ { 2 } \right ) = \det \left ( \lambda I _ { n } - A \right ) \det \left ( \lambda I _ { n } + A \right ) = \gamma _ { A } ( \lambda ) ( - 1 ) ^ { n } \gamma _ { A } ( - \lambda ) ,$$

Exercice 15 Soit λ ∈ I K . Si λ = 0, alors, l'opération élémentaire par blocs C 2 ← C 2 + λ -1 AC 1 donne :

et, par conséquent :

$$et , \, \text {par conjugleit} \colon \\ \chi _ { B } ( \lambda ) = \det \left ( \lambda ^ { 2 } I _ { n } - A ^ { 2 } \right ) = \det \left ( \lambda I _ { n } - A \right ) \det \left ( \lambda I _ { n } + A \right ) = \chi _ { A } ( \lambda ) ( - 1 ) ^ { n } \chi _ { A } ( - \lambda ) . \\ \text {Si } \, \lambda = 0 , \, \text {on a le mestre réselat.} \, \text {Ainsi } \, \chi _ { B } ( X ) = ( - 1 ) ^ { n } \chi _ { A } ( X ) \chi _ { A } ( - X ) .$$

Si λ = 0, on a le même résultat. Ainsi χ B ( X ) = ( -1) n χ A ( X ) χ A ( -X ) .

Exercice 16 Pour tout complexe λ , on a :

$$\begin{array} { r l } & { \tt t \, c o m p l e x e \ \lambda , \, o n a \colon } \\ & { \quad \chi _ { C } ( \lambda ) = \left | \begin{array} { c c c } { \lambda I _ { n } - A } & { - B } \\ { - B } & { \lambda I _ { n } - A } \end{array} \right | . } \\ & { - C _ { 1 } + C _ { 2 } \ p u i s \ L _ { 2 } \leftarrow L _ { 2 } - L _ { 1 } \ d o n n e n t \colon } \\ & { \tt t r \, n - A - B \quad - B \quad \left | \begin{array} { c c c } { \lambda I _ { n } - A - B } \end{array} \right | } \end{array}$$

Les opérations C 1 ← C 1 + C 2 puis L 2 ← L 2 -L 1 donnent :

$$\text {Les operations } C _ { 1 } \leftarrow & C _ { 1 } + C _ { 2 } \ p u i \ L _ { 2 } \leftarrow L _ { 2 } - L _ { 1 } \text { donnent } \colon \\ \chi _ { C } ( \lambda ) = & \left | \begin{array} { c c c c } \lambda I _ { n } - A - B & - B \\ \lambda I _ { n } - A - B & \lambda I _ { n } - A & = \left | \begin{array} { c c c c } \lambda I _ { n } - A - B & - B \\ 0 & \lambda I _ { n } - A + B \end{array} \right | \\ \text {donc } \chi _ { C } ( \lambda ) = & \chi _ { A + B } ( \lambda ) \chi _ { A - B } ( \lambda ) . \ p u i \ \chi _ { C } ( X ) = \chi _ { A + B } ( X ) \chi _ { A - B } ( X ) .$$

Exercice 17 Par l'opération L 0 ← L 0 + XL 1 + · · · + X p -1 L p -1 , la matrice XI p -A se transforme en :

BF

$$\begin{array} { r l } & { \ar \, 1 \, o r a p e r a t i o n \, L _ { 0 } \leftarrow L _ { 0 } + X \, L _ { 1 } + \cdots + X ^ { P } \, \cdot L _ { p - 1 } \, , \, l a m a n } \\ & { e n \colon } \\ & { \left ( \begin{array} { c c c c c } & & 0 & 0 & \dots & \dots & 0 & P ( X ) \\ & - 1 & X & \dots & \dots & 0 & a _ { 1 } \\ & 0 & - 1 & \ddots & & & & \\ & \vdots & \vdots & \ddots & \ddots & & \vdots \\ & 0 & 0 & \dots & - 1 & X & a _ { p - 2 } \\ & 0 & 0 & \dots & 0 & - 1 & X + a _ { p - 1 } \end{array} \right ) } \end{array}$$

## BVCWCPD4CXD8D6CT BE BA CA AJ CTCSD9CRD8CXD3D2 CSCTD7 CTD2CSD3D1D3D6D4CWCXD7D1CTD7

avec P ( X ) = X p + a p -1 X p -1 + · · · + a 1 X + a 0 . Un développement suivant la première ligne donne alors :

$$\chi _ { A } \left ( X \right ) & = ( - 1 ) ^ { p + 1 } P ( X ) ( - 1 ) ^ { p - 1 } = P ( X ) . \\ \\$$

- Exercice 18 Dans une base adaptée au sous-espace vectoriel Im u , la matrice de u est de la forme :

Son polynôme caractéristique est donc X n -1 ( X -α 1 , 1 ). Comme α 1 , 1 est la trace de u , on obtient :

$$\begin{array} { r l } & { a s e a d a p t e e a u s o u s - e s p a c e v e c t o r i e l r i n g t a r r o w } \\ & { \quad } \\ & { \quad } & { \left ( \begin{array} { l l l l } { \alpha _ { 1 , 1 } } & { \dots } & { \dots } & { \alpha _ { 1 , n } } \\ { 0 } & { \dots } & { \dots } & { 0 } \\ { \vdots } & & { \vdots } & \\ { 0 } & { \dots } & { \dots } & { 0 } \end{array} \right ) . } \\ & { i s t i q u e e s t d o n c X ^ { n - 1 } ( X - \alpha _ { 1 , 1 } ) . C o n s i t i l e s t t a r r o w } \\ & { i s t i q u e e s t d o n c X ^ { n - 1 } ( X - \alpha _ { 1 , 1 } ) . C o n s i t i l e s t t a r r o w } \end{array}$$

$$\chi _ { u } ( X ) = X ^ { n - 1 } \left ( X - \text {Tr} \, u \right ) .$$

- Proposition 32 Soit p la dimension de F et B = ( e 1 , . . . , e n ) une base de E adaptée à F , c'est-à-dire telle que B F = ( e 1 , . . . , e p ) soit une base de F .

La matrice de u dans B est alors de la forme ( A B 0 D ) , où A est la matrice de u F dans la base B F . Le polynôme caractéristique de u , égal à χ A ( X ) χ D ( X ) est donc divisible par le polynôme caractéristique χ A ( X ) de u F .

- Proposition 33 En effet, si F est stable par u , alors χ u F divise le polynôme scindé χ u , d'après la proposition 32 de la page 83, donc est scindé.
- Proposition 34 Notons n ( λ ) la dimension du sous-espace propre E λ ( u ) . Comme E λ ( u ) est non réduit à { 0 } , on a 1 ⩽ n ( λ ) . De plus, E λ ( u ) est stable par u et l'endomorphisme induit par u sur E λ ( u ) est l'homothétie λ Id E λ ( u ) ; son polynôme caractéristique vaut donc ( X -λ ) n ( λ ) . D'après la proposition 32, il divise χ u ( X ) , ce qui donne n ( λ ) ⩽ m ( λ ) .
- Proposition 36 D'après la définition 10 de la page 82, on a :

$$\chi _ { u } \left ( X \right ) = X ^ { n } - \left ( T r \, u \right ) \, X ^ { n - 1 } + \dots + \left ( - 1 \right ) ^ { n } \det u .$$

D'après les hypothèses, on a aussi χ u ( X ) = n ∏ i =1 ( X -μ i ) . En utilisant les relations entre coefficients et racines d'un polynôme scindé, on obtient :

$$\text {Tr} \, u = \sum _ { i = 1 } ^ { n } \mu _ { i } \, \ e t \, \det u = \prod _ { i = 1 } ^ { n } \mu _ { i } . \\ \text {es} \, \text {on a} \, \lfloor \L e q a l i t e \rfloor \colon$$

Comme, à l'ordre près, on a l'égalité :

on obtient :

BG

$$( \mu _ { 1 } , \dots , \mu _ { n } ) = \underbrace { ( \lambda _ { 1 } , \dots , \lambda _ { 1 } , \dots , \underbrace { \lambda _ { p } , \dots , \lambda _ { p } } } _ { m ( \lambda _ { 1 } ) \text { for } \text { } m ( \lambda _ { p } ) \text { } \text { } f o i s } } \\$$

$$\text {Tr} \, u = \sum _ { i = 1 } ^ { p } m \left ( \lambda _ { i } \right ) \lambda _ { i } \ \det \ d e t { u } = \prod _ { i = 1 } ^ { p } \lambda _ { i } ^ { m ( \lambda _ { i } ) } .$$

Proposition 37 S'il existe une base de E constituée de vecteurs propres de u , alors la matrice de u dans cette base est diagonale donc u est diagonalisable.

Réciproquement, s'il existe une base B de E telle que la matrice de u dans cette base soit diagonale, alors la base B est constituée de vecteurs propres de u .

̸

- Exercice 19 Pour P = 0, on a deg ( P ′ ) &lt; deg ( P ) ; par suite P ′ = D n ( P ) = λP est impossible avec λ = 0. Ainsi, sp D n ⊂ { 0 } .

̸

Comme Ker( D n ) = I K 0 [ X ] , les vecteurs propres de D n sont de degré nul donc il n'existe pas de base de I K n [ X ] constituée de vecteurs propres de D n .

Par suite, D n n'est pas diagonalisable.

- Exercice 20 Une matrice A non nulle est vecteur propre de f pour la valeur propre λ si, et seulement si, f ( A ) = λA , c'est-à-dire si, et seulement si, ( λ -1) A = Tr( A ) I n . Deux cas se présentent :
- λ = 1. Dans ce cas f ( A ) = A équivaut à Tr( A ) = 0. Ainsi 1 est valeur propre de f et le sous-espace propre associé est égal à l'ensemble des matrices de trace nulle. Il s'agit du noyau de la forme linéaire non nulle Tr donc d'un hyperplan.
- λ = 1. Dans ce cas f ( A ) = λA entraîne A ∈ Vect ( I n ).

̸

Comme f ( I n ) = ( n +1) I n , on en déduit que n + 1 est valeur propre de f , de sous-espace propre associé Vect ( I n ).

Comme I n / ∈ H et que H est un hyperplan de M n ( I K ), on sait qu'alors :

$$\mathcal { M } _ { n } \left ( \mathbb { K } \right ) & = \mathcal { H } \oplus V e c t \left ( I _ { n } \right ) . \\ \intertext { l } \mathcal { M } _ { n } \left ( \mathbb { K } \right ) & = \mathcal { H } \oplus V e c t \left ( I _ { n } \right ) .$$

Ainsi, en réunissant une base de H et une base de Vect ( I n ), on obtient une base de M n ( I K ) constituée de vecteurs propres de f .

En conclusion, f est diagonalisable.

## Proposition 38

- Soit p un projecteur de E . On a E = Ker p ⊕ Ker( p -Id E ) . Donc, si l'on réunit une base de Ker p et une base de Ker( p -Id E ) , on obtient une base de E constituée de vecteurs propres de p . Ainsi p est diagonalisable.
- On peut même préciser que le spectre de p est { 0 , 1 } sauf si p = 0 (auquel cas sp( p ) = { 0 } ) ou p = Id E (auquel cas sp( p ) = { 1 } ).
- Soit s une symétrie de E . On a E = Ker( s -Id E ) ⊕ Ker( s +Id E ) . Donc, si l'on réunit une base de Ker( s -Id E ) et une base de Ker( s +Id E ) , on obtient une base de E constituée de vecteurs propres de s . Ainsi, s est diagonalisable.
- On peut même préciser que son spectre est {-1 , 1 } sauf si s = Id (auquel cas sp( s ) = { 1 } ) ou s = -Id E (auquel cas sp( s ) = {-1 } ).

## Exercice 21

- Pour le calcul de χ A ( X ), notons C 1 , C 2 et C 3 les colonnes de la matrice XI 3 -A . L'opération C 1 ← C 1 + C 2 -C 3 donne :

BH

$$- \, C _ { 1 } + C _ { 2 } - C _ { 3 } \, \text { d o nne } \colon \\ \chi _ { A } \left ( X \right ) = \left | \begin{array} { c c c c } X - 1 & - 3 & - 2 \\ X - 1 & X - 5 & - 2 \\ 1 - X & 3 & X \end{array} \right | .$$

## BVCWCPD4CXD8D6CT BE BA CA AJ CTCSD9CRD8CXD3D2 CSCTD7 CTD2CSD3D1D3D6D4CWCXD7D1CTD7

En notant cette fois L 1 , L 2 et L 3 les lignes du nouveau déterminant, les opérations L 2 ← L 2 -L 1 et L 3 ← L 3 + L 1 donnent :

Ainsi, sp( A ) = { 1 , 2 } .

$$L _ { 2 } & \leftarrow L _ { 2 } - L _ { 1 } \text { et } L _ { 3 } \leftarrow L _ { 3 } + L _ { 1 } \text { d o nnent } \colon \\ & \quad \chi _ { A } ( X ) = ( X - 1 ) \left | \begin{array} { c c c } 1 & - 3 & - 2 \\ 0 & X - 2 & 0 \\ 0 & 0 & X - 2 \end{array} \right | = ( X - 1 ) ( X - 2 ) ^ { 2 } \, . \\ \intertext { A i n s i , s p ( A ) = \{ 1 , 2 \} . } \text {On obtient le sous-espace propre associe à la valeur propre 1 en résolvant le } & \quad$$

$$\begin{array} { r l } & { \quad s o i t \colon } \\ & { \quad \left \{ \begin{array} { l l l } { - x } & { + } & { 3 y } & { + } & { 2 z } & { = 0 } \\ { - 2 x } & { + } & { 4 y } & { + } & { 2 z } & { = 0 } \\ { 2 x } & { - } & { 3 y } & { - } & { z } & { = 0 . } \end{array} } \\ & { E _ { 3 } \, l e s \, \hat { e } q u a t i o n s \, d e \, c e \, s y t e m e . \, E n \, e f f e c } \\ & { E _ { 3 } \, \leftarrow \, E _ { 3 } + E _ { 1 } , \, o n \, m o n t r e \, q u e \, c e \, s y t e } \end{array}$$

- On obtient le sous-espace propre associé à la valeur propre 1 en résolvant le système AX = X soit :

Notons E 1 , E 2 et E 3 les équations de ce système. En effectuant les opérations E 2 ← E 2 -E 1 et E 3 ← E 3 + E 1 , on montre que ce système est équivalent à x = y = -z . Ainsi E 1 ( A ) = I K v 1 , où :

L'étude du sous-espace propre associé à la valeur propre 2 conduit au système :

$$v _ { 1 } , \, o \dot { u } \colon \\ v _ { 1 } = \left ( \begin{array} { c } 1 \\ 1 \\ - 1 \end{array} \right ) . \\ \intertext { v _ { 1 } = \left ( \begin{array} { c } 1 \\ 1 \\ - 1 \end{array} \right ) . }$$

$$\begin{array} { r l } & { e p r o p r e a s s o c i e \hat { a } l a v a l e u r p r o p r e 2 } \\ & { \quad \left \{ - 2 x + 3 y + 2 z = 0 } \\ & { \left \{ - 2 x + 3 y + 2 z = 0 } \\ & { 2 x - 3 y - 2 z = 0 , } \\ & { - 2 z = 0 . O n o b t i e n t E _ { 2 } ( A ) = \left | K v _ { 2 } \infty \right | } \\ & { \left ( 3 \right ) } \end{array}$$

équivalent à 2 x -3 y -2 z = 0. On obtient E 2 ( A ) = I K v 2 ⊕ I K v 3 où :

- Comme les sous-espaces propres sont en somme directe d'après la proposition 6 de la page 69, C = ( v 1 , v 2 , v 3 ) est une famille libre donc une base de vecteurs propres. Ainsi, la matrice A est diagonalisable.

$$3 y - 2 z & = 0 . \, O n \, o b t i e n t \ E _ { 2 } ( A ) = \left \| K v _ { 2 } \oplus \mathbb { I } K v _ { 3 } \right \| \\ v _ { 2 } & = \left ( \begin{array} { c c } 3 \\ 2 \\ 0 \end{array} \right ) \ e t \ v _ { 3 } = \left ( \begin{array} { c } 1 \\ 0 \\ 1 \end{array} \right ) . \\ \intertext { p r o p r e s s o n t e n s o m m e d i r e c t e d ' a p r e s }$$

La matrice de passage de la base canonique à C est :

On peut donc conclure que P -1 AP = ⎛ ⎝ 1 0 0 0 2 0 0 0 2 ⎞ ⎠ .

$$\begin{array} { c } l a \ b a s e \ c a n o n i q u e \ \hat { a } \ \mathcal { C } \ e s t \ \colon \\ P = \left ( \begin{array} { c c c } 1 & 3 & 1 \\ 1 & 2 & 0 \\ - 1 & 0 & 1 \end{array} \right ) . \\ \\ P = \left ( \begin{array} { c c c } 1 & 0 & 0 \\ - 1 & 0 & 1 \end{array} \right ) . \\ \end{array}$$

Proposition 41 D'après la proposition 6 de la page 69, la somme p ⊕ i =1 E λ i est directe.

- Supposons ( i ) . Puisqu'il existe une base de vecteurs propres de u , la somme directe p ⊕ i =1 E λ i contient E , ce qui implique ( ii ) .

BI

- La somme p ⊕ i =1 E λ i étant directe, on a :

On en déduit que ( ii ) ⇒ ( iii ) .

$$\dim \left ( \bigoplus _ { i = 1 } ^ { p } E _ { \lambda _ { i } } ( u ) \right ) = \sum _ { i = 1 } ^ { p } \dim E _ { \lambda _ { i } } ( u ) \, .$$

- Supposons ( iii ) . En réunissant des bases de chaque sous-espace propre de u , on obtient, d'après la proposition 6 de la page 69, une famille libre de n vecteurs propres de u ; ce qui prouve ( i ) .

Corollaire 43 Comme deg ( χ u ) = n , l'endomorphisme u possède n valeurs distinctes si, et seulement si, χ u est scindé à racines simples.

D'après le corollaire 35 de la page 85, chaque sous-espace propre est alors de dimension 1 .

Si sp ( u ) = { λ 1 , . . . , λ n } , on a donc n ∑ i =1 dim E λ i ( u ) = n = dim E . On conclut avec la proposition 41 de la page 88.

- Exercice 22 Le polynôme caractéristique de A , ( X -1)( X -4)( X -6) est scindé simple donc A est diagonalisable.

$$\text {Theoreme 44} \ \text {On pose } F & = \ \bigoplus _ { \lambda \in \text {sp} ( u ) } E _ { \lambda } ( u ) . \\ D ^ { \prime } a p r e \ l a \text { proposition 41, } u \text { est diagonalisable} \text {si}$$

$$a \dim E _ { \lambda } ( u ) \leqslant m ( \lambda ) . \ A nsl , \colon \\ \dim F = \sum _ { \lambda \in s p ( u ) } \dim E _ { \lambda } ( u ) \leqslant \sum _ { \lambda \in s p ( u ) } m ( \lambda ) \leqslant \deg ( \chi _ { u } ) = \dim E . \\ \text {Par suite} \ u \text { est diagonalisable si } \ e t \text { selement} \text { si } \colon$$

D'après la proposition 41, u est diagonalisable si, et seulement si, F = E donc si, et seulement si, dim F = dim E . Or, d'après la proposition 34, pour tout λ ∈ sp( u ) , on a dim E λ ( u ) ⩽ m ( λ ) . Ainsi, :

Par suite, u est diagonalisable si, et seulement si :

$$\forall \lambda \in \text {sp} ( u ) \quad \dim E _ { \lambda } ( u ) = m ( \lambda ) \quad \text {et} \quad \sum _ { \lambda \in \text {sp} ( u ) } m ( \lambda ) = \deg ( \chi _ { u } ) ; \\$$

c'est-à-dire si, et seulement si :

$$\forall \lambda \in \text {sp} ( u ) \ \dim E _ { \lambda } ( u ) = m ( \lambda ) \quad \text {et} \quad \chi _ { u } \text { est scindé.}$$

- Exercice 23 On a χ A = ( X -1) 2 ( X +1) ; ainsi χ A est scindé, -1 est valeur propre simple et 1 est valeur propre double.

D'après le corollaire 35 de la page 85, on a dim E -1 ( A ) = 1. D'après le corollaire 45 de la page 91, la matrice A est diagonalisable si, et seulement si, dim E 1 ( A ) = 2.

En appliquant le théorème du rang, cela équivaut à :

$$& \text {le theoreme du rang, cela equivalaut a } \colon \\ & \quad \ r g \left ( A - I \right ) = \dim \left ( \mathbb { R } ^ { 3 } \right ) - \dim E _ { 1 } \left ( A \right ) = 1 . \\ & - \left ( \begin{array} { c c } 0 & a & b \\ 0 & 0 & a \\ \end{array} \right ) _ { \ } o n o r \left ( A _ { \ } I \right ) = 1 _ { \ } \text {si} \ o t \text {soulmont}$$

Comme A -I = ⎛ ⎝ 0 a b 0 0 c 0 0 -2 ⎞ ⎠ , on a rg ( A -I ) = 1 si, et seulement si, la deuxième colonne est proportionnelle à la dernière, ce qui équivaut à a = 0.

BJ

$$\sum _ { \in s p ( w ) }$$

## BVCWCPD4CXD8D6CT BE BA CA AJ CTCSD9CRD8CXD3D2 CSCTD7 CTD2CSD3D1D3D6D4CWCXD7D1CTD7

Exercice 24 En revenant à la définition, on a ∀ ( i, j ) ∈ [ [1 , n ] ] 2 B i,j = A n +1 -i,n +1 -j . On passe donc de A à B par une « symétrie centrale ».

Théorème 48 D'après la proposition 46 de la page 93, il est équivalent d'établir le résultat pour les matrices ou pour les endomorphismes.

- Si un endomorphisme u est trigonalisable, alors son polynôme caractéristique est égal à celui d'une matrice triangulaire supérieure ; il est donc scindé sur I K, d'après la proposition 25 de la page 79.
- Montrons la réciproque par récurrence.

Pour n = 1 il n'y a rien à prouver.

Supposons le résultat vrai au rang n ⩾ 1 et considérons u ∈ L ( E ) tel que dim E = n +1 et χ u soit scindé.

Comme χ u est scindé il possède une racine. Par conséquent, il existe λ ∈ sp ( u ) et x un vecteur propre associé. Complétons x en une base B de E de sorte que :

$$\text {Mat} _ { B } ( u ) = \left ( \begin{array} { c c } \lambda & L \\ 0 & A \end{array} \right ) , \\$$

où le bloc nul est une colonne de M n, 1 ( I K ) , L ∈ M 1 ,n ( I K ) et A ∈ M n ( I K ) .

Notons P n +1 la matrice par blocs P n +1 = ( 1 0 0 P n ) . Il s'agit d'une matrice inver-

En développant le polynôme caractéristique de u par rapport à la première colonne, on obtient χ u ( X ) = ( X -λ ) χ A ( X ) . Comme χ u est scindé sur IK, on en déduit que χ A l'est également. D'après l'hypothèse de récurrence, l'endomorphisme canoniquement associé à A est trigonalisable, il existe donc P n ∈ GL n ( I K ) tel que P -1 n AP n soit triangulaire supérieure.

$$\ s i b l e \ d i n v e r s \ P _ { n + 1 } ^ { - 1 } & = \left ( \begin{array} { c c } 1 & 0 \\ 0 & P _ { n } ^ { - 1 } \end{array} \right ) . \\ \ U n p d u i t \ p a r \ b l o c s \ d o n n e \ a l o r s \ & \colon$$

Un produit par blocs donne alors :

$$U \prod { u } { \prod { p } { u } } \, \par { b l o c s \, d o n n e \, a l o s } \colon \\ P _ { n + 1 } ^ { - 1 } \, \pi { M a t _ { B } ( u ) } \, P _ { n + 1 } = \left ( \begin{array} { c c } 1 & 0 \\ 0 & P _ { n } ^ { - 1 } \end{array} \right ) \left ( \begin{array} { c c } \lambda & L \\ 0 & A \end{array} \right ) \left ( \begin{array} { c c } 1 & 0 \\ 0 & P _ { n } \end{array} \right ) \\ = \left ( \begin{array} { c c } \lambda & L \\ 0 & P _ { n } ^ { - 1 } A \end{array} \right ) \left ( \begin{array} { c c } 1 & 0 \\ 0 & P _ { n } \end{array} \right ) = \left ( \begin{array} { c c } \lambda & L P _ { n } \\ 0 & P _ { n } ^ { - 1 } A P _ { n } \end{array} \right ) . \\ \ A i n s i _ { n + 1 } P _ { n } ( u ) \, P _ { n + 1 } \, \text {est triangular are superieure, ce qui permet de conclosure que} \, u$$

Ainsi P -1 n +1 Mat B ( u ) P n +1 est triangulaire supérieure, ce qui permet de conclure que u est trigonalisable.

Exercice 25 Le polynôme caractéristique de u F divise celui de u qui est scindé. Ainsi, le polynôme caractéristique de u F est scindé donc u F est trigonalisable.

Exercice 26 Comme cela a été fait en remarque, il existe une base ( u, v, w ) telle que, en notant P la matrice de passage de la base canonique de I K 3 à cette base, on ait :

$$P ^ { - 1 } A P = \left ( \begin{array} { c c c } \lambda & 0 & \alpha \\ 0 & \mu & \beta \\ 0 & 0 & \mu \end{array} \right ) .$$

BK

## D´ emonstrations et solutions des exercices du cours

Soit ( a, b, c ) ∈ I K 3 et f l'endomorphisme canoniquement associé à A .

On pose w ′ = au + bv + cw avec c non nul de sorte que la famille ( u, v, w ′ ) soit une base.

On a alors :

$$f ( w ^ { \prime } ) = a \lambda u + b \mu v + c \left ( \alpha u + \beta v + \mu w \right ) = \left ( a \lambda + c \alpha - a \mu \right ) u + \left ( b \mu + c \beta - b \mu \right ) v + \mu w ^ { \prime } .$$

Ainsi, on prend a = cα μ -λ , de sorte que la matrice de f dans la base ( u, v, w ′ ) soit

̸

$$C _ { 2 } + 2 C _ { 1 } - C _ { 3 } \ d o n n e \colon \\ \chi _ { A } \left ( X \right ) = \left | \begin{array} { c c c } X & 2 X & - 3 \\ 1 & X & - 6 \\ - 2 & - X & X + 1 0 \end{array} \right | . \\ \intertext { s l _ { 1 } , l _ { 2 } e t l _ { 3 } e l s l i g n e s d u n o u v e a u d \hat { e } t e r m i n } \intertext { i . } L _ { 3 } \leftarrow L _ { 3 } + L _ { 2 } \ d o n n e n t \ ;$$

$$\ A i n s i , \, o n \, p r e n d \, \ a & = \frac { c \alpha } { \mu - \lambda } \, , \, \text {d} e \\ \hat { \ e g a l e } \, \hat { a } & \left ( \begin{array} { c c c } \lambda & 0 & 0 \\ 0 & \mu & c \beta \\ 0 & 0 & \mu \end{array} \right ) \, . \\ \text {Commime dim } E _ { \mu } \left ( f \right ) & = 1 \, , \, \text {on}$$

Comme dim E μ ( f ) = 1, on a β = 0 et l'on prend c = 1 /β pour obtenir la forme annoncée.

## Exercice 27

1. Pour le calcul de χ A ( X ), notons C 1 , C 2 et C 3 les colonnes de la matrice XI 3 -A . L'opération C 2 ← C 2 +2 C 1 -C 3 donne :

∣ ∣ En notant cette fois L 1 , L 2 et L 3 les lignes du nouveau déterminant, les opérations L 1 ← L 1 -2 L 2 et L 3 ← L 3 + L 2 donnent :

Une liste de valeurs propres de A est donc (0 , -1 , -1). Comme la matrice :

$$L _ { 1 } - 2 L _ { 2 } \ e t \ L _ { 3 } \leftarrow L _ { 3 } + L _ { 2 } \ d o n n e n t \colon \\ \chi _ { A } ( X ) = X \left | \begin{array} { c c c } X - 2 & 0 & 9 \\ 1 & 1 & - 6 \\ - 1 & 0 & X + 4 \end{array} \right | = X \left ( X + 1 \right ) ^ { 2 } . \\ \ e t e d v a l e u r s \text { pres} \, d e A \ e s t \, d o n c \, ( 0 , - 1 , - 1 ) . \, C o m m e \, l a \, m a t r i c e \\ \left ( \begin{array} { c c c } 1 & 3 & 3 \end{array} \right )$$

n'est pas de rang 1, on a dim E -1 ( A ) = 2.

$$\begin{array} { c } \text {propres de A est done (0, - 1 , - 1).} \end{array} \\ \\ A + I _ { 3 } = \left ( \begin{array} { c c c } 1 & 3 & 3 \\ - 1 & 9 & 6 \\ 2 & - 1 4 & - 9 \end{array} \right ) \\ \intertext { o n a d i m E _ { - 1 } ( A ) \neq 2 . }$$

D'après le corollaire 45 de la page 91, la matrice A n'est pas diagonalisable.

̸

2. Comme χ A est scindé, la matrice A est trigonalisable, d'après le théorème 48 de la page 93. En étudiant les systèmes AX = 0 et AX = -X , on obtient facilement que :
- E -1 ( A ) = Vect ( v ), avec v = ⎛ ⎝ 3 3 -4 ⎞ ⎠ .

$$\text {que} \colon \\ \bullet \quad E _ { 0 } \left ( A \right ) & = \text {Vect} \left ( u \right ) , \text { avec} \ u = \left ( \begin{array} { c c } & & 2 \\ & & 1 \\ & & 1 \end{array} \right ) , \\ \bullet \quad E _ { 1 } \left ( A \right ) = \text {Vect} \left ( u \right ) \text {, avec} \ v = \left ( \begin{array} { c c } & & 3 \\ & & 3 \\ & & 3 \end{array} \right )$$

BL

## BVCWCPD4CXD8D6CT BE BA CA AJ CTCSD9CRD8CXD3D2 CSCTD7 CTD2CSD3D1D3D6D4CWCXD7D1CTD7

On peut compléter ( u, v ) en une base de M 3 , 1 ( I K ) à l'aide de w = ⎛ ⎝ 1 0 0 ⎞ ⎠ .

de M 3 , 1 ( I K ) à la base ( u, v, w ), il existe ( α, β, γ ) ∈ I K 3 tel que :

En notant P = ⎛ ⎝ 2 3 1 1 3 0 -1 -4 0 ⎞ ⎠ la matrice de passage de la base canonique

$$E \left ( u , v , w \right ) , & \text { if existe } \left ( \alpha , \beta , \gamma \right ) \in \text {K} ^ { - 1 } \ t e l \text { of } \\ P ^ { - 1 } A P & = \left ( \begin{array} { c c c } 0 & 0 & \alpha \\ 0 & - 1 & \beta \\ 0 & 0 & \gamma \end{array} \right ) . \\ & \left ( \begin{array} { c c c } 0 & 4 & 3 \\ 0 & 4 & 3 \end{array} \right )$$

On peut soit calculer P -1 = ⎝ 0 4 3 0 -1 -1 1 -5 -3 ⎠

⎛ ⎞ et obtenir, par un simple calcul

$$\begin{array} { r l } { \ m a t r i c { y } { l , P ^ { - 1 } A P = } \left ( \begin{array} { l l l } { 1 } & { - 5 } & { - 3 } \end{array} \right ) , } \\ { \ m a t r i c { y } { l , P ^ { - 1 } A P = } \left ( \begin{array} { l l l } { 0 } & { 0 } & { 2 } \\ { 0 } & { - 1 } & { - 1 } \\ { 0 } & { 0 } & { - 1 } \end{array} \right ) . } \\ { \ m a t r i c { y } { l , P ^ { - 1 } A P = } \left ( \begin{array} { l l l } { 0 } & { 0 } & { - 1 } \end{array} \right ) , } \\ { \ m a t r i c { y } { l , P ^ { - 1 } A P = } \left ( \begin{array} { l l l } { 0 } & { 0 } & { 1 } \end{array} \right ) , } \end{array}$$

$$\text { on en dueduit que } P ^ { - 1 } A P & = \left ( \begin{array} { c c } 2 & \end{array} \right ) \\ \text { on en dueduit que } P ^ { - 1 } A P & = \left ( \begin{array} { c c } 0 & 0 & 2 \\ 0 & - 1 & - 1 \\ 0 & 0 & - 1 \end{array} \right ) . \\$$

On peut aussi obtenir Aw = ⎛ ⎝ 0 -1 2 ⎞ ⎠ = 2 u -v -w par résolution d'un système ;

## Exercice 28

1. On a χ A ( X ) = ∣ ∣ ∣ ∣ ∣ ∣ X -14 -18 -18 6 X +7 9 2 3 X +1 ∣ ∣ ∣ ∣ ∣ ∣ . En retranchant la deuxième colonne de la troisième, il vient :

∣ ∣ En ajoutant la dernière ligne à la deuxième, puis en développant par rapport à la dernière colonne, on obtient :

$$\begin{array} { r } { 1 e , i l v i v \colon } \\ { \chi _ { A } ( X ) = \left | \begin{array} { c c c } X - 1 4 & - 1 8 & 0 \\ 6 & X + 7 & - X + 2 \\ 2 & 3 & X - 2 \end{array} \right | . } \\ { l a d r n i e r e l i g n e \dot { a } l a d e u x i e m e , p u i s e n d e l o p p a n t p a n t } \\ { n n e , o n o b t i e n t \colon } \end{array}$$

$$\text {dernière colonne, on obtient :} \\ \chi _ { A } \left ( X \right ) = \left | \begin{array} { c c c } X - 1 4 & - 1 8 & 0 \\ 8 & X + 1 0 & 0 \\ 2 & 3 & X - 2 \\ \end{array} \right | = \left ( X - 2 \right ) \left | \begin{array} { c c c } X - 1 4 & - 1 8 & 0 \\ 8 & X + 1 0 & 0 \\ \end{array} \right | \\ = \left ( X - 2 \right ) \left ( X ^ { 2 } - 4 X + 4 \right ) = \left ( X - 2 \right ) ^ { 3 } . \\ \text {Ainsi} \, \chi _ { A } \, \text {est scindé et admet 2 pour racine triple. Comme A # 2I_{3}, A n'est pas} \\ \text {diagonalisable, d'après l'exemple 1 de la page 88.}$$

Ainsi χ A est scindé et admet 2 pour racine triple. Comme A = 2 I 3 , A n'est pas diagonalisable, d'après l'exemple 1 de la page 88.

Comme χ A est scindé, la matrice A est trigonalisable.

BEBC

̸

## D´ emonstrations et solutions des exercices du cours

2. On cherche une base ( U, V, W ) de M 3 , 1 ( I K ) telle que :

Les vecteurs U et V sont donc à chercher dans le sous-espace propre de A pour la valeur propre 2. Comme A -2 I 3 = ⎛ ⎝ 12 18 18 -6 -9 -9 -2 -3 -3 ⎞ ⎠ est de rang 1, l'espace propre E 2 ( A ) est le plan de I K 3 d'équation 2 x +3 y +3 z = 0.

$$\begin{array} { r l } { e } & ( U , V , W ) \, d e \ \mathcal { M } _ { 3 , 1 } ( \mathbb { I } K ) \ t e l l e \ q u e \colon } \\ & \left \{ \begin{array} { l l l } { ( A - 2 I _ { 3 } ) \, U } & = } & { 0 } \\ { ( A - 2 I _ { 3 } ) \, V } & = } & { 0 } \\ { ( A - 2 I _ { 3 } ) \, W } & = } & { V . } \end{array} } \\ { V \, s o n t \, d o n c \, \hat { a } \, c h e r c h e r \, d a n s \, l e \, s o u s \, - e s p a } \\ & \left \{ \begin{array} { l l l } { 1 2 } & { 1 8 } & { 1 8 } \end{array} \right \} } \end{array}$$

De plus, le vecteur V doit appartenir à Im( A -2 I 3 ) = Vect ⎛ ⎝ 6 -3 -1 ⎞ ⎠ .

Les vecteurs U et V forment une base du plan E 2 ( A ) d'équation 2 x +3 y +3 z = 0 et W ̸∈ E 2 ( A ) donc la famille ( U, V, W ) est une base de M 3 , 1 ( I K ) vérifiant ( ⋆ ).

$$& \Pr o n s \ W = \left ( \begin{array} { c } 1 \\ 0 \\ 0 \end{array} \right ) , \, V = \left ( \begin{array} { c } 1 2 \\ - 6 \\ - 2 \end{array} \right ) , \, \text {puis} \ U = \left ( \begin{array} { c } 0 \\ 1 \\ - 1 \end{array} \right ) . \\ & \text {Les vecteurs} \ U \ et \ V \ f o r m e \ base \, d u \, \text { plan } E _ { 2 } ( A ) \, d ^ { \prime } \, \text {equation} \, 2 x + 1$$

$$\ e t \ W \not \in E _ { 2 } ( A ) \ d o n c \ l a \ f a m i lle \ ( U , V , W ) \ e s t \ u n e \ b a s e \ d \ \mathcal { M } _ { 3 , 1 } ( I K ) \ \text { verify} \\ \text {Si} \ l o n \ p o s e \ P = \left ( \begin{array} { c c c } 0 & 1 2 & 1 \\ 1 & - 6 & 0 \\ - 1 & - 2 & 0 \end{array} \right ) , \, a lors \ P \in \mathcal { G } _ { 3 } ( I K ) \ e t \colon \\$$

## Exercice 29

1. Le résultat est immédiat si E est de dimension 1.

Supposons désormais le résultat vrai pour tout espace vectoriel de dimension dim E 1 et considérons un endomorphisme u annulé par un polynôme scindé

$$P ( X ) = \prod _ { k = 1 } ^ { \prod } ( X - \beta _ { k } ) . \, L a \, \text { relation } ( u - \beta _ { 1 } \, \text {Id} _ { E } ) \circ \dots \circ ( u - \beta _ { m } \, \text {Id} _ { E } ) = 0 \, \text { implies} \\$$

alors qu'il existe i ∈ [ [1 , m ] ] tel que ( u -β i Id E ) soit non inversible. L'endomorphisme non injectif ( u -β i Id E ) est alors d'image F strictement contenue dans E . Choisissons alors un hyperplan H de E contenant F .

-m ∏

Comme F = Im( u -β i Id E ) ⊂ H , l'hyperplan H est stable par ( u -β i Id E ) et donc par u . L'endomorphisme induit u H vérifie P ( u H ) = 0 ; il est donc annulé par un polynôme scindé et, par hypothèse de récurrence, trigonalisable.

Il existe donc une base B ′ de H dans laquelle la matrice de u H est triangulaire supérieure. Dans toute base B de E , obtenue en complétant B ′ par un seul vecteur, la matrice de u est triangulaire supérieure ; ce qui conclut la récurrence.

BEBD

$$P ^ { - 1 } A P = \left ( \begin{array} { c c c } 2 & 0 & 0 \\ 0 & 2 & 1 \\ 0 & 0 & 2 \end{array} \right ) .$$

## BVCWCPD4CXD8D6CT BE BA CA AJ CTCSD9CRD8CXD3D2 CSCTD7 CTD2CSD3D1D3D6D4CWCXD7D1CTD7

2. Supposons que la matrice de u dans la base B = ( e 1 , . . . , e n ) soit de la forme :

Notons alors F i le sous-espace vectoriel Vect( e 1 , . . . , e i ) . Les relations

$$\begin{pmatrix} \text {ce de u dans la base } \mathcal { B } = ( e _ { 1 } , \dots , \dots , \dots ) \\ 0 & \ddots & \vdots \\ \vdots & \ddots & \ddots & \vdots \\ 0 & \dots & 0 & \alpha _ { n } \end{pmatrix} .$$

$$( u - \alpha _ { i } \text { Id} _ { E } ) \left ( e _ { i } \right ) \in F _ { i - 1 } \quad \text {et} \quad \forall k \in [ 1 , i - 1 ] \ \ u ( e _ { k } ) \in F _ { i - 1 } \\ \\ ( u - \alpha _ { i } \text { Id} _ { E } ) \left ( e _ { i } \right ) \in F _ { i - 1 } \quad \text {et} \quad \forall k \in [ 1 , i - 1 ] \ \ u ( e _ { k } ) \in F _ { i - 1 } \\ \\ \\ ( u - \alpha _ { i } \text { Id} _ { E } ) \left ( e _ { i } \right ) \in F _ { i - 1 } \quad \text {et} \quad \forall k \in [ 1 , i - 1 ] \ \ u ( e _ { k } ) \in F _ { i - 1 } \\$$

montrent que l'on a ( u -α i Id E ) ( F i ) ⊂ F i -1 pour tout i. Le sous-espace vectoriel :

$$( u - \alpha _ { 1 } \, I d _ { E } ) \circ \dots \circ ( u - \alpha _ { n } \, I d _ { E } ) \left ( F _ { n } \right ) \\ \intertext { u d o n s } \intertext { w d o n s }$$

est donc contenu dans :

$$( u - \alpha _ { 1 } \, I d _ { E } ) \circ \dots \circ ( u - \alpha _ { n - 1 } \, I d _ { E } ) \, ( F _ { n - 1 } ) \\ ( u - \alpha _ { 1 } \, I d _ { E } ) \circ \dots \circ ( u - \alpha _ { n - 1 } \, I d _ { E } ) \, ( F _ { n - 1 } ) \\$$

et par itération dans ( u -α 1 Id E ) ( F 1 ) qui est réduit à { 0 } . On a donc χ u ( u ) = 0 .

3. D'après la question précédente et le théorème 48 de la page 93, si u est un endomorphisme trigonalisable de E , alors il est annulé par un polynôme scindé. La réciproque ayant été montrée à la première question, l'équivalence est prouvée.

## Exercice 30

1. Comme e λ est vecteur propre de D pour la valeur propre λ , en appliquant la proposition 18, on obtient :
2. Soit P un polynôme annulateur de D . Comme les fonctions e λ sont toutes non nulles, on a, d'après la première question :

$$\begin{array} { c } \vdots \\ P ( D ) \left ( e _ { \lambda } \right ) = P \left ( \lambda \right ) e _ { \lambda } . \\ \end{array}$$

$$\forall \lambda \in \mathbb { I } R \ P \left ( \lambda \right ) = 0 . \\ \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n g t a l l } \intertext { i n s f i n t i n$$

Le polynôme P , ayant une infinité de racines, est donc nul.

Par conséquent, l'idéal annulateur de D soit réduit au polynôme nul.

## Proposition 54

1. On considère ϕ u l'application linéaire qui à tout polynôme P associe P ( u ) . Comme L ( E ) est de dimension finie (égale à n 2 si dim E = n ), le théorème du rang implique la non injectivité de ϕ u puisque IK [ X ] est de dimension infinie.
2. Il suffit d'appliquer ce qui précède à l'endomorphisme canoniquement associé à A .

## Exercice 31

1. · Si p = 0, on a π p = X .
- Dans les autres cas, comme p n'est pas une homothétie et vérifie p 2 = p , on a π p = X 2 -X .
- Si p = Id E , on a π p = X -1.
2. · Si s = Id E , on a π s = X -1.
- Dans les autres cas, comme s n'est pas une homothétie et vérifie s 2 = Id E , on a π s = X 2 -1.
- Si s = -Id E , on a π s = X +1.

BEBE

## Exercice 32

- On sait, d'après la proposition 20, que toute valeur propre de u est racine de π u .
- Pour la réciproque, on raisonne par l'absurde. Soit μ une racine de π u non valeur propre de u . On peut écrire : π = ( X μ ) P , avec deg ( P ) &lt; deg ( π ).

Comme μ sp( u ), on a ( u μ Id E ) ( E

$$( u - \mu \, I d _ { E } ) \circ P \left ( u \right ) & = \pi _ { u } ( u ) = 0 \\ \intertext { u r m o w } \pi _ { 0 } = \pi _ { 0 } \otimes \pi _ { 0 } \, n u _ { 1 } \, D _ { 0 } \, n o n \, n u _ { 2 } \, o n \, n v _ { 1 } \, O ( K )$$

- u -u ̸∈ -∈ GL ). On déduit alors de :

que P ( u ) = 0. Comme π u est non nul, P non plus car I K [ X ] est intègre. Or deg ( P ) &lt; deg ( π u ), ce qui contredit le caractère minimal de π u .

En conclusion, toute racine de π u est valeur propre de u .

Proposition 55 La famille F = ( u k ) k ∈ [ [0 ,d -1] ] est bien sûr une famille d'endomorphismes de IK [ u ] .

$$\bullet \quad & \text { so } ( \lambda _ { 0 } , \dots , \lambda _ { d - 1 } ) \in \mathbb { K } ^ { d } \ \{ ( 0 , \dots , 0 ) \} \ \text { tel que } \sum _ { k = 0 } ^ { d - 1 } \lambda _ { k } u ^ { k } = 0 . \\ & \quad \text {Le polonum } P = \sum _ { k } ^ { d - 1 } \lambda _ { k } X ^ { k } \ e s t \ a lors \, \text {un polonum} \, \text {anullateur non null de } u$$

strictement plus petit que d = deg π u , ce qui contredit la définition du polynôme minimal π u . La famille F est donc libre.

Le polynôme P = d -1 ∑ k =0 λ k X k est alors un polynôme annulateur non nul de u , de degré

- Soit v ∈ I K [ u ] ; il existe donc P ∈ I K [ X ] tel que v = P ( u ) . La division euclidienne de P par π u s'écrit :

$$P = Q \pi _ { u } + R \ \ a v e c { \ \deg ( R ) < d } .$$

En appliquant le morphisme d'algèbres ϕ u , on obtient :

$$v = P \left ( u \right ) & = Q \left ( u \right ) \circ \pi _ { u } \left ( u \right ) + R \left ( u \right ) = R \left ( u \right ) , \\ ( \, ) \quad & 0 \, \subsetneq \, C \quad , \quad ( D ) \quad , \quad 1 \quad , \quad ( D ) \quad , \quad 0 \, \subsetneq \, U \quad , \quad ( I ) \quad , \quad 0 \, \subsetneq \, D \quad ,$$

En conclusion, la famille F est une base de IK [ u ] .

puisque π u ( u ) = 0 . Comme deg ( R ) &lt; d , on a v ∈ Vect ( Id E , u, . . . , u d -1 ) , ce qui prouve que la famille F est une famille génératrice de I K [ u ] .

## Exercice 33

1. · On a immédiatement :

d'où l'on déduit par récurrence :

$$\forall k \in [ 0 , p - 2 ] \ A E _ { k } = E _ { k + 1 } , \\ \intertext { a r w o w w o }$$

$$\forall k \in [ 0 , p - 1 ] \ \ A ^ { k } E _ { 0 } = E _ { k } . \\$$

̸

- La famille A k E 0 k ∈ [ [0 ,p -1] ] est donc libre. Par suite, si Q ∈ I K p -1 [ X ] est un polynôme non nul, on a Q ( A ) E = 0 et donc Q ( A ) = 0.

Comme il n'existe pas de polynôme annulateur non nul de A de degré inférieur ou égal à p 1, on a deg ( π ) ⩾ p .

2. · On a AE p -1 = -p -1 ∑ k =0 a k E k , c'est-à-dire :
2. ( ) 0 -A

Par suite, P ( A ) E 0 = 0.

$$A ^ { p } E _ { 0 } = - \sum _ { k = 0 } ^ { p - 1 } a _ { k } A ^ { k } E _ { 0 } .$$

̸

## D´ emonstrations et solutions des exercices du cours

BEBF

## BVCWCPD4CXD8D6CT BE BA CA AJ CTCSD9CRD8CXD3D2 CSCTD7 CTD2CSD3D1D3D6D4CWCXD7D1CTD7

- Pour k ∈ [ [1 , p -1] ] , on a P ( A ) E k = P ( A ) A k E 0 = A k P ( A ) E 0 = 0 , en utilisant la commutativité de I K [ A ] .
- Comme ( E 0 , . . . , E p -1 ) est une base de M p, 1 ( I K ), on en déduit P ( A ) = 0. Le polynôme P est un polynôme unitaire de degré p , annulateur de A . D'après la première question, on a π A = P .

$$u \ p r e c { i } { 4 } \ q u n o { 1 , o n } \ u n _ { A } = & 1 . \\ \text {Exercise 34 } & \ \ N o t o n s \ F _ { x } = \text {Vect} \left ( ( u ^ { k } ( x ) ) _ { k \in \mathbb { N } } \right ) . \\ & \ \bullet \ \text {Si} \ F \ e s t \ u n \ s o u s \text {space vectoriel de } E \text { stable par }$$

$$\forall k \in \mathbb { N } \ \ u ^ { k } \left ( x \right ) \in F , \\ \intertext { v a r k } \ s u t + s u t + s u t = 0 \ s u t + s u t \cdot s u t = 0 \intertext { r e f } \intertext { s u t } \ s u t = 0 \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t } \intertext { s u t$$

- Si F est un sous-espace vectoriel de E stable par u et contenant x , on a :

donc F x ⊂ F . Comme F x est stable par u et contient x , F x est le plus petit sous-espace vectoriel de E stable par u et contenant x .

- La famille de F x , ( u k ( x ) ) 0 ⩽ k ⩽ p , contient p éléments, il suffit donc de montrer qu'elle est génératrice pour conclure.

Soit y ∈ F x . Il existe P ∈ I K [ X ] tel que y = P ( u )( x ).

∈ p

Par ailleurs, la famille à p + 1 éléments, ( u k ( x ) ) 0 ⩽ k ⩽ p , est liée donc il existe T I K [ X ] non nul tel que T ( u )( x ) = 0.

On effectue la division euclidienne de P par T :

$$P = Q T + R \ a v e c { \deg ( R ) } < p .$$

On en déduit y = P ( u ) ( x ) = Q ( u ) ◦ T ( u ) ( x ) + R ( u ) ( x ). Comme T ( u ) ( x ) = 0 et deg ( R ) &lt; p -1, on a alors y ∈ Vect ( ( u k ( x ) ) 0 ⩽ k ⩽ p -1 ) .

Théorème 56 Soit x ∈ E \ { 0 } et F x le plus petit sous-espace vectoriel de E stable par u et contenant x dont on note p la dimension. D'après le lemme précédent, ( u k ( x ) ) 0 ⩽ k ⩽ p -1 est une base de F x donc il existe ( a 0 , . . . , a p -1 ) ∈ I K p tel que

En conclusion, la famille ( u k ( x ) ) 0 ⩽ k ⩽ p -1 engendre F x , c'est est donc une base.

u p ( x ) = -p -1 ∑ k =0 a k u k ( x ) . Il en résulte que la matrice de l'endomorphisme induit u F x

Or, d'après les exercices 17 et 33, si A est une matrice compagnon, alors π A = χ A . Par conséquent, π u Fx = χ u Fx D'après la proposition 32, χ u x divise χ u donc χ u ( u x ) = 0 . Comme x ∈ E x , on peut écrire :

par u sur F x dans la base ( u k ( x ) ) 0 ⩽ k ⩽ p -1 est une matrice compagnon.

$$\chi _ { u } \left ( u \right ) \left ( x \right ) = \chi _ { u } \left ( u _ { x } \right ) \left ( x \right ) = 0 .$$

Cette dernière égalité a été établie pour tout x ∈ E \ { 0 } . On en déduit que χ u ( u ) = 0 .

Exercice 35 On a vu que χ A ( X ) = X 3 -3 X 2 +3 X -2. En appliquant le théorème de Cayley-Hamilton, on obtient A 3 -3 A 2 +3 A -2 I 3 = 0. On en déduit :

Par suite, A est inversible et l'on a A -1 = 1 2 ( A 2 -3 A +3 I 3 ) .

BEBG

$$\text {obtient } A ^ { 2 } - 3 A ^ { 2 } + 3 A - 2 I _ { 3 } & = 0 . \, . \, . \\ A \left ( \frac { A ^ { 2 } } { 2 } - \frac { 3 A } { 2 } + \frac { 3 I _ { 3 } } { 2 } \right ) & = I _ { 3 } .$$

Théorème 58 On procède par récurrence sur r ⩾ 2 .

- Montrons le résultat pour r = 2 .

Soit P 1 , P 2 deux polynômes premiers entre eux et P = P 1 P 2 .

- ∗ Comme P ( u ) = P 1 ( u ) ◦ P 2 ( u ) , on a Ker P 2 ( u ) ⊂ Ker P ( u ) . Par commutativité de IK [ u ] , on a aussi P ( u ) = P 2 ( u ) ◦ P 1 ( u ) puis Ker P 1 ( u ) ⊂ Ker P ( u ) . Par suite, Ker P 1 ( u ) + Ker P 2 ( u ) ⊂ Ker P ( u ) .
- ∗ D'après le théorème de Bézout, il existe ( U 1 , U 2 ) ∈ I K [ X ] 2 tel que P 1 U 1 + P 2 U 2 = 1 ; on a donc P 1 ( u ) ◦ U 1 ( u ) + P 2 ( u ) ◦ U 2 ( u ) = Id E . Soit x ∈ Ker P ( u ) ; posons :

On a alors x = x + x

$$x _ { 1 } = P _ { 2 } \left ( u \circ U _ { 2 } \left ( u \right ) \left ( x \right ) \right ) \quad \text {et} \quad x _ { 2 } = P _ { 1 } \left ( u \circ U _ { 1 } \left ( u \right ) \left ( x \right ) . \\ \text {On a alors } x = x _ { 1 } + x _ { 2 } \ e t \colon \\ P _ { 1 } ( u ) ( x _ { 1 } ) = P _ { 1 } ( u ) \circ P _ { 2 } \left ( u \circ U _ { 2 } \left ( u \right ) \left ( x \right ) = U _ { 2 } \left ( u \right ) \circ P _ { 1 } ( u ) \circ P _ { 2 } \left ( u \right ) ( x ) \\ = U _ { 2 } ( u ) \circ P ( u ) ( x ) = 0 . \\ \text {danc } x _ { 1 } \in K \, \text {Per} \left ( u \right ) \ e t , \, \text {de } \hat { m } \hat { e } \, x _ { 2 } \in K \, \text {Per} \left ( u \right ) . \, \text {On a donicmetatable} \, I ^ { \prime } \text {inclusion} \, .$$

donc x 1 ∈ Ker P 1 ( u ) et, de même x 2 ∈ Ker P 2 ( u ) . On a donc établi l'inclusion :

$$K e r \, P \left ( u \right ) & \subset K e r \, P _ { 1 } \left ( u \right ) + K e r \, P _ { 2 } \left ( u \right ) \\ \\ \left ( u \right ) \left ( u \right ) & \subset \left ( K e r \, P _ { 1 } \left ( u \right ) + K e r \, P _ { 2 } \left ( u \right ) \right ) \\$$

et, avec le point précédent, l'égalité Ker P ( u ) = Ker P 1 ( u ) + Ker P 2 ( u ) .

- ∗ Si x ∈ Ker P 1 ( u ) ∩ Ker P 2 ( u ) , l'égalité x = U 1 ( u ) ◦ P 1 ( u ) ( x )+ U 2 ( u ) ◦ P 2 ( u ) ( x ) montre que x = 0 . Par suite, Ker P 1 ( u ) ∩ Ker P 2 ( u ) = { 0 } .
- Soit r ⩾ 3 tel que le résultat soit vrai au rang r -1 . Considérons ( P 1 , . . . , P r ) , une famille de r polynômes deux à deux premiers entre eux, et P = r ∏ k =1 P k .

On a donc prouvé Ker P ( u ) = Ker P 1 ( u ) ⊕ Ker P 2 ( u ) .

Posons Q = r -1 ∏ k =1 P k ; les polynômes Q et P r sont premiers entre eux, car si un polynôme irréductible divise Q et P r , il divise l'un des P k , avec k ∈ [ [1 , r -1] ] , et P r , ce qui est contraire aux hypothèses.

D'après le premier point, on a Ker P ( u ) = Ker Q ( u ) ⊕ Ker P r ( u ) et, d'après l'hypothèse de récurrence, on a Ker Q ( u ) = r -1 ⊕ k =1 Ker P k ( u ) .

Corollaire 59 C'est une conséquence immédiate du lemme des noyaux.

On en déduit Ker P ( u ) = r ⊕ k =1 Ker P k ( u ) , ce qui achève la récurrence.

## Exercice 36

- Commençons par le montrer pour r = 2. D'après le théorème de Bézout, il existe ( U 1 , U 2 ) ∈ I K [ X ] 2 tel que P 1 U 1 + P 2 U 2 = 1.

On a donc P 1 ( u ) ◦ U 1 ( u ) + P 2 ( u ) ◦ U 2 ( u ) = Id E ce qui, pour tout x ∈ E donne :

$$x = \underbrace { P _ { 2 } \left ( u \right ) \circ U _ { 2 } \left ( u \right ) \left ( x \right ) } _ { \in K e r { P _ { 1 } ( u ) } } + \underbrace { P _ { 1 } \left ( u \right ) \circ U _ { 1 } \left ( u \right ) \left ( x \right ) } _ { \in K e r { P _ { 2 } ( u ) } } .$$

## BVCWCPD4CXD8D6CT BE BA CA AJ CTCSD9CRD8CXD3D2 CSCTD7 CTD2CSD3D1D3D6D4CWCXD7D1CTD7

Ainsi, les projections associées à la décomposition :

$$K e r \, P ( u ) & = K e r \, P _ { 1 } ( u ) \oplus K e r \, P _ { 2 } ( u ) \\$$

sont les endomorphismes ( U 1 P 1 ) ( u ) et ( U 2 P 2 ) ( u ).

- Soit r ⩾ 3 tel que le résultat soit vrai au rang r -1. Considérons ( P 1 , . . . , P r ), une famille de r polynômes deux à deux premiers entre eux, et P = r ∏ k =1 P k tel que P ( u ) = 0.

On pose alors Q = r -1 ∏ k =1 P k ; les polynômes Q et P r sont premiers entre eux (car si un polynôme irréductible divise Q et P r , il divise l'un des P k , avec k ∈ [ [1 , r -1] ] , et P r , ce qui est contraire aux hypothèses).

D'après le premier point, on a E = Ker Q ( u ) ⊕ Ker P r ( u ) et il existe des polynômes Q 1 et Q 2 tels que Q 1 ( u ) soit la projection sur Ker Q ( u ) et Q 2 ( u ), celle sur Ker P r ( u ).

Si l'on considère ˜ u l'endomorphisme induit pas u sur Ker Q ( u ), alors Q (˜ u ) = 0.

D'après l'hypothèse de récurrence, on a Ker Q (˜ u ) = r -1 ⊕ k =1 Ker P k (˜ u ) et, pour tout

Ker Q (˜ u ) = Ker Q ( u ). De plus, pour tout i ∈ [ [1 , r -1] ] , x i appartient à Ker P i ( u ) = Ker P i (˜ u ) (car Ker P i (˜ u ) = Ker P i ( u ) ∩ Ker Q ( u )) donc :

i ∈ [ [1 , r ] ] , il existe un polynôme R i tel que , R i (˜ u ) soit la projection sur Ker P i (˜ u ). Soit x ∈ E . Considérons sa décomposition x = x 1 + · · · + x r dans la somme directe r ⊕ k =1 Ker P k ( u ). Le vecteur x ′ = x 1 + · · · + x r -1 appartient à

$$x _ { i } = R _ { i } ( \tilde { u } ) ( x ^ { \prime } ) = R _ { i } ( u ) ( x ^ { \prime } ) = R _ { i } ( u ) \left ( Q _ { 1 } ( u ) \right ) .$$

Par conséquent, pour tout i ∈ [ [1 , r -1] ] , la projection sur Ker P i ( u ) est R i Q ( u ) ; c'est donc un polynôme en u . Celle sur Ker P r ( u ) étant égale à Q 2 ( u ), cela achève la récurrence.

## Théorème 60

- Supposons ( i ) et prouvons ( ii ) . Comme u est diagonalisable, on a :

$$E = \bigoplus _ { i = 1 } ^ { p } E _ { \lambda _ { i } } \left ( u \right ) \ \ a v e { \quad } s p \left ( u \right ) = \{ \lambda _ { 1 } , \dots , \lambda _ { p } \} \, .$$

Considérons le polynôme scindé à racines simples P = p ∏ i =1 ( X -λ i ) . L'endomorphisme P ( u ) coïncide avec l'endomorphisme nul sur tous les E λ i ( u ) ; ils sont donc égaux ; ce qui prouve que P est un polynôme annulateur de u .

Ainsi, l'endomorphisme u est annulé par le polynôme P qui est scindé simple.

- L'implication ( ii ) = ⇒ ( iii ) est évidente, puisque tout diviseur d'un polynôme scindé à racines simples est scindé à racines simples et que le polynôme minimal de u divise tout polynôme annulateur de u .

## D´ emonstrations et solutions des exercices du cours

- Supposons ( iii ) et prouvons ( i ) . Soit π u = p ∏ i =1 ( X -λ i ) le polynôme minimal de u ; on a vu dans l'exercice 32 de la page 97 que sp ( u ) = { λ 1 , . . . , λ p } . Comme les λ i sont deux à deux distincts, les polynômes X -λ i sont deux à deux premiers entre eux. D'après le lemme des noyaux, on a p ⊕ i =1 E λ i ( u ) = E ; par suite, u est diagonalisable, ce qui établit ( i ) .
- Corollaire 61 En effet, d'après le théorème 60 le polynôme minimal π u de u est scindé à racines simples et, comme π u ( u F ) = 0 , on déduit du même théorème que u F est diagonalisable.
- Exercice 37 Le sens direct est clair puisque dans une base de diagonalisation simultanée, les matrices des endomorphismes sont diagonales donc commutent deux à deux. Montrons la réciproque par récurrence sur la dimension de E .

Elle est évidente si E est de dimension 1.

Soit n ⩾ 2. Supposons le résultat démontré sur tout espace vectoriel de dimension strictement inférieur à n et considérons un espace vectoriel E de dimension n ainsi qu'une famille ( u i ) i ∈ I d'endomorphismes de E diagonalisables et commutant deux à deux.

- Si tous les u i sont des homothéties, n'importe quelle base de E est une base de diagonalisation commune aux u i .
- Sinon, il existe i 0 ∈ I tel que u i 0 ne soit pas une homothétie. On peut alors écrire E = F ⊕ G où F est un sous-espace vectoriel propre de u i 0 et G la somme non réduite à { 0 } des autres sous-espaces vectoriels propres de cet endomorphisme. Ces sous-espaces vectoriels sont stables par u i pour tout i par hypothèse de commutation. Les familles ( u ′ i ) i ∈ I et ( u ′′ i ) i ∈ I d'endomorphismes induits sur F et G sont alors formées d'endomorphismes diagonalisables commutant deux à deux. Les dimensions de F et G étant strictement inférieures à celle de E, elles possèdent des bases B ′ et B ′′ de diagonalisation simultanée. La réunion B de B ′ et B ′′ fournit une base de diagonalisation simultanée des ( u i ) i ∈ I .

## Proposition 62

- Soit u ∈ L ( E ) nilpotent d'indice r . Montrons, par récurrence sur n , que son polynôme caractéristique est X n .

Si n = 1 , alors, comme Ker u = { 0 } , u = 0 puis χ u = X .

̸

Supposons le résultat vérifié pour les espaces vectoriels de dimension strictement inférieure à celle de E .

Comme u n'est pas injectif, il existe un vecteur x non nul appartenant au noyau de u . Complétons x en une base B de E , de sorte que :

$$\begin{array} { c } { { \bar { \ } e } \, B \, d e \, E \, , d e \, s o r t e \, q u e \, . } } \\ { { M a t _ { B } ( u ) = \left ( \begin{array} { c c } { 0 } & { L } \\ { 0 } & { A } \end{array} \right ) , } } } \\ { { 1 } \, C \, M a t _ { B } ( u ) } \end{array}$$

où L ∈ M 1 ,n -1 ( I K ) et A ∈ M n -1 ( I K ) .

BEBJ

## BVCWCPD4CXD8D6CT BE BA CA AJ CTCSD9CRD8CXD3D2 CSCTD7 CTD2CSD3D1D3D6D4CWCXD7D1CTD7

On vérifie alors que Mat B ( u r ) = ( 0 L ′ 0 A r ) . Ainsi A r = 0 donc l'endomorphisme canoniquement associé à A est nilpotent. Par hypothèse de récurrence, on a χ A = X n -1 , ce qui permet de conclure car χ u = X × χ A ( X ) .

- Si χ u est égal à X n , l'endomorphisme u est scindé donc il existe une base dans laquelle la matrice de u est triangulaire supérieure. Comme la diagonale de cette matrice est formée de la liste des valeurs propres de u, cette matrice est triangulaire supérieure stricte.
- Supposons qu'il existe une base ( e 1 , . . . , e n ) dans laquelle la matrice A de u est triangulaire supérieure stricte. Ainsi, u ( e 1 ) = 0 et :

$$\forall i \in \mathbb { [ } 2 , n ] \ \ u ( e _ { i } ) \in \text {Vect} \left ( e _ { 1 } , \dots , e _ { i - 1 } \right ) . \\ \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \quad \\ \qu$$

Par suite, pour tout i ∈ [ [2 , n ] ] , u i -1 ( e i ) ∈ Vect( e 1 ) puis u i ( e i ) = 0 . On en déduit que, pour tout i ∈ [ [1 , n ] ] , u n ( e i ) = 0 , et donc que u n = 0 .

Exercice 38 Soit ( α 0 , . . . , α r -1 ) ∈ I K r tel que r -1 ∑ k =0 α k u k ( x 0 ) = 0.

alors u r -2 , il vient α 1 u r -1 ( x 0 ) = 0 et donc α 1 = 0 .

On a alors u r -1 ( r -1 ∑ k =0 α k u k ( x 0 ) ) = α 0 u r -1 ( x 0 ) = 0 et donc α 0 = 0 . En appliquant

On montre ainsi que α 0 = · · · = α r -1 = 0 et donc que la famille ( u k ( x 0 ) ) 0 ⩽ k ⩽ r -1 est libre.

## Exercice 39

1. D'après l'exercice précédent, la famille ( u k ( x 0 ) ) 0 ⩽ k ⩽ n -1 est libre. Cette famille comportant n éléments, c'est une base de E.
2. Soit x = n -1 ∑ ℓ =0 α l u l ( x 0 ) . On a :

$$u ^ { k } ( x ) = \sum _ { \ell = 0 } ^ { n - 1 } \alpha _ { \ell } u ^ { k + \ell } ( x _ { 0 } ) = \sum _ { \ell = 0 } ^ { n - k - 1 } \alpha _ { l } u ^ { k + l } ( x _ { 0 } ) . \\ \text {Kor} u ^ { k } \text { si } \text { et} \text { element} \text { si } \text { pour} \text { tout } \text { i } \in \mathbb { [ } 0 \text { } n - k - 1 \text { ] } \text { le } \text { scaler}$$

Donc x ∈ Ker u k si, et seulement si, pour tout i ∈ [ [0 , n -k -1] ] , le scalaire α i est nul. Le sous-espace Ker u k est donc engendré par la famille libre ( u ℓ ( x 0 ) ) ℓ ⩾ n -k , ce qui prouve qu'il est de dimension k.

3. Soit F un sous-espace vectoriel stable par u de dimension k ∈ [ [0 , n ] ] . L'endomorphisme u F induit par u est alors nilpotent donc vérifie u k F = 0. Par conséquent, F est inclus dans Ker( u k ).

Pour des raisons de dimension, on a donc F = Ker u k .

Exercice 40 Prouvons cette assertion par récurrence sur n.

Elle est évidente si n = 1 puisque, dans ce cas, L ( E ) = I K Id E donc tout endomorphisme nilpotent est nul.

BEBK

## D´ emonstrations et solutions des exercices du cours

Supposons-la acquise pour toute dimension strictement inférieure à n. L'espace F = Im u n est de dimension r &lt; n puisque u n n'est pas bijective et est stable par u i pour tout i. La famille ( u ′ 1 , . . . , u ′ r ) des endomorphismes induits vérifiant les mêmes hypothèses, il vient donc u ′ 1 ◦ · · · ◦ u ′ r = 0 . Cela implique u ′ 1 ◦ · · · ◦ u ′ n -1 = 0 et, vu la définition de F :

$$u _ { 1 } \circ \dots \circ u _ { n } = 0 .$$

Théorème 68 Si u est annulé par un polynôme scindé r ∏ i =1 ( X -λ i ) α i où les scalaires λ 1 , . . . , λ r sont distincts deux à deux, alors le lemme des noyaux permet d'écrire :

$$K e r \, P \left ( u \right ) & = \bigoplus _ { k = 1 } ^ { r } K e r \left ( u - \lambda _ { i } \, I d \right ) ^ { \alpha _ { i } } . \\ \intertext { l e s o u s e a n s e c t o r i e l } \left [ e x t e r i o n \right ] \, E _ { i } - K e r \left ( u - \lambda _ { i } \, I d \right ) ^ { \alpha _ { i } }$$

Pour tout i ∈ [ [1 , r ] ] , le sous-espace vectoriel E i = Ker( u -λ i Id) α i est stable par u et l'endomorphisme u i induit par u sur E i vérifie ( u i -λ i Id E i ) α i = 0 . Ainsi, l'endomorphisme n i = u i -λ i Id E i est nilpotent et u i est la somme de l'homothétie λ i Id E i et d'un endomorphismes nilpotent.

L'endomorphisme induit u i est donc la somme d'une homothétie et d'un endomorphisme nilpotent.

## CBB3CTD2D8D6CPCM AGD2CTD6 CTD8 CPD4D4D6D3CUD3D2CSCXD6

- 2.1 Soit u ∈ L ( E ) avec E de dimension finie.

Prouver que si Ker u possède un supplémentaire F stable par u , alors F = Im u .

- 2.2 Déterminer les sous-espaces de I R n stables par tous les endomorphismes :

avec σ ∈ S n .

$$u _ { \sigma } \colon ( x _ { 1 } , \dots , x _ { n } ) \longmapsto ( x _ { \sigma ( 1 ) } , \dots , x _ { \sigma ( n ) } )$$

- 2.3 Soit E un espace vectoriel de dimension finie. Déterminer les endomorphismes stabilisant tous les hyperplans de

E.

- 2.4 Soit F un sous-espace vectoriel de E et L F ( E ) l'ensemble des endomorphismes stabilisant F .
1. Montrer que l'application ϕ : u ↦→ u F un morphisme d'algèbres de L F ( E ) vers L ( F ) .
2. On suppose F de dimension finie. Montrer que l'inverse de tout élément inversible u de L F ( E ) stabilise aussi F et que l'on a :

$$( u ^ { - 1 } ) _ { F } = ( u _ { F } ) ^ { - 1 } .$$

3. En considérant l'endomorphisme de I K ( X ) qui à P associe XP , prouver que le résultat de la question précédente est faux si F n'est pas de dimension finie.
4. On suppose que F

Montrer que le morphisme u u de ( E ) vers ( F ) est surjectif.

- possède un supplémentaire. ↦→ F L F L
- ⋆ 2.5 Soit u et v deux endomorphismes d'un espace vectoriel E de dimension finie tels que v soit nilpotent et vérifie u ◦ v = v ◦ u . Montrer que l'on a :

$$\det ( u + v ) = \det u .$$

$$2 . 6 \ S o i t \ A = \left ( \begin{array} { c c c } 1 & 2 & - 2 \\ 2 & 1 & - 2 \\ & 2 & 2 & - 3 \end{array} \right ) . \\ 1 . \ D e r \term e r m i n e \ u n e \ m a t r i c e \ P$$

1. Déterminer une matrice P inversible et une matrice D diagonale telles que A = PDP -1 .
2. Déterminer le polynôme minimal de A .

$$2 . 7 \ S o i t \ B = \left ( \begin{array} { c c c } 3 & 0 & 8 \\ 3 & - 1 & 6 \\ - 2 & 0 & - 5 \end{array} \right ) . \\ 1 . \ L a \ m a t r i c e \ B \ e s t \text {-ellie diagonalals} \\ 2 . \ D o t \text {-polynomial} \widehat { \L a } \min$$

1. La matrice B est-elle diagonalisable ?
2. Déterminer le polynôme minimal de la matrice B .
3. Montrer que matrice B est semblable à ⎛ ⎝ -1 0 0 0 -1 1 0 0 -1 ⎞ ⎠

BFBC

$$-$$

- 2.8 Diagonaliser la matrice réelle de taille n :

$$c e r \text {celle de taille } n \colon \\ A = \left ( \begin{array} { c c c c c } 0 & 1 & 0 & \dots & 0 \\ 1 & 0 & 1 & & \vdots \\ 0 & 1 & \ddots & \ddots & 0 \\ \vdots & & \ddots & 0 & 1 \\ 0 & \dots & 0 & 1 & 0 \end{array} \right ) \\ ( i , j ) \ a v e c \ | i - j | = 1 \ v a l e n t \ 1 , \, l e s \ a u t r e$$

(les éléments d'indices ( i, j ) avec | i -j | = 1 valent 1 , les autres sont nuls).

D2CSCXCRCPD8CXD3D2 BM Il s'agit d'un exercice classique où il est difficile d'obtenir le polynôme caractéristique de A sous forme factorisé. On déterminera donc les éléments propres par la résolution de systèmes.

- 2.9 Soit A une matrice de M n ( I R ) vérifiant A ( A 2 + A + I n ) = 0 . Montrer que le rang de A est pair.
- 2.10 Soit A ∈ M n ( I R ) telle que :

Montrer que A est de déterminant strictement positif.

- 2.11 (Polytechnique 2015)

$$A ^ { 3 } - 3 A - 5 I _ { n } = 0 \\ \intertext { i n v e r } \intertext { i n t i o n t e r } \intertext { i n t i f }$$

$$2 . 1 1 \, ( P o l y t e c h n i q u e \ 2 0 1 5 ) \\ \hat { R } \dot { s o u d r e } \, d a n s \ \mathcal { M } _ { 2 } ( \mathbb { C } ) \, l \hat { \epsilon } \dot { q u a t i o n } \ M ^ { 2 } + M & = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} .$$

- 2.12 Soit A ∈ M 2 ( Z Z ) .

On suppose qu'il existe un entier naturel non nul p tel que A = I 2 Montrer que A 12 = I 2 .

p .

- ⋆ 2.13 Soit u un endomorphisme de I R n vérifiant u 2 + u +Id I R n = 0 .
2. Montrer qu'il existe une base de I R n dans laquelle la matrice de u est diagonale par blocs de blocs ( 0 -1 1 -1 ) et, qu'en particulier, n est pair.
1. Soit F un sous-espace stable par u et x / ∈ F. Montrer que Vect ( x, u ( x ) ) est un plan, stable par u et en somme directe avec F.
- 2.14 On dit qu'un nombre complexe α est algébrique s'il est racine d'un polynôme unitaire (donc non nul) P ( X ) ∈ Q [ X ] .
1. Montrer qu'un nombre complexe est algébrique si, et seulement s'il est valeur propre d'une matrice à coefficients rationnels.
2. En déduire que si un nombre complexe α est algébrique, alors, pour tout r ∈ I N , le nombre complexe α r est aussi algébrique.

On pourra utiliser le résultat sur les matrices compagnons de l'exercice 17 .

BFBD

## BVCWCPD4CXD8D6CT BE BA CA AJ CTCSD9CRD8CXD3D2 CSCTD7 CTD2CSD3D1D3D6D4CWCXD7D1CTD7

- 2.15 1. Montrer qu'il existe ( a 0 , . . . , a n -1 ) ∈ I K n tel que :

$$\forall P \in \mathbb { K } _ { n - 1 } \left [ X \right ] \ \ P ( X + n ) + \sum _ { k = 0 } ^ { n - 1 } a _ { k } P ( X + k ) = 0 . \\$$

2. Déterminer une telle famille.

On pourra utiliser l'endomorphisme P ( X ) ↦→ P ( X +1) de I K [ X ]

- 2.16 Déterminer les sous-espaces stables par l'endomorphisme u canoniquement associé à la matrice réelle :

$$A = \left ( \begin{array} { c c c } 0 & 1 & 1 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{array} \right ) . \\$$

- 2.17 Soit a un endomorphisme d'un espace vectoriel de dimension finie E . On considère les endomorphismes M a : u ↦→ a ◦ u et ad ( a ) : u ↦→ a ◦ u -u ◦ a de L ( E ).
1. Déterminer les éléments propres de l'endomorphisme M a en fonction de ceux de a . En déduire que l'endomorphisme M a est diagonalisable, si, et seulement si, a l'est.
2. Montrer que si a est diagonalisable, alors l'endomorphisme ad ( a ) l'est aussi et préciser ses valeurs propres en fonction de celles de a .
3. Montrer que si a est nilpotent, alors M a et ad ( a ) le sont également.
- 2.18 Soit u un endomorphisme d'un espace vectoriel E de dimension finie n et λ une valeur propre de u. Montrer que les assertions suivantes sont équivalentes :
6. ( i ) E λ ( u ) = Ker ( u -λ Id E ) 2 ,
7. ( iii ) E λ ( u ) possède un supplémentaire stable par u ,
8. ( ii ) E λ ( u ) ⊕ Im( u -λ Id E ) = E ,
9. ( iv ) la dimension de E λ ( u ) est égale à la multiplicité de λ dans le polynôme caractéristique de u ,
10. ( v ) λ est une racine simple du polynôme minimal de u .

$$2 . 1 9 \, \text {Sort} \, A \in \mathcal { M } _ { n } ( \mathbb { C } ) \, \text { et } \, B = \left ( \begin{array} { c c } 0 & A \\ I _ { n } & 0 \end{array} \right ) \in \mathcal { M } _ { 2 n } ( \mathbb { C } ) . \\ \\ 1 \, \ D o t { s } \, \text {min} \, \text {o} \, \text {pol} \, \hat { \hat { \Omega } } \, \text {o} \, \text {sort} \, \text {i} \, \text {i} \, \text {two} \, \text {o} \, \text {f} \, \text {on} \, \text {f} \, \text {o} \, \text {f} \, \text {on} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \text {o} \, \text {f} \, \$$

1. Déterminer le polynôme caractéristique de B en fonction de celui de A.
2. Discuter la diagonalisabilité de B en fonction de celle de A .
- 2.20 Soit A ∈ M n ( C ) . Montrer que la matrice par blocs :

$$B & = \left ( \begin{array} { c c } 4 A & 2 A \\ - 3 A & - A \end{array} \right ) \in \mathcal { M } _ { 2 n } ( \mathbb { C } ) \\$$

est diagonalisable si, et seulement si, A l'est.

BFBE

- 2.21 Soit A et B deux matrices de M n ( C ).
1. On suppose A inversible. Montrer que χ AB = χ BA .
3. En déduire que l'on a toujours χ AB = χ BA .
2. Soit r ∈ [ [0 , n ] ] . Prouver que χ J r B = χ BJ r où J r = ( I r 0 0 0 ) .
- 2.22 Soit A et B deux matrices de M n ( C ).

Montrer que A et B ont une valeur propre commune si, et seulement s'il existe une matrice U non nulle de M n ( C ) telle que AU = UB.

- 2.23 (Polytechnique 2015)

Soit A et B deux matrices de M n ( C ).

Montrer que s'il existe une matrice U de rang r tel que AU = UB, alors les polynômes caractéristiques de A et B ont un facteur commun de degré r

- 2.24 Soit u et v deux endomorphisme d'un C -espace vectoriel de dimension fine..
1. On suppose que u et v commutent. Montrer que u et v ont un vecteur propre commun.
2. On suppose que u ◦ v -v ◦ u = αu avec α ∈ C ∗ . Montrer que u est nilpotent et que u et v ont un vecteur propre commun.
3. En déduire que si u ◦ v -v ◦ u ∈ Vect( u, v ), alors u et v ont un vecteur propre commun.
- 2.25 (Polytechnique 2015)

Soit A et B deux matrices de M n ( C ) telles que AB = 0. Montrer qu'elles sont simultanément trigonalisables.

- 2.26 Soit A et B deux matrices de M n ( C ) vérifiant AB = BA.

Trouver une condition nécessaire et suffisante pour que la matrice par blocs :

$$M = \left ( \begin{array} { c c } A & B \\ 0 & A \end{array} \right ) .$$

soit diagonalisable.

- 2.27 Montrer qu'un endomorphisme u est nilpotent si, et seulement s'il vérifie Tr( u k ) = 0 pour tout k ∈ [ [1 , n ] ] .
- 2.28 (Centrale 2015)

Soit G un sous-groupe de GL n ( C ).

1. On suppose que G est fini.
2. (a) Montrer que pour tout g ∈ G , il existe un entier N g tel que g N g = I n .
3. (b) Montrer que tous les éléments de G sont diagonalisables et que { Tr g ; g ∈ G } est fini.
2. Établir la réciproque. Indication : considérer une base ( A 1 , . . . , A p ) de Vect( G ) et f : X ∈ G ↦→ (Tr( A 1 X ) , . . . , Tr( A p X )) .

BFBF

## CBD3D0D9D8CXD3D2 CSCTD7 CTDCCTD6CRCXCRCTD7

- 2.1 Supposons que E = F ⊕ Ker u , avec F stable par u . Grâce au théorème du rang, on a dim F = dimIm u .

Soit x ∈ Im u . Par définition, il existe t ∈ E tel que x = u ( t ). Comme F ⊕ Ker u , il existe ( t 1 , t 2 ) ∈ F × Ker u tel que t = t 1 + t 2 . On en déduit que x = u ( t 2 ) ∈ F car F est stable par u . Par suite, Im u ⊂ F puis Im u = F .

- 2.2 Il est clair que { 0 E } , I R n , la droite D = I R (1 , . . . , 1) et l'hyperplan H d'équation :

$$x _ { 1 } + \dots + x _ { n } = 0$$

sont stables par les u σ .

Réciproquement, soit F un sous-espace vectoriel de E stable par les u σ . S'il est inclus dans D , alors il est égal à { 0 } ou D. Sinon, il contient un vecteur x = ( x i ) 1 ⩽ i ⩽ n ayant deux composantes x r = x s , avec r &lt; s . Notons ( e i ) 1 ⩽ i ⩽ n la base canonique de I R n . Si l'on considère la transposition τ = ( r, s ), la stabilité de F implique que :

̸

$$( x _ { r } - x _ { s } ) \left ( e _ { r } - e _ { s } \right ) & = x - u _ { \tau } ( x ) \in F \\$$

puis que e r -e s ∈ F .

Pour tout i ∈ [ [1 , n -1] ] , il existe une permutation σ i qui transforme r en i et s en i +1 donc :

$$e _ { i } - e _ { i + 1 } = _ { u } \sigma _ { i } ( e _ { r } - e _ { s } ) \in F .$$

Comme les vecteurs e 1 -e 2 , . . . , e n -1 -e n sont indépendants, ils engendrent un hyperplan, et cet hyperplan est inclus dans H , puis égal à H pour des raisons de dimension. On en déduit que F contient H ; il est donc égal à H ou I R n .

Par conséquent, les sous-espaces de I R n stables par tous les endomorphismes u σ sont { 0 } , I R n , D = I R (1 , . . . , 1) et H .

- 2.3 Il est clair que les homothéties stabilisent les hyperplans.

Réciproquement, soit u un endomorphisme stabilisant tous les hyperplans, on va prouver qu'il s'agit d'une homothétie en établissant que, pour tout vecteur x ∈ E , la famille ( x, u ( x )) est liée (voir l'exercice 1 de la page 65).

Supposons par l'absurde, qu'il existe un vecteur x non nul tel que u ( x ) n'appartienne pas à I K x. La famille ( x, u ( x ) ) est alors libre, on peut donc la compléter en une base ( x, u ( x ) , e 3 , . . . , e n ) de E . L'endomorphisme u ne stabilise donc pas l'hyperplan Vect ( x, e 3 , . . . , e n ), ce qui est absurde.

Ainsi, si u stabilise les hyperplans, alors u est une homothétie.

BFBG

- 2.4 1. Il est évident que Id E appartient à L F ( E ) et que l'on a ϕ (Id E ) = Id F .

Pour tout x ∈ F, on a u ( x ) ∈ F, v ( x ) ∈ F et par suite ( αu + βv ) ( x ) ∈ F . L'application αu + βv appartient donc à L F ( E ) et ( αu + βv ) F = αu F + βv F . Ainsi, L F ( E ) est un sous-espace vectoriel de L ( E ) et ϕ est linéaire.

Soit ( u, v ) ∈ L F ( E ) 2 et ( α, β ) ∈ I K 2 .

Soit ( u, v ) ∈ L F ( E ) 2 .

Par suite, L F ( E ) est une algèbre et ϕ est un morphisme d'algèbres de L F ( E ) vers L ( F ) .

Pour tout x ∈ F , on a v ( x ) ∈ F puis u ( v ( x ) ) ∈ F . Ainsi u ◦ v appartient à L F ( E ) et ( u ◦ v ) ( x ) = u F ( v F ( x ) ) , donc ( u ◦ v ) F = u F ◦ v F .

2. Soit u appartenant à L F ( E ) ∩ GL ( E ). L'endomorphisme induit u F est injectif (car Ker u F = F ∩ Ker u ). Comme F est de dimension finie, le théorème du rang s'applique et implique la surjectivité et donc la bijectivité de u F .

Pour tout x de F, l'unique antécédent u -1 ( x ) de x par u appartient donc à F. Ainsi, u -1 appartient à L F ( E ) . La relation u ◦ u -1 = u -1 ◦ u = Id E entraîne :

$$u _ { F } \circ ( u ^ { - 1 } ) _ { F } = ( u ^ { - 1 } ) _ { F } \circ u _ { F } = I d _ { F } , \\ ) _ { F } ( 1 - u _ { F } \circ ( u ^ { - 1 } ) _ { F } ) _ { F } = ( u ^ { - 1 } ) _ { F } \circ u _ { F } = I d _ { F } ,$$

puis ( u -1 ) F = ( u F ) -1 .

3. L'endomorphisme u : Q ↦→ XQ , de l'espace des fractions rationnelles I K ( X ), est inversible et stabilise F = I K [ X ] mais l'endomorphisme induit u F n'est pas surjectif car l'unité 1 n'appartient pas à l'image de I K [ X ] par u . Le résultat de la question précédente n'est donc pas vrai si F n'est pas de dimension finie.
4. Supposons que le sous-espace vectoriel F possède un supplémentaire que l'on notera G et notons p la projection de E sur F parallèlement à G.

Soit v ∈ L ( F ). L'application u : E → E, x ↦→ v ◦ p ( x ) est un élément de L F ( E ) et u F = v ; ce qui prouve la surjectivité de ϕ .

- 2.5 Montrons le résultat par récurrence forte sur la dimension n ∈ I N ∗ de E .

Si n = 1 , alors l'endomorphisme v est nul et la proposition est évidente.

Soit n ∈ I N ∗ tel que la proposition soit vraie pour toute dimension strictement inférieure à n .

Considérons u et v deux endomorphismes de E , avec dim E = n , tels que u et v commutent et v soit nilpotent.

Comme v est nilpotent, l'endomorphisme v n'est pas inversible et la dimension r du sous-espace F = Im v appartient à [ [0 , n -1] ] . Si v = 0, alors le résultat est évident. On supposera donc désormais v non nul et donc que r &gt; 0.

Choisissons alors une base B de E adaptée à F. Comme F = Im v est stable par u et v, les matrices de u et v dans B sont de la forme :

$$\begin{array} { c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c$$

avec ( U 1 , 1 , V 1 , 1 ) ∈ M r ( I K ) 2 .

BFBH

## BVCWCPD4CXD8D6CT BE BA CA AJ CTCSD9CRD8CXD3D2 CSCTD7 CTD2CSD3D1D3D6D4CWCXD7D1CTD7

Comme u et v commutent, les endomorphismes u F et v F induits par u et v sur F aussi. De même, v F est nilpotent. La dimension de F étant strictement inférieure à n , l'hypothèse de récurrence donne :

$$\det ( u _ { F } + v _ { F } ) = \det u _ { F }$$

$$\det \left ( U _ { 1 , 1 } + V _ { 1 , 1 } \right ) = \det U _ { 1 , 1 } .$$

soit, en termes de matrices :

Par conséquent :

$$\begin{array} { r l } & { \ar \, c o n s e q u e n t \colon } \\ & { \quad d e t \left ( \begin{array} { c c } { U _ { 1 , 1 } + V _ { 1 , 1 } } & { U _ { 1 , 2 } + V _ { 1 , 2 } } \\ { 0 } & { U _ { 2 , 2 } } \end{array} \right ) = \det \left ( U _ { 1 , 1 } + V _ { 1 , 1 } \right ) \det U _ { 2 , 2 } } \\ & { = \det U _ { 1 , 1 } \det U _ { 2 , 2 } } \end{array}$$

donc det( u + v ) = det u.

- 2.6 1. L'opération élémentaire C 1 ← C 1 + C 2 + C 3 , donne :

$$& \text {En retranchant la première ligne aux deux autres, on a alors } ; \\ & \quad \chi _ { A } ( X ) = ( X - 1 ) \left | \begin{array} { c c c } 1 & & - 2 & 2 \\ & & & 0 \\ & & & 0 \\ & & & 0 \\ 0 & & & X + 1 \\ & & & 0 \\ & & & X + 1 \end{array} \right | = ( X - 1 ) ( X + 1 ) ^ { 2 } \, . \\ & \text {Les valours propres de A sont donc 1 de multiplicité 1 et -1 de multiplicité 2} . \\ & \text {On détermine le sous-espace propre E1 en réesolvant le système } \colon$$

$$2 . 6 \, \left [ 1 . \ L ^ { \prime } o p e r a t i o n \, \text {elementaire } C _ { 1 } \leftarrow C _ { 1 } + C _ { 2 } + C _ { 3 } , \, \text {donne } \colon \\ & \quad \left | \, X - 1 \right | \, - 2 \quad 2 \quad \left | \, 1 \right | \, - 2 \quad 2 \quad \left | \, 1 \right | \, - 2 \quad 2 \quad \left | \, . \, \\ & \quad \chi _ { A } ( X ) = \left | \, \begin{array} { c c c } X - 1 & - 2 & 2 \\ - 2 & X - 1 & 2 \\ - 2 & - 2 & X + 3 \end{array} \right | \, \left | \, 1 \right | \, X - 1 \quad 2 \quad 2 \quad \left | \, . \, \\ & \quad \text {En retranchant la premier ligne aux deux autres, on a alors } \\ & \quad \left | \, 1 \right | \, - 2 \quad 2 \quad \left | \, . \, \\$$

∣ ∣ Les valeurs propres de A sont donc 1 de multiplicité 1 et -1 de multiplicité 2 . On détermine le sous-espace propre E 1 en résolvant le système :

qui est équivalent à x = y = z. On a donc E 1 = I R f 1 avec f 1 = ⎛ ⎝ 1 1 1 ⎞ ⎠ .

$$\begin{array} { r l } & { \text {pace propre} \, E _ { 1 } \, e n r { \hat { s o l v a n t } } \, l e s o l } \\ & { \left \{ \begin{array} { l l l } { 2 y - 2 z } & { = } & { 0 } \\ { 2 x } & { - 2 z } & { = } & { 0 } \\ { 2 x + 2 y - 4 z } & { = } & { 0 } \end{array} } \end{array} \\ & { y = z . \, O n a d o n c \, E _ { 1 } = I R f _ { 1 } \, a v } \end{array}$$

On détermine le sous-espace propre E -1 en résolvant le système :

qui est équivalent à 2 x +2 y -2 z = 0 donc :

$$\begin{array} { r l } & { p a c e p r o p r e E _ { - 1 } e n r e s o l v a n t l e } \\ & { \left \{ \begin{array} { l l l } { 2 x + 2 y - 2 z } & { = } & { 0 } \\ { 2 x + 2 y - 2 z } & { = } & { 0 } \\ { 2 x + 2 y - 2 z } & { = } & { 0 } \end{array} } \\ & { + 2 y - 2 z = 0 d o n c \colon } \\ & { + z \choose z } \left ( - 1 \right ) } \end{array} \, .$$

$$f _ { 2 } = \left ( \begin{array} { c c } { { - 1 } } \\ { { 1 } } \\ { { 0 } } \end{array} \right ) \ e t \ f _ { 3 } = \left ( \begin{array} { c } { 1 } \\ { 0 } \\ { 1 } \end{array} \right ) .$$

$$\text { qui est équivalent à 2 x + 2 y - 2 z} = 0 \, \text { d'onc } \colon \\ E _ { - 1 } = \left \{ \left ( \begin{array} { c } - y + z \\ y \\ z \end{array} \right ) = y \left ( \begin{array} { c } - 1 \\ 1 \\ 0 \end{array} \right ) + z \left ( \begin{array} { c } 1 \\ 0 \\ 1 \end{array} \right ) , \, ( y , z ) \in \mathbb { K } ^ { 2 } \right \} . \\ \ A \text {is} \ E _ { - 1 } = \text {IR} _ { 2 } \oplus \text {IR} _ { 3 } \ a v e c \ f _ { 2 } = \left ( \begin{array} { c } - 1 \\ 1 \\ 0 \end{array} \right ) \ e t \ f _ { 3 } = \left ( \begin{array} { c } 1 \\ 0 \\ 1 \end{array} \right ) .$$

BFBI

Puisque dim E 1 +dim E -1 = 3 , la matrice A est diagonalisable et ( f 1 , f 2 , f 3 ) est une base de diagonalisation. Par conséquent :

avec :

$$A = P \left ( \begin{array} { c c c } 1 & 0 & 0 \\ 0 & - 1 & 0 \\ 0 & 0 & - 1 \end{array} \right ) P ^ { - 1 } \\$$

2. Puisque A est diagonalisable de spectre 1 , 1 , le polynôme minimal de A est :

$$\begin{array} { r l } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & { \quad } & {$$

$$\pi _ { A } ( X ) = ( X - 1 ) ( X + 1 ) .$$

- {-} .
- 2.7 1. En développant par rapport à la deuxième colonne, il vient χ B ( X ) = ( X +1) 3 . La matrice B n'a donc qu'une valeur propre : -1. Si elle était diagonalisable, alors elle serait égale à la matrice -I 3 ce qui n'est pas le cas. La matrice B n'est donc pas diagonalisable.
2. D'après le théorème de Cayley-Hamilton, le polynôme minimal de B est un diviseur de ( X +1) 3 .

̸

$$\text {seur de } ( X + 1 ) ^ { 3 } . \\ \text {Poisson alors } C = B + I _ { 3 } = \left ( \begin{array} { c c c } 4 & 0 & 8 \\ 3 & 0 & 6 \\ - 2 & 0 & - 4 \end{array} \right ) . \text { On a } C \neq 0 \ e t \ C ^ { 2 } = 0 . \text { Le } \\ \text {polyomé minimal de } B \ e s t d o n c \, \pi _ { B } ( X ) = ( X + 1 ) ^ { 2 } . \\ 3 . \text { On chesterne base } ( f _ { 1 } , f _ { 2 } , f _ { 3 } ) \text { telle que } f _ { 1 } \ e t \ f _ { 2 } \text { so } \text {des vecteurs propres de } B .$$

3. On cherche une base ( f 1 , f 2 , f 3 ) telle que f 1 et f 2 soit des vecteurs propres de B et que Bf 3 = f 2 -f 3 c'est-à-dire Cf 3 = f 2 .

On détermine E -1 en résolvant le système :

Si l'on prend un vecteur f 3 non nul, alors comme C 2 = 0, Cf 3 , s'il est non nul, est un vecteur propre de B . Il suffit de ne pas prendre f 3 dans E -1 puis de compléter f 2 = Cf 3 en une base ( f 1 , f 2 ) de E -1 pour conclure.

qui est équivalent à x +2 z = 0 .

$$\begin{array} { r l } & { \text {vlant le systeme } \colon } \\ & { \left \{ \begin{array} { l l l } { 4 x + 8 z } & { = } & { 0 } \\ { 3 x + 6 z } & { = } & { 0 } \\ { - 2 x - 4 z } & { = } & { 0 } \end{array} } \\ & { = 0 . } \end{array}$$

$$f _ { 2 } = C f _ { 3 } = \left ( \begin{array} { c c } 1 & \end{array} \right ) \\ \intertext { i n e b a s e d E _ { - 1 } , l a f m i lle ( f _ { 1 } , f _ { 2 } , f _ { 3 } ) e s t u n b a s d a n s l a q u e }$$

Ainsi, le vecteur f 3 = ⎛ ⎝ 0 0 1 ⎞ ⎠ n'appartient pas à E -1 . Comme les vecteurs :

forment une base de E -1 , la famille ( f 1 , f 2 , f 3 ) est une base dans laquelle l'endomorphisme u B canoniquement associé à B est :

BFBJ

$$\begin{pmatrix} \, \begin{matrix} - 1 & 0 & 0 \\ 0 & - 1 & 1 \\ 0 & 0 & - 1 \end{matrix} \end{pmatrix} .$$

## BVCWCPD4CXD8D6CT BE BA CA AJ CTCSD9CRD8CXD3D2 CSCTD7 CTD2CSD3D1D3D6D4CWCXD7D1CTD7

La matrice B est donc semblable à la matrice annoncée.

$$P = \left ( \begin{array} { c c c } 0 & 8 & 0 \\ 1 & 6 & 0 \\ 0 & - 4 & 1 \end{array} \right ) \quad \text {et} \quad P ^ { - 1 } = \frac { 1 } { 8 } \left ( \begin{array} { c c c } - 6 & 8 & 0 \\ 1 & 0 & 0 \\ 4 & 0 & 8 \end{array} \right ) .$$

Plus précisément, on a P -1 BP = ⎛ ⎝ -1 0 0 0 -1 1 0 0 -1 ⎞ ⎠ avec :

- 2.8 Il s'agit d'un exercice classique où il est difficile d'obtenir le polynôme caractéristique de A sous forme factorisé. On détermine donc ses éléments propres par la résolution de systèmes.

Soit X = ( x i ) 1 ⩽ i ⩽ n un vecteur propre de A associé au scalaire λ . Il est donc non nul et vérifie le système :

.

Si l'on pose x 0 = 0 et x n +1 = 0 , la suite ( x k ) 0 ⩽ k ⩽ n +1 est le début d'une suite vérifiant la relation de récurrence linéaire d'ordre deux :

$$\begin{array} { r l } & { e \colon } \\ & { \quad } \\ & { \quad } \\ & { x _ { 1 } - \lambda x _ { 2 } + x _ { 2 } } & = 0 } \\ & { \quad } \\ & { x _ { 1 } - \lambda x _ { 2 } + x _ { 3 } } & = 0 } \\ & { \quad } \\ & { \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots$$

$$x _ { k - 2 } - \lambda x _ { k - 1 } + x _ { k } = 0 .$$

L'équation caractéristique associée est X 2 -λX +1 de discriminant Δ = λ 2 -4. On étudie les différents cas suivant le signe de Δ.

- Si Δ = 0 c'est-à-dire si λ = ± 2, alors l'équation caractéristique admet une racine double ε = ± 1 et il existe des scalaires α et β tels que :

$$\forall k \in [ 0 , n + 1 ] \ \ x _ { k } = \alpha \varepsilon ^ { k } + \beta k \varepsilon ^ { k } . \\ 0 \quad 1 \cdot \dot { \cdot } \cdot \dot { \cdot } + \quad 0 \quad 0 \quad \dot { \cdot } \cdot \dot { \cdot } + \quad 0$$

Comme x 0 = x n +1 = 0, on obtient α = β = 0 ce qui contredit la non nullité de X .

- Si Δ &gt; 0, alors l'équation caractéristique admet deux racines réelles distinctes r 1 et r 2 = 1 /r 1 et il existe des scalaires α et β tels que :

$$\forall k \in [ 0 , n + 1 ] \quad x _ { k } = \alpha r _ { 1 } ^ { k } + \beta r _ { 2 } ^ { k } . \\$$

̸

Comme x 0 = x n +1 = 0, on obtient α = -β et α r n +1 1 ( r 2 n +2 1 -1 ) = 0, ce qui est impossible car r 1 = 1 et X = 0.

̸

Par conséquent, si λ est valeur propre, alors Δ &lt; 0. Il existe donc θ ∈ ]0 , π [ tel que λ = 2 cos θ . Les racines de X 2 -λX +1 étant e iθ et e -iθ , il existe des scalaires α et β tels que :

$$\forall k \in \mathbb { [ } 0 , n + 1 ] \quad x _ { k } = \alpha e ^ { i k \theta } + \beta e ^ { - i k \theta } . \\ 0 \, o n t r o i n o \, \alpha \, | \, \beta = 0 \, o t \, \cdot$$

La relation x 0 = 0 entraîne α + β = 0 et :

$$\forall k \in [ 0 , n + 1 ] \ \ x _ { k } = 2 \alpha i \sin ( k \theta ) .$$

BFBK

La relation x n +1 = 0 et la non nullité de X implique que sin ( ( n +1) θ ) = 0 , c'està-dire que θ est de la forme ℓπ ℓ Z Z .

$$e \ \frac { \ell n } { n + 1 } , \, \ell \in \mathbb { Z }$$

Il suffit alors de remonter les calculs, pour prouver que, pour tout l de [ [1 , n ] ] , le vecteur :

est un vecteur propre de A associé à la valeur propre λ ℓ = 2 cos ℓπ n +1 ·

$$X _ { l } & = \left ( \sin \frac { k \ell \pi } { n + 1 } \right ) _ { k \in [ 1 , n ] } \\$$

Les réels λ ℓ , ℓ ∈ [ [1 , n ] ] , étant deux à deux distincts du fait de l'injectivité de la fonction cos sur [0 , π ] , la matrice A est diagonalisable sur I R de spectre :

et la famille ( X ℓ ) ℓ ∈ [ [1 ,n ] ] est une base de diagonalisation.

$$0 , \pi ] \, , \, l a \ m a t r i c e \ A \ e s t \ d i a g n a l i s a b l e \ s u r \ \mathbb { R } \ d e s p \\ \quad & s p ( A ) = \left \{ 2 \cos \left ( \frac { \ell \pi } { n + 1 } \right ) \colon \ell \in \mathbb { I } , n \right \} \\ \ell \in [ 1 , n ] \ \ e s t \ u n e \ b a s e \ d i a g n a l i s a t i o n .$$

En fait, la matrice A est symétrique réelle et le théorème spectral (voir le chapitre 14 « Endomorphismes des espaces euclidiens ») prouve a priori qu'elle est diagonalisable et que la base ( X ℓ ) ℓ ∈ [ [1 ,n ] ] dont les vecteurs sont associés à des valeurs propres deux à deux distinctes est orthogonale. Nous allons redémontrer cette propriété.

Notons ϕ = π n +1 · Pour tous ℓ et ℓ ′ de [ [1 , n ] ] , on a :

$$n + 1 & & n + 1 & \\ & ( X _ { \ell } \, | \, X _ { \ell ^ { \prime } } ) = \sum _ { k = 1 } ^ { n } \sin ( k \ell \varphi ) \sin ( k \ell ^ { \prime } \varphi ) \\ & = \frac { 1 } { 2 } \sum _ { k = 1 } ^ { n } \cos \left ( ( \ell - \ell ^ { \prime } ) k \varphi \right ) - \frac { 1 } { 2 } \sum _ { k = 1 } ^ { n } \cos \left ( ( \ell + \ell ^ { \prime } ) k \varphi \right ) . \\ \intertext { u r } x \neq 0 [ 2 \pi ] , \, o n a \colon &$$

$$\text {Pour } x \neq & \, 0 [ 2 \pi ] , \, \text {on a } \colon \\ & \sum _ { k = 1 } ^ { n } \cos ( k x ) = R \sum _ { k = 1 } ^ { n } e ^ { i k x } = R e \left ( e ^ { i x } \frac { 1 - e ^ { i n x } } { 1 - e ^ { i x } } \right ) = R e \left ( e ^ { i x } \frac { e ^ { i n x / 2 } \sin ( ( n x / 2 ) } { e ^ { i x / 2 } \sin ( x / 2 ) } \right ) \\ & = \frac { \cos ( ( n + 1 ) x / 2 ) \sin ( ( n x / 2 ) } { \sin ( x / 2 ) } .$$

Pour x ̸≡ 0[2 π ] , on a :

En particulier, si p est un entier non multiple de 2( n +1), alors n ∑ k =1 cos( pkϕ ) est nul

Comme ℓ et ℓ ′ ont la même parité et appartiennent à [ [1 , n ] ] , il vient :

̸

Finalement, la famille (√ 2 n +1 X ℓ ) ℓ ∈ [ [1 ,n ] ] est une base orthonormée de diagonali-

sation de A .

La matrice de passage P correspondante est donc orthogonale et P -1 = t P .

si p est pair et égal à -1 sinon.

$$\L a m { \hat { \widehat { e } } } { \ p a r i t { \hat { e } } { \ e t \ a p p a r t i e n n e n t \hat { a } } } \left [ 1 , n \right ] , \text { il} \\ ( X _ { \ell } \left | \ X _ { \ell ^ { \prime } } \right ) = \begin{cases} 0 & \text {si } \ell \neq \ell ^ { \prime } \\ \frac { n + 1 } { 2 } & \sinon \\ \end{cases} \\ \text {le } \left ( \sqrt { \frac { 2 } { n + 1 } } X _ { \ell } \right ) _ { \ell \in \mathbb { I } [ 1 , n ] } \quad \text {est une base orthono}$$

- 2.9 Comme A est annulée par le polynôme X ( X 2 + X +1) scindé à racines simples dans C , elle est diagonalisable sur C et la dimension de son noyau est égal à la multiplicité de 0 dans χ A De plus, ses valeurs propres appartiennent à { 0 , j, j 2 } donc il existe des entiers p et q tels que Son polynôme caractéristique χ A soit égal à :

La matrice A étant réelle, son polynôme caractéristique aussi, donc p = q . Le théorème du rang donne alors rg A = 2 p .

$$q \ t e l s \ q e \text { So polynome caracteristiche } \chi _ { A } \text { soft eigen} \\ \chi _ { A } ( X ) = X ^ { n - p - q } \left ( X - j \right ) ^ { p } \left ( X - j ^ { 2 } \right ) ^ { q } . \\ \text {cant réelle, soin polynôme caractérisique auSSI, donc} \\ \text {née alors rg A = 2 p} ,$$

- 2.10 La matrice A est annulée par le polynôme P = X 3 -3 X -5. L'étude des variations de la fonction x ↦→ x 3 -3 x -5 montre que P a une unique racine réelle α strictement positive. Ses deux autres racines dans C sont donc complexes conjuguées. Il existe donc ω ∈ C \ I R tel que :

$$P & = ( X - \alpha ) ( X - \omega ) ( X - \overline { \omega } ) \\ \\$$

Puisque P annule A ses valeurs propres appartiennent à { α, ω, ω } donc il existe des entiers p et q tels que

$$\chi _ { A } ( X ) = ( X - \alpha ) ^ { n - p - q } ( X - \omega ) ^ { p } ( X - \overline { \omega } ) ^ { q } . \\ \intertext { t u n e m a t r i c e r $ \hat { \omega } $ e l l e $ l e $ o l v n o l $ e q $ }$$

Comme A est une matrice réelle, le polynôme χ A aussi, d'où p = q. Par conséquent :

$$\det A = ( - 1 ) ^ { n } \chi _ { A } ( 0 ) = \alpha ^ { n - 2 p } \left | \omega \right | ^ { 2 p } > 0 .$$

- 2.11 Raisonnons par analyse-synthèse.
- Considérons une matrice M solution.

Le polynôme ( X 2 + X )( X 2 + X -2) = X ( X +1)( X -1)( X +2) annule donc M . Comme ce polynôme est scindé à racines simples, on en déduit que M est diagonalisable.

La matrice A = ( 1 1 1 1 ) est annulée par son polynôme caractéristique X ( X -2).

$$\ n a l s a b l e . & & \ n a l s a b l e . & & \ S o i t \ P \in \mathcal { G L } _ { 2 } ( \mathbb { C } ) \ t e l \ q u e \ P ^ { - 1 } M P = \begin{pmatrix} \alpha & 0 \\ 0 & \beta \end{pmatrix} . \\ & & \ S o i t \ P \in \mathcal { G L } _ { 2 } ( \mathbb { C } ) \ t e l \ q u e \ P ^ { - 1 } M P = \begin{pmatrix} \alpha ^ { 2 } + \alpha & 0 \\ 0 & \beta \end{pmatrix} .$$

La matrice M a donc comme polynôme caractéristique (et donc annulateur) un des quatre polynômes suivants : X ( X -1), X ( X +2), ( X +1)( X -1) ou ( X +1)( X +2).

$$0 & \quad ( 0 \quad \beta ) ^ { \cdot } \\ \intertext { o n a l o r s $ P ^ { - 1 } A P = \begin{pmatrix} \alpha ^ { 2 } + \alpha & 0 \\ 0 & \beta ^ { 2 } + \beta \end{pmatrix} } \intertext { L a m t r i c e M a d o n c o m m e p o l u n o \hat { o m e } c a r a t e r i s }$$

- ∗ Dans le premier cas, les relations M 2 + M = A et M 2 -M = 0 donnent M = 1 2 A ;
- ∗ dans le deuxième cas, les relations M 2 + M = A et M 2 +2 M = 0 donnent M = -A ;
- ∗ dans le dernier cas, les relations M 2 + M = A et M 2 +3 M +2 I n = 0 donnent M = -1 2 A -I n .
- ∗ dans le troisième cas, les relations M 2 + M = A et M 2 -I n = 0 donnent M = A -I n ;
- On vérifie que les quatre matrices conviennent.

$$\bullet \ \text {On verifiable que les quatree matrices conviennent.} \\ \text {Par conséquent } \mathcal { S } = \left \{ \frac { 1 } { 2 } \left ( \begin{matrix} 1 & 1 \\ 1 & 1 \end{matrix} \right ) , \left ( \begin{matrix} - 1 & - 1 \\ - 1 & - 1 \end{matrix} \right ) , \left ( \begin{matrix} 0 & 1 \\ 1 & 0 \end{matrix} \right ) , \frac { 1 } { 2 } \left ( \begin{matrix} - 3 & - 1 \\ - 1 & - 3 \end{matrix} \right ) \right \} .$$

BGBC

- 2.12 La matrice A annule le polynôme X p -1 dont les racines complexes sont simples. Elle est donc diagonalisable dans M 2 ( C ) et ses valeurs propres sont des racines p -ièmes de l'unité. Ainsi, A est semblable, à une matrice diagonale Diag( α, β ) où α et β sont des racines p -ième de l'unité.

D'un autre côté, le polynôme caractéristique χ A ( X ) = X 2 + aX + b de A est à coefficients entiers. La relation a = -Tr A = -( α + β ) montre, du fait de l'inégalité triangulaire, que a est un entier de module inférieur ou égal à 2 et que b = det A = αβ est un entier de module 1 c'est-à-dire b = ± 1.

- Si A possède un valeur propre réelle, alors comme a est réel, l'autre valeur propre est également réelle. Comme α et β sont des racines p -ièmes de l'unité, la matrice A est alors semblable à Diag(1 , 1) , Diag(1 , -1) ou Diag( -1 , -1) et A 2 = I 2 .
- ∗ Diag( j, j 2 ) et dans ce cas A 3 = I 2 ;
- Si A possède une valeur propre non réelle, e iθ avec θ ̸≡ 0[ π ] , alors l'autre est conjuguée et leur produit b vaut 1. On en déduit que a = -2 cos θ ∈ {-1 , 0 , 1 } car a est un entier et θ ̸≡ 0[ π ] . Le polynôme caractéristique est alors égal à X 2 + X +1 , X 2 -X +1 ou X 2 +1 . La matrice A est semblable à :
- ∗ Diag( -j 2 , -j ) et dans ce cas A 6 = I 2
- ∗ ou Diag( i, -i ) et dans ce cas A 4 = I 2 .

Dans tous les cas, A 12 = I 2 et 12 est le plus petit entier convenable.

- 2.13 1. Supposons par l'absurde que Vect ( x, u ( x ) ) ne soit pas un plan. Comme le vecteur x est non nul, il existe donc un réel λ tel que u ( x ) = λx . Le réel λ étant une valeur propre de u , c'est une racine du polynôme annulateur X 2 + X +1, ce qui est absurde car ce polynôme n'a pas de racine réelle. Par conséquent, Vect ( x, u ( x ) ) est un plan.

$$\text {out} \ ( \lambda , \mu ) \in \mathbb { R } \ , \text { on a } \colon \\ u \ ( \lambda x + \mu u ( x ) ) = - \mu x + ( \lambda - \mu ) u ( x ) \in \text {Vect} \ ( x , u ( x ) ) \\ \text {Vect} \left ( x , u ( x ) \right ) \ \text {est stable par } u .$$

Pour tout ( λ, μ ) ∈ I R 2 , on a :

donc Vect ( x, u ( x ) ) est stable par u. Supposons par l'absurde qu'il existe y non nul dans F ∩ Vect ( x, u ( x ) ) . Comme cette intersection est stable par u , elle contient Vect ( y, u ( y ) ) , qui, d'après ce qui précède, est un plan. Pour des raisons de dimensions, on a donc :

puis Vect ( x, u ( x ) ) ⊂ F , ce qui n'est pas possible car x ̸∈ F . Ainsi, F et Vect x, u ( x ) sont en somme directe.

$$& \text {Plan.} \text { For des reasons of dimensions, on a d o n c } \\ & \quad F \cap \text {Vect} ( x , u ( x ) ) = \text {Vect} ( x , u ( x ) ) , \\ & ) \subset F , \, \text {ce qui n'est pas possible car } x \not \in F .$$

$$u ( e _ { 2 k } ) = u ^ { 2 } ( e _ { 2 k - 1 } ) = - u ( ( e _ { 2 k - 1 } ) ) - ( e _ { 2 k - 1 } ) = - e _ { 2 k } - e _ { 2 k - 1 }$$

- ( ) 2. Commençons par remarquer que si la matrice de u dans une base ( e 1 , · · · , e n ) est de la forme annoncée, alors n est pair et pour tout k ∈ [ [1 , n/ 2] ] , u ( e 2 k -1 ) = e 2 k . Réciproquement, s'il existe une base de la forme ( e 1 , u ( e 1 ) , . . . , e n/ 2 , u ( e n/ 2 ) ) , alors pour tout k ∈ [ [1 , n/ 2] ] :

BGBD

## BVCWCPD4CXD8D6CT BE BA CA AJ CTCSD9CRD8CXD3D2 CSCTD7 CTD2CSD3D1D3D6D4CWCXD7D1CTD7

donc la matrice de u dans cette base est de la forme annoncée.

On considère donc l'ensemble A des entiers k tels qu'il existe x 1 , . . . , x k de I R n avec x , u ( x ) , . . . , x , u ( x ) libre.

En utilisant la question précédente avec F = { 0 } , on montre que A est non vide. Elle est également bornée puisqu'une famille libre est de cardinal inférieur ou égal à n . Elle admet donc un maximum que nous noterons p . Il existe alors des vecteurs x 1 , . . . , x p de I R n tels que ( x 1 , u ( x 1 ) , . . . , x p , u ( x p ) ) soit libre. Le sous-espace :

( 1 1 k k )

$$F = \text {Vect} ( x _ { 1 } , u ( x _ { 1 } ) , \dots , x _ { p } , u ( x _ { p } ) ) = \bigoplus _ { k = 1 } ^ { p } \text {Vect} ( x _ { k } , u ( x _ { k } ) ) \\ \text {stable par } u . \ S ^ { \prime } i l \ n ^ { \prime } e s t \ p \ \tilde { e } g a l \ \mathring { a } \ I R ^ { \prime } , \ a lors \ i l \ \text {exist} \ x _ { p + 1 } \notin F \ e t , \ d ^ { \prime } a p \hat { r } \$$

est stable par u . S'il n'est pas égal à I R n , alors il existe x p +1 / ∈ F et, d'après la question précédente, Vect ( x p +1 , u ( x p +1 ) ) est en somme directe avec F. La famille ( x 1 , u ( x 1 ) , . . . , x p +1 , u ( x p +1 ) ) est alors libre ce qui contredit la définition de p. On a donc F = I R n , et par conséquent ( x 1 , u ( x 1 ) , . . . , x p , u ( x p ) ) est une base de I R n . Dans cette base, la matrice de u est de la forme désirée. On a aussi n = 2 p.

- 2.14 1. Si un nombre complexe α est valeur propre d'une matrice à coefficients rationnels, alors, il est racine de son polynôme caractéristique qui est unitaire et à coefficient rationnels, donc α est algébrique.

Réciproquement, si un nombre complexe α est algébrique, alors il est racine d'un polynôme unitaire P ( X ) = X p + r 1 X p -1 + · · · + r p de Q [ X ] . La matrice compagnon :

de M p ( Q ) étant de polynôme caractéristique P , α est valeur propre de C .

$$P ( X ) = X ^ { p } + r _ { 1 } X ^ { p } - + \cdots + r _ { p } \, d e \, \mathbb { Q } [ X ] \, . \\ C = \left ( \begin{array} { c c c c } 0 & \dots & \dots & 0 & - r _ { p } \\ 1 & \ddots & & & \\ \vdots & \ddots & \ddots & & \\ 0 & \dots & 1 & 0 & - r _ { 1 } \end{array} \right ) \\ \text {polymode caract$eristique $ P$, } \alpha \text { est value} \\ \text {complex} \, \alpha \, \text {brieque } \, \| \text {est alors value} \, \| _ { p }$$

2. Soit α un nombre complexe algébrique. Il est alors valeur propre d'une matrice M à coefficient rationnels. Pour tout entier r , α r est alors valeur propre de M r qui est à coefficients rationnels, ce qui prouve que α r est algébrique.
- 2.15 1. L'endomorphisme P ( X ) ↦→ P ( X + 1) de I K [ X ] induit un endomorphisme u de E = I K n -1 [ X ] . Notons :

$$\chi ( X ) = X ^ { n } + \sum _ { k = 0 } ^ { n - 1 } a _ { k } X ^ { k } \\ \text {tigeus} \ P u i s q u e \ u ^ { k } ( P ) \ e s t \ \vec { e } g a l \ \hat { a }$$

son polynôme caractéristique. Puisque u k ( P ) est égal à P ( X + k ) , on a d'après le théorème de Cayley-Hamilton :

$$\forall P \in \mathbb { K } _ { n - 1 } \left [ X \right ] \ \ P ( X + n ) + \sum _ { k = 0 } ^ { n - 1 } a _ { k } P ( X + k ) = 0 .$$

BGBE

2. L'endomorphisme Δ = u -Id E est nilpotent et vérifie Δ n = 0 puisque, pour P non constant, deg (Δ( P )) = deg P -1 . On a donc :

et :

Pour tout k ∈ [ [0 , n -1] ] , on pose a k = ( -1) k -n ( n k ) de sorte que :

$$0 & = ( u - I d _ { E } ) ^ { n } = \sum _ { k = 0 } ^ { n } ( - 1 ) ^ { n - k } \binom { n } { k } u ^ { k }$$

$$\forall P \in \mathbb { K } _ { n - 1 } \left [ X \right ] \ \sum _ { k = 0 } ^ { n } ( - 1 ) ^ { k } \binom { n } { k } P ( X + k ) = 0 . \\ k \in \mathbb { I } 0 , n - 1 \right ] , \, \text {on } \text {pose } a _ { k } = ( - 1 ) ^ { k - n } \binom { n } { k } \, \text {de sorte que } \colon$$

$$\forall P \in \mathbb { K } _ { n - 1 } \left [ X \right ] \ \ P ( X + n ) + \sum _ { k = 0 } ^ { n - 1 } a _ { k } P ( X + k ) = 0 .$$

- 2.16 Le polynôme caractéristique de A est χ A ( X ) = ( X -1) 2 ( X +1) et les sous espaces propres sont E 1 = I R e 1 et E -1 = I R e -1 avec :

Soit F un sous-espaces stable par l'endomorphisme u .

$$E _ { 1 } & = \text {IRe} _ { 1 } \ e t \ E _ { - 1 } = \text {IRe} _ { - 1 } \ a v e c \colon \\ & \quad e _ { 1 } = \left ( \begin{array} { c } 1 \\ 1 \\ 0 \end{array} \right ) \quad \text {et} \quad e _ { - 1 } = \left ( \begin{array} { c } - 1 \\ 1 \\ 0 \end{array} \right ) \, . \\ \intertext { s } \text {espaces stable par $ l$endomorphism} u .$$

- Si F est de dimension 0 ou 3, il est respectivement égal à { 0 } ou I R 3 .
- Si F est de dimension 2 , le polynôme caractéristique de l'endomorphisme induit est un polynôme de degré deux divisant χ A .
- Si F est de dimension 1, alors F est une droite engendrée par un vecteur propre de A c'est-à-dire F = I R e 1 ou F = I R e -1 .

$$& \text {II vaut donc (X - 1)^{2} ou (X - 1)(X + 1).} \\ & \text {Doris la non-primion ou} \ F o t \ o n t o n u \ d o n c l o w o r$$

Dans le second cas, F contient un vecteur propre associé à 1 et un vecteur propre associé à -1 . Il est donc égal à I R e 1 ⊕ I R e -1 .

Dans le premier cas, F est contenu dans le noyau de ( A -I 3 ) 2 qui est égal au plan d'équation 2 x -2 y -z = 0.

Ainsi, les sous-espaces stables par u sont { 0 } , I R 3 , I R e 1 , I R e -1 , I R e 1 ⊕ I R e -1 et le plan d'équation 2 x -2 y -z = 0.

- 2.17 1. Soit u ∈ L ( E ) et λ ∈ I K . On a l'équivalence :

$$a \circ u & = \lambda u \Longleftrightarrow I m \, u \subset E _ { \lambda } ( a ) . \\ \\ a ( \Gamma ) \vdash u & = \Gamma \, ( \Gamma ) \supseteq \Gamma \, ( \Gamma ) .$$

Ainsi, E λ ( M a ) = { u ∈ L ( E ) | Im u ⊂ E λ ( a ) } . En particulier,

$$E _ { \lambda } ( M _ { a } ) \simeq \mathcal { L } ( E , E _ { \lambda } ( a ) ) , \\$$

ce qui prouve que M a et a ont les mêmes valeurs propres. De plus, pour tout scalaire λ , dim E λ ( M a ) = dim E × dim E λ ( a ). Comme dim L ( E ) = dim E × dim E , on en déduit que M a est diagonalisable si, et seulement si, a l'est.

BGBF

## BVCWCPD4CXD8D6CT BE BA CA AJ CTCSD9CRD8CXD3D2 CSCTD7 CTD2CSD3D1D3D6D4CWCXD7D1CTD7

2. Supposons a diagonalisable et considérons B = ( e 1 , . . . , e n ) une base de diagonalisation de a et ( λ 1 , . . . , λ n ) les valeurs propres associées

Pour tout ( i, j ) ∈ [ [1 , n ] ] 2 , on note u i,j l'endomorphisme de E défini par :

$$\forall k \in [ 1 , n ] \ \ u _ { i , j } ( e _ { k } ) = \delta _ { j , k } e _ { i } . \\$$

La famille ( u i,j ) 1 ⩽ i,jn est alors une base de diagonalisation de ad ( a ). En effet, pour tout ( i, j, k ) [ [1 , n ] ] 3 , on a :

∈

$$\text {pour tout } & ( i , j , k ) \in [ 1 , n ] ^ { 3 } , \, \text {on a } \colon \\ & \quad \text {ad} ( u _ { i , j } ) \left ( e _ { k } \right ) = a ( u _ { i , j } ( e _ { k } ) ) - u _ { i , j } ( a ( e _ { k } ) ) = \lambda _ { i } u _ { i , j } ( e _ { k } ) - u _ { i , j } ( \lambda _ { k } e _ { k } ) \\ & = \lambda _ { i } u _ { i , j } ( e _ { k } ) - \lambda _ { k } \delta _ { j , k } e _ { i } = \lambda _ { i } u _ { i , j } ( e _ { k } ) - \lambda _ { j } \delta _ { j , k } e _ { i } \\ & = ( \lambda _ { i } - \lambda _ { j } ) \, u _ { i , j } ( e _ { k } ) \\ \text {done} \, \text {ad} ( u _ { i } ) & = ( \lambda _ { i } - \lambda _ { j } ) \, u _ { i j } .$$

donc ad ( a )( u i,j ) = ( λ i -λ j ) u i,j .

3. Supposons a nilpotent. Il existe donc un entier p tel que a p = 0 . On a alors :

Par conséquent, ad ( a ) est diagonalisable et sp ( ad ( a )) = { λ i -λ j ; ( i, j ) ∈ [ [1 , n ] ] 2 } .

soit ( M a ) p = 0 . Ainsi l'endomorphisme M a est nilpotent.

$$\text {exist and un entier } p \text { tel qu} \\ ( M _ { a } ) ^ { p } ( u ) = a ^ { p } \circ u = 0 \\ \text {andomorphism } M _ { a } \text { est nilpoten} \\$$

Notons N a l'endomorphisme u ↦→ u ◦ a de L ( E ) . On a de même ( N a ) p = 0 . Comme M a et N a commutent, la formule du binôme fournit :

$$C o m i c M _ { a } \ c o n d c { C } , & \text {at} \ a \text { and } \text {bomc o n d c } \cdot \\ ( a d ( a ) ) ^ { 2 p - 1 } = ( M _ { a } - N _ { a } ) ^ { 2 p - 1 } = \sum _ { k = 0 } ^ { 2 p - 1 } ( - 1 ) ^ { k } \binom { 2 p - 1 } { k } \left ( M _ { a } \right ) ^ { 2 p - 1 - k } \circ ( N _ { a } ) ^ { k } . \\ \intertext { f o r $ t o u t _ { k } $ d $ e . $ } \intertext { p o r $ t o u t _ { k } $ d $ e . $ } \intertext { p o r $ t o u t _ { k } $ d $ e . $ }$$

$$0$$

Pour tout k de [ [0 , p -1] ] , on a 2 p -1 -k ⩾ p donc ( M a ) 2 p -1 -k = 0 puis ( M a ) 2 p -1 -k ◦ ( N a ) k = 0. De même, pour tout k de [ [ p, 2 p -1] ] , on a ( N a ) k = 0 puis ( M a ) 2 p -1 -k ( N a ) k = 0.

Ainsi ad ( a ) 2 p -1 = 0, ce qui prouve que ad ( a ) est nilpotent.

- 2.18 On peut, quitte à remplacer u par u -λ Id E , supposer que la valeur propre λ est nulle.
- Supposons ( i ) et montrons ( ii ). Grâce au théorème du rang, il suffit de montrer que Ker u et Im u sont en somme directe. Soit x ∈ Ker u ∩ Im u . Par définition, u ( x ) = 0 et il existe t tel que x = u ( t ) . Ainsi, u 2 ( t ) = 0 donc t ∈ Ker u 2 = Ker u puis x = 0. Ainsi, Ker u ⊕ Im u = E.
- Supposons ( ii ) et montrons ( iii ). Comme Im u est stable par u , l'implication est évidente.
- Supposons ( iii ) et montrons ( iv ). On a E = Ker u ⊕ F avec F stable par u. On peut donc définir u ′ l'endomorphisme induit par u sur F . Comme Ker u et F sont stables par u , un déterminant par blocs donne :

$$\chi _ { u } ( X ) = \chi _ { u ^ { \prime } } ( X ) X ^ { d } ,$$

où d = dimKer u . Comme F et Ker u sont en somme directe, 0 n'est pas valeur propre de χ u ′ , la multiplicité de 0 dans χ u est égale à d.

BGBG

̸

- Supposons ( iv ) et montrons ( v ). Par hypothèse, χ u ( X ) = X d P ( X ) où d = dimKer u et P est un polynôme tel que P (0) = 0 . Les polynômes P et X d étant premiers entre eux, le lemme des noyaux et le théorème de Cayley-Hamilton donne :

$$E & = K e r \, u ^ { d } \oplus K e r \, P ( u ) . \\$$

Si l'on note, u ′ et u ′′ les endomorphismes respectivement induits par u sur Ker u d et Ker P ( u ), alors χ u ( X ) = χ u ′ ( X ) χ u ′′ ( X ) = X d ′ χ u ′′ ( X ) avec d ′ = dimKer u k . L'endomorphisme u ′′ étant annulé par P donc il n'admet pas 0 comme valeur propre. Par conséquent, d ′ = d . Comme Ker u ⊂ Ker u d , on en déduit que Ker u = Ker u k puis que E = Ker u ⊕ Ker P ( u ) . Le polynôme XP ( X ) annule donc u , ce qui prouve que 0 est racine simple du polynôme minimal de u .

̸

- Supposons ( v ) et montrons ( i ). Comme Ker u ⊂ Ker u 2 , il suffit de prouver que Ker u 2 ⊂ Ker u . Soit x ∈ Ker u 2 . Par hypothèse, le polynôme minimal de u est de la forme XQ ( X ) avec Q (0) = 0 donc, d'après le lemme des noyaux, on a E = Ker u ⊕ Ker Q ( u ). Il existe donc ( x 1 , x 2 ) ∈ Ker u × Ker Q ( u ) tel que x = x 1 + x 2 . Comme Ker u et Ker Q ( u ) sont stables par u et en somme directe, l'égalité u 2 ( x ) = u 2 ( x 1 ) + u 2 ( x 2 ) = 0 donne x 2 ∈ Ker Q ( u ) ∩ Ker u 2 . Les polynômes, X 2 et Q étant en somme directe, on en déduit que x 2 = 0 puis que x = x 1 ∈ Ker u .
- 2.19 1. Les opérations élémentaires C i + n ← C i + n + XC i puis C i ↔ C i + n pour i ∈ [ [1 , n ] ] donnent :

$$| \Gamma _ { n } ^ { 1 } \ 2 X _ { n } | & | \Gamma _ { n } ^ { 1 } \ 2 X _ { n } | + | \Gamma _ { n } ^ { 1 } \ 2 X _ { n } | \\ \text {Aisni, } \chi _ { B } ( X ) & = ( - 1 ) ^ { 2 n } \det \left ( X ^ { 2 } I _ { n } - A \right ) = \chi _ { A } ( X ^ { 2 } ) . \\ 2 . \text { Comme } \chi _ { B } ( X ) & = \chi _ { A } ( X ^ { 2 } ) , \text { un nombre complexe } \lambda \text { est va} \\ \text {ot soumont, } \text {si } \sigma _ { 2 } & = \sigma _ { 2 } \text { ou sur le propto do } \sigma _ { 3 } \text { Si } \sigma _ { 2 } \text { on } \sigma _ { 3 } \text { )}$$

$$\text {doment} \colon & & \text {doment} \colon & & \chi _ { B } ( X ) = \left | \begin{array} { c c c } X I _ { n } & - A & \left | \begin{array} { c c c } X I _ { n } & - A + X ^ { 2 } I _ { n } & \left | \begin{array} { c c c } - ( - 1 ) ^ { n } \right | & - A + X ^ { 2 } I _ { n } & X I _ { n } \\ - I _ { n } & X I _ { n } & - I _ { n } & 0 & - I _ { n } & \right | . \end{array} \\ \text {Ainsi, } \chi _ { B } ( X ) = ( - 1 ) ^ { 2 n } \det \left ( X ^ { 2 } I _ { n } - A \right ) = \chi _ { A } ( X ^ { 2 } ) . \\ 2 . \text { Commute } \gamma _ { R } ( X ) = \gamma _ { A } ( X ^ { 2 } ) , \text { un nombre complexe } \lambda \text { est value sur forme de } B \text { si } & & & &$$

2. Comme χ B ( X ) = χ A ( X 2 ), un nombre complexe λ est valeur propre de B si, et seulement si, λ 2 est valeur propre de A . Si l'on note λ 1 , . . . , λ d les valeurs propres distinctes de A et m λ 1 , . . . , m λ d leurs multiplicité dans χ A , alors :

$$\chi _ { B } ( X ) = \prod _ { i = 1 } ^ { d } \left ( X ^ { 2 } - \lambda _ { i } \right ) ^ { m _ { \lambda _ { i } } } = \prod _ { i = 1 } ^ { d } \left ( X - \mu _ { i } \right ) ^ { m _ { \lambda _ { i } } } \left ( X + \mu _ { i } \right ) ^ { m _ { \lambda _ { i } } } , \\ \dot { \mu } _ { i } , \, \text {pour tout} \, i \in \mathbb { [ } 1 , d \right ] , \, \mu _ { i } \text { est une racine carée de } \lambda _ { i } .$$

où, pour tout i ∈ [ [1 , d ] ] , μ i est une racine carrée de λ i .

On en déduit tout valeur propre μ non nulle de B , a une multiplicité dans χ B égale à m μ 2 si μ est non nul et 2 m 0 sinon.

Déterminons la dimension des espaces propres de B en fonction de ceux de A .

Soit μ une valeur propre de B . Un vecteur ( X Y ) avec ( X,Y ) ∈ ( I R n ) 2 appartient au sous-espace propre E λ ( B ) si, et seulement si, on a :

$$\left \{ \begin{array} { l c l } { A Y } & { = } & { \mu X } \\ { X } & { = } & { \mu Y } \end{array}$$

## BVCWCPD4CXD8D6CT BE BA CA AJ CTCSD9CRD8CXD3D2 CSCTD7 CTD2CSD3D1D3D6D4CWCXD7D1CTD7

c'est-à-dire si, et seulement si, Y ∈ E μ 2 ( A ) et X = μY . L'application :

$$\begin{array} { c c c } E _ { \mu ^ { 2 } } ( A ) & \longrightarrow & E _ { \mu } ( A ) \\ Y & \longmapsto & \left ( \begin{array} { c } \mu Y \\ Y \end{array} \right ) \\ \end{array}$$

est donc un isomorphisme d'où dim E μ ( B ) = dim E μ 2 ( A ) pour tout μ ∈ sp B.

Comme B est diagonalisable si, et seulement si, pour tout μ ∈ sp( B ) la dimension de E μ ( B ) est égale à la multiplicité de μ dans χ B , on en déduit que :

- si 0 n'est pas valeur propre de A , alors B est diagonalisable si, et seulement si, A l'est ;
- si 0 est valeur propre de A , alors B n'est pas diagonalisable.

## 2.20 On étudie la matrice :

$$U = \left ( \begin{array} { c c } 4 & 2 \\ - 3 & - 1 \end{array} \right ) .$$

Son polynôme caractéristique, X 2 -3 X +2, est scindé simple de racines 1 et 2 , donc la matrice U est diagonalisable. Plus précisément, on a :

$$U = \left ( \begin{array} { c c } 2 & 1 \\ - 3 & - 1 \end{array} \right ) \left ( \begin{array} { c c } 1 & 0 \\ 0 & 2 \end{array} \right ) \left ( \begin{array} { c c } - 1 & - 1 \\ 3 & 2 \end{array} \right ) .$$

On vérifie alors que :

$$\begin{array} { c c c } \text {On vertex aIs que} \cdot \\ & & \\ & \left ( \begin{array} { c c c } 4 A & 2 A \\ - 3 A & - A \end{array} \right ) = \left ( \begin{array} { c c c } 2 I _ { n } & I _ { n } \\ - 3 I _ { n } & - I _ { n } \end{array} \right ) \left ( \begin{array} { c c c } A & 0 \\ 0 & 2 A \end{array} \right ) \left ( \begin{array} { c c c } - I _ { n } & - I _ { n } \\ 3 I _ { n } & 2 I _ { n } \end{array} \right ) \\ \end{array}$$

et que :

ce qui prouve que la matrice B est semblable à C = ( A 0 0 2 A ) .

$$\left ( \begin{array} { c c } 2 I _ { n } & I _ { n } \\ - 3 I _ { n } & - I _ { n } \end{array} \right ) ^ { - 1 } = \left ( \begin{array} { c c } - I _ { n } & - I _ { n } \\ 3 I _ { n } & 2 I _ { n } \end{array} \right ) ;$$

- Si B est diagonalisable, alors la matrice C aussi donc il existe un polynôme P scindé à racines simples tel que P ( C ) = ( P ( A ) 0 0 P (2 A ) ) = 0 donc la matrice A est diagonalisable.
- Si A est diagonalisable, alors il existe une matrice P inversible et une matrice diagonale D telles que A = PDP -1 . On a alors :

$$\left ( \begin{array} { c c } A & 0 \\ 0 & 2 A \end{array} \right ) = \left ( \begin{array} { c c } P & 0 \\ 0 & P \end{array} \right ) \left ( \begin{array} { c c } D & 0 \\ 0 & 2 D \end{array} \right ) \left ( \begin{array} { c c } P & 0 \\ 0 & P \end{array} \right ) ^ { - 1 } .$$

Ainsi, C est diagonalisable donc B aussi.

BGBI

- 2.21 1. Comme la matrice A est inversible, alors AB = A ( BA ) A -1 donc les matrices AB et BA sont semblables. En particulier, χ AB ( X ) = χ BA ( X ).

$$\left ( \ B _ { 3 } \ B _ { 4 } \ \right ) \\ J _ { r } B = \left ( \begin{array} { c c } \ B _ { 1 } & \ B _ { 2 } \\ 0 & 0 \end{array} \right ) \quad \text {et} \quad \ B J _ { r } = \left ( \begin{array} { c c } \ B _ { 1 } & 0 \\ \ B _ { 3 } & 0 \end{array} \right ) . \\ \gamma _ { r } \, \ B = \gamma _ { r } \, \gamma _ { r } \, ( X )$$

2. En écrivant B = ( B 1 B 2 B 3 B 4 ) avec B 1 ∈ M r ( C ) et B 4 ∈ M n -r ( C ), on obtient :

Ainsi, χ J r B = χ BJ r = X n -r χ B 1 ( X ) .

3. La matrice A est équivalente à la matrice J r où r = rg A .Il existe donc deux matrices inversibles P et Q telles que A = PJ r Q . Comme P est inversible, on a :

$$\chi _ { A B } ( X ) = \chi _ { P J _ { r } Q B } ( X ) = \chi _ { J _ { r } Q B P } ( X )$$

donc, d'après la question précédente, χ AB ( X ) = χ QBPJ r ( X ). La matrice Q étant inversible, on en déduit que χ AB ( X ) = χ BPJ r Q ( X ) = χ BA ( X ).

- 2.22 Supposons qu'il existe une matrice U non nulle de M n ( C ) telle que AU = UB. Pour tout scalaire λ , on a ( A -λI n ) U = U ( B -λI n ). Comme χ B est scindé dans C , on en déduit que χ B ( A ) U = Uχ B ( B ) = 0 d'après le théorème de Cayley Hamilton. La

matrice χ B ( A ) est donc non inversible. Si l'on pose χ B ( X ) = n ∏ k =1 ( X -λ i ), alors le

Réciproquement, supposons que les matrices A et B possède une valeur propre commune λ , alors λ est aussi valeur propre de t B puisqu'une matrice et sa transposée ont le même spectre. Il existe donc deux vecteurs colonnes non nuls X et Y tels que l'on a ait AX = λX et t BY = λY. La matrice U = X t Y vérifie alors :

produit des matrices A -λ i I n est non inversible donc il existe une valeur propre de B telle que A -λI n soit non inversible, c'est-à-dire une valeur propre commune.

$$\text {on a at } A X & = \lambda X \ e t \ B Y = \lambda Y . \, \text {La matrice } U = X \, \text {Y} \ \text {verhe alors} \colon \\ & \quad A U = A X ^ { t } Y = \lambda X ^ { t } Y \quad \text {et} \quad U B = X ^ { t } Y B = X ^ { t } ( B Y ) = \lambda X ^ { t } Y . \\ \text {Comme les vecteurs } X & \ e t \ Y \ s o n \ n u l s , \, \text {la matrice } U \ e s t \ n o n \ n u lle \ car \, \text {il existe} \\ \text {un groupe } ( i \ j ) \subset [ 1 \ n ] ^ { 2 } \ t o l \, \text {o} \, U & = X Y . \neq 0$$

̸

Comme les vecteurs X et Y sont non nuls, la matrice U est non nulle car il existe un couple ( i, j ) ∈ [ [1 , n ] ] 2 tel que U i,j = X i Y j = 0.

- 2.23 Supposons qu'il existe une matrice U de rang r tel que AU = UB . Il existe alors deux matrices inversibles P et Q telles que U = PJ r Q. La relation APJ r Q = PJ r QB donne alors A ′ J r = J r B ′ avec A ′ = P -1 AP et B ′ = QBQ -1 .

B ′ = ( B ′ 1 B ′ 2 B ′ 3 B ′ 4 ) , avec B ′ 1 ∈ M r ( C ) et B ′ 4 ∈ M n -r ( C ), alors on a :

Si l'on écrit A ′ = ( A ′ 1 A ′ 2 A ′ 3 A ′ 4 ) , avec A ′ 1 ∈ M r ( C ) et A ′ 4 ∈ M n -r ( C ) et, de même,

$$B _ { 3 } ^ { \ } B _ { 4 } ^ { \prime } \ J _ { r } = \left ( \begin{array} { c c c } A ^ { \prime } J _ { r } = \left ( \begin{array} { c c c } A _ { 1 } ^ { \prime } & 0 \\ A _ { 3 } ^ { \prime } & 0 \end{array} \right ) & & \ e t \quad J _ { r } B ^ { \prime } = \left ( \begin{array} { c c c } B _ { 1 } ^ { \prime } & B _ { 2 } ^ { \prime } \\ 0 & 0 \end{array} \right ) \\ A _ { r } ^ { \prime } = B _ { r } ^ { \prime } \ A _ { r } ^ { \prime } = 0 \ e t \ R _ { r } ^ { \prime } = 0$$

donc A ′ 1 = B ′ 1 , A ′ 3 = 0 et B ′ 2 = 0 .

Par suite, χ A = χ A ′ = χ A ′ 1 ( X ) χ A ′ 4 ( X ) et χ B ( X ) = χ B ( X ) = χ B ′ 1 ( X ) χ B ′ 4 ( X ). Ainsi, χ A ( X ) et χ B ( X ) ont un facteur de degré r en commun : χ A ′ 1 ( X ).

BGBJ

## BVCWCPD4CXD8D6CT BE BA CA AJ CTCSD9CRD8CXD3D2 CSCTD7 CTD2CSD3D1D3D6D4CWCXD7D1CTD7

- 2.24 1. Comme E est un C -espace vectoriel, u possède une valeur propre λ. Le sousespace propre associé est stable par v car u et v commutent. L'endomorphisme v ′ induit par v sur E λ ( u ) possède alors un vecteur propre x qui est un vecteur propre de v car v ( x ) = v ′ ( x ) et un vecteur propre de u puisque x ∈ E λ ( u ).
2. Pour tout entier k , on a u k +1 ◦ v -v ◦ u k +1 = u ◦ ( u k ◦ v -v ◦ u k ) +( u ◦ v -v ◦ u ) ◦ u k , ce qui permet de prouver par récurrence que, pour tout entier k , on a :

$$u ^ { k } \circ v - v \circ u ^ { k } = \alpha k u ^ { k } .$$

Ainsi, pour tout polynôme P , on a P ( u ) ◦ v -v ◦ P ( u ) = αu ◦ P ′ ( u ). Comme E est de dimension finie, on peut considérer π u le polynôme minimal de u . Comme α = 0, le polynôme Xπ ′ u ( X ) annule u . Pour des raisons de degré, il existe donc un scalaire C non nul tel que :

$$\pi _ { u } = C X \pi _ { u } ^ { \prime } ( X ) .$$

Si l'on considère une racine non nulle z de π u de multiplicité m , alors z est une racine de Xπ ′ u ( X ) de multiplicité m -1 ce qui est absurde. Par conséquent, π u n'a que 0 comme racine, ce qui prouve qu'il est de la forme X d et donc que u est nilpotent.

En particulier, Ker u n'est pas réduit à { 0 } et est stable par v car si x ∈ Ker u , alors u ( v ( x )) = v ◦ u ( x )+ αu ( x ) = 0. L'endomorphisme v ′ induit par v sur Ker u possède alors un vecteur propre qui est un vecteur propre commun à u et v .

3. Supposons qu'il existe ( α, β ) C tel que u v v u = αu + βv .

Si β = 0, alors on conclut grâce à la question précédente. Sinon, l'endomorphisme w = u ◦ v -v ◦ u vérifie alors u ◦ w -w ◦ u = βw et la question précédente implique que les endomorphismes u et w possèdent un vecteur propre x commun. Il existe donc deux nombres complexes λ et μ tels que u ( x ) = λx et w ( x ) = μx . Comme β

est non nul, on en déduit que v ( x ) = β x . Le vecteur x est donc un vecteur propre commun à u et v.

- ∈ 2 ◦ -◦ μ -αλ
- 2.25 Si B est la matrice nulle alors le résultat est évident.

On suppose donc désormais que B est non nul.

Démontrons le résultat par récurrence sur n .

Si n = 1 alors le résultat est évident.

Soit n ⩾ 2 tel que le résultat soit vrai pour des matrices de taille n -1.

Notons a et b les endomorphismes canoniquement associés aux matrices A et B .

Comme B est non nul, l'image de b est un espace vectoriel non réduit à { 0 } et stable par b . L'endomorphisme induit par b sur Im b possède alors un vecteur propre x car le corps de base est C . Le vecteur x est alors un vecteur propre de b . De plus, il appartient à l'image de b donc au noyau de a car la relation AB = 0 donne a ◦ b = 0. Par conséquent, a et b possèdent un vecteur propre commun.

BGBK

̸

Soit B une base de premier vecteur x . Les matrices de a et b dans B sont alors de

taille n -1. Il suffit alors de montrer que les matrices A ′ et B ′ sont simultanément trigonalisables pour conclure.

$$\text {Soit B one base de premier vecteur } x . \text { Lats matrices of a et b dans B sort alors de } \\ \text {la forme } A ^ { \prime } = \left ( \begin{array} { c c c c } 0 & * & \dots & * \\ 0 & & & \\ & & 0 & \\ & & & \vdots & A ^ { \prime \prime } \\ & & & 0 & \\ \end{array} \right ) \, \text {et } B ^ { \prime } = \left ( \begin{array} { c c c } \mu & * & \dots & * \\ 0 & & & \\ & & 0 & \\ & & & \vdots & B ^ { \prime \prime } \\ & & & 0 & \\ \end{array} \right ) \, \text {avec } A ^ { \prime \prime } \, \text { et } B ^ { \prime \prime } \, \text { de } \\ \ t a lle \, n - 1 . \, \text {ll suff alors de monterre que les matrices } A ^ { \prime } \, \text { et } B ^ { \prime } \, \text { sort simultanément} \\ \text {trigonalsable pour conclosure.} \end{array}$$

Comme a ◦ b = 0, on a A ′′ B ′′ = 0. D'après l'hypothèse de récurrence, il existe donc P ∈ GL n -1 ( C ) telle que P -1 A ′′ P et P -1 B ′′ P soient triangulaires supérieures.

Considérons la matrice

$$\ t e l l e q u e \ P ^ { - 1 } A ^ { \prime \prime } P \ e t \ P ^ { - 1 } B ^ { \prime \prime } P \\ \text {price} \ Q = \left ( \begin{array} { c c c } 1 & 0 & \dots & 0 \\ 0 & & & \\ \vdots & & & P \\ 0 & & & \end{array} \right ) . \ U m$$

met de vérifier que Q est inversible d'inverse

les matrices Q -1 A ′ Q et Q -1 B ′ Q soient triangulaires supérieures ; ce qui conclut la récurrence.

. Un calcul matriciel par blocs per-

$$\begin{array} { c } \end{array} \rangle = \left ( \begin{array} { c c c c } 1 & 0 & \dots & 0 \\ 0 & & & \\ \vdots & & P ^ { - 1 } & \\ 0 & & & \\ \end{array} \right ) \, \text { et que} \\ \ t r i a n g u l a i r s \superseti r e u r e s ; \, c e \, q u i \, c o n c l u t \, l a$$

- 2.26 Comme A et B commutent, on prouve par récurrence que :

$$\text {commutent, on prove par recurrence que} \colon \\ \forall k \in \mathbb { N } \ M ^ { k } = \left ( \begin{array} { c c } A ^ { k } & k A ^ { k - 1 } B \\ 0 & A ^ { k } \end{array} \right ) . \\ \text {polyname} \ P \colon$$

Ainsi, pour tout polynôme P :

$$P \left ( M \right ) & = \left ( \begin{array} { c c } P ( A ) & P ^ { \prime } ( A ) B \\ 0 & P ( A ) \end{array} \right ) .$$

En particulier, si M est diagonalisable, alors il existe un polynôme P scindé à racines simples qui annule M . On en déduit, que P ( A ) = 0 puis que A est diagonalisable. De plus, P ′ est premier avec P. Il existe donc des polynômes U et V tels que :

$$U P + V P ^ { \prime } = 1 .$$

Par suite B = U ( A ) P ( A ) B + V ( A ) P ′ ( A ) B = 0.

Réciproquement, si A est diagonalisable et B = 0, alors il existe une matrice P ∈ GL n ( C ) et une matrice D ∈ M n ( C ) diagonale telle que A = PDP -1 ce qui donne :

et prouve que M est diagonalisable.

$$\begin{array} { r l } { d o n n e \colon } \\ { M = \left ( \begin{array} { c c c } { A } & { 0 } \\ { 0 } & { A } \end{array} \right ) \ = \left ( \begin{array} { c c c } { P } & { 0 } \\ { 0 } & { P } \end{array} \right ) \left ( \begin{array} { c c c } { D } & { 0 } \\ { D } & { 0 } \\ { 0 } & { D } \end{array} \right ) \left ( \begin{array} { c c c } { P } ^ { - 1 } & { 0 } \\ { P } ^ { - 1 } & { 0 } \\ { P ^ { - 1 } } \end{array} \right ) } \\ { = \left ( \begin{array} { c c c } { P } & { 0 } \\ { 0 } & { P } \end{array} \right ) \left ( \begin{array} { c c c } { D } & { 0 } \\ { D } & { 0 } \\ { 0 } & { P } \end{array} \right ) \left ( \begin{array} { c c c } { P } & { 0 } \\ { P } ^ { - 1 } & { 0 } \\ { P } ^ { - 1 } \end{array} \right ) ^ { - 1 } } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \quad } \\ { \qu$$

Par conséquent, M est diagonalisable si, et seulement si, la matrice A est diagonalisable et la matrice B est nulle.

## BVCWCPD4CXD8D6CT BE BA CA AJ CTCSD9CRD8CXD3D2 CSCTD7 CTD2CSD3D1D3D6D4CWCXD7D1CTD7

- 2.27 Si u est nilpotent, il existe une base dans laquelle la matrice A de u est triangulaire supérieure stricte. Les matrices A k étant triangulaires supérieures strictes pour tout k &gt; 0, on a Tr( u k ) = 0 pour tout k &gt; 0 .

Nous prouverons la réciproque par récurrence sur n . Elle est évidente pour n = 1 . Supposons le résultat acquis en dimension strictement inférieure à n.

Soit u vérifiant Tr( u k ) = 0 pour tout k ∈ [ [1 , n ] ] . Le théorème de Cayley-Hamilton

donne :

puis :

$$\chi ( u ) = u ^ { n } + \alpha _ { 1 } u ^ { n - 1 } + \cdots + \alpha _ { n - 1 } u + ( - 1 ) ^ { n } \det u \ I d _ { E } = 0 \\$$

$$\text {Tr} ( u ^ { n } ) + \alpha _ { 1 } \text { Tr} ( u ^ { n - 1 } ) + \dots + \alpha _ { n - 1 } \text { Tr} ( u ) + ( - 1 ) ^ { n } \det u \text { Tr} ( I d _ { E } ) = 0 , \\ \cdot \text { } u \cdot \text { } v \cdot \text { } 1 \cdot \text { } 0 \cdot \text { } \cdot \cdot \cdot \text { } \text { } T ( U 1 ) \cdot \text { } 0 \cdot \text { } U \cdot \text { } 1 \cdot \text { } 1 \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot \text { } \cdot \cdot \cdot$$

̸

c'est-à-dire det u = 0 puisque Tr(Id E ) = n = 0. L'endomorphisme u n'est donc pas inversible. D'après le théorème du rang, le sous-espace vectoriel Im u est de dimension strictement inférieure à n .

Dans une base adaptée à Im u , la matrice de u k est :

$$\begin{pmatrix} \ B ^ { k } & * \\ 0 & 0 \end{pmatrix}$$

où B est la matrice de v , l'endomorphisme induit par u sur Im u .

On en déduit que Tr( v k ) = 0 pour tout k ∈ [ [1 , rg u ] ] et, par hypothèse de récurrence, que v est nilpotent. On a donc, en posant r = rg u , v r = 0.

Ainsi, pour tout y ∈ Im u , on a u r ( y ) = 0. Par conséquent, pour tout x ∈ E , on a :

$$u ^ { r + 1 } ( x ) = u ^ { r } \left ( u ( x ) \right ) = 0$$

donc u r +1 = 0 ; ce qui conclut la récurrence.

- 2.28 1. (a) Comme G est fini, tout élément g de G est d'ordre fini et il existe par conséquent N g ∈ I N ∗ tel que g N g = I n .

Pour tout g ∈ G , le polynôme X N g -1 est scindé à racines simples et annule g , donc g est diagonalisable.

- (b) Comme G est fini, { Tr g ; g ∈ G } aussi.
2. Supposons que tous les éléments de G soient diagonalisables et que { Tr g ; g ∈ G } soit fini et montrons que G est fini.

L'espace vectoriel Vect( G ) est de dimension finie car inclus dans M n ( C ). De la partie génératrice G , on peut donc extraire une base ( A 1 , . . . , A p ). Comme { Tr g ; g ∈ G } est fini, l'application f : X ∈ G ↦→ (Tr( A 1 X ) , . . . , Tr( A p X )) est à valeurs dans un ensemble fini. Il suffit donc de prouver que f est injective pour conclure.

Soit ( g, g ′ ) ∈ G 2 tel que f ( g ) = f ( g ′ ). Par linéarité de la trace, on a donc Tr( hg ) = Tr( hg ′ ) pour tout h ∈ Vect( G ). Pour tout h ∈ G , hg -1 ∈ G donc Tr( hg -1 g ) = Tr( hg -1 g ′ ) puis Tr ( h ( g -1 g ′ -I n )) = 0. Par linéarité de la trace, on a donc :

$$\forall h \in \text {Vect} ( G ) \ \text {Tr} \left ( h \left ( g ^ { - 1 } g ^ { \prime } - I _ { n } \right ) \right ) = 0 .$$

En particulier, comme g -1 g ′ -I n ∈ Vect( G ), pour tout entier k , on a :

En utilisant l'exercice 2.27, on en déduit que g -1 g ′ -I n est nilpotent. Or, g -1 g ′ appartient à G donc il est diagonalisable. Par conséquent, g -1 g ′ -I n aussi et, comme il est nilpotent, il s'agit de l'endomorphisme nul d'où g = g ′ , ce qui achève la démonstration.

BHBD

$$g - I _ { n } \in \text {vec} ( G ) , \, \text {pour tout} \, I _ { n } \\ \text {Tr} \left ( ( g ^ { - 1 } g ^ { \prime } - I _ { n } ) ^ { k } \right ) = 0 . \\ 2 7 , \, \text {on} \, \text {e} d \hat { e } d u i t \, \text {que} \, g ^ { - 1 } g ^ { \prime } - I _ { n }$$