# **Code Smells**

**Índice de code smells**:
1. 

# **Bloaters**

Los bloaters son código, métodos y clases que han aumentado a proporciones tan gigantescas que es difícil trabajar con ellos. Este tipo de errores suelen suceder cuando se desarrolla un código durante bastante tiempo.

## **Long methods**

### **Signos para reconocer**:
* Normalmente, cualquier método de más de diez líneas debería hacer que comiences a pensar sobre refactorizar. También cuando necesites comentar lo que hace el método es que o es muy largo lo que quieres hacer con el método o el nombre del mismo el poco descriptivo.

### **Razones del problema**:
* Mentalmente, a menudo es más difícil crear un nuevo método que agregar uno existente: "Pero son solo dos líneas, no sirve de nada crear un método completo solo para eso..." Lo que significa que se agrega otra línea y luego todavía otro, dando a luz a una maraña de código de espagueti.

### **Tratamiento**:
* Para reducir la longitud del cuerpo de un método, utilice *Método de extracción*.
* Si las variables y los parámetros locales interfieren con la extracción de un método, use *Reemplazar temporal con consulta* , *Introduce Object Parameter* o *Preserve All Data Object*.
* Si ninguna de las recetas anteriores ayuda, intente mover todo el método a un objeto separado a través de *Replace method with method object*.
* Los operadores condicionales y los bucles son una buena pista de que el código se puede mover a un método separado. Para condicionales, utilice *Descomponer condicional* . Si hay bucles en el camino, pruebe el *Extraction Method*.

## **Long Classes**
### **Signos para reconocer**:
* Cuando una clase contiene muchos campos/métodos/líneas de código.

### **Razones del problema**:
* Como también es el caso con los métodos largos, los programadores generalmente encuentran mentalmente menos agotador colocar una nueva función en una clase existente que crear una nueva clase para la función.

### **Tratamiento**:

* *Extract Class* ayuda si parte del comportamiento de la clase grande se puede dividir en un componente separado.
* *Extract Subclass* ayuda si parte del comportamiento de la clase grande se puede implementar de diferentes maneras o se usa en casos excepcionales.
* *Extract Interface* ayuda si es necesario tener una lista de las operaciones y comportamientos que el cliente puede usar.
* Si una clase grande es responsable de la interfaz gráfica, puede intentar mover algunos de sus datos y comportamiento a un objeto de dominio separado. Al hacerlo, puede ser necesario almacenar copias de algunos datos en dos lugares y mantener la coherencia de los datos. *Duplicate observed data* ofrece una manera de hacer esto.

## **Primitive Obsession**

### **Signos para reconocer**:
* Uso de primitivas en lugar de objetos pequeños para tareas simples (como moneda, rangos, cadenas especiales para números de teléfono, etc.)
* Uso de constantes para codificar información (como una constante `USER_ADMIN_ROLE = 1` para referirse a usuarios con derechos de administrador).
* Uso de constantes de cadena como nombres de campo para su uso en matrices de datos.

### **Razones del problema**:
* Como la mayoría de los demás code smells, las obsesiones primitivas nacen en momentos de debilidad. 

### **Tratamiento**:
* Si tiene una gran variedad de campos primitivos, puede ser posible agrupar lógicamente algunos de ellos en su propia clase. Aún mejor, mueva el comportamiento asociado con estos datos a la clase también. Para esta tarea, intente *Replace Data Vlue Object*.
* Si los valores de los campos primitivos se utilizan en los parámetros del método, elija *Introduce Parameter Object* o *Preserve Whole Object*.
* Cuando se codifican datos complicados en variables, use *Replace Type Code with Class* , *Replace Type Code with Subclasses* o *Replace Type Code with State/Strategy*.
* Si hay matrices entre las variables, use *Replace Array with Object*.

## **Long Parameter List**

### **Signos para reconocer**:
* Más de tres o cuatro parámetros para un método.

### **Razones del problema**:
* Las listas largas de parámetros pueden surgir cuando queremos que una clase tenga más independencia. 
* Cuando hay larga lista de parámetros para reducirlos se pueden enviar otros objetos como parámetros, estos objetos ya contendrán la información necesaria que necesita el método, pero lo pasaremos como un objeto y no como una lista de parámetros.

