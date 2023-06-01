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


## **Replace Temp with Query**
### **Antes**
Usted coloca el resultado de una expresión en una variable local para su uso posterior en su código.
```python
def calculateTotal():
    basePrice = quantity * itemPrice
    if basePrice > 1000:
        return basePrice * 0.95
    else:
        return basePrice * 0.98
```
### **Después**
Mueva la expresión completa a un método separado y devuelva el resultado. Consulta el método en lugar de usar una variable. Incorpore el nuevo método en otros métodos, si es necesario.
```python
def calculateTotal():
    if basePrice() > 1000:
        return basePrice() * 0.95
    else:
        return basePrice() * 0.98

def basePrice():
    return quantity * itemPrice
```
### **Por qué refactorizar**
* Esta refactorización puede sentar las bases para aplicar el *Extract Method* para una parte de un método muy largo.
* A veces, la misma expresión también se puede encontrar en otros métodos, lo cual es una razón para considerar la creación de un método común.

### **Beneficios**
* Legibilidad del código. Es mucho más fácil entender el propósito del método `getTax()` que la línea `orderPrice() * 0.2`.
* Código más delgado a través de la deduplicación, si la línea que se reemplaza se usa en varios métodos.

### **Inconvenientes**
* Esta refactorización puede generar la pregunta de si este enfoque puede causar un impacto en el rendimiento. La respuesta honesta es: sí, lo es, ya que el código resultante puede verse afectado por la consulta de un nuevo método. Pero con las rápidas CPU de hoy en día y los excelentes compiladores, la carga casi siempre será mínima. Por el contrario, el código legible y la capacidad de reutilizar este método en otros lugares del código del programa, gracias a este enfoque de refactorización, son beneficios muy notables.
* No obstante, si su variable temporal se usa para almacenar en caché el resultado de una expresión que realmente consume mucho tiempo, es posible que desee detener esta refactorización después de extraer la expresión a un nuevo método.

### **Cómo refactorizar**
* Asegúrese de que se asigna un valor a la variable una vez y solo una vez dentro del método. De lo contrario, use *Split Temporaly Variable* para asegurarse de que la variable se use solo para almacenar el resultado de su expresión.
* Utilice *Extract Method* para colocar la expresión de interés en un nuevo método. Asegúrese de que este método solo devuelva un valor y no cambie el estado del objeto. Si el método afecta el estado visible del objeto, use *Separate Query from Modifier*.
* Reemplace la variable con una consulta a su nuevo método.

## **Split Temporary Variable**
### **Antes**
Tiene una variable local que se usa para almacenar varios valores intermedios dentro de un método (excepto las variables de ciclo).
```python
temp = 2 * (height + width)
print(temp)
temp = height * width
print(temp)
```
### **Después**
Use diferentes variables para diferentes valores. Cada variable debe ser responsable de una sola cosa en particular.
```python
perimeter = 2 * (height + width)
print(perimeter)
area = height * width
print(area)
```
### **Por qué refactorizar**
* Si está escatimando en la cantidad de variables dentro de una función y reutilizándolas para varios propósitos no relacionados, seguramente encontrará problemas tan pronto como necesite realizar cambios en el código que contiene las variables. Tendrá que volver a comprobar cada caso de uso de variables para asegurarse de que se utilizan los valores correctos.

### **Beneficios**
* Cada componente del código del programa debe ser responsable de una sola cosa. Esto hace que sea mucho más fácil mantener el código, ya que puede reemplazar fácilmente cualquier cosa en particular sin temor a efectos no deseados.
* El código se vuelve más legible..
* Esta técnica de refactorización es útil si prevé utilizar el *Extract Method* más adelante.

### **Cómo refactorizar**
* Encuentre el primer lugar en el código donde se da un valor a la variable. Aquí debe cambiar el nombre de la variable con un nombre que corresponda al valor que se le está asignando.
* Utilice el nuevo nombre en lugar del antiguo en los lugares donde se utilice este valor de la variable.
* Repita según sea necesario para los lugares donde a la variable se le asigna un valor diferente.


## **Remove Assignments to Parameters**
### **Antes**
Se asigna algún valor a un parámetro dentro del cuerpo del método.
```python
def discount(inputVal, quantity):
    if quantity > 50:
        inputVal -= 2
    # ...
```
### **Después**
Utilice una variable local en lugar de un parámetro.
```python
def discount(inputVal, quantity):
    result = inputVal
    if quantity > 50:
        result -= 2
    # ...
```
### **Por qué refactorizar**
* Las razones para esta refactorización son las mismas que para *Split Temp Variable*, pero en este caso estamos tratando con un parámetro, no con una variable local.
* Primero, si un parámetro se pasa a través de una referencia, luego de cambiar el valor del parámetro dentro del método, este valor se pasa al argumento que solicitó llamar a este método. Muy a menudo, esto ocurre accidentalmente y conduce a efectos desafortunados. Incluso si los parámetros generalmente se pasan por valor (y no por referencia) en su lenguaje de programación, esta peculiaridad de codificación puede alejar a aquellos que no están acostumbrados a ella.
* En segundo lugar, las múltiples asignaciones de diferentes valores a un solo parámetro dificultan saber qué datos debe contener el parámetro en un momento determinado. El problema empeora si su parámetro y su contenido están documentados, pero el valor real es capaz de diferir de lo que se espera dentro del método.

