# **Configurar aplicaciones de Python mediante JSON**

Muchas aplicaciones, como por ejemplo Visual Studio Code, permite cambiar la apariencia, colores, configuraciones, etc, desde un archivo `.json`. Pero si queremos que la aplicación que creemos con Python pueda ser configurada mediante un archivo `.json` se deberá incluir una lógica en el código de la aplicación que permita este tipo de interacción.

# **Aplicación de CustomTkinter personalizable**

En este ejemplo crearemos una aplicación con interfaz gráfica que podrá ser configurada desde un archivo `.json`.
```json
{
  "appearance_mode": "dark"
}
```


```python
import json
import customtkinter

# Verificar si existe el archivo JSON, si no, crearlo y colocar una configuración por defecto.
try:
    with open('config.json', 'r+') as json_file:
        config = json.load(json_file)
except FileNotFoundError:
    with open('config.json', 'w') as json_file:
        config = {
            "appearance_mode": "dark"
        }
        json.dump(config, json_file)

# Verificar si existe el archivo JSON, si no, crearlo
try:
    with open('config.json', 'r') as json_file:
        config = json.load(json_file)
except FileNotFoundError as error:
    print(error)


def mostrar_mensaje():
    print("Botón Presionado")

ventana = customtkinter.CTk()
ventana.title("Aplicación en modo claro")

customtkinter.set_appearance_mode(config['appearance_mode'])

button = customtkinter.CTkButton(ventana, text="CTkButton", command=mostrar_mensaje)
button.pack(pady=10)

ventana.mainloop()
```

Se puede complicar más el ejemplo pero básicamente la complejidad radica el cuanto de grande sea la aplicación y el archivo JSON. Si el archivo JSON es muy grande quizá sea mejor recorrerlo y almacenar las diferentes configuraciones en diferentes variables. 

## **Verificar que el contenido del archivo JSON sea correcto**

Existe una execpción provista por el módulo JSON que permite saber si el archivo JSON está bien escrito.

```python
import json

try:
    with open('config.json', 'r') as json_file:
        config = json.load(json_file)
    print("El formato del archivo JSON es válido.")
except json.JSONDecodeError as error:
    print("Error al leer el archivo JSON de configuración:", error)
```


