
Trabajar de manera mas facil con las fechas

# Pasar de str a datetime

**datetime** es el tipo de dato con el que se trabaja
```python
## volver a tipo de dato datetime
fch =  datetime.strptime(fecha, "%d/%m/%Y")
## retorna en string en el formato deseado
return fch.strftime("%m/%d/%Y")

```