### **Tratamiento**:
* Si algunos de los argumentos son solo resultados de llamadas a métodos de otro objeto, use *Replace Parameter with method call* . Este objeto puede colocarse en el campo de su propia clase o pasarse como un parámetro de método.
* En lugar de pasar un grupo de datos recibidos de otro objeto como parámetros, pase el objeto mismo al método, usando *Preserve Whole Object*.
* Pero si estos parámetros provienen de diferentes fuentes, puede pasarlos como un único objeto de parámetro a través de *Introduce Parameter Object*.

### **Cuando ignorar**:
* No se deshaga de los parámetros si hacerlo causaría una dependencia no deseada entre las clases.

## **Data Clumps**

### **Signos para reconocer**:
* A veces, diferentes partes del código contienen grupos idénticos de variables (como parámetros para conectarse a una base de datos). Estos grupos deben convertirse en sus propias clases.

### **Razones del problema**:
* A menudo, estos grupos de datos se deben a una estructura deficiente del programa o "copypaste programming". Si desea asegurarse de que algunos datos sean o no un grupo de datos, simplemente elimine uno de los valores de datos y vea si los otros valores aún tienen sentido. Si este no es el caso, es una buena señal de que este grupo de variables debe combinarse en un objeto.

### **Tratamiento**:
* Si los datos repetidos comprenden los campos de una clase, use *Extract Class* para mover los campos a su propia clase.
* Si se pasan los mismos grupos de datos en los parámetros de los métodos, use *introduce Parameter Object* para establecerlos como una clase.
* Si algunos de los datos se pasan a otros métodos, piense en pasar todo el objeto de datos al método en lugar de solo campos individuales. *Preserve Whole Object* ayudará con esto.
* Mire el código usado por estos campos. Puede ser una buena idea mover este código a una clase de datos.

### **Cuando ignorar**:
Pasar un objeto completo en los parámetros de un método, en lugar de pasar solo sus valores (tipos primitivos), puede crear una dependencia no deseada entre las dos clases.

# **Object-Orientation Abusers**

Todos estos olores son aplicaciones incompletas o incorrectas de los principios de programación orientada a objetos.

## **Alternative Classes with Differente Interfaces**

### **Signos para reconocer**:
* Dos clases realizan funciones idénticas pero tienen diferentes nombres de métodos.

### **Razones del problema**:
* El programador que creó una de las clases probablemente no sabía que ya existía una clase funcionalmente equivalente.

### **Tratamiento**:
Intenta poner la interfaz de clases en términos de un denominador común:
* *Rename Methods* para hacerlos idénticos en todas las clases alternativas.
* *Move methods* , *Add Parameter* y *Parameterize Method* para que la firma y la implementación de los métodos sean iguales.
* Si solo se duplica una parte de la funcionalidad de las clases, intente usar *Extract Superclass* . En este caso, las clases existentes se convertirán en subclases.
* Una vez que haya determinado qué método de tratamiento usar y lo haya implementado, es posible que pueda eliminar una de las clases.

### **Cuando ignorar**:
* A veces fusionar clases es imposible o tan difícil que no tiene sentido. Un ejemplo es cuando las clases alternativas están en diferentes bibliotecas y cada una tiene su propia versión de la clase.

## **Refused Bequest**

### **Signos para reconocer**:
* Si una subclase usa solo algunos de los métodos y propiedades heredados de sus padres, la jerarquía está fuera de lugar. Los métodos innecesarios pueden simplemente no usarse o redefinirse y generar excepciones.

### **Razones del problema**:
* Alguien estaba motivado para crear herencia entre clases solo por el deseo de reutilizar el código en una superclase. Pero la superclase y la subclase son completamente diferentes.

### **Tratamiento**:
* Si la herencia no tiene sentido y la subclase realmente no tiene nada en común con la superclase, elimine la herencia a favor de *Replace Inheritance with Delegation*.
* Si la herencia es apropiada, elimine los campos y métodos innecesarios en la subclase. Extraiga todos los campos y métodos que necesita la subclase de la clase principal, colóquelos en una nueva superclase y configure ambas clases para heredar de ella (*Extract Superclass).

## **Switch Statements**

### **Signos para reconocer**:
* Tiene un operador switch complejo o una secuencia de declaraciones if.