### **Beneficios**
* Cada elemento del programa debe ser responsable de una sola cosa. Esto hace que el mantenimiento del código sea mucho más fácil en el futuro, ya que puede reemplazar el código de manera segura sin efectos secundarios.
* Esta refactorización ayuda a *Repetitive code to separete methods*.

### **Cómo refactorizar**
* Create a local variable and assign the initial value of your parameter.
* In all method code that follows this line, replace the parameter with your new local variable.

## **Replace Method with Method Object**
### **Antes**
Tiene un método largo en el que las variables locales están tan entrelazadas que no puede aplicar el Método de extracción .
```python
class Order:
    # ...
    def price(self):
        primaryBasePrice = 0
        secondaryBasePrice = 0
        tertiaryBasePrice = 0
        # Perform long computation.
```
### **Después**
Transforme el método en una clase separada para que las variables locales se conviertan en campos de la clase. Luego puede dividir el método en varios métodos dentro de la misma clase.
```python
class Order:
    # ...
    def price(self):
        return PriceCalculator(self).compute()


class PriceCalculator:
    def __init__(self, order):
        self._primaryBasePrice = 0
        self._secondaryBasePrice = 0
        self._tertiaryBasePrice = 0
        # Copy relevant information from the
        # order object.

    def compute(self):
        # Perform long computation.
```
### **Por qué refactorizar**
* Un método es demasiado largo y no puede separarlo debido a las masas enredadas de variables locales que son difíciles de aislar entre sí.
* El primer paso es aislar todo el método en una clase separada y convertir sus variables locales en campos de la clase.
* En primer lugar, esto permite aislar el problema a nivel de clase. En segundo lugar, allana el camino para dividir un método grande y difícil de manejar en otros más pequeños que de todos modos no encajarían con el propósito de la clase original.

### **Beneficios**
* Aislar un método largo en su propia clase permite evitar que un método aumente de tamaño. Esto también permite dividirlo en submétodos dentro de la clase, sin contaminar la clase original con métodos de utilidad.

### **Inconvenientes**
* Se agrega otra clase, lo que aumenta la complejidad general del programa.

### **Cómo refactorizar**
* Crear una nueva clase. Nómbrelo según el propósito del método que está refactorizando.
* En la nueva clase, cree un campo privado para almacenar una referencia a una instancia de la clase en la que se encontraba el método anteriormente. Podría usarse para obtener algunos datos requeridos de la clase original si es necesario.
* Cree un campo privado separado para cada variable local del método.
* Cree un constructor que acepte como parámetros los valores de todas las variables locales del método y también inicialice los campos privados correspondientes.
* Declare el método principal y copie el código del método original en él, reemplazando las variables locales con campos privados.
* Reemplace el cuerpo del método original en la clase original creando un objeto de método y llamando a su método principal.


## **Substitute Algorithm**
### **Antes**
Entonces, ¿quieres reemplazar un algoritmo existente por uno nuevo?
```python
def foundPerson(people):
    for i in range(len(people)):
        if people[i] == "Don":
            return "Don"
        if people[i] == "John":
            return "John"
        if people[i] == "Kent":
            return "Kent"
    return ""
```
### **Después**
Reemplace el cuerpo del método que implementa el algoritmo con un nuevo algoritmo.
```python
def foundPerson(people):
    candidates = ["Don", "John", "Kent"]
    return people if people in candidates else ""
```
### **Por qué refactorizar**
* La refactorización gradual no es el único método para mejorar un programa. A veces, un método está tan repleto de problemas que es más fácil acabar con el método y empezar de nuevo. Y quizás haya encontrado un algoritmo que es mucho más simple y más eficiente. Si este es el caso, simplemente debe reemplazar el algoritmo anterior por el nuevo.
* A medida que pasa el tiempo, es posible que su algoritmo se incorpore a una biblioteca o marco conocido y desee deshacerse de su implementación independiente para simplificar el mantenimiento.
* Los requisitos para su programa pueden cambiar tanto que su algoritmo existente no se puede salvar para la tarea.

### **Beneficios**
* Código más simple y legible.

### **Cómo refactorizar**
* Asegúrese de haber simplificado el algoritmo existente tanto como sea posible. Mueva el código sin importancia a otros métodos usando el método de extracción . Cuantas menos partes móviles tenga su algoritmo, más fácil será reemplazarlo.
* Cree su nuevo algoritmo en un nuevo método. Reemplace el antiguo algoritmo con el nuevo y comience a probar el programa.
* Si los resultados no coinciden, regrese a la implementación anterior y compare los resultados. Identificar las causas de la discrepancia. Si bien la causa suele ser un error en el algoritmo anterior, es más probable que se deba a que algo no funciona en el nuevo.
* Cuando todas las pruebas se completen con éxito, ¡elimine el algoritmo anterior para siempre!
