***Índice de contenidos:***
* Constantes
  * Definir una constante

# 🧮 **Constantes**

Una constante es parecida a las variables, con la excepción de que su valor asignado no cambia durante la ejecución del programa. La mayoría de lenguajes de programación contienen alguna manera de definir una constante. Python no contiene ningún tipo de forma de declarar una constante pero si hay maneras de copiar su comportamiento.

Si se quiere declarar un constante en Python no hay manera alguna, pero los desarrolladores utilizan nombres todos en mayúsculas que Python interpreta como si fuese una constante, aunque en verdad no deja de ser una variable que podemos cambiar su valor. Es simplemente una manera de distinguir las variables que usualemente se escriben todas en minúsculas, ya que para definir una constante por conveción se debe escribir su nombre todo en mayúsuculas. Las reglas de nombramiento de constantes es la misma que para las variables.

**Las constantes se suelen utilizar para:**
* Definir valores por defecto que no deberían de ser modificados
* Valores de configuración o entorno
* Constantes matemáticas
* Simplemente valores que no quieren/tienen que modificar

## 💫 Definir una constante en Python

Como ya dijimos en verdad es una variable lo que estamos pero Python, al estar todo el nombre en mayúsculas colorea diferente a la variable a modo de identificación de que se trata de una constante y no una variable. 

```python
PI = 3.14
```
Se puede realizar todo tipo de opearciones con constantes ya que en verdad estaríamos tratando con una variable pero no es recomendable ya que perdería el fin de definir a ese valor como una constante ya que si definimos una constante es porque no queremos que este valor sea modificado.
