# **Refactoring**

La refactorización de código es un tema muy complejo y delicado. Clean Code es una filosofía utilizada en el desarrollo de software cuyo objetivo es hacer más fácil la lectura y escritura de código

* **El código debe ser obvio para todos los programadores**: los nombres de las variables, clases, métodos deben ser obvios y significativos.
* **No debe haber código duplicado**: el utilizar código duplicado varias veces sin empaquetarlo en una función hace que cuando se quiera modificar este se pierda tiempo teniendo que cambiar el mismo código en otras partes del mismo.
* **El código debe ser simple**: un buen código no contiene gran cantidad de clases, y código extenso. El código tiene que ser acotado pero a la vez lo suficientemente móvil para que se puedan agregar nuevas funcionalidades.

## **Deuda técnica**

La deuda técnica fue un concepto creado por "Ward Cunningham". Este concepto hace referecia a que el tiempo que te ahorres escribiendo código sucio y no haciendo tests lo tendrás que pagar más tarde gastando tiempo corrigiendo el código y haciendo los tests.

**Causas de la deuda técnica:**
* **Presión empresarial**: la presión de tener que presentar el código en un tiempo ajustado hace que no se pueda tener toda la calidad y tiempo para solucionar bugs y hacer tests.
* **Falta de compresión de las consecuencias de la deuda técnica**: a veces el cliente o el gerente del proyecto no comprende la importancia de dedicar tiempo a la refactorización, lo que puede llevar a que no se tome en cuenta este paso.
* **No combatir la estricta coherencia de los componentes**: la semejanza de un proyecto a un monolito puede llevar a la difícil compresión del código, difícil mantención y difícil colaboración en equipo.
* **Falta de tests**: la falta de documentación interna del código hace que luego no se sepa como se implementaron ciertas partes del código.
* **Falta de interacción entre los miembros del equipo**: la falta de coordinación o interacción entre los desarolladores del proyecto hace que el desarrollo se realentice, se implementen funcionalidades innecesarias.
* **Refactorización retrasada**: la refactorización retrasada hace que se acumule el trabajo de refactorización, esto hace que luego se tenga que modificar todo el código, volver a escribir, surgen nuevos bugs, etc.
* **Falta de seguimiento del cumplimiento**: esto sucede cuando todos los desarrolladores del proyecto no siguien la mismas reglas de escritura del código, lo que genera inconsistente.
* **Incompetencia**: la falta de concocimiento sobre la escritura del código o alguna tecnología puede generar código sucio.

## **Cuando refactorizar**

**Regla de tres**:
1. Cuando estés haciendo algo por primera vez, simplemente hazlo.
2. Cuando esté haciendo algo similar por segunda vez, sienta vergüenza de tener que repetirlo, pero haga lo mismo de todos modos.
3. Cuando esté haciendo algo por tercera vez, comience a refactorizar.

**Al agregar una característica**:
* La refactorización lo ayuda a comprender el código de otras personas. Si tiene que lidiar con el código sucio de otra persona, intente refactorizarlo primero. 
* La refactorización facilita la adición de nuevas funciones. Es mucho más fácil hacer cambios en código limpio. 

**Al corregir un error**:
* Limpie su código y los errores prácticamente se descubrirán solos.

**Durante una revisión de código**:
* La revisión del código puede ser la última oportunidad de arreglar el código antes de que esté disponible para el público.

## **Cómo refactorizar**

La refactorización se debe realizar como una serie de pequeños cambios, cada uno de los cuales mejora un poco el código existente y deja el programa en condiciones de funcionamiento.

**Como saber si he realizado correctamente la refactorización**:
* **El código debería volverse más limpio**:  es importante verificar que la refactorización hizo cambios en el código y no sigue igual, si no es que algo hemos hecho mal. Esto puede suceder cuando el código es extremadamente desatrozo, en estos casos los mejor es reescribir el código.
* **No se debe crear una nueva funcionalidad durante la refactorización**: no mezcle la refactorización y el desarrollo directo de nuevas características porque son cosas diferentes.
* **Todas las pruebas existentes deben pasar después de la refactorización**: hay dos casos en los que las pruebas pueden fallar después de la refactorización:
  * Cometiste un error durante la refactorización. Esta es una obviedad: siga adelante y corrija el error.
  * Tus pruebas fueron de muy bajo nivel. Por ejemplo, estaba probando métodos privados de clases.
  
  En este caso, las pruebas tienen la culpa. Puede refactorizar las pruebas en sí o escribir un conjunto completamente nuevo de pruebas de nivel superior.