### **Razones del problema**:
* El uso relativamente raro de los operadores switch y case es uno de los sellos distintivos del código orientado a objetos. A menudo, el código de un solo switch puede estar disperso en diferentes lugares del programa. Cuando se agrega una nueva condición, debe encontrar todo el switchcódigo y modificarlo.
* Como regla general, cuando veas switchdebes pensar en polimorfismo.

### **Tratamiento**:
* Para aislarlo switch y colocarlo en la clase correcta, es posible que necesite *Extract Method* y luego *Move method*.
* Si a switch se basa en el código de tipo, como cuando se cambia el modo de tiempo de ejecución del programa, use *Replace Type Code with Subclasses* o *Replace Type Code with State/Strategy*.
* Después de especificar la estructura de herencia, use *Replace Conditional with Polymorphism*.
* Si no hay demasiadas condiciones en el operador y todos llaman al mismo método con diferentes parámetros, el polimorfismo será superfluo. Si este es el caso, puede dividir ese método en varios métodos más pequeños con *Replace Parameter with Explicit Methods* y cambiarlos switch en consecuencia.
* Si una de las opciones condicionales es null, utilice *Introduce Null Object*.

### **Cuando Ignorar**
* Cuando un switch operador realiza acciones simples, no hay motivo para realizar cambios en el código.
* A menudo, los patrones de diseño de fábrica utilizan operador switch(*Fabric Method* o *Absctract Fabric*) para seleccionar una clase creada.

## **Temporary Field**

### **Signos para reconocer**:
* Los campos temporales obtienen sus valores (y, por lo tanto, los objetos los necesitan) solo en determinadas circunstancias. Fuera de estas circunstancias, están vacíos.

### **Razones del problema**:
* A menudo, los campos temporales se crean para su uso en un algoritmo que requiere una gran cantidad de entradas. Entonces, en lugar de crear una gran cantidad de parámetros en el método, el programador decide crear campos para estos datos en la clase. Estos campos se usan solo en el algoritmo y no se usan el resto del tiempo.
* Este tipo de código es difícil de entender. Espera ver datos en campos de objetos pero, por algún motivo, casi siempre están vacíos.
  
### **Tratamiento**:
* Los campos temporales y todo el código que opera en ellos se pueden colocar en una clase separada a través de *Extract Class*. En otras palabras, está creando un objeto de método, logrando el mismo resultado que si realizara *Replace Mehod with Object*.
* *Introduce Null Object* e intégrelo en lugar del código condicional que se usó para verificar la existencia de los valores de campo temporales.

# **Change preventers**
* Estos code-smells significan que si necesita cambiar algo en un lugar de su código, también debe realizar muchos cambios en otros lugares. Como resultado, el desarrollo del programa se vuelve mucho más complicado y costoso.

## **Divergent Change**

### **Signos para reconocer**:
* Se encuentra teniendo que cambiar muchos métodos no relacionados cuando realiza cambios en una clase. Por ejemplo, al agregar un nuevo tipo de producto, debe cambiar los métodos para buscar, mostrar y ordenar productos.

### **Razones del problema**:
* A menudo, estas modificaciones divergentes se deben a una estructura deficiente del programa o "programación copypasta".

### **Tratamiento**:
* Divida el comportamiento de la clase a través de *Extract Class*.
* Si diferentes clases tienen el mismo comportamiento, es posible que desee combinar las clases a través de la herencia ( *Extract Superclass* y *Extract subclass*).

## **Parallel Inheritance Hierarchies**

