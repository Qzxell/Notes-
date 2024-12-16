## Problemas

>[!nto] Problem 5
> $$\int \dfrac{1}{x \sqrt{x^{2a} + x^{a} + 1}} dx  
$$

**Solution**

- usar la sustitucion $u = x^{-a}$ -> se obtiene $du = -ax^{-a-1}dx$ 
- remplazando tenemos 

 $$\dfrac{1}{-a}\int \dfrac{1}{x^{-a} \sqrt{x^{2a} + x^{a} + 1}} dx  = \dfrac{1}{-a}\int \dfrac{1}{ \sqrt{u^2 + u + 1}} du $$
 
 - tenemos otra integral mas facil, con la sustitucion $u+\frac{1}{2} =\frac{\sqrt{3}}{2}\tan \theta$ se vuelva una integral  inmediata, $du=\frac{\sqrt{3}}{2}\sec^{2} \theta d\theta$  
  $$\int \dfrac{1}{ \sqrt{u^2 + u + 1}} du  = \int \dfrac{1}{ \sqrt{(u+\frac{1}{2})^2 + \frac{3}{4}}} du = \int \sec\theta  d \theta = \ln (\sec \theta + \tan \theta) + c = $$
