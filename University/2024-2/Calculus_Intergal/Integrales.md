---
autor: Michael Spivak
---
>[!definition] 
> Sea $a<b$ . Una particion del intervalo $[a,b]$ es una coleccion finita de puntos de $[a,b]$, uno de los cuales es a y otros es b. 

>[!note]
>Los puntos pueden ser :
>$$a= t_0<t_1<\cdots<t_{n-1}<t_n = b$$


>[!def]
> Supongamos que $f$ esta acotada en $[a,b]$ y que P = {$t_0, c\dots,t_n$} es una particion de $[a,b]$.Sea
> $$m_i = inf{f(x):t_{i-1}\leq x \leq t_i}$$
> $$M_i = sup{f(x):t_{i-1}\leq x \leq t_i}$$
> La suma inferior de f respecto a P, representada mediante L(f,P),se define como 
> $$L(f,P)=\sum_{i=1}^{n}m_i(t_i-t_{i-1})$$
> La suma inferior de f respecto a P representada mediante U(f,P) se define como
> $$U(f,P)=\sum_{i=1}^{n}M_i(t_i-t_{i-1})$$

>[!note]
> Esta definiciones se definieron sin el concepto de area

>[!note]
> -  El requisito de que f este acotada, es esencial para que los $m_i$ y $M_{i}$ esten bien definidos.
> - Adema es esencial definir a $m_i$ y $M_i$ como infimos y supremos, y no como maximos y minimos. ya que no se supone que f sea continua

>[!obsevaciones]
> Es algo obvio y que verifican la siguiente desigualdad 
> $$L(f,P)\leq U(f,P)$$

ya que  
$$L(f,P)=\sum_{i=1}^{n}m_i(t_i-t_{i-1})$$
 $$U(f,P)=\sum_{i=1}^{n}M_i(t_i-t_{i-1})$$
y para cada i se cumple $m_i(t-t_{i-1}) \leq M_i(t_i-t_{i-1})$

>[!observacion]
>otra observacion menos obvia es 
>$$L(f,P_1) \leq U_(f,P_2)$$

> [!lemma]
> si Q contiene a P, entonces
> $$L(f,P) \leq L(f,Q)$$
> $$U(f,Q) \leq U(f,P)$$

>[!n] Theorem 1
> Sean $P_1$ y $P_2$ particiones de $[a,b]$, y sea f una funcion acotada en $[a,b]$ entonces
> $$L(f,P_1) \leq U(f,P_2)$$

- Demostracion:
Existe una particion que contiene tanto a $P_1$ como a $P_2$ ,segun el lemma anterior se puede demostrar que :
 $$L(f,P_1)\leq L(f,P)\leq U(f,P) \leq U(f,P_2)$$

 De esto se puede demostrar que cualquier suma inferior es una cota inferior de una suma superior, analogamente, cualquier suma superior es una cota superior de cualquier suma inferior. Es decir:
$$\text{sup} \{L(f,P)\text{ : P una particion de [a,b]} \} \leq U(f,P') $$
$$\text{sup} \{L(f,P)\} \} \leq \text{inf}\{U(f,P'\}) $$
>[!n] Vista a areas
> para alguna particion del conjunto de todas las particiones posibles, puede pasar que 
> $$L(f,P') = U(f,P')$$
> Este seria el candidato ideal para el valor del area R(f,a,b)
> Aunque no sabemos cuando cumple esta igualdad.

 >[!def] Definicion de Integral
 >Una funcion f acotada $[a,b]$ es integrable en $[a,b]$ si 
 >- $sup\{L(f,P) \} = inf\{U(f,P) \}$ . En este caso, a este numero comun se le denomina la integral f de $[a,b]$ y se representa mediante
 >$$\int_{a}^{b}f$$
 > - La integral se denomina tambien el area de R(f,a,b) cuando $f(x)\geq 0$ para todo x en $[a,b]$ 
 
 >[!theorem 2]
 > Si $f$ esta acotada en $[a,b]$ , entonces f es integrable en $[a,b]$, si y solo si para cada $\epsilon > 0$  existe una particion P talque 
 > $$U(f,P) - L(f,P) < \epsilon$$

 >[!theorem 3]
 > Si $f$ es continua en $[a,b]$ , entonces f es integrable en $[a,b]$

 >[!theorem 4]
 > Si $f$ es integrable en $[a,b]$ , y $f$ se define en $[a,b]$ mediante
 > $$F(x)= \int_a^x f$$
 > Entonces $F$ es continua en $[a,b]$
 
 