![](https://refactoring.guru/images/refactoring/content/smells/parallel-inheritance-hierarchies-01.png?id=9167875f5f0e80256edcc8fcaaed3563)

### **Signos para reconocer**:
* Cada vez que crea una subclase para una clase, se encuentra con la necesidad de crear una subclase para otra clase.

### **Razones del problema**:
* Todo iba bien mientras la jerarquía se mantuviera pequeña. Pero con la adición de nuevas clases, hacer cambios se ha vuelto cada vez más difícil.

### **Tratamiento**:
* Puede desduplicar jerarquías de clases paralelas en dos pasos. Primero, haga que las instancias de una jerarquía se refieran a instancias de otra jerarquía. Luego, elimine la jerarquía en la clase referida, usando *Move Method* y *Move Field*.

## **Shotgun Surgery**

### **Signos para reconocer**:
* Hacer cualquier modificación requiere que haga muchos pequeños cambios en muchas clases diferentes.

### **Razones del problema**:
* Una sola responsabilidad se ha repartido entre un gran número de clases. Esto puede suceder después de una aplicación demasiado entusiasta de *Divergent Change*.

### **Tratamiento**:
* Utilice *Move Method* y *Move field* para mover comportamientos de clase existentes a una sola clase. Si no hay una clase apropiada para esto, cree una nueva.
* Si mover el código a la misma clase deja las clases originales casi vacías, intente deshacerse de estas clases ahora redundantes a través de *Inline Class*.

# **Dispensables**
Un prescindible es algo sin sentido e innecesario cuya ausencia haría que el código fuera más limpio, más eficiente y más fácil de entender.

## **Comments**

### **Signos para reconocer**:
* Un método está lleno de comentarios explicativos.

### **Razones del problema**:
* Los comentarios generalmente se crean con las mejores intenciones, cuando el autor se da cuenta de que su código no es intuitivo ni obvio. En tales casos, los comentarios son como un desodorante que enmascara el olor del código sospechoso que podría mejorarse.

> "El mejor comentario es un buen nombre para un método o clase".

### **Tratamiento**:
* Si un comentario pretende explicar una expresión compleja, la expresión debe dividirse en subexpresiones comprensibles utilizando *Extract Variable*.
* Si un comentario explica una sección de código, esta sección se puede convertir en un método separado a través de *Extract Method*. Lo más probable es que el nombre del nuevo método se pueda tomar del propio texto del comentario.
* Si ya se ha extraído un método, pero aún se necesitan comentarios para explicar lo que hace el método, asígnele un nombre que se explique por sí mismo. Use *Rename Method* para esto.
* Si necesita afirmar reglas sobre un estado que es necesario para que el sistema funcione, use *Introduce Assertion*.


## **Duplicate Code**

### **Signos para reconocer**:
* Dos fragmentos de código parecen casi idénticos.

### **Razones del problema**:
* La duplicación generalmente ocurre cuando varios programadores están trabajando en diferentes partes del mismo programa al mismo tiempo. Dado que están trabajando en diferentes tareas, es posible que no sepan que su colega ya ha escrito un código similar que podría reutilizarse para sus propias necesidades.
* También hay una duplicación más sutil, cuando partes específicas del código se ven diferentes pero en realidad realizan el mismo trabajo. Este tipo de duplicación puede ser difícil de encontrar y corregir.

### **Tratamiento**:
* Si se encuentra el mismo código en dos o más métodos de la misma clase: use *Extract Method* y realice llamadas para el nuevo método en ambos lugares.

## **Data Class**

### **Signos para reconocer**:
* Una clase de datos se refiere a una clase que contiene solo campos y métodos crudos para acceder a ellos (getters y setters). Estos son simplemente contenedores de datos utilizados por otras clases. Estas clases no contienen ninguna funcionalidad adicional y no pueden operar de forma independiente con los datos que poseen.

### **Razones del problema**:
* Es algo normal cuando una clase recién creada contiene solo unos pocos campos públicos (y tal vez incluso un puñado de getters/setters). Pero el verdadero poder de los objetos es que pueden contener tipos de comportamiento u operaciones en sus datos.

### **Tratamiento**:
* Si una clase contiene campos públicos, use *Encapsulate Field* para ocultarlos del acceso directo y exigir que el acceso se realice solo a través de captadores y definidores.
* Utilice *Encapsulate Collection* para los datos almacenados en colecciones (como matrices).
* Revise el código de cliente que usa la clase. En él, puede encontrar funcionalidades que estarían mejor ubicadas en la propia clase de datos. Si este es el caso, use *Move Method* y *Extract Method* para migrar esta funcionalidad a la clase de datos.
* Una vez que la clase se ha llenado con métodos bien pensados, es posible que desee deshacerse de los métodos antiguos para acceder a los datos que brindan un acceso demasiado amplio a los datos de la clase. Para esto, *Remove Setting Method* y * *Hide Method* pueden ser útiles.


## **Dead Code**

### **Signos para reconocer**:
* Una variable, parámetro, campo, método o clase ya no se usa (generalmente porque está obsoleta).

### **Razones del problema**:
* Cuando los requisitos para el software cambiaron o se hicieron correcciones, nadie tuvo tiempo de limpiar el código antiguo.
* Dicho código también podría encontrarse en condicionales complejos, cuando una de las ramas se vuelve inalcanzable (debido a un error u otras circunstancias).

### **Tratamiento**:
* La forma más rápida de encontrar código muerto es usar un buen IDE .
* Elimine el código no utilizado y los archivos innecesarios.
* En el caso de una clase innecesaria, se puede aplicar *Inline Class* o *Collapse Hierarchy* si se usa una subclase o una superclase.
* Para eliminar parámetros innecesarios, utilice *Remove Parameter*.


## **Lazy Class**

### **Signos para reconocer**:
* Comprender y mantener las clases siempre cuesta tiempo y dinero. Entonces, si una clase no hace lo suficiente para llamar su atención, debe eliminarse.

### **Razones del problema**:
* Tal vez una clase fue diseñada para ser completamente funcional, pero después de algunas refactorizaciones se ha vuelto ridículamente pequeña.
* O tal vez fue diseñado para respaldar el trabajo de desarrollo futuro que nunca se hizo.

### **Tratamiento**:
* Los componentes que son casi inútiles deben recibir el tratamiento de *Inline Class*.
* Para subclases con pocas funciones, intente *Collapse Hierarchy*.

### **Cuando Ignorar**:
* A veces, se crea una clase perezosa para delinear las intenciones de desarrollo futuro. En este caso, intente mantener un equilibrio entre claridad y simplicidad en su código.

## **Speculative Generality**

### **Signos para reconocer**:
* Hay una clase, método, campo o parámetro sin usar.

### **Razones del problema**:
* A veces, el código se crea "por si acaso" para admitir funciones futuras anticipadas que nunca se implementan. Como resultado, el código se vuelve difícil de entender y admitir.

### **Tratamiento**:
* Para eliminar clases abstractas no utilizadas, intente *Collapse Hierarchy*.
* La delegación innecesaria de funcionalidad a otra clase se puede eliminar a través de *Inline Class*.
* ¿Métodos no utilizados? Utilice el *Inline Method* para deshacerse de ellos.
* Los métodos con parámetros no utilizados deben revisarse con la ayuda de *Remove Parameter*.
* Los campos no utilizados se pueden eliminar simplemente.

### **Cuando Ignorar**:
* Si está trabajando en un framework, es eminentemente razonable crear una funcionalidad que no se usa en el marco en sí, siempre que los usuarios de los marcos necesiten la funcionalidad.
* Antes de eliminar elementos, asegúrese de que no se utilicen en pruebas unitarias. Esto sucede si las pruebas necesitan una forma de obtener cierta información interna de una clase o realizar acciones especiales relacionadas con las pruebas.

# **Couplers**
Todos los olores de este grupo contribuyen al acoplamiento excesivo entre clases o muestran lo que sucede si el acoplamiento se reemplaza por una delegación excesiva.

## **Feature Envy**

### **Signos para reconocer**:
* Un método accede a los datos de otro objeto más que a sus propios datos.

### **Razones del problema**:
* Este olor puede ocurrir después de que los campos se muevan a una dataclass. Si este es el caso, es posible que también desee mover las operaciones sobre los datos a esta clase.

### **Tratamiento**:
* Como regla básica, si las cosas cambian al mismo tiempo, debes mantenerlas en el mismo lugar. Por lo general, los datos y las funciones que usan estos datos se cambian juntos (aunque son posibles las excepciones).
* Si claramente se debe mover un método a otro lugar, use *Move Method*.
* Si solo una parte de un método accede a los datos de otro objeto, use *Extract Method* para mover la parte en cuestión.
* Si un método usa funciones de varias otras clases, primero determine qué clase contiene la mayoría de los datos usados. Luego coloque el método en esta clase junto con los otros datos. De manera alternativa, use *Extract Method* para dividir el método en varias partes que se pueden colocar en diferentes lugares en diferentes clases.

### **Cuando Ignorar**:
* A veces, el comportamiento se mantiene separado deliberadamente de la clase que contiene los datos. La ventaja habitual de esto es la capacidad de cambiar dinámicamente el comportamiento (ver Estrategia , Visitante y otros patrones).


## **Inappropriate Intimacy**

### **Signos para reconocer**:
* Una clase usa los campos y métodos internos de otra clase.

### **Razones del problema**:
Esté atento a las clases que pasan demasiado tiempo juntas. Las buenas clases deben saber lo menos posible unas de otras. Tales clases son más fáciles de mantener y reutilizar.

### **Tratamiento**:
* La solución más simple es usar *Move Method* y *Move Field* para mover partes de una clase a la clase en la que se usan esas partes. Pero esto funciona solo si la primera clase realmente no necesita estas partes.
* Otra solución es usar *Extract Class* y *Hide Delegate* en la clase para hacer que las relaciones de código sean "oficiales".
* Si las clases son mutuamente interdependientes, debe usar *Change Bidirectional Association to Unidirectional.
* Si esta "intimidad" es entre una subclase y la superclase, considere *Replace Delegation with Inheritance*.

## **Incomplete Library Class**

### **Signos para reconocer**:
* Tarde o temprano, las bibliotecas dejan de satisfacer las necesidades de los usuarios. La única solución al problema, cambiar la biblioteca, a menudo es imposible ya que la biblioteca es de solo lectura.

### **Razones del problema**:
* El autor de la biblioteca no ha proporcionado las funciones que necesita o se ha negado a implementarlas.

### **Tratamiento**:
* Para introducir algunos métodos en una clase de biblioteca, utilice *Introduce Foreign Method*.
* Para grandes cambios en una biblioteca de clases, use *Introduce Local Extension*.

### **Cuando Ignorar**:
* Ampliar una biblioteca puede generar trabajo adicional si los cambios en la biblioteca implican cambios en el código.


## **Message Chains**

### **Signos para reconocer**:
* En el código, ve una serie de llamadas que se asemejan a `$a->b()->c()->d()`.

### **Razones del problema**:
* Una cadena de mensajes ocurre cuando un cliente solicita otro objeto, ese objeto solicita otro más, y así sucesivamente. Estas cadenas significan que el cliente depende de la navegación a lo largo de la estructura de clases. Cualquier cambio en estas relaciones requiere modificar el cliente.

### **Tratamiento**:
* Para eliminar una cadena de mensajes, use *Hide Delegate*.
* A veces es mejor pensar por qué se usa el objeto final. Tal vez tendría sentido usar el *Extract Method* para esta funcionalidad y moverlo al comienzo de la cadena, usando **Move Method**.

### **Cuando Ingorar**:
* La ocultación de delegados demasiado agresiva puede generar un código en el que es difícil ver dónde está ocurriendo realmente la funcionalidad. Que es otra forma de decir, evita *Middle Man* smell.

## **Middle Man**

### **Signos para reconocer**:
* Si una clase realiza solo una acción, delegando trabajo a otra clase, ¿por qué existe?

### **Razones del problema**:
* Este code-smell puede ser el resultado de una eliminación excesiva de *Message Chains*.
* En otros casos, puede ser el resultado de que el trabajo útil de una clase se traslade gradualmente a otras clases. La clase permanece como un caparazón vacío que no hace nada más que delegar.

### **Tratamiento**:
Si la mayoría de las clases de un método delegan a otra clase, *Remove Middle Man* está en orden.

### **Cuando Ignorar**:
* No elimine intermediarios que se hayan creado por una razón:
* Es posible que se haya agregado un intermediario para evitar las dependencias entre clases.
* Algunos patrones de diseño crean intermediarios a propósito (como *Proxy* o *Decorator*).

# **Otros code-smells**

## **Incomplete Library Class**

### **Signos para reconocer**:
* Tarde o temprano, las bibliotecas dejan de satisfacer las necesidades de los usuarios. La única solución al problema, cambiar la biblioteca, a menudo es imposible ya que la biblioteca es de solo lectura.

### **Razones del problema**:
* El autor de la biblioteca no ha proporcionado las funciones que necesita o se ha negado a implementarlas.
* En otros casos, puede ser el resultado de que el trabajo útil de una clase se traslade gradualmente a otras clases. La clase permanece como un caparazón vacío que no hace nada más que delegar.

### **Tratamiento**:
* Para introducir algunos métodos en una clase de biblioteca, utilice *Introduce Foreign Method*.
* Para grandes cambios en una biblioteca de clases, use *Introduce Local Extension*.

### **Cuando Ignorar**:
*Ampliar una biblioteca puede generar trabajo adicional si los cambios en la biblioteca implican cambios en el código.
