# **Técnicas de refactoring**

Las técnicas de refactoring son justamente aquellas acciones que nos permiten no cometer o arreglar los code-smells. Cada code-smell tiene sus técnias a aplicar para refactorizarlo. 

# **Composing methods**

Se refiere a las técnicas que se refieren a la correcta escritura de los métodos, para evitar los code-smells ya vistos.

**Índice de técnicas de refactorización**:
* Extract Method
* Inline Method
* Extract Variable
* Inline Temp
* Replace Temp with Query
* Split Temporary Variable
* Remove Assignments to Parameters
* Replace Method with Method Object
* Substitute Algorithm


## **Extract Method**

### **Antes**

El método es muy largo y hace más de una acción. Por lo que el nombre del método no me está indicando completamente todo lo que puede hacer.
```python
def printOwing(self):
    self.printBanner()

    # print details
    print("name:", self.name)
    print("amount:", self.getOutstanding())
```

### **Después**

Mueva este código a un nuevo método (o función) separado y reemplace el código anterior con una llamada al método.
```python
def printOwing(self):
    self.printBanner()
    self.printDetails(self.getOutstanding())

def printDetails(self, outstanding):
    print("name:", self.name)
    print("amount:", outstanding)
```

### **Por qué refactorizar**
* Cuantas más líneas se encuentran en un método, más difícil es averiguar qué hace el método. Esta es la razón principal de esta refactorización.
* Además de eliminar las asperezas de su código, la extracción de métodos también es un paso en muchos otros enfoques de refactorización.


### **Beneficios**
* ¡Código más legible! Asegúrese de dar al nuevo método un nombre que describa el propósito del método: `createOrder()`, `renderCustomerInfo()`, etc.
* Menos duplicación de código. A menudo, el código que se encuentra en un método se puede reutilizar en otros lugares de su programa. Entonces puede reemplazar los duplicados con llamadas a su nuevo método.
* Aísla partes independientes del código, lo que significa que es menos probable que se produzcan errores (por ejemplo, si se modifica la variable incorrecta).

### **Cómo refactorizar**
* Cree un nuevo método y asígnele un nombre que haga evidente su propósito.
* Copie el fragmento de código relevante en su nuevo método. Elimine el fragmento de su ubicación anterior y haga una llamada para el nuevo método allí.
* Encuentre todas las variables utilizadas en este fragmento de código. Si se declaran dentro del fragmento y no se usan fuera de él, simplemente déjelas sin cambios: se convertirán en variables locales para el nuevo método.
* Si las variables se declaran antes del código que está extrayendo, deberá pasar estas variables a los parámetros de su nuevo método para usar los valores contenidos anteriormente en ellos. A veces es más fácil deshacerse de estas variables recurriendo a *Replace Temp with Query*.
* Si ve que una variable local cambia en su código extraído de alguna manera, esto puede significar que este valor modificado será necesario más adelante en su método principal. ¡Doble verificación! Y si este es el caso, devuelva el valor de esta variable al método principal para que todo siga funcionando.



## **Inline Method**


### **Antes**
Cuando el cuerpo de un método es más obvio que el propio método, utilice esta técnica.
```python
class PizzaDelivery:
    # ...
    def getRating(self):
        return 2 if self.moreThanFiveLateDeliveries() else 1
  
    def moreThanFiveLateDeliveries(self):
        return self.numberOfLateDeliveries > 5
```

### **Después**
Reemplace las llamadas al método con el contenido del método y elimine el método en sí.
```python
class PizzaDelivery:
  # ...
  def getRating(self):
    return 2 if self.numberOfLateDeliveries > 5 else 1
```

### **Por qué refactorizar**
* Un método simplemente delega a otro método. En sí misma, esta delegación no es un problema. Pero cuando hay muchos métodos de este tipo, se convierten en una maraña confusa que es difícil de resolver.
* A menudo, los métodos no son demasiado cortos originalmente , pero se vuelven así a medida que se realizan cambios en el programa. Así que no se avergüence de deshacerse de los métodos que han sobrevivido a su uso.

### **Beneficios**
* Al minimizar la cantidad de métodos innecesarios, hace que el código sea más sencillo.

