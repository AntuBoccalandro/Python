# **Interfaces gráficas con CustomTkinter**

CustomTkinter es una alternativa a Tkinter, la sintaxis y organización es parecida pero permite crear aplicaciones con una interfaz moderna

# Crear Aplicación básica

```python
import customtkinter

# Creamos la app
app = customtkinter.CTk()
# Mantenemos abierta la ventana
app.mainloop()
```

# **Gestor de geometría GRID**

El grid divide una ventana o marco en columnas y filas, que se colapsan cuando están vacías, pero se adaptan al tamaño de los widgets colocados dentro de ellas. 

![](https://www.pythontutorial.net/wp-content/uploads/2021/01/Tkinter-grid-Grid-Geometry.png)

## **window.grid_columnconfigure(index, weight=1)**
Este método permite configurar la columna especificada con un factor de peso, que determina cuánto espacio adicional se asigna a esa columna en relación con otras columnas cuando se redimensiona la ventana. Un mayor valor de peso hará que la columna se expanda más. Por ejemplo, un weight de 4, hará que la columna especificada sea 4 veces mayor que las otras.

## **window.grid_rowconfigure(index, weight=1)**
Este método permite configurar la fila especificada con un factor de peso, que determina cuánto espacio adicional se asigna a esa fila en relación con otras filas cuando se redimensiona la ventana. Un mayor valor de peso hará que la fila se expanda más.

Los métodos grid_columnconfigure y grid_rowconfigure se aplican a la ventana como tal. En cambio el metódo grid se aplica solamente al elemento que se quiere crear.

## **element.grid(row=n, column=n, padx=n, pady=n, stiscky="")**
Este método crea el elemento seleccionado y lo muestra en pantalla. 
* **row**: la fila a posicionarse.
* **column**: la columna a posicionarse.
* **padx**: espaciado exterior en píxeles de los bordes izquierdo y derecho.
* **pady**: espaciado exterior en píxeles de los bordes inferior y superior.
* **ipadx**: espaciado interior en píxeles de los bordes izquierdo y derecho.
* **ipady**: espaciado interior en píxeles de los bordes inferior y superior.
* **sticky**: para controlar cómo se expande o se adhiere un windget a su celda en la grid. Determina la/las dirección por las que un widget se expanderá. Acepta los siguientes valores:
    | **Sticky** | **Descripción**                                                                         |
    | ---------- | --------------------------------------------------------------------------------------- |
    | `N`        | Norte o centro superior                                                                 |
    | `S`        | Centro Sur o Inferior                                                                   |
    | `E`        | Centro Este o Derecha                                                                   |
    | `W`        | Oeste o Centro Izquierdo                                                                |
    | `NW`       | Noroeste o arriba a la izquierda                                                        |
    | `NE`       | Noreste o arriba a la derecha                                                           |
    | `SE`       | Sudeste o abajo a la derecha                                                            |
    | `SW`       | Sudoeste o abajo a la izquierda                                                         |
    | `NS`       | NS estira el widget verticalmente.Sin embargo, deja el widget centrado horizontalmente. |
    | `EW`       | EW estira el widget horizontalmente.Sin embargo, deja el widget centrado verticalmente. |

  Estos valores pueden ser combinados para formar diferentes combinaciones, como estás: `NS`.

  ![](https://www.pythontutorial.net/wp-content/uploads/2021/01/Tkinter-grid-Sticky-N.png)
  ![](https://www.pythontutorial.net/wp-content/uploads/2021/01/Tkinter-grid-Sticky-NS-1.png)

## **Combinación de celdas**

![](https://www.pythontutorial.net/wp-content/uploads/2021/01/Tkinter-grid-columnspan-rowspan.png)

* **rowspan**: Este parámetro especifica cuántas filas debe ocupar un widget en la cuadrícula. Por ejemplo, si estableces rowspan=2, el widget se extenderá verticalmente a través de dos filas.
* **columnspan**: Este parámetro especifica cuántas columnas debe ocupar un widget en la cuadrícula. Si estableces columnspan=3, el widget se extenderá horizontalmente a través de tres columnas.

# **POO en las aplicaciones**

Si es una aplicación muy pequeña no sería necesario, pero si se quiere realizar una aplicación más grande es recomendable utilizar diferentes clases que hereden directamente de CTk.

**Ejemplo de aplicación**
```python
import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("400x150")
        self.grid_columnconfigure((0, 1), weight=1)

        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
        self.checkbox_1 = customtkinter.CTkCheckBox(self, text="checkbox 1")
        self.checkbox_1.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")
        self.checkbox_2 = customtkinter.CTkCheckBox(self, text="checkbox 2")
        self.checkbox_2.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w")
        
    def button_callback(self):
        print("button pressed")

app = App()
app.mainloop()
``` 

# **Frames**

Un marco es un widget que se muestra como un simple rectángulo. Por lo general, usa un marco para organizar otros widgets tanto visualmente como a nivel de codificación.

**CTk.CTkFrame(container, \*\*params)**:

| **argument**   | **value**                                                                           |
| -------------- | ----------------------------------------------------------------------------------- |
| `master`       | root, Frame or Toplevel                                                             |
| `width`        | width in px                                                                         |
| `height`       | height in px                                                                        |
| `border_width` | width of border in px                                                               |
| `fg_color`     | foreground color, tuple: (light_color, dark_color) or single color or "transparent" |
| `border_color` | border color, tuple: (light_color, dark_color) or single color                      |


**Ejemplo**:
```python
import customtkinter

class MyCheckboxFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.checkbox_1 = customtkinter.CTkCheckBox(self, text="checkbox 1")
        self.checkbox_1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.checkbox_2 = customtkinter.CTkCheckBox(self, text="checkbox 2")
        self.checkbox_2.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("400x180")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.checkbox_frame = MyCheckboxFrame(self)
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")

        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    def button_callback(self):
        print("button pressed")

app = App()
app.mainloop()
```

**Configuraciones del Frame**:
Para cambiar las propiedades del Frame se puede configurar de la siguiente manera:
```python
# Ejemplo que cambia el color de fondo del Frame
self.checkbox_frame.configure(fg_color="#FF0000")
``` 

## **Dynamic Frames**

Consiste
```python
import customtkinter

class MyScrollableCheckboxFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, title, values):
        super().__init__(master, label_text=title)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.checkboxes = []

        # Creamos tantas checkboxes como elementos tenga la lista pasada como argumento
        for i, value in enumerate(self.values):
            checkbox = customtkinter.CTkCheckBox(self, text=value)
            checkbox.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(checkbox)

    # La función get añade a una lista tantos elementos como checkboxes estén checkeadas
    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("400x220")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        values = ["value 1", "value 2", "value 3", "value 4", "value 5", "value 6"]
        self.scrollable_checkbox_frame = MyScrollableCheckboxFrame(self, title="HOLA", values=values)
        self.scrollable_checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

    def button_callback(self):
        print("checkbox_frame:", self.scrollable_checkbox_frame.get())

app = App()
app.mainloop()
```

# **Colores y temas**

Los colores y temas de la aplicación pueden ser personalizables desde un archivo JSON. 

## **Archivo JSON por defecto**:
```json
{
  "CTk": {
    "fg_color": ["gray95", "gray10"]
  },
  "CTkToplevel": {
    "fg_color": ["gray95", "gray10"]
  },
  "CTkFrame": {
    "corner_radius": 6,
    "border_width": 0,
    "fg_color": ["gray90", "gray13"],
    "top_fg_color": ["gray85", "gray16"],
    "border_color": ["gray65", "gray28"]
  },
  "CTkButton": {
    "corner_radius": 6,
    "border_width": 0,
    "fg_color": ["#3a7ebf", "#1f538d"],
    "hover_color": ["#325882", "#14375e"],
    "border_color": ["#3E454A", "#949A9F"],
    "text_color": ["#DCE4EE", "#DCE4EE"],
    "text_color_disabled": ["gray74", "gray60"]
  },
  "CTkLabel": {
    "corner_radius": 0,
    "fg_color": "transparent",
    "text_color": ["gray14", "gray84"]
  },
  "CTkEntry": {
    "corner_radius": 6,
    "border_width": 2,
    "fg_color": ["#F9F9FA", "#343638"],
    "border_color": ["#979DA2", "#565B5E"],
    "text_color": ["gray14", "gray84"],
    "placeholder_text_color": ["gray52", "gray62"]
  },
  "CTkCheckbox": {
    "corner_radius": 6,
    "border_width": 3,
    "fg_color": ["#3a7ebf", "#1f538d"],
    "border_color": ["#3E454A", "#949A9F"],
    "hover_color": ["#325882", "#14375e"],
    "checkmark_color": ["#DCE4EE", "gray90"],
    "text_color": ["gray14", "gray84"],
    "text_color_disabled": ["gray60", "gray45"]
  },
  "CTkSwitch": {
    "corner_radius": 1000,
    "border_width": 3,
    "button_length": 0,
    "fg_color": ["#939BA2", "#4A4D50"],
    "progress_color": ["#3a7ebf", "#1f538d"],
    "button_color": ["gray36", "#D5D9DE"],
    "button_hover_color": ["gray20", "gray100"],
    "text_color": ["gray14", "gray84"],
    "text_color_disabled": ["gray60", "gray45"]
  },
  "CTkRadiobutton": {
    "corner_radius": 1000,
    "border_width_checked": 6,
    "border_width_unchecked": 3,
    "fg_color": ["#3a7ebf", "#1f538d"],
    "border_color": ["#3E454A", "#949A9F"],
    "hover_color": ["#325882", "#14375e"],
    "text_color": ["gray14", "gray84"],
    "text_color_disabled": ["gray60", "gray45"]
  },
  "CTkProgressBar": {
    "corner_radius": 1000,
    "border_width": 0,
    "fg_color": ["#939BA2", "#4A4D50"],
    "progress_color": ["#3a7ebf", "#1f538d"],
    "border_color": ["gray", "gray"]
  },
  "CTkSlider": {
    "corner_radius": 1000,
    "button_corner_radius": 1000,
    "border_width": 6,
    "button_length": 0,
    "fg_color": ["#939BA2", "#4A4D50"],
    "progress_color": ["gray40", "#AAB0B5"],
    "button_color": ["#3a7ebf", "#1f538d"],
    "button_hover_color": ["#325882", "#14375e"]
  },
  "CTkOptionMenu": {
    "corner_radius": 6,
    "fg_color": ["#3a7ebf", "#1f538d"],
    "button_color": ["#325882", "#14375e"],
    "button_hover_color": ["#234567", "#1e2c40"],
    "text_color": ["#DCE4EE", "#DCE4EE"],
    "text_color_disabled": ["gray74", "gray60"]
  },
  "CTkComboBox": {
    "corner_radius": 6,
    "border_width": 2,
    "fg_color": ["#F9F9FA", "#343638"],
    "border_color": ["#979DA2", "#565B5E"],
    "button_color": ["#979DA2", "#565B5E"],
    "button_hover_color": ["#6E7174", "#7A848D"],
    "text_color": ["gray14", "gray84"],
    "text_color_disabled": ["gray50", "gray45"]
  },
  "CTkScrollbar": {
    "corner_radius": 1000,
    "border_spacing": 4,
    "fg_color": "transparent",
    "button_color": ["gray55", "gray41"],
    "button_hover_color": ["gray40", "gray53"]
  },
  "CTkSegmentedButton": {
    "corner_radius": 6,
    "border_width": 2,
    "fg_color": ["#979DA2", "gray29"],
    "selected_color": ["#3a7ebf", "#1f538d"],
    "selected_hover_color": ["#325882", "#14375e"],
    "unselected_color": ["#979DA2", "gray29"],
    "unselected_hover_color": ["gray70", "gray41"],
    "text_color": ["#DCE4EE", "#DCE4EE"],
    "text_color_disabled": ["gray74", "gray60"]
  },
  "CTkTextbox": {
    "corner_radius": 6,
    "border_width": 0,
    "fg_color": ["gray100", "gray20"],
    "border_color": ["#979DA2", "#565B5E"],
    "text_color": ["gray14", "gray84"],
    "scrollbar_button_color": ["gray55", "gray41"],
    "scrollbar_button_hover_color": ["gray40", "gray53"]
  },
  "CTkScrollableFrame": {
    "label_fg_color": ["gray80", "gray21"]
  },
  "DropdownMenu": {
    "fg_color": ["gray90", "gray20"],
    "hover_color": ["gray75", "gray28"],
    "text_color": ["gray14", "gray84"]
  },
  "CTkFont": {
    "macOS": {
      "family": "SF Display",
      "size": 13,
      "weight": "normal"
    },
    "Windows": {
      "family": "Roboto",
      "size": 13,
      "weight": "normal"
    },
    "Linux": {
      "family": "Roboto",
      "size": 13,
      "weight": "normal"
    }
  }
}
``` 
## **Setear un tema**

**Temas por defecto**:
```python
# List of themes: "blue" (default), "green", "dark-blue"
customtkinter.set_default_color_theme("dark-blue")
```

**Temas propios**:
Si se quiere se puede crear un tema propio en un archivo JSON propio que contenga la lista de colores y fuentes para nuestra aplicación.
```python
customtkinter.set_default_color_theme("path/to/your/custom_theme.json")
```

# **Modo de apariencia**

El modo de apariencia decide qué color se seleccionará. Si establece el modo de apariencia en `system`, el modo actual se lee desde el sistema operativo. También se adaptará si el modo de apariencia del sistema operativo cambia durante el tiempo de ejecución del programa. Tenga en cuenta que en Linux siempre estará en `light` modo si se establece en "`system`", porque el modo no se puede leer desde el sistema operativo en este momento, esto probablemente se implementará en el futuro.

```python
# Default
customtkinter.set_appearance_mode("system")
customtkinter.set_appearance_mode("dark")
customtkinter.set_appearance_mode("light")
```

# **Escalado de DPI**

**Desactivar escalado automático de DPI**:
```python
customtkinter.deactivate_automatic_dpi_awareness()
```

**Activar escalado de DPI**:
Además del factor de escala detectado automáticamente, también puede establecer sus propios factores de escala para la aplicación como los siguientes:

```python
customtkinter.set_widget_scaling(float_value)  # widget dimensions and text size
customtkinter.set_window_scaling(float_value)  # window geometry dimensions
```

# **Widgets**

## **Button**
**Ejemplos**
```python

``` 
**Propiedades**
| argumento | valor                          |
| --------- | ------------------------------ |
| maestro   | raíz, tkinter.Frame o CTkFrame |
| ancho     | ancho del botón en px          |
| altura    | altura del botón en px         |

