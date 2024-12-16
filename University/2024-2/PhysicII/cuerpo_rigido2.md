## Energia en el movimiento rotacional

El cuerpo rigido cuando rota tiene energia cinetica.
$$K=\sum_i \frac{1}{2}m_i^2 r_i^2 w^2$$
$$K=\frac{1}{2}(\sum_i m_ir_i^2)w^2$$
De acuerdo con la ecuacion podemos definir el momento de inercia.
$$I=\sum m_ir_i^2$$

**Tenemos**
$$K=\frac{1}{2}Iw^2$$

>[!note] Que es el momento de inercia?
>  Es una medida de como la masa de un cuerpo se distribuye con respecto a un eje de rotacion.
>  - De manera analoga a la **inercia** en en el movimiento traslacional, determina cuanra resistencia tiene el cuerpo a cambios en su velocidad de rotacion

## Teorema de los ejes paralelos

Haciendo calculos se puede obtener que :
$$I_r=I_{cm}+Md^2$$

![[2024-09-09-125515_248x326_scrot 1.png]]

## Torca y aceleracion angular de un cuerpo rigido

$$\tau_{1,z} = I_1\alpha_z = m_1r_1^2\alpha_z$$
Sumando todo, tenemos:
$$\sum \tau_{i,z} = I \alpha_z$$

# Dinamica : traslacion y rotacion combinadas

En el movimiento de traslacion tenemos
$$\sum \vec{F}_{ext}=M\vec{a}_{cm}$$
En el movimiento rotacional alrededor del centro de masa se describe mediante :
$$\sum \tau_{z} = I_{cm} \alpha_z$$

## Momento Angular de una particula
 
 - de manera analoga a lo que es el momentum esta cantidad esta reacionada a la oposicion que tienen los cuerpos a rotar.
 - Se define el momento angular $\vec{L}$ como una cantidad fisica vectorial relacionada con el movimiento de la rotacion de los cuerpos, es decir con la velocidad angular
 $$\vec{L} = \vec{r} \times \vec{p}$$
 - r -> posicion de de la particula
 - p -> momentum (misma direccion que la velocidad)
 
 ![[2024-09-02-115344_460x228_scrot.png]]

 - Su modulo seria  : $$ L = mrv \sin \theta$$
 ## Relacion entre el torque aplicado a una particula y su momento angular
 
-  torque -> la capacidad de una fuerza para prodicir movimiento.
- en el estudio de una particula 
$$\vec{F} = \dfrac{d\vec{p}}{dt} = m\dfrac{d\vec{v}}{dt}$$
- Si esta fuerza es capaz de producir rotacion respecto algun eje  o entonces:
$$\vec{\tau}^{o} = \vec{r} \times \vec{F} = \vec{r}\times\dfrac{d\vec{p}}{dt}$$
- Si analizamos la rapidez de cambio del momento angulas
$$\dfrac{d\vec{L}}{dt} = \dfrac{d}{dt}(\vec{r}\times\vec{p}) = \vec{r}\times\vec{p}=\vec{\tau}^o$$
>[!note]
> Entonces la rapidez de cambio del momento angular de una particula es igual al torque aplicado sobre ella

- Para un sistema de N particulas el torque neto es la sumatoria, de igual maneta para el momento angular

>[!note] Conservacion del momento angular
> Si la torca externa neta  que actua sobre un sistema es cero, el momento angular total del sistema es constante.