### **Cómo refactorizar**
* Asegúrese de que el método no esté redefinido en las subclases. Si se redefine el método, abstenerse de esta técnica.
* Encuentra todas las llamadas al método. Reemplace estas llamadas con el contenido del método.
* Eliminar el método.

## **Extract Variable**

### **Antes**
Tienes una expresión que es difícil de entender.
```python
def renderBanner(self):
    if (self.platform.toUpperCase().indexOf("MAC") > -1) and \
       (self.browser.toUpperCase().indexOf("IE") > -1) and \
       self.wasInitialized() and (self.resize > 0):
        # do something
```
### **Después**
Coloque el resultado de la expresión o sus partes en variables separadas que se explican por sí mismas
```python
def renderBanner(self):
    isMacOs = self.platform.toUpperCase().indexOf("MAC") > -1
    isIE = self.browser.toUpperCase().indexOf("IE") > -1
    wasResized = self.resize > 0

    if isMacOs and isIE and self.wasInitialized() and wasResized:
        # do something
```
### **Por qué refactorizar**
* La principal razón para extraer variables es hacer que una expresión compleja sea más comprensible, dividiéndola en sus partes intermedias. Estos podrían ser:
* Condición del `if()` operador o una parte del ?: operador en lenguajes basados ​​en C.
* Una expresión aritmética larga sin resultados intermedios.
* Líneas largas de varias partes.
* Extraer una variable puede ser el primer paso para realizar el *Extract Method* si ve que la expresión extraída se usa en otros lugares de su código.

### **Beneficios**
* ¡Código más legible! Trate de dar a las variables extraídas buenos nombres que anuncien alto y claro el propósito de la variable. Más legibilidad, menos comentarios prolijos. Busca nombres como customerTaxValue, cityUnemploymentRate, clientSalutationString, etc.

### **Inconvenientes**
Más variables están presentes en su código. Pero esto se ve contrarrestado por la facilidad de lectura de su código.

* Al refactorizar expresiones condicionales, recuerde que lo más probable es que el compilador las optimice para minimizar la cantidad de cálculos necesarios para establecer el valor resultante. Digamos que tienes una siguiente expresión `if (a() || b()) ...`. El programa no llamará al método b si el método adevuelve trueporque el valor resultante seguirá siendo true, sin importar qué valor devuelva b.
* Sin embargo, si extrae partes de esta expresión en variables, siempre se llamará a ambos métodos, lo que podría perjudicar el rendimiento del programa, especialmente si estos métodos realizan un trabajo pesado.

### **Cómo refactorizar**
* Inserte una nueva línea antes de la expresión relevante y declare una nueva variable allí. Asigne parte de la expresión compleja a esta variable.
* Reemplace esa parte de la expresión con la nueva variable.
* Repita el proceso para todas las partes complejas de la expresión.


## **Inline Temp**
### **Antes**
Tienes una variable temporal a la que se le asigna el resultado de una expresión simple y nada más.
```python
def hasDiscount(order):
    basePrice = order.basePrice()
    return basePrice > 1000
```
### **Después**
Reemplace las referencias a la variable con la expresión misma.
```python
def hasDiscount(order):
    return order.basePrice() > 1000
```
### **Por qué refactorizar**
* Las variables locales en línea casi siempre se usan como parte de *Replace Temp with Query* con consulta o para allanar el camino para el *Extract Method*.
  
### **Beneficios**
* Esta técnica de refactorización no ofrece casi ningún beneficio en sí misma. Sin embargo, si a la variable se le asigna el resultado de un método, puede mejorar marginalmente la legibilidad del programa al deshacerse de la variable innecesaria.

### **Inconvenientes**
* A veces, se utilizan temporales aparentemente inútiles para almacenar en caché el resultado de una operación costosa que se reutiliza varias veces. Entonces, antes de usar esta técnica de refactorización, asegúrese de que la simplicidad no se produzca a costa del rendimiento.

### **Cómo refactorizar**
* Encuentra todos los lugares que usan la variable. En lugar de la variable, utilice la expresión que le ha sido asignada.
* Elimine la declaración de la variable y su línea de asignación.